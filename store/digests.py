"""Per-day digest records: what was sent, and which Telegram message carries it."""

from __future__ import annotations

import json
from pathlib import Path

from store import REPO_ROOT

DIGEST_DIR = REPO_ROOT / "data" / "digests"


def digest_path(date: str) -> Path:
    return DIGEST_DIR / f"{date}.json"


def save_digest(digest: dict, date: str) -> None:
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    digest_path(date).write_text(
        json.dumps(digest, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def load_digest(date: str) -> dict | None:
    path = digest_path(date)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def recent_digests(days: int = 7) -> list[dict]:
    if not DIGEST_DIR.exists():
        return []
    paths = sorted(DIGEST_DIR.glob("*.json"), reverse=True)[:days]
    return [json.loads(p.read_text(encoding="utf-8")) for p in paths]
