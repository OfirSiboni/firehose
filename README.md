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
| curator routine | Claude cloud routine, daily | Judge ranks, Writer drafts, publishes `docs/`; prompt in `routines/curator.md` |
| `send.yml` | Actions, on push to `data/digests/**` | Sends the digest to Telegram |
| `watchdog.yml` | Actions, daily 10:00 UTC | Alerts if no digest was committed today |

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
- `send/` — Telegram delivery and static-site publication
- `agents/` — plain-Python prep scripts that assemble each agent's input file
- `.claude/skills/` — the Judge, Writer and relearn agent prompts
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
5. Create two Claude Code cloud routines pointed at this repo: a daily one with the
   prompt in `routines/curator.md`, and a weekly one with the prompt in
   `routines/relearn.md`.

## Design

`docs/superpowers/specs/2026-09-21-tldr-curator-design.md`
