"""Validation gate for Judge output. Nothing is sent unless this passes."""

from __future__ import annotations

import json
from pathlib import Path

from store import REPO_ROOT

RANKED_PATH = REPO_ROOT / "data" / "ranked.json"
TIERS = {"headline", "discovery"}
REQUIRED = ("id", "url", "title", "source", "tier", "score", "saturation", "reason", "read")


class ValidationError(Exception):
    pass


def validate_ranked(payload: dict, pool_ids: set[str]) -> None:
    items = payload.get("items")
    if not isinstance(items, list) or not items:
        raise ValidationError("payload has no non-empty 'items' list")

    seen: set[str] = set()
    for index, item in enumerate(items):
        where = f"items[{index}]"
        missing = [key for key in REQUIRED if key not in item]
        if missing:
            raise ValidationError(f"{where} missing keys: {missing}")
        if item["id"] in seen:
            raise ValidationError(f"{where} duplicate id {item['id']}")
        seen.add(item["id"])
        if item["id"] not in pool_ids:
            raise ValidationError(f"{where} id {item['id']} not in pool")
        if item["tier"] not in TIERS:
            raise ValidationError(f"{where} bad tier {item['tier']!r}")
        if not isinstance(item["score"], (int, float)) or not 0 <= item["score"] <= 10:
            raise ValidationError(f"{where} score out of range: {item['score']!r}")
        if not isinstance(item["saturation"], (int, float)) or not 0 <= item["saturation"] <= 1:
            raise ValidationError(f"{where} saturation out of range")
        if not str(item.get("reason", "")).strip():
            raise ValidationError(f"{where} has an empty reason")


def load_ranked(pool_ids: set[str], path: Path = RANKED_PATH) -> dict:
    if not path.exists():
        raise ValidationError(f"{path} was not produced")
    payload = json.loads(path.read_text(encoding="utf-8"))
    validate_ranked(payload, pool_ids)
    return payload


def unpublishable_ids(items) -> frozenset[str]:
    """Pool items that must never reach a digest.

    A TLDR item links to something readable. An HN text post is a discussion
    thread, not an artifact — worth keeping in the pool as research signal, and
    worth showing in the site's tail, but never publishable.
    """
    return frozenset(i.id for i in items if i.meta.get("kind") == "discussion")


def top(
    payload: dict, n: int = 8, exclude_ids: frozenset[str] = frozenset()
) -> list[dict]:
    """Highest scores first, minus anything unpublishable.

    `exclude_ids` is derived from the pool, which only Python writes. So the
    Judge cannot promote a discussion thread into the digest even if it scores
    it 10 — the rule is enforced here rather than hoped for in a prompt.
    """
    eligible = [i for i in payload["items"] if i["id"] not in exclude_ids]
    return sorted(eligible, key=lambda i: i["score"], reverse=True)[:n]
