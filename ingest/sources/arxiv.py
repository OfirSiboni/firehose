"""arXiv cs.AI / cs.LG / cs.CL via the Atom export API."""

from __future__ import annotations

import sys

import feedparser

from ingest.http import get_text
from store.item import Item, iso_utc, make_item

API = "http://export.arxiv.org/api/query"
CATEGORIES = "cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL"


def parse(xml: str) -> list[Item]:
    feed = feedparser.parse(xml)
    items: list[Item] = []
    for entry in feed.entries:
        title = " ".join(entry.get("title", "").split())
        if not title:
            continue
        link = entry.get("link") or entry.get("id", "")
        if not link:
            continue
        categories = [t.get("term") for t in entry.get("tags", []) if t.get("term")]
        try:
            items.append(
                make_item(
                    url=link,
                    title=title,
                    source="arxiv",
                    text=" ".join(entry.get("summary", "").split()),
                    meta={
                        "authors": [a.get("name") for a in entry.get("authors", [])],
                        "primary_category": categories[0] if categories else None,
                        "published": iso_utc(entry.get("published")),
                    },
                )
            )
        except ValueError as exc:  # one unusable row must not cost the source
            print(f"[arxiv] skipped {link}: {exc}", file=sys.stderr)
    return items


def fetch(max_results: int = 50) -> tuple[list[Item], int]:
    """Returns (items, failed units). One call, so nothing partial to count.

    max_results is 50 because the export API answers this query with a flat
    406 above roughly 70 entries — reproducibly, not as a throttle. That is
    what zeroed arXiv out of the committed pool. 50 newest submissions every
    3h still overlaps run to run; nothing here pages, by design.
    """
    url = (
        f"{API}?search_query={CATEGORIES}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    )
    return parse(get_text(url)), 0
