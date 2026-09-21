"""The rolling candidate pool, stored as JSONL in the repo."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from store.item import Item

POOL_PATH = Path("data/pool.jsonl")


def _parse_ts(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def load_pool(path: Path = POOL_PATH) -> list[Item]:
    if not path.exists():
        return []
    return [
        Item.from_dict(json.loads(line))
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def save_pool(items: list[Item], path: Path = POOL_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "\n".join(json.dumps(i.to_dict(), ensure_ascii=False) for i in items)
    path.write_text(body + "\n" if body else "", encoding="utf-8")


def merge(existing: list[Item], incoming: list[Item]) -> tuple[list[Item], int]:
    """Add items we have not seen. Existing entries win — first_seen is preserved."""
    known = {item.id for item in existing}
    fresh = []
    for item in incoming:
        if item.id in known:
            continue
        known.add(item.id)
        fresh.append(item)
    return existing + fresh, len(fresh)


def expire(items: list[Item], now: datetime | None = None, days: int = 7) -> list[Item]:
    cutoff = (now or datetime.now(timezone.utc)) - timedelta(days=days)
    return [i for i in items if _parse_ts(i.first_seen) >= cutoff]


def unsent_since(
    items: list[Item], hours: int = 36, now: datetime | None = None
) -> list[Item]:
    cutoff = (now or datetime.now(timezone.utc)) - timedelta(hours=hours)
    return [
        i for i in items if i.sent_in is None and _parse_ts(i.first_seen) >= cutoff
    ]


def mark_sent(items: list[Item], ids: list[str], digest_date: str) -> list[Item]:
    targets = set(ids)
    for item in items:
        if item.id in targets:
            item.sent_in = digest_date
    return items
