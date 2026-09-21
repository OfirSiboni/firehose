"""Feedback labels, append-only."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from store import REPO_ROOT

LABELS_PATH = REPO_ROOT / "data" / "labels.jsonl"
OFFSET_PATH = REPO_ROOT / "data" / "tg_offset.txt"

# Emoji vocabulary. Telegram sends the writing hand with and without VS16.
VERDICTS = {
    "👍": "up",
    "👎": "down",
    "✍": "published",
    "✍️": "published",
}


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_labels() -> list[dict]:
    if not LABELS_PATH.exists():
        return []
    return [
        json.loads(line)
        for line in LABELS_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def append_labels(rows: list[dict]) -> None:
    if not rows:
        return
    LABELS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LABELS_PATH.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def recent_labels(n: int = 20) -> list[dict]:
    return load_labels()[-n:]


def read_offset() -> int:
    if not OFFSET_PATH.exists():
        return 0
    return int(OFFSET_PATH.read_text(encoding="utf-8").strip() or 0)


def write_offset(value: int) -> None:
    OFFSET_PATH.parent.mkdir(parents=True, exist_ok=True)
    OFFSET_PATH.write_text(str(value), encoding="utf-8")


def build_message_index(digest_list: list[dict]) -> dict[int, dict]:
    """message_id -> the item it carries, stamped with its digest date."""
    index: dict[int, dict] = {}
    for digest in digest_list:
        for item in digest.get("items", []):
            message_id = item.get("message_id")
            if message_id is None:
                continue
            index[message_id] = {**item, "digest_date": digest["date"]}
    return index


def reactions_to_labels(
    updates: list[dict], message_index: dict[int, dict]
) -> list[dict]:
    rows: list[dict] = []
    for update in updates:
        reaction = update.get("message_reaction")
        if not reaction:
            continue
        item = message_index.get(reaction.get("message_id"))
        if item is None:
            continue
        for entry in reaction.get("new_reaction", []):
            verdict = VERDICTS.get(entry.get("emoji", ""))
            if verdict is None:
                continue
            rows.append(
                {
                    "ts": _now(),
                    "digest_date": item["digest_date"],
                    "item_id": item["id"],
                    "url": item["url"],
                    "title": item["title"],
                    "tier": item["tier"],
                    "source": item["source"],
                    "verdict": verdict,
                }
            )
    return rows


def mark_ignored(digest: dict) -> list[dict]:
    """Every item in `digest` with no label yet becomes a weak negative."""
    labelled = {row["item_id"] for row in load_labels()}
    return [
        {
            "ts": _now(),
            "digest_date": digest["date"],
            "item_id": item["id"],
            "url": item["url"],
            "title": item["title"],
            "tier": item["tier"],
            "source": item["source"],
            "verdict": "ignored",
        }
        for item in digest.get("items", [])
        if item["id"] not in labelled
    ]
