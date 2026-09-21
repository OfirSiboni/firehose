"""Fetch every source, merge into the pool, expire the tail."""

from __future__ import annotations

import sys

from ingest.sources import arxiv, blogs, github, hn
from store import health, pool
from store.item import dedupe

SOURCES = {
    "hn": hn.fetch,
    "arxiv": arxiv.fetch,
    "github": github.fetch,
    "blogs": blogs.fetch,
}


def collect() -> tuple[list, dict[str, int]]:
    """Fetch every source in isolation. One failure must not lose the others."""
    items, counts = [], {}
    for name, fetch in SOURCES.items():
        try:
            found = fetch()
            counts[name] = len(found)
            items.extend(found)
            print(f"[{name}] {len(found)} items")
        except Exception as exc:
            counts[name] = 0
            print(f"[{name}] FAILED: {exc}", file=sys.stderr)
    return items, counts


def main(smoke: bool = False) -> int:
    items, counts = collect()
    if smoke:
        dead = [name for name, count in counts.items() if count == 0]
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
