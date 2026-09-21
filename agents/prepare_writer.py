"""Hand the Writer only the top stories and the facts already gathered."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from store import REPO_ROOT, pool, ranked

INPUT_PATH = REPO_ROOT / "data" / "writer_input.json"
KEEP = ("id", "url", "title", "source", "tier", "reason", "key_facts")


def build(
    payload: dict, n: int = 8, exclude_ids: frozenset[str] = frozenset()
) -> dict:
    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "stories": [
            {key: story[key] for key in KEEP}
            for story in ranked.top(payload, n, exclude_ids)
        ],
    }


def main() -> int:
    items = pool.load_pool()
    payload = ranked.load_ranked({i.id for i in items})
    built = build(payload, exclude_ids=ranked.unpublishable_ids(items))
    INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    INPUT_PATH.write_text(json.dumps(built, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"writer input: {len(built['stories'])} stories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
