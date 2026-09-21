"""Fetch every source, merge into the pool, expire the tail."""

from __future__ import annotations

import sys

from ingest.sources import arxiv, blogs, github, hn
from store import health, pool
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
    pool.save_pool(kept)
    print(f"\n+{new_count} new, {len(kept)} in pool")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(smoke="--smoke" in sys.argv))
