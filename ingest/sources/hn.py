"""Hacker News via the Algolia search API."""

from __future__ import annotations

import time

from ingest.http import get_json
from ingest.text import plain
from store.item import Item, make_item

API = "https://hn.algolia.com/api/v1/search_by_date"


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
                },
            )
        )
    return items


def fetch(hours: int = 24, min_points: int = 30) -> list[Item]:
    cutoff = int(time.time()) - hours * 3600
    url = (
        f"{API}?tags=story"
        f"&numericFilters=points>{min_points},created_at_i>{cutoff}"
        f"&hitsPerPage=100"
    )
    return parse(get_json(url))
