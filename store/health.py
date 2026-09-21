"""Per-run source counts, so a quietly dead source becomes visible."""

from __future__ import annotations

import json

from store import REPO_ROOT

HEALTH_PATH = REPO_ROOT / "data" / "source_health.json"


def _load() -> list[dict]:
    if not HEALTH_PATH.exists():
        return []
    return json.loads(HEALTH_PATH.read_text(encoding="utf-8"))


def _items(entry) -> int:
    """Item count for one source in one run.

    Runs recorded before failure counts existed store a bare int; newer ones
    store {"items": n, "failed": m}. Both must read the same way, or the first
    run after this change crashes on its own history.
    """
    if isinstance(entry, dict):
        return int(entry.get("items") or 0)
    return int(entry or 0)


def record(counts: dict, keep: int = 8) -> None:
    history = (_load() + [counts])[-keep:]
    HEALTH_PATH.parent.mkdir(parents=True, exist_ok=True)
    HEALTH_PATH.write_text(json.dumps(history, indent=2), encoding="utf-8")


def dead_sources(runs: int = 3) -> list[str]:
    """Sources that returned nothing across the last `runs` runs."""
    history = _load()[-runs:]
    if len(history) < runs:
        return []
    names = {name for run in history for name in run}
    return sorted(n for n in names if all(_items(run.get(n)) == 0 for run in history))
