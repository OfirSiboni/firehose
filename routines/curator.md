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
8. `python -m agents.prepare_critic` (fetches today's TLDR AI issue and blinds it
   against ours). If it prints "no tldr issue today" or "no digest today", skip
   steps 9-10.
   If the fetch itself is blocked, read `https://tldr.tech/ai/<date>` with WebFetch,
   save the page to `/tmp/tldr.html`, and re-run `python -m agents.prepare_critic --html /tmp/tldr.html`.
9. Spawn a **subagent** whose entire prompt is: *"Follow `.claude/skills/critic/SKILL.md`
   exactly."* Pass it nothing else — no context from this session, no hint about which
   newsletter is ours. That blind is the feature; do not run the Critic yourself, because
   you know which one you just wrote.
10. `python -m agents.finalize_critic` (names the winner and deletes the blinding key)
11. `python -m send.publish`
12. `git add data/ docs/ && git commit -m "chore: digest <date>"`, then `git pull --rebase` and `git push` to `master`.

Never send to Telegram; never add secrets. A push is what triggers delivery.
The verdict rides along to Telegram only — `send.publish` never reads it, so it
stays out of `docs/`.
