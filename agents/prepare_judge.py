"""Assemble everything the Judge needs into one file."""

from __future__ import annotations

import json
from pathlib import Path

from store import REPO_ROOT, digests, labels, pool

INPUT_PATH = REPO_ROOT / "data" / "judge_input.json"


def main() -> int:
    candidates = pool.unsent_since(pool.load_pool(), hours=36)
    payload = {
        "candidates": [
            {
                "id": i.id, "url": i.url, "title": i.title, "source": i.source,
                "first_seen": i.first_seen, "text": i.text[:1500], "meta": i.meta,
            }
            for i in candidates
        ],
        "recent_labels": labels.recent_labels(20),
        "recently_sent_titles": [
            item["title"] for digest in digests.recent_digests(7)
            for item in digest.get("items", [])
        ],
    }
    INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    INPUT_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"judge input: {len(payload['candidates'])} candidates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
