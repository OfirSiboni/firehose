"""Aggregate all feedback into one file for the relearn agent."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from store import REPO_ROOT, labels

INPUT_PATH = REPO_ROOT / "data" / "relearn_input.json"
ACCEPTED = {"up", "published"}


def summarize(rows: list[dict]) -> dict:
    counts: dict[str, int] = defaultdict(int)
    by_source: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    accepted, rejected = [], []
    for row in rows:
        verdict = row["verdict"]
        counts[verdict] += 1
        by_source[row.get("source", "unknown")][verdict] += 1
        (accepted if verdict in ACCEPTED else rejected).append(row.get("title", ""))
    return {
        "counts": dict(counts),
        "by_source": {k: dict(v) for k, v in by_source.items()},
        "accepted": accepted,
        "rejected": rejected,
        "total": len(rows),
    }


def main() -> int:
    built = summarize(labels.load_labels())
    INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    INPUT_PATH.write_text(json.dumps(built, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"relearn input: {built['total']} labels")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
