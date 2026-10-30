# Firehose — 2026-10-30

## [Codex plugins patch bugs and verify fixes don't cause regressions](https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/)

`discovery` · blog

Trail of Bits open-sourced two Codex plugins: patching-bugs proves a fix with a three-arm test (fails on the original code, passes on the patch, fails again once reverted), and regression-hunt traces diffs to live repros before an adjudication agent rules on real regressions. Against a baseline Codex agent, regression-hunt cut false positives 25% (95% CI 14-38%) and confirmed 21 regressions across 130+ merged PRs. Engineers can now hand patch and regression checks to agents and get verified evidence instead of a manual diff review. (3 minute read)

## [Gemini 4 Carbon leads new cybersecurity benchmarks for bug hunting](https://thehackernews.com/2026/10/googles-gemini-4-carbon-leads.html)

`headline` · blog

Gemini 4 Carbon scores 88.2% on SEC-bench Pro for finding vulnerabilities, 54.8% on ExploitGym for exploitation, and 71.0% on CWE-bench for patching. Google says it's twice as likely to generate secure code as predecessor Argon and resisted every evaluated indirect prompt-injection attempt. Access starts limited to a subset of cyber defenders through the Fairwind Program. (3 minute read)

## [A smarter scheduler recovers 27% more usable Grace Blackwell GPUs](https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler)

`discovery` · hn

NVL72 racks give full NVLink speed only to jobs that stay on one rack, so node failures and uneven job lengths strand usable GPUs across racks. SkyPilot's topology-aware scheduler and automatic defragmentation recover 27% more usable nodes on a 128-rack, 2,304-node cluster (2,037 vs 1,602) versus naive 18-node slicing, and NVIDIA's GR00T team saw a 14.4% pre-training throughput gain from rack-aware placement alone. Teams running multi-node jobs on Grace Blackwell can reclaim that capacity without buying more racks. (4 minute read)

## [Claude Code regularly sends each background agent's transcript to its model](https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce)

`discovery` · hn

Claude Code sends each background agent's full transcript to its model roughly every 30 seconds just to write a 3-5 word status line, with no setting to turn it off since v2.1.232. Independent telemetry in GitHub issue #86879 puts this at 16-26% of a user's total agent spend. Anyone running background agents can now check their own OpenTelemetry query\_source field, or apply an unofficial Bun preload script that neutralizes the timer and recovers that spend. (4 minute read)

## [A CVSS 10.0 GitLab bug got actively probed against Alpine's own GitLab](https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html)

`headline` · hn

An attacker spent six days probing CVE-2026-97229, a CVSS 10.0 regex-engine bug in GitLab's CI config parser, against Alpine Linux's own GitLab instance, crashing worker processes 8 times and partially completing the exploit chain 4 times. Alpine's GitLab update didn't close the hole because its container image shipped unpatched upstream Ruby, so it rebuilt the instance from scratch and reset every password. Anyone self-hosting GitLab needs to upgrade Ruby separately, since the fix doesn't ship inside the GitLab update itself. (4 minute read)

## [Cloudflare uses OpenAI's Daybreak to investigate its own vulnerabilities](https://openai.com/index/cloudflare-cyber)

`discovery` · blog

Cloudflare uses OpenAI's Daybreak model to investigate vulnerabilities and propose fixes for human review, while its developers use Codex to ship code faster and improve its quality. It's a production example of AI handling the investigation step of vulnerability response, with people still deciding what actually ships. (2 minute read)

## [OpenAI's Patch the Planet coordinates fixes for agent-found bugs](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities)

`discovery` · blog

OpenAI's Patch the Planet connects security researchers, maintainers, and incident responders around critical open-source vulnerabilities that AI agents surface. It's a coordination layer built for turning agent-found bugs into shipped fixes, not just more vulnerability reports. (2 minute read)

## [Google's Sleep framework teaches LLMs new facts without forgetting old ones](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)

`discovery` · hn

Google Research's Sleep framework alternates a wake phase that stores new information and a sleep phase that consolidates it into a Hope-architecture MoE's long-term parameters, rather than fine-tuning over frozen weights. It held near-zero forgetting when continually translating into unseen languages Manchu and Kalamang, where in-context learning, Cartridges, and SFT all degraded badly, and scaled BABILong recall out to 10M tokens past GPT-4 and Titans. No code has shipped yet, only the arXiv paper. (4 minute read)

## Also in the pool

- [2akouwu/reverify](https://github.com/2akouwu/reverify) — github
- [jwuthri-cloud/Tracely-ai](https://github.com/jwuthri-cloud/Tracely-ai) — github
- [Using thousands of AI agents to uncover new leads in biological data](https://openai.com/index/scaling-ai-research-for-complex-biological-data) — blog
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — github
- [Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents](https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/) — hn
- [Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html) — blog
- [Fake ChatGPT and Claude Apps Abuse Signed Executables to Deploy Crypto Miners](https://thehackernews.com/2026/10/fake-chatgpt-and-claude-apps-abuse.html) — blog
- [Webinar: How to Build AI Threat Readiness Into Your Security Operations](https://thehackernews.com/2026/08/learn-how-to-build-security-operations.html) — blog
- [The Rise of the Threat Operator: How AI Will Redefine Security Operations and Careers](https://thehackernews.com/2026/10/the-rise-of-threat-operator-how-ai-will.html) — blog
- [ThreatsDay: Critical Firewall Flaws, Banking Trojans Rented, Weaponized PDF, Token Theft + 26 More Stories](https://thehackernews.com/2026/10/threatsday-critical-firewall-flaws.html) — blog
- [Hugging Face malware campaign returns to hijack GPUs for crypto mining](https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/) — blog
- [How we detect frontier model misalignment](https://openai.com/index/how-we-detect-frontier-model-misalignment) — blog
- [Zero click, silent, remote Android DoS](https://smsofdeath.com/) — hn
- [Hackers expose the identities of more than 40k DHS employees](https://text.npr.org/nx-s1-6021497) — hn
- [marclou/mailcheap](https://github.com/marclou/mailcheap) — github
- [Yamz-Labs/kyojin](https://github.com/Yamz-Labs/kyojin) — github
- [himovo/movo](https://github.com/himovo/movo) — github
- [rollroyces/py-idp](https://github.com/rollroyces/py-idp) — github
- [Fazmin/AILearningGuide](https://github.com/Fazmin/AILearningGuide) — github
- [YOLOW92/pagesift](https://github.com/YOLOW92/pagesift) — github

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-30.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
