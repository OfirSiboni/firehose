"""The blind head-to-head verdict for a day. Telegram-only, never published."""

from __future__ import annotations

import json
from pathlib import Path

from store import REPO_ROOT

CRITIQUE_DIR = REPO_ROOT / "data" / "critique"


def critique_path(date: str) -> Path:
    return CRITIQUE_DIR / f"{date}.json"


def save_critique(critique: dict, date: str) -> None:
    CRITIQUE_DIR.mkdir(parents=True, exist_ok=True)
    critique_path(date).write_text(
        json.dumps(critique, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def load_critique(date: str) -> dict | None:
    path = critique_path(date)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
