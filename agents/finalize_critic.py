"""Un-blind the Critic's verdict and file it for the sender.

The Critic writes about `{{A}}` and `{{B}}` because it does not know which is
which. Only this script holds the key, so only this script can name them.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from agents.prepare_critic import INPUT_PATH, KEY_PATH, NAMES
from store import REPO_ROOT, critique

VERDICT_PATH = REPO_ROOT / "data" / "critique_verdict.json"


def _replacements(key: dict) -> dict[str, str]:
    return {side: NAMES[key[side]] for side in ("A", "B")}


def reveal(text: str, key: dict) -> str:
    """Swap the placeholders — and any stray "Newsletter A" — for real names."""
    names = _replacements(key)
    for side, name in names.items():
        text = text.replace("{{" + side + "}}", name)
        text = re.sub(rf"\bnewsletter {side}\b", name, text, flags=re.IGNORECASE)
    return text


def build(verdict: dict, key: dict) -> dict:
    winner = str(verdict.get("winner", "")).strip().upper()
    sides = {
        key[side]: {
            note: reveal(str(verdict.get(f"{side.lower()}_{note}", "")).strip(), key)
            for note in ("strength", "weakness")
        }
        for side in ("A", "B")
    }
    return {
        "date": key["date"],
        "winner": NAMES.get(key.get(winner, ""), "tie"),
        "verdict": reveal(str(verdict.get("verdict", "")).strip(), key),
        "ours": sides["firehose"],
        "theirs": sides["tldr"],
        "blind_order": {"A": NAMES[key["A"]], "B": NAMES[key["B"]]},
    }


def main() -> int:
    if not VERDICT_PATH.exists() or not KEY_PATH.exists():
        print("no blind verdict to finalize")
        return 0

    key = json.loads(KEY_PATH.read_text(encoding="utf-8"))
    verdict = json.loads(VERDICT_PATH.read_text(encoding="utf-8"))
    built = build(verdict, key)
    critique.save_critique(built, key["date"])

    # The key and the raw A/B verdict are scratch. Leaving them behind would
    # let a later run send yesterday's opinion.
    for path in (KEY_PATH, VERDICT_PATH, Path(INPUT_PATH)):
        path.unlink(missing_ok=True)
    print(f"critique {key['date']}: winner {built['winner']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
