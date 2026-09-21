"""AI company and practitioner blogs via RSS/Atom."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit

import feedparser

from ingest.http import get_text
from ingest.text import plain
from store.item import Item, make_item

FEEDS_PATH = Path(__file__).resolve().parent.parent / "feeds.txt"


def load_feeds(path: Path | None = None) -> list[str]:
    lines = (path or FEEDS_PATH).read_text(encoding="utf-8").splitlines()
    return [
        stripped
        for line in lines
        if (stripped := line.strip()) and not stripped.startswith("#")
    ]


def parse(xml: str, feed_name: str) -> list[Item]:
    feed = feedparser.parse(xml)
    items: list[Item] = []
    for entry in feed.entries:
        title = " ".join(entry.get("title", "").split())
        link = entry.get("link")
        if not title or not link:
            continue
        body = entry.get("summary") or entry.get("description") or ""
        items.append(
            make_item(
                url=link,
                title=title,
                source="blog",
                text=plain(body)[:2000],
                meta={"feed": feed_name, "published": entry.get("published")},
            )
        )
    return items


def fetch(path: Path | None = None) -> list[Item]:
    items: list[Item] = []
    for url in load_feeds(path):
        name = urlsplit(url).netloc.lower().removeprefix("www.")
        try:
            items.extend(parse(get_text(url), name))
        except Exception as exc:  # one dead feed must not kill the rest
            print(f"[blogs] {name} failed: {exc}")
    return items
