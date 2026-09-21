"""Hacker News via the Algolia search API."""

from __future__ import annotations

import sys
import time
from datetime import datetime, timezone

from ingest.http import get_json
from ingest.text import plain
from store.item import Item, iso_utc, make_item

API = "https://hn.algolia.com/api/v1/search_by_date"


def _published(hit: dict) -> str | None:
    """When the story was posted, not when we happened to see it.

    The fetch window is 24h, so first_seen can lag the real posting time by a
    day — the Judge cannot tell a fresh story from a stale one without this.
    """
    stamp = iso_utc(hit.get("created_at"))
    if stamp:
        return stamp
    epoch = hit.get("created_at_i")
    if epoch is None:
        return None
    return datetime.fromtimestamp(epoch, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(payload: dict) -> list[Item]:
    items: list[Item] = []
    for hit in payload.get("hits", []):
        object_id = hit.get("objectID")
        title = hit.get("title")
        if not title or not object_id:
            continue
        permalink = f"https://news.ycombinator.com/item?id={object_id}"
        # No url means a text post (Ask HN, Tell HN, jobs): the thread *is* the
        # content. Keep it as research signal, but mark it unpublishable — a
        # TLDR item has to link to something readable.
        external = hit.get("url")
        try:
            items.append(
                make_item(
                    url=external or permalink,
                    title=title,
                    source="hn",
                    text=plain(hit.get("story_text") or ""),
                    meta={
                        "points": hit.get("points", 0),
                        "comments": hit.get("num_comments", 0),
                        "hn_url": permalink,
                        "kind": "article" if external else "discussion",
                        "published": _published(hit),
                    },
                )
            )
        except ValueError as exc:  # one unusable row must not cost the source
            print(f"[hn] skipped {object_id}: {exc}", file=sys.stderr)
    return items


def fetch(hours: int = 24, min_points: int = 30) -> tuple[list[Item], int]:
    """Returns (items, failed units). One call, so nothing partial to count."""
    cutoff = int(time.time()) - hours * 3600
    url = (
        f"{API}?tags=story"
        f"&numericFilters=points>{min_points},created_at_i>{cutoff}"
        f"&hitsPerPage=100"
    )
    return parse(get_json(url)), 0
