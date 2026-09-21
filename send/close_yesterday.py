"""Anything in the previous digest with no reaction becomes a weak negative."""

from __future__ import annotations

from store import digests, labels


def main() -> int:
    recent = digests.recent_digests(2)
    previous = next((d for d in recent if d.get("sent")), None)
    if previous is None:
        print("no previous digest to close")
        return 0
    rows = labels.mark_ignored(previous)
    labels.append_labels(rows)
    print(f"closed {previous['date']}: {len(rows)} ignored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
