"""Recently created AI repos with traction, via the GitHub search API."""

from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone

from ingest.http import get_json
from store.item import Item, iso_utc, make_item

API = "https://api.github.com/search/repositories"
TOPICS = ["llm", "ai-agents", "machine-learning", "inference", "rag"]


def parse(payload: dict) -> list[Item]:
    items: list[Item] = []
    for repo in payload.get("items", []):
        url = repo.get("html_url")
        name = repo.get("full_name")
        if not url or not name:
            continue
        created = iso_utc(repo.get("created_at"))
        try:
            items.append(
                make_item(
                    url=url,
                    title=name,
                    source="github",
                    text=repo.get("description") or "",
                    meta={
                        "stars": repo.get("stargazers_count", 0),
                        "topics": repo.get("topics", []),
                        "language": repo.get("language"),
                        "created_at": created,
                        "pushed_at": iso_utc(repo.get("pushed_at")),
                        # Every source spells recency the same way for the Judge.
                        "published": created,
                    },
                )
            )
        except ValueError as exc:  # one unusable row must not cost the source
            print(f"[github] skipped {name}: {exc}", file=sys.stderr)
    return items


def fetch(days: int = 60, min_stars: int = 150) -> tuple[list[Item], int]:
    """Returns (items, failed topics).

    A partial result is not a healthy one: four of five topics dying used to
    look identical to a clean run, so the failure count travels with the items.
    """
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    items: list[Item] = []
    failed = 0
    for topic in TOPICS:
        query = f"topic:{topic}+created:>{since}+stars:>{min_stars}"
        url = f"{API}?q={query}&sort=stars&order=desc&per_page=20"
        try:
            items.extend(parse(get_json(url)))
        except Exception as exc:  # one bad topic must not lose the other four
            failed += 1
            print(f"[github] topic {topic} failed: {exc}", file=sys.stderr)
    return items, failed
