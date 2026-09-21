# Firehose — Tasks 7–15 reworked for the split runtime

Replaces Tasks 7–15 of `docs/superpowers/plans/2026-09-21-tldr-curator.md` (the "original
plan"). Spec: `docs/superpowers/specs/2026-09-21-tldr-curator-design.md`, section "Why the
runtime is split" and "Data flow" are authoritative.

Where a task below says "verbatim from original plan lines X–Y", copy that code exactly,
except for the global adjustments listed here.

## Global Constraints

- All global constraints of the original plan (lines 13–23) still hold, except secrets:
  the only secrets are `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`, in GitHub Actions.
  No `CLAUDE_CODE_OAUTH_TOKEN`, no `anthropics/claude-code-action`.
- **Paths:** existing modules anchor data paths on `store.REPO_ROOT`
  (e.g. `POOL_PATH = REPO_ROOT / "data" / "pool.jsonl"`). Every new module-level path
  constant (`DIGEST_DIR`, `LABELS_PATH`, `OFFSET_PATH`, `RANKED_PATH`, `INPUT_PATH`, `DOCS`)
  does the same instead of a bare relative `Path("data/...")`.
- Project name is **firehose**. Git bot identity in workflows: `firehose-bot` /
  `firehose-bot@users.noreply.github.com`. Default branch is `master`.
- Site URL: `https://ofirsiboni.github.io/firehose`.
- The recency baseline (`send/baseline.py`) is not built.
- Run tests with `.venv/Scripts/python -m pytest -q`.

---

### Task A: Storage, Telegram client, feedback, ingest workflow

Original Tasks 7, 8 and 9, minus the baseline sender and minus every manual/ops step
(bot setup, sending real messages, reaction verification, pushing, Actions-tab checks).

**Files:**
- Create: `store/digests.py`, `tests/test_digests.py` — verbatim from original plan lines 1750–1833
- Create: `send/__init__.py` (empty), `send/telegram.py` — verbatim from lines 1839–1876
- Create: `store/labels.py`, `tests/test_labels.py` — verbatim from lines 2007–2225
- Modify: `send/telegram.py` — append `get_updates`, lines 2240–2251
- Modify: `ingest/run.py` — add `collect_feedback`, lines 2257–2290 (imports go at the top
  of the file with the other imports, not above `main`)
- Create: `.github/workflows/ingest.yml` — from lines 1595–1636 with these changes:
  - the "Fetch sources into the pool" step gets
    `env: TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}` (it drains reactions)
  - bot identity per Global Constraints
  - add a final step `Report failure to Telegram`, `if: failure()`, env
    `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` from secrets and
    `RUN_URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}`,
    running `python -m send.alert` (created in Task C)

**Verify:** full test suite passes, including the 3 digest and 10 label tests.
Commit: `feat: digests, telegram client, reaction feedback, ingest workflow`.

---

### Task B: Judge, Writer, publish, relearn — the Python and the skills

Original Tasks 11, 13, 14, 15 — only the Python modules, tests, taste files and skills.
No workflow YAML, no local `claude` runs, no GitHub Pages steps.

**Files:**
- Create: `taste/profile.md`, `taste/voice.md` — lines 2501–2549
- Create: `store/ranked.py`, `tests/test_ranked.py` — lines 2555–2744
- Create: `agents/__init__.py` (empty), `agents/prepare_judge.py` — lines 2760–2797
- Create: `.claude/skills/judge/SKILL.md` — lines 2803–2895. The Output block (lines
  2869–2888) is inside the skill as shown; keep it unfenced exactly as the plan has it.
- Create: `tests/fixtures/golden_pool.jsonl` — a copy of `data/pool.jsonl`
- Create: `agents/prepare_writer.py`, `tests/test_prepare_writer.py` — lines 3118–3218
- Create: `.claude/skills/writer/SKILL.md` — lines 3232–3277
- Create: `send/publish.py`, `tests/test_publish.py` — lines 3352–3519, with
  `SITE_URL = "https://ofirsiboni.github.io/firehose"` and the page/feed titles
  `Firehose — {date}` / `Firehose` instead of `TLDR AI …`. Update the test expectations
  only where they depend on those strings (they currently do not).
- Create: `agents/prepare_relearn.py`, `tests/test_prepare_relearn.py` — lines 3581–3670
- Create: `.claude/skills/relearn/SKILL.md` — lines 3684–3723

**Verify:** full suite passes (adds 11 ranked, 5 writer, 4 publish, 4 relearn tests).
Commit: `feat: judge, writer, publish and relearn — modules, skills, taste`.

---

### Task C: Split-runtime glue — sender, watchdog, workflows, routine prompts

New code. Depends on A and B.

**Files:**
- Create: `send/alert.py` — verbatim from lines 2339–2363, but the message text comes from
  env `ALERT_TEXT` when set, defaulting to the original "digest failed" text.
- Create: `send/close_yesterday.py` — verbatim from lines 2367–2389.
- Create: `send/digest.py` — the Telegram sender run by `send.yml`. Based on lines
  2957–3030 with these differences:
  - Sends the **newest** digest file (`digests.recent_digests(1)`), not "today's", so a
    routine that finishes near midnight still sends. No digest, or `sent: true` → print
    and return 0 (idempotent).
  - Items come only from that digest file (the Writer wrote it). No fallback to
    `ranked.top`.
  - Header: `<b>Firehose — {date}</b>` then `{n} stories`; append
    `· {pool_size} candidates · {read_count} read in full` only if
    `store.ranked.load_ranked` succeeds (wrap in try/except — the header must not block
    sending). Keep the `health.dead_sources(3)` warning line.
  - After sending: save the digest with `sent: True` and each item's `message_id`; mark
    those ids sent in the pool (`pool.mark_sent`, `pool.save_pool`).
  - Pure function `render(item) -> str` as in the original; add a small test file
    `tests/test_digest_send.py` covering: `render` escapes HTML in title; `main` returns 0
    and sends nothing when the newest digest is already sent (monkeypatch
    `digests.DIGEST_DIR` to tmp_path and `send.digest.send_message` to a stub that fails
    the test if called; set the two env vars with monkeypatch).
- Create: `send/watchdog.py` — if `digests.load_digest(<today UTC>)` is None, send
  `⚠️ <b>no digest today</b>\nThe curator routine did not commit data/digests/{date}.json.`
  via `send_message` and return 0. Otherwise print "ok" and return 0.
- Create: `.github/workflows/send.yml` — `on: push` to `branches: [master]` with
  `paths: ["data/digests/**"]`, plus `workflow_dispatch`. Same concurrency group
  `data-write`, `contents: write`. Steps: checkout, python 3.11 + pip cache, install,
  `python -m send.digest` with both Telegram secrets in env, commit
  `data/` as `chore: sent digest $(date -u +%Y-%m-%d)` with the same
  "no changes → exit 0; pull --rebase; push" shell as ingest.yml, and the same
  `if: failure()` alert step as ingest.yml. (Pushes made with the default GITHUB_TOKEN do
  not trigger workflows, so the job's own commit cannot re-trigger it.)
- Create: `.github/workflows/watchdog.yml` — `schedule: cron "0 10 * * *"` plus
  `workflow_dispatch`, `contents: read`; checkout, python, install,
  `python -m send.watchdog` with both secrets.
- Create: `routines/curator.md` — the prompt pasted into the daily Claude cloud routine.
  Plain numbered steps the routine executes in the cloned repo:
  1. `pip install -r requirements.txt`
  2. `python -m send.close_yesterday`
  3. `python -m agents.prepare_judge`
  4. Follow `.claude/skills/judge/SKILL.md` exactly (writes `data/ranked.json`)
  5. Validate: `python -c "from store import pool, ranked; ranked.load_ranked({i.id for i in pool.load_pool()})"` — if it fails, stop: commit nothing.
  6. `python -m agents.prepare_writer`
  7. Follow `.claude/skills/writer/SKILL.md` exactly (writes `data/digests/<date>.json`, `sent: false`)
  8. `python -m send.publish`
  9. `git add data/ docs/ && git commit -m "chore: digest <date>"`, then
     `git pull --rebase` and `git push` to `master`. Never send to Telegram; never add
     secrets. A push is what triggers delivery.
  Plus one line at the top stating the routine's purpose and that it needs no credentials.
- Create: `routines/relearn.md` — weekly routine prompt: install,
  `python -m agents.prepare_relearn`, follow `.claude/skills/relearn/SKILL.md`, verify with
  `git diff taste/profile.md` that only the `## Learned` section changed (if `## Mine`
  changed, `git checkout taste/profile.md` and stop), commit
  `chore: relearn taste profile <date>`, pull --rebase, push.
- Create: `README.md` — original lines 1642–1680 with: title `# firehose`; the "How it
  runs" table replaced by four rows — `ingest.yml` (Actions, every 3h), curator routine
  (Claude cloud routine, daily, prompt in `routines/curator.md`), `send.yml` (Actions, on
  push to `data/digests/**`), `watchdog.yml` (Actions, daily 10:00 UTC) — plus relearn
  routine (weekly, `routines/relearn.md`); Layout gains `agents/` and `routines/`. Add a
  short "Setup" section: Telegram bot + channel (bot as admin), the two Actions secrets,
  Actions "Read and write" permissions, Pages from `master` `/docs`, and creating the two
  routines from the prompt files.

**Verify:** full suite passes. `python -c "import yaml"` is not available — instead
eyeball each workflow file for valid YAML indentation.
Commit: `feat: split-runtime sender, watchdog, workflows, and routine prompts`.
