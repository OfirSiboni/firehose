"""Put today's digest next to TLDR AI's, with every tell removed.

The Critic must not be able to work out which newsletter is ours, so the
blinding happens here, in plain Python, and the key is written to a file the
Critic is told not to read. `data/critique_input.json` carries titles and
summaries only: no URLs (TLDR's tracking domains would give it away), no source
labels, no reading times, and no brand names.
"""

from __future__ import annotations

import argparse
import json
import random
import re
from datetime import datetime, timezone
from pathlib import Path

from ingest import tldr
from store import REPO_ROOT, digests

INPUT_PATH = REPO_ROOT / "data" / "critique_input.json"
KEY_PATH = REPO_ROOT / "data" / ".critique_key.json"

# Both feeds get the same number of stories: a list twice as long reads as a
# different kind of product, and length is not what is being judged.
LIMIT = 8

NAMES = {"firehose": "Firehose", "tldr": "TLDR AI"}

_BRAND = re.compile(r"\b(tldr(\.tech)?|firehose)\b", re.IGNORECASE)


def scrub(text: str) -> str:
    """Remove the two newsletters' own names from prose."""
    return " ".join(_BRAND.sub("[redacted]", str(text or "")).split())


def blind(ours: list[dict], theirs: list[dict], rng: random.Random) -> tuple[dict, dict]:
    """Return `(input_payload_fragment, key)` with the two sides shuffled."""
    sides = {
        "firehose": [
            {
                "title": scrub(tldr.READ_SUFFIX.sub("", item["title"])),
                "summary": scrub(tldr.READ_SUFFIX.sub("", item.get("summary", "").strip())),
            }
            for item in ours[:LIMIT]
        ],
        "tldr": [
            {"title": scrub(item["title"]), "summary": scrub(item["summary"])}
            for item in theirs[:LIMIT]
        ],
    }
    order = ["firehose", "tldr"]
    rng.shuffle(order)
    key = {"A": order[0], "B": order[1]}
    return {"newsletter_a": sides[key["A"]], "newsletter_b": sides[key["B"]]}, key


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--html",
        type=Path,
        help="read the TLDR issue from a file instead of fetching it, for when "
        "outbound HTTP is blocked and the page was fetched by other means",
    )
    args = parser.parse_args()

    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    digest = digests.load_digest(date)
    if not digest or not digest.get("items"):
        print("no digest today; nothing to compare")
        return 0

    theirs = (
        tldr.parse(args.html.read_text(encoding="utf-8"))
        if args.html
        else tldr.fetch(date)
    )
    if not theirs:
        # A weekend, a holiday, or a page shape that changed. Either way the
        # comparison is skipped: half a head-to-head is worse than none.
        print("no tldr issue today; skipping the comparison")
        INPUT_PATH.unlink(missing_ok=True)
        KEY_PATH.unlink(missing_ok=True)
        return 0

    payload, key = blind(digest["items"], theirs, random.SystemRandom())
    INPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    INPUT_PATH.write_text(
        json.dumps({"date": date, **payload}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    KEY_PATH.write_text(
        json.dumps({"date": date, **key}, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(
        f"critique input: {len(payload['newsletter_a'])} vs "
        f"{len(payload['newsletter_b'])} stories, blinded"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
