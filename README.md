# firehose

A daily AI-news curator. Collects from Hacker News, arXiv, GitHub and AI company
blogs; a Claude agent ranks and drafts the best 6-8 stories; the result goes to a
Telegram channel and a static site.

Selection stays human. The system raises recall and removes blank-page cost, and
learns which stories are worth surfacing from emoji-reaction feedback.

## How it runs

| Workflow | Cadence | What it does |
|---|---|---|
| `ingest.yml` | Actions, every 3h | Fetch sources, dedupe into `data/pool.jsonl`, collect Telegram reactions |
| curator routine | Claude cloud routine, daily | Judge ranks, Writer drafts, Critic compares, publishes `docs/`; prompt in `routines/curator.md` |
| `send.yml` | Actions, on push to `data/digests/**` | Sends the digest to Telegram |
| `watchdog.yml` | Actions, daily 10:00 UTC | Alerts if no digest was committed today |

## The blind verdict

Each day, after the digest is drafted, the same day's [TLDR AI](https://tldr.tech/ai)
issue is fetched and put next to ours with every tell removed — no URLs, no source
labels, no reading times, no brand names, and the two sides shuffled into `A` and `B`.
A fresh subagent (`.claude/skills/critic/SKILL.md`) reads only that blinded file and
picks a winner; a second script holds the key and names the sides afterwards.

The verdict lands in `data/critique/<date>.json` and is sent to Telegram as one extra
message after the stories. `send.publish` never reads it, so it never reaches
`docs/` — the site and the Markdown mirror are unchanged. On a weekend, or any day
TLDR does not publish, the comparison is skipped silently.

Plus a weekly relearn routine (Claude cloud routine, weekly) that regenerates the
learned half of the taste profile; prompt in `routines/relearn.md`.

## Local use

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
.venv/Scripts/python -m ingest.run --smoke   # check every source is alive
.venv/Scripts/python -m ingest.run           # fetch into data/pool.jsonl
.venv/Scripts/python -m pytest -q
```

## Layout

- `store/` — item model, pool, labels, digests, schema validation
- `ingest/` — one module per source, plus `feeds.txt` (the blog list; edit this, not code)
  and `tldr.py`, which reads the rival newsletter for the daily blind comparison
- `send/` — Telegram delivery and static-site publication (HTML, Markdown, RSS)
- `agents/` — plain-Python prep scripts that assemble each agent's input file
- `.claude/skills/` — the Judge, Writer, Critic and relearn agent prompts
- `routines/` — the prompts pasted into the daily and weekly Claude cloud routines
- `taste/profile.md` — what counts as a good story. Hand-edit the `## Mine` half freely.

## Setup

1. Create a Telegram bot ([@BotFather](https://t.me/BotFather)) and a channel, and add
   the bot as an admin of the channel.
2. Add two Actions secrets to the repo: `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`
   (the channel id).
3. Under repo Settings → Actions → General, give the default `GITHUB_TOKEN`
   "Read and write permissions" so the workflows can commit `data/` and `docs/`.
4. Under repo Settings → Pages, serve from the `master` branch, `/docs` folder.
   Each day publishes three files there: `<date>.html` (and `index.html`),
   `<date>.md` (and `latest.md`), and `feed.xml`. The Markdown carries no YAML
   front matter on purpose — Pages runs Jekyll, and front matter would make it
   render `<date>.md` over the `<date>.html` written next to it.
5. Create two Claude Code cloud routines pointed at this repo: a daily one with the
   prompt in `routines/curator.md`, and a weekly one with the prompt in
   `routines/relearn.md`.

## Design

`docs/superpowers/specs/2026-09-21-tldr-curator-design.md`
