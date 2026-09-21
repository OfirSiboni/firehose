"""Fetch every source, merge into the pool, expire the tail."""

from __future__ import annotations

import os
import sys

from ingest.sources import arxiv, blogs, github, hn
from send.telegram import get_updates
from store import digests, health, labels, pool
from store.item import Item, dedupe

SOURCES = {
    "hn": hn.fetch,
    "arxiv": arxiv.fetch,
    "github": github.fetch,
    # Keyed "blog" to match Item.source, so health names and pool rows agree.
    "blog": blogs.fetch,
}


def collect() -> tuple[list[Item], dict[str, dict[str, int]]]:
    """Fetch every source in isolation. One failure must not lose the others.

    Each fetch returns its haul plus the number of sub-units (GitHub topics,
    blog feeds) that blew up, so a source limping along on one of six feeds is
    distinguishable from a healthy one.
    """
    items: list[Item] = []
    counts: dict[str, dict[str, int]] = {}
    for name, fetch in SOURCES.items():
        try:
            found, failed = fetch()
            counts[name] = {"items": len(found), "failed": failed}
            items.extend(found)
            note = f", {failed} unit(s) failed" if failed else ""
            print(f"[{name}] {len(found)} items{note}")
        except Exception as exc:
            # The whole source died: that is one failed unit at this level.
            counts[name] = {"items": 0, "failed": 1}
            print(f"[{name}] FAILED: {exc}", file=sys.stderr)
    return items, counts


def collect_feedback() -> int:
    """Sole consumer of getUpdates — a second consumer would race the offset."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("[feedback] no token, skipping")
        return 0
    try:
        updates = get_updates(token, labels.read_offset())
        if not updates:
            return 0

        index = labels.build_message_index(digests.recent_digests(7))
        rows = labels.reactions_to_labels(updates, index)
        labels.append_labels(rows)
        labels.write_offset(max(u["update_id"] for u in updates) + 1)
        print(f"[feedback] {len(rows)} labels from {len(updates)} updates")
        return len(rows)
    except Exception as exc:
        print(f"[feedback] FAILED: {exc}", file=sys.stderr)
        return 0


def main(smoke: bool = False) -> int:
    items, counts = collect()
    if smoke:
        dead = [name for name, count in counts.items() if count["items"] == 0]
        print(f"\nsmoke: {counts}")
        if dead:
            print(f"smoke: NO ITEMS from {dead}", file=sys.stderr)
            return 1
        return 0

    health.record(counts)
    existing = pool.load_pool()
    merged, new_count = pool.merge(existing, dedupe(items))
    kept = pool.expire(merged)
    collect_feedback()
    pool.save_pool(kept)
    print(f"\n+{new_count} new, {len(kept)} in pool")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(smoke="--smoke" in sys.argv))
