"""Per-run source counts, so a quietly dead source becomes visible."""

from __future__ import annotations

import json
from pathlib import Path

HEALTH_PATH = Path("data/source_health.json")


def _load() -> list[dict[str, int]]:
    if not HEALTH_PATH.exists():
        return []
    return json.loads(HEALTH_PATH.read_text(encoding="utf-8"))


def record(counts: dict[str, int], keep: int = 8) -> None:
    history = (_load() + [counts])[-keep:]
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    HEALTH_PATH.write_text(json.dumps(history, indent=2), encoding="utf-8")


def dead_sources(runs: int = 3) -> list[str]:
    """Sources that returned nothing across the last `runs` runs."""
    history = _load()[-runs:]
    if len(history) < runs:
        return []
    names = {name for run in history for name in run}
    return sorted(n for n in names if all(run.get(n, 0) == 0 for run in history))
