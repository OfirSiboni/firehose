# Firehose weekly relearn routine

Regenerates the learned half of the taste profile from a week of feedback labels.
Needs no credentials — it only reads and writes files in the repo it was given.

1. `pip install -r requirements.txt`
2. `python -m agents.prepare_relearn`
3. Follow `.claude/skills/relearn/SKILL.md` exactly (rewrites `taste/profile.md`)
4. Verify with `git diff taste/profile.md` that only the `## Learned` section changed. If `## Mine` changed, `git checkout taste/profile.md` and stop.
5. `git add taste/profile.md && git commit -m "chore: relearn taste profile <date>"`, then `git pull --rebase` and `git push` to `master`.
