"""The rolling candidate pool, stored as JSONL in the repo."""

from __future__ import annotations

import json
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from store import REPO_ROOT
from store.item import Item, combine

POOL_PATH = REPO_ROOT / "data" / "pool.jsonl"


def _parse_ts(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def load_pool(path: Path = POOL_PATH) -> list[Item]:
    """Read the pool, skipping any row this version cannot make sense of.

    One unreadable line must cost one item, never the whole run.
    """
    if not path.exists():
        return []
    items: list[Item] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            items.append(Item.from_dict(json.loads(line)))
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            print(f"[pool] skipped bad row {path}:{number}: {exc}", file=sys.stderr)
    return items


def save_pool(items: list[Item], path: Path = POOL_PATH) -> None:
    """Write atomically: this file is the only datastore there is.

    A truncate-and-write interrupted midway would lose the 7-day pool, so the
    new content lands in a sibling temp file and is then renamed over the old
    one — os.replace is atomic on Windows and POSIX alike.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "\n".join(json.dumps(i.to_dict(), ensure_ascii=False) for i in items)
    handle, temp = tempfile.mkstemp(dir=path.parent, prefix=path.name, suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as out:
            out.write(body + "\n" if body else "")
        os.replace(temp, path)
    except BaseException:
        Path(temp).unlink(missing_ok=True)
        raise


def merge(existing: list[Item], incoming: list[Item]) -> tuple[list[Item], int]:
    """Add unseen items; refresh the ones we already hold.

    An id we already know keeps its identity — `id`, `first_seen` and
    `sent_in` are the pool's memory — but its `title`, `text` and `meta` are
    refreshed from the incoming row. Without that, volatile metadata freezes
    at first sight: an HN story captured at 45 points stays 45 forever, and
    the Judge scores saturation straight off that number.
    """
    index = {item.id: position for position, item in enumerate(existing)}
    out = list(existing)
    fresh = 0
    for item in incoming:
        position = index.get(item.id)
        if position is None:
            index[item.id] = len(out)
            out.append(item)
            fresh += 1
        else:
            out[position] = combine(out[position], item, refresh_title=True)
    return out, fresh


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
