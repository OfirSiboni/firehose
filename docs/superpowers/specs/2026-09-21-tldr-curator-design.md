# TLDR AI Curator — Design

**Date:** 2026-09-21
**Status:** Approved

## Purpose

A daily tool that compresses the AI-news firehose into a reviewable shortlist, so that
selecting and writing 6–8 stories takes an hour instead of an evening of scrolling.

Context: the [TLDR AI Curator role](https://jobs.ashbyhq.com/tldr.tech/038c4419-5b48-4279-a75e-6f7a0afdb240)
asks for a person who picks 6–8 stories five days a week from x.com, arXiv, Hacker News,
Discord, GitHub, and AI company blogs, and writes concise summaries.

The system does **not** replace curatorial judgment. It raises recall (surface what a human
would otherwise miss) and removes blank-page cost (draft summaries that are edited, not
written). Selection stays human, and the feedback loop encodes *this operator's* taste
rather than a generic notion of importance.

**Primary success criterion:** the operator reads it every morning and stops scrolling
elsewhere. Reliability outranks sophistication throughout.

## Scope

**In scope (v1):** Hacker News, arXiv, GitHub, AI company blogs (RSS). Telegram channel
delivery. GitHub Pages + RSS publication. Reaction-based feedback capture. Weekly
regeneration of a learned taste profile.

**Deferred:** x.com and Discord ingestion. The X API's usable tier is ~$200/mo, and every
free workaround (nitter, RSSHub, cookie scraping) fails silently — the worst property for a
daily tool. Discord requires a bot invited to servers the operator does not control.
Interim workaround: the operator forwards links to the bot manually.

**Deferred (Phase 7):** trained scorer. Design seams are specified below; nothing is built.

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Runtime | Split: GitHub Actions for code, a Claude cloud routine for judgment | Each runs what it is best at — see below |
| Repo visibility | Public | Unmetered Actions minutes; doubles as a portfolio artifact |
| Claude auth | The routine runs as a Claude Code cloud session on the operator's account | No metered API billing, and no dependence on an OAuth token surviving in CI |
| Architecture | Plain-code ingest/send, two agents (Judge, Writer) | Taste and voice tune independently |
| Storage | Files in the repo | Free, versioned, diffable; agent reads/writes natively |
| Feedback | Telegram emoji reactions | No `answerCallbackQuery` round-trip, so no spinner on a 3h poll |
| Learning | Prompt-level: exemplars + regenerated profile section | Works from day one; inspectable and hand-editable |

### Why the runtime is split

Three constraints decide this, and each piece lands where it costs least:

- **Ingest needs no Claude and no secrets.** It is pure Python over public APIs, so it runs
  in GitHub Actions on a 3-hour cron. Spending subscription usage on it would be waste.
- **The Judge and Writer need Claude but no secrets.** They read the repo, rank, draft, and
  commit. A Claude **cloud routine** runs them daily: it clones the repo, has Bash/Read/Write,
  runs unattended in Anthropic's cloud with the operator's machine off, and bills as a Claude
  Code cloud session on the operator's account rather than as metered API usage. Publishing
  the static site and RSS is part of this step, because a commit needs no credentials.
- **Telegram delivery needs a secret and no Claude.** Cloud routines have no secrets store —
  no local environment variables, connectors only — so the bot token cannot live there
  safely. A GitHub Actions job holds it, triggered **on push to `data/digests/**`**, so it
  fires when the routine commits the day's digest. Event-triggered rather than time-coupled,
  so a slow routine run never races the sender.

The Claude Code GitHub Action does support subscription auth via `CLAUDE_CODE_OAUTH_TOKEN`
(`claude setup-token`), and an Actions-only deployment is viable. The routine is preferred
because it removes a dependency: no long-lived token to expire in CI, and the judgment step
runs on the same surface the operator can invoke by hand.

**Nothing about this is baked into the code.** Every step is either plain Python with a file
contract or a Claude skill with a file contract, so `claude "/judge"` is the identical command
whether a routine, an Actions job, or the operator's terminal runs it. Changing harness is a
configuration change, and the Judge can be run by hand at any time to see what it would pick.

Routine constraints worth recording: cron is UTC with a **1-hour minimum interval** (fine —
the routine runs daily), the routine needs the repo's GitHub URL, and it cannot reach local
files or local environment variables.

### Why the Claude step is an agent, not an API call

Ranking must be based on article content, not titles. As a single API call this is
chicken-and-egg: the fetch set must be chosen before the model has seen anything. Fetching
all ~60 candidates is wasteful; fetching none means ranking headlines; heuristically
pre-selecting means doing the judging in Python. As an agent, choosing what to investigate
*is* the judgment, and only the model can make it.

Accepted costs: variable runtime and turn count (capped), reduced reproducibility (tolerable
for news curation), and contract-level rather than output-level testing.

Secondary constraint: a Claude subscription authenticates the Claude Code Action but cannot
authenticate raw Messages API calls, so the agent harness is also the only available path.

## Architecture

### Repository layout

```
tldrcreator/
├─ .github/workflows/
│  ├─ ingest.yml              cron every 3h — plain Python, no LLM
│  └─ digest.yml              cron daily 07:00 — Judge → Writer → send
├─ .claude/skills/
│  ├─ judge/SKILL.md          Judge agent prompt
│  ├─ writer/SKILL.md         Writer agent prompt
│  └─ relearn/SKILL.md        weekly taste-profile regeneration
├─ ingest/
│  ├─ item.py                 Item model, URL normalization, dedupe
│  ├─ pool.py                 append / expire / load-unsent
│  ├─ sources/{hn,arxiv,github,blogs}.py
│  ├─ feeds.txt               blog feed list, one URL per line, # comments
│  └─ run.py                  fetch → normalize → dedupe → append
├─ send/
│  ├─ telegram.py             post digest, collect reactions
│  └─ publish.py              render Pages HTML + RSS
├─ taste/
│  ├─ profile.md              two halves: Mine (authoritative) / Learned (regenerated)
│  └─ voice.md                writing style rules
├─ data/
│  ├─ pool.jsonl              rolling 7-day candidate pool
│  ├─ labels.jsonl            feedback, append-only
│  ├─ tg_offset.txt           Telegram getUpdates cursor
│  └─ digests/YYYY-MM-DD.json
├─ docs/                      GitHub Pages output
└─ tests/
```

No database. Files in the repo are free, versioned, diffable, and readable by the agent with
the tools it already has. Each day's digest and each label is a commit, producing a complete
audit trail of what the system thought and what the operator thought of it.

### Data flow

```
every 3h   ingest.yml                                   [GitHub Actions — no Claude]
           ├─ fetch HN / arXiv / GitHub / blogs        (plain Python)
           ├─ normalize + dedupe → append pool.jsonl
           ├─ expire entries older than 7 days
           ├─ drain Telegram reactions → labels.jsonl   ← sole consumer
           └─ commit

daily      curator routine                              [Claude cloud routine]
           ├─ clone repo (sees the pool Actions committed)
           ├─ mark yesterday's unreacted items as "ignored"
           ├─ prepare_judge.py → judge_input.json       (plain Python)
           ├─ JUDGE          pool (last 36h, unsent) + taste/profile.md
           │                  + last 20 labels + last 7 digests
           │                  fetches and reads promising links
           │                  → ranked.json
           ├─ validate       schema; abort before writing on failure
           ├─ prepare_writer.py → writer_input.json     (plain Python)
           ├─ WRITER         top 8 + key_facts → data/digests/DATE.json
           ├─ publish.py     docs/index.html, docs/DATE.html, docs/feed.xml
           └─ commit + push                             ← no secrets needed

on push to data/digests/**  send.yml                    [GitHub Actions — holds the token]
           └─ telegram.py    header + 8 messages to the channel, records message_ids

daily 10:00  watchdog.yml                               [GitHub Actions]
           └─ no digest committed for today? → Telegram alert
```

The send job is triggered by the routine's own push rather than by a clock, so a slow or
retried routine run can never race it. It is idempotent — it checks the digest's `sent` flag
— so a re-push cannot double-send.

Only the ingest job drains Telegram: `getUpdates` supports one consumer, or the offset
cursor races. A 3h cadence keeps collection well inside Telegram's 24h update retention.

## Components

### Item model and dedupe

Canonical record appended to `pool.jsonl`:

```json
{
  "id": "sha1(normalized_url)[:12]",
  "url": "https://...",
  "normalized_url": "...",
  "title": "...",
  "source": "hn|arxiv|github|blog",
  "first_seen": "2026-09-21T06:00:00Z",
  "text": "abstract / excerpt / README intro — full text preserved",
  "meta": {"points": 412, "comments": 88},
  "sent_in": null
}
```

`meta["kind"]` is `"article"` or `"discussion"`. Only HN sets it meaningfully: Algolia
returns `url: null` for text posts (Ask HN, Tell HN, jobs), where the thread *is* the
content. Those are tagged `discussion`, fall back to the HN permalink as their URL, and are
**never eligible for a digest** — a TLDR item links to a readable artifact, and a discussion
thread is not one. They stay in the pool because they are real research signal, and they
appear in the site's tail. Enforcement lives in `ranked.top()`, which excludes them using ids
derived from the pool; a prompt rule would be advisory, and this failure would be silent.

Source text arrives as HTML from both HN (`story_text`) and RSS feeds, with tags and escaped
entities — often double-escaped, so XML unescaping alone is not enough. A single
`ingest.text.plain()` helper strips tags, decodes entities, and collapses whitespace for both
sources, so the Judge reads prose rather than `I&#x27;m a 24 y&#x2F;o`.

`text` is preserved in full because it is the training input for the deferred scorer.
Nothing is embedded at ingest time — Anthropic serves no embedding endpoint, and adding a
second vendor for an unbuilt feature is premature. Preserving text keeps the option open at
zero cost.

URL normalization must collapse: `utm_*` and `ref` query params, trailing slashes,
`http`→`https`, `www.` prefix, arXiv `/pdf/` → `/abs/` and version suffixes.

Pool entries expire after 7 days.

### Judge agent

Skill at `.claude/skills/judge/SKILL.md`, invoked as `prompt: "/judge"`.

**Reads:** unsent pool items from the last 36h; `taste/profile.md`; the last 20 labels as
worked examples; the last 7 digests (rehash detection).

**Does:** triages all candidates on metadata, selects ~12–15 worth opening, fetches and reads
them, scores every candidate, writes `data/ranked.json`.

**Two tiers.** An aggregator ranking by popularity is redundant — a 2,000-point HN post has
already been seen. Saturation is an input to the score:

- `headline` — big enough that not knowing it is a gap. Usually saturated. Target 3/day.
- `discovery` — high signal, low saturation. Target 5/day.

**Output contract (`data/ranked.json`):**

```json
{
  "generated_at": "2026-09-21T07:02:11Z",
  "pool_size": 61,
  "read_count": 14,
  "items": [{
    "id": "a3f9c21b4e07",
    "url": "https://arxiv.org/abs/...",
    "title": "...",
    "source": "arxiv",
    "tier": "discovery",
    "score": 8.5,
    "saturation": 0.2,
    "reason": "New KV-cache eviction policy, 3.1x throughput at same quality; authors are the FlashAttention group. 14h old, no HN traction yet.",
    "read": true,
    "key_facts": ["3.1x throughput vs baseline", "drop-in, no retraining", "code released"],
    "dedupe_of": null
  }]
}
```

`reason` is required for **every** item, rejects included — this is what makes a bad day
debuggable rather than mysterious. `key_facts` carries article content to the Writer so it
never re-fetches.

Guardrails: `--max-turns 40`; at most ~20 URL fetches.

### Writer agent

Skill at `.claude/skills/writer/SKILL.md`.

**Reads:** top 8 of `ranked.json` (with `key_facts`); `taste/voice.md`.
**Writes:** `data/digests/YYYY-MM-DD.json` — per story: headline, 2–3 sentence summary, URL,
tier, read time. Plus a digest-level header line.

Voice rules (in `taste/voice.md`, deliberately short so output stays stable):

- Lead with what changed, never with who announced it
- Numbers instead of adjectives — "3.1x throughput", not "dramatically faster"
- Banned: revolutionary, game-changing, groundbreaking, breakthrough
- Assume the reader knows what a transformer is
- No editorializing; hype should have been cut by the Judge

Guardrail: `--max-turns 10`.

### Taste profile

`taste/profile.md` has two halves with different ownership:

```markdown
## Mine (authoritative — never auto-edited)
- Always: inference infrastructure, eval methodology, DeepSeek/Qwen releases
- Never: funding rounds under $50M, crypto, "X is dead" takes,
  model rumors without a primary source
- I care more about how things are served than how they're trained

## Learned (regenerated weekly from labels — edit freely, it will be overwritten)
- Rejects ~80% of arXiv items with no released code
- Accepts benchmark posts only when the benchmark itself is new
```

The hand-written half is never touched. The learned half is regenerated wholesale each week.
This is the fix for the standard feedback-loop failure: the system infers something wrong, it
compounds, and there is nowhere to go to unlearn it. Here it is one line in one file.

### Feedback

Native Telegram emoji reactions, not inline buttons. A tapped inline button spins until the
bot calls `answerCallbackQuery`; on a 3-hour poll that spinner times out, and a feedback
mechanism that feels broken stops being used.

**Open risk:** receiving `message_reaction` updates requires listing it in `allowed_updates`,
and in a **channel** the bot must be an admin. Verify with a short spike before building on
it. Fallback if it does not work: inline buttons, accepting the delayed acknowledgement.

One message per story (plus a header message) — separate messages are what make per-story
reactions possible.

| Gesture | `verdict` | Weight |
|---|---|---|
| 👍 | `up` | strong positive |
| 👎 | `down` | strong negative |
| ✍️ | `published` | strongest positive |
| none after 24h | `ignored` | weak negative |

`ignored` is recorded automatically when the next digest runs. Most items receive no
reaction; treating that as *no data* discards the majority of the signal, while treating it
as a *weak* negative is both accurate and free.

```jsonl
{"ts":"2026-09-21T09:14:02Z","digest_date":"2026-09-21","item_id":"a3f9c21b4e07","url":"...","title":"...","tier":"discovery","source":"arxiv","verdict":"published"}
```

### Publication

`publish.py` writes static files with one HTML template and no framework:

- `docs/index.html` — today: the 8 with summaries, then the ~20-item tail
- `docs/YYYY-MM-DD.html` — archive
- `docs/feed.xml` — RSS

RSS is how the "email" requirement is met without building email: any reader subscribes, and
others can follow. Real SMTP delivery is one additional file if wanted later, not a redesign.

### Weekly relearn

Sunday run of `.claude/skills/relearn/SKILL.md`: read all of `labels.jsonl` plus the Judge's
stored `reason` for each labelled item, rewrite **only** the `## Learned` half of
`taste/profile.md`, commit directly to main.

No PR gate — the change is a git commit, so the diff is the review and a bad week is one
`git revert` away. The stored `reason` values matter here: they show not only what was
rejected but what the system believed it was surfacing, which is where correctable mistakes
live.

## Error handling

| Failure | Handling |
|---|---|
| A source 404s, changes format, or rate-limits | Per-source try/except; ingest never fails wholesale. A source returning 0 items for 3 consecutive runs is flagged in the next digest header |
| Malformed `ranked.json` | Schema validation before send; job fails, nothing is sent |
| Agent hits max-turns without writing output | Same path — missing output file fails the job |
| **The routine dies entirely** (cloud failure, repo access lost, a bad prompt edit) | A routine cannot post its own failure — it holds no Telegram token, and a dead run reports nothing. So a separate `watchdog.yml` runs at 10:00 and alerts if no digest exists for today. This is the only failure detector for the judgment half; without it, digests simply stop and go unnoticed for days |
| A GitHub Actions job dies | `if: failure()` step posts to Telegram with the run URL |
| Thin day — fewer than 8 clear the bar | Send fewer. Never pad. A curator who fills quota with filler stops being read |
| Judge ranks a discussion thread highly | `ranked.top()` excludes it using pool-derived ids. Enforced in code, so a prompt regression cannot publish an unlinkable item |
| Ingest and digest both writing `data/` | `concurrency` group so runs queue; `git pull --rebase` before push |
| Job re-run after partial failure | Digest checks for an existing `data/digests/TODAY.json` marked sent; idempotent |

GitHub disables cron on public repos after 60 days of inactivity; this repo commits every
three hours, so it never goes quiet.

## Testing

**Parsing.** Each source module has a recorded fixture response; tests assert `normalize()`
produces the right shape. Offline and instant. A `--smoke` flag hits all sources live and
asserts each returns more than zero items. Fixtures catch local regressions; smoke catches
upstream changes.

**Dedupe.** One test over a list of URL pairs that must collapse (`utm_*`, trailing slash,
scheme, `www.`, arXiv `/abs/` vs `/pdf/`). This is where near-duplicates leak through and
make a digest look sloppy.

**Agent output.** Contract tests only, never text assertions: valid schema, at most 8 items,
scores in range, every `id` present in the pool, no duplicate ids. Runs before send, so a bad
Judge run never reaches the channel.

**Golden day.** One real `pool.jsonl` committed to `tests/fixtures/`. Re-run the Judge against
it after any prompt change and read the picks. Not automated — selection is a judgment task
and asserting on it would be dishonest — but it makes prompt changes comparable instead of
vibes-based.

## Build order

Phases 1 and 2 ship deliberately **without** Claude. This provides a baseline the agent must
beat and real labels that predate the agent. Built the other way round, there is no way to
answer whether the LLM is helping. It also puts a working daily digest in place by day two,
which is what makes the project get finished.

| Phase | Deliverable | Effort |
|---|---|---|
| 0 | Repo, HN only, pool printed to stdout | ½ day |
| 1 | All four sources, dedupe, `ingest.yml` on cron. **Then run 3 days and read `pool.jsonl`** — are the right stories present? Recall precedes ranking; an absent story cannot be ranked | 1 day |
| 2 | Telegram channel, reactions, top-20-by-recency baseline | 1 day |
| 3 | Judge agent, `ranked.json`, validation. Compare against the baseline | 1–2 days |
| 4 | Writer agent and voice | ½ day |
| 5 | Pages and RSS | ½ day |
| 6 | Weekly relearn | ½ day |
| 7 | Trained scorer (~200 labels) — deferred | later |

Roughly four to five evenings to Phase 5.

## Deferred: trained scorer (Phase 7)

Nothing is built now, but three seams accumulate from day one so this is later a weekend
project rather than an archaeology project:

- `labels.jsonl` keys every verdict to a stable `item_id`
- `ranked.json` is committed daily, preserving the LLM's score for comparison
- **`data/digests/YYYY-MM-DD.json` carries each sent item's full `text`** — not just
  its summary

That third point is a correction. An earlier version of this spec named `pool.jsonl` as the
place full text accumulates, which contradicts the 7-day expiry two sections above: at ~200
labels (25+ days at 8 stories/day), most labelled items would have been expired out of the
pool weeks before the scorer was ever trained, and the corpus would have to be rebuilt by
walking git history — exactly the archaeology the seam exists to prevent.

Digests are permanent, one file per day, never expired, and already keyed by `item_id`. So
the training corpus is `digests/ × labels.jsonl`, joined on `item_id`, with no new file and
no migration. The pool keeps full `text` too, but only as working data for the Judge; its
7-day window is now purely an operational bound rather than a promise about history.

At ~200 labels: `scorer/train.py` embeds `title + key_facts`, fits a logistic regression,
commits `model.pkl`. The Judge receives the model's prior as one additional input. If it
never beats the prompt, the cost is one weekend and one deleted file.

## Secrets

| Secret | Where | Source |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | GitHub Actions secrets | @BotFather |
| `TELEGRAM_CHAT_ID` | GitHub Actions secrets | Channel id; bot added as admin |

That is the whole list. The judgment half needs no credential at all: the routine
authenticates as the operator's own Claude Code cloud session and pushes to the repo it was
given. Nothing expires, so there is no token-rotation chore.

Never put the bot token in a routine prompt. Routine prompts are stored configuration, not a
secrets store, and the token would sit in plaintext in a place not built to hold it. If the
Telegram step ever needs to move out of Actions, add a proper secrets mechanism first.

*(If the deployment is ever flipped to Actions-only, a `CLAUDE_CODE_OAUTH_TOKEN` from
`claude setup-token` goes in Actions secrets. It is long-lived but does expire, and the
watchdog above is what would make that expiry visible.)*
