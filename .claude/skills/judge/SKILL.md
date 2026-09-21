---
name: judge
description: Score today's candidate pool and write data/ranked.json
allowed-tools: Read, Write, WebFetch, Grep
---

# Judge

Score every candidate in `data/judge_input.json` and write `data/ranked.json`.

## Read first

1. `data/judge_input.json` — `candidates`, `recent_labels`, `recently_sent_titles`
2. `taste/profile.md` — both halves. The `## Mine` half is authoritative and
   overrides anything you infer.

`recent_labels` are the operator's verdicts on recent picks: `up` (good pick),
`down` (should not have been surfaced), `published` (strongest positive — they
actually used it), `ignored` (weak negative). Treat them as worked examples of
the operator's taste, not as rules.

## Method

1. Triage all candidates on title, source and metadata alone.
2. Choose 12-15 that look non-obvious or consequential and **fetch and read them**.
   Do not exceed 20 fetches. Ranking on titles alone is the failure mode this
   whole step exists to avoid.
3. Score every candidate, read or not.

**Discussion threads.** A candidate whose `meta.kind` is `"discussion"` is an HN text post —
an Ask HN or Tell HN thread. It has no article behind it, so it can never be a digest item:
a TLDR entry links to something readable. Do not spend fetches trying to rank one for
selection. They are still worth skimming, because a thread often names the paper or repo that
*is* the story — if you find one, look for it among the other candidates and let that finding
raise its score. Score discussion threads normally; the selection step filters them out, so
your score for them only affects the site's tail.

## Scoring

Two tiers, and the distinction matters:

- `headline` — big enough that not knowing it is a gap. Usually already
  saturated. Target about 3 per day.
- `discovery` — high signal, low saturation. The thing the operator would have
  found at 11pm if they kept scrolling. Target about 5 per day.

`saturation` (0-1) estimates how likely the operator has already seen it. A
2000-point HN post is ~0.95. A 14-hour-old arXiv paper with no traction is ~0.1.
**High saturation lowers a `discovery` score but does not lower a `headline`
score** — that is the whole point of having two tiers.

`score` (0-10) weighs:
- Does this change what a working engineer or researcher would do?
- Is it new information, or a rehash? Check `recently_sent_titles` and
  `data/digests/` before scoring something highly.
- Is it verifiable — a paper, a repo, an official post — rather than a rumor?
- Running code beats a description of the same idea.

Set `dedupe_of` to another candidate's `id` when two entries cover the same news,
and score the duplicate low.

## Output

Write `data/ranked.json`. Every candidate gets an entry, including rejects.

{
  "generated_at": "<UTC ISO-8601 with Z>",
  "pool_size": <int>,
  "read_count": <int>,
  "items": [
    {
      "id": "<candidate id, unchanged>",
      "url": "<candidate url>",
      "title": "<candidate title>",
      "source": "<candidate source>",
      "tier": "headline" | "discovery",
      "score": <0-10>,
      "saturation": <0-1>,
      "reason": "<one line: why this matters, or why it does not>",
      "read": <true if you fetched it>,
      "key_facts": ["<concrete facts from the article>"],
      "dedupe_of": <id or null>
    }
  ]
}

`reason` is required on **every** item, rejects included — it is what makes a bad
day debuggable. `key_facts` is how the Writer gets article content without
re-fetching, so fill it for everything you read: concrete, numeric, no adjectives.

Write the file and stop. Do not send anything.
