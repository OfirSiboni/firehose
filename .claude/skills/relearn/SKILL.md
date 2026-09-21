---
name: relearn
description: Rewrite the Learned half of taste/profile.md from accumulated feedback
allowed-tools: Read, Edit
---

# Relearn

Rewrite **only** the `## Learned` section of `taste/profile.md`.

## Read first

1. `data/relearn_input.json` — verdict counts, per-source breakdown, and the
   titles the operator accepted and rejected
2. `taste/profile.md` — both halves
3. `data/ranked.json` — the Judge's stored `reason` for recent items

Verdicts: `published` (strongest positive), `up`, `ignored` (weak negative),
`down` (strong negative). Most items are `ignored`; that is normal and it is a
weak signal, not a strong one — do not over-read it.

## Rules

- **Never modify the `## Mine` section.** It is the operator's own writing and
  it overrides anything you infer.
- Replace the entire `## Learned` section body. Do not append to it — stale
  inferences compounding is the failure this design exists to prevent.
- Write 3-7 bullets. Each must be a pattern a ranker could act on, stated
  concretely. "Rejects arXiv papers with no released code" is actionable;
  "prefers quality content" is not.
- Only claim a pattern the data supports. With fewer than 30 labels, write
  `_Not enough data yet (N labels)._` and nothing else.
- Do not restate anything already in `## Mine`.
- Where the Judge's `reason` shows it surfaced something for a stated purpose
  the operator then rejected, say so — that is the most correctable kind of
  mistake.

Edit the file and stop.
