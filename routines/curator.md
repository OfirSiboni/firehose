# Firehose daily curator routine

Ranks the candidate pool, drafts the day's digest, and publishes the static site.
Needs no credentials — it only reads and writes files in the repo it was given.

1. `pip install -r requirements.txt`
2. `python -m send.close_yesterday`
3. `python -m agents.prepare_judge`
4. Follow `.claude/skills/judge/SKILL.md` exactly (writes `data/ranked.json`)
5. Validate: `python -c "from store import pool, ranked; ranked.load_ranked({i.id for i in pool.load_pool()})"` — if it fails, stop: commit nothing.
6. `python -m agents.prepare_writer`
7. Follow `.claude/skills/writer/SKILL.md` exactly (writes `data/digests/<date>.json`, `sent: false`)
8. `python -m send.publish`
9. `git add data/ docs/ && git commit -m "chore: digest <date>"`, then `git pull --rebase` and `git push` to `master`.

Never send to Telegram; never add secrets. A push is what triggers delivery.
