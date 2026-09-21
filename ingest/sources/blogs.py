"""AI company and practitioner blogs via RSS/Atom."""

from __future__ import annotations

import calendar
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import feedparser

from ingest.http import get_text
from ingest.text import plain
from store.item import Item, iso_utc, make_item

FEEDS_PATH = Path(__file__).resolve().parent.parent / "feeds.txt"

# Full text is the training input for the deferred scorer, so the cap exists
# only to bound a pathological feed, not to summarize.
MAX_TEXT = 20000


def load_feeds(path: Path | None = None) -> list[str]:
    lines = (path or FEEDS_PATH).read_text(encoding="utf-8").splitlines()
    return [
        stripped
        for line in lines
        if (stripped := line.strip()) and not stripped.startswith("#")
    ]


def parse(xml: str, feed_name: str, days: int = 14) -> list[Item]:
    feed = feedparser.parse(xml)
    items: list[Item] = []
    cutoff = time.time() - days * 86400
    for entry in feed.entries:
        title = " ".join(entry.get("title", "").split())
        link = entry.get("link")
        if not title or not link:
            continue
        when = entry.get("published_parsed") or entry.get("updated_parsed")
        if when and calendar.timegm(when) < cutoff:
            continue
        # feedparser hands back RFC-822 in `published`; the parsed struct is
        # already UTC, so it is the better source for the shared key.
        published = (
            datetime.fromtimestamp(calendar.timegm(when), timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
            if when
            else iso_utc(entry.get("published"))
        )
        body = entry.get("summary") or entry.get("description") or ""
        try:
            items.append(
                make_item(
                    url=link,
                    title=title,
                    source="blog",
                    text=plain(body)[:MAX_TEXT],
                    meta={"feed": feed_name, "published": published},
                )
            )
        except ValueError as exc:  # one unusable row must not cost the source
            print(f"[blogs] skipped {link}: {exc}", file=sys.stderr)
    return items


def fetch(path: Path | None = None, days: int = 14) -> tuple[list[Item], int]:
    """Returns (items, failed feeds).

    A six-feed source almost never reaches zero items, so a dying source is
    invisible unless the count of feeds that blew up travels with the haul.
    """
    items: list[Item] = []
    failed = 0
    for url in load_feeds(path):
        name = urlsplit(url).netloc.lower().removeprefix("www.")
        try:
            items.extend(parse(get_text(url), name, days=days))
        except Exception as exc:  # one dead feed must not kill the rest
            failed += 1
            print(f"[blogs] {name} failed: {exc}", file=sys.stderr)
    return items, failed
