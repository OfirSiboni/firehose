"""arXiv cs.AI / cs.LG / cs.CL via the Atom export API."""

from __future__ import annotations

import feedparser

from ingest.http import get_text
from store.item import Item, make_item

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
        items.append(
            make_item(
                url=link,
                title=title,
                source="arxiv",
                text=" ".join(entry.get("summary", "").split()),
                meta={
                    "authors": [a.get("name") for a in entry.get("authors", [])],
                    "primary_category": categories[0] if categories else None,
                    "published": entry.get("published"),
                },
            )
        )
    return items


def fetch(max_results: int = 100) -> list[Item]:
    url = (
        f"{API}?search_query={CATEGORIES}"
        f"&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    )
    return parse(get_text(url))
