# Firehose — 2026-11-04

## [MCP tool poisoning succeeds in 23% of agent-framework trials](https://arxiv.org/abs/2611.03555v1)

`discovery` · arxiv

A cross-framework study ran 9,720 MCP tool-poisoning trials across 12 agentic frameworks and 18 models, finding a 22.9% attack success rate and confirmed secret exfiltration in 12.1% of vulnerable cases. None of the 12 frameworks had built-in defenses, and all five vendor disclosures were rejected. Treat tool descriptions and schema fields as untrusted input, not just model behavior. (3 minute read)

## [Ubuntu still unpatched for a CVSS 9.8 remote-root Linux bug](https://chalmovsky.com/posts/wtf-ubuntu)

`headline` · hn

Debian patched CVE-2026-98432, a CVSS 9.8 remote-root Linux kernel TCP bug dating to 2016, on October 16. Two weeks later every supported Ubuntu release, including LTS, is still listed vulnerable, while Red Hat, Arch, and Alpine have already shipped fixes. Ubuntu's fix sits in an opt-in testing channel with no ship date. (3 minute read)

## [Postman auto-installs Claude Code and Codex plugins on upgrade](https://github.com/postmanlabs/postman-app-support/issues/14370)

`headline` · hn

Upgrading Postman past 12.33.4 silently installed Claude Code and Codex plugins plus a startup hook that pushes Postman's skill into any non-trivial API task. The installer self-approves that hook, writing its own trust record into hooks.state so both tools treat it as pre-vetted. No data exfiltration is confirmed, but the opt-in users expected wasn't there. (3 minute read)

## [CWE-bench v2 ships 100 open security-fix tasks with a leaderboard](https://huggingface.co/blog/cwe-bench)

`discovery` · blog

CWE-bench v2's 100 hand-reviewed tasks across 91 CWEs ask an agent to find and fix a real repo vulnerability without breaking tests. Gemini 4 Argon leads at 67.8% pass@1, just ahead of Claude Opus 5.5's 67.3%, and even the top model fails 19% of tasks on every attempt. DeepSeek V4.1 Flash gets close at $0.04 a rollout against Opus's $1.83. (4 minute read)

## [LLMjacking has cost some companies $1 million in cloud bills](https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html)

`discovery` · blog

Attackers stealing LLM API keys and cloud credentials are running up fraudulent charges past $100,000 in a single day, with some victims losing $1 million before access was revoked. UNC6993 minted extra API keys inside victim cloud projects; others exploited LiteLLM's CVE-2026-40217 to escalate privileges. 'LLM Mixer' resale services now sell the stolen capacity for about $60 a month. (3 minute read)

## [Codex backported security fixes for 149 CVEs into stable Linux](https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/)

`discovery` · blog

Trail of Bits' Codex-based pipeline for its Patch the Planet effort backported fixes for 149 CVEs into stable Linux kernel releases as of October 29. A straightforward backport now takes about 30 minutes of human review instead of days; a harder one takes roughly three hours. The pipeline itself isn't released, only a public CVE-tracking dashboard. (3 minute read)

## [Revolut cut inference costs 10x by self-hosting GLM on 56 B200s](https://twitter.com/guilleflorvs/status/2117379073785696395)

`headline` · hn

Revolut moved off Anthropic and OpenAI APIs to self-hosted GLM on 56 Nvidia B200 GPUs, at a blended cost of about $0.30 per million tokens, roughly a tenth of its prior frontier-API spend. GDPR and zero-data-retention rules pushed the regulated bank toward self-hosting, not just cost. One report flags GLM correctness issues on long context under vLLM. (3 minute read)

## [AI-assisted bug hunting is delaying PostgreSQL 19's release](https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html)

`discovery` · blog

An estimate that 3% of all critical bugs in recorded history were found in the past month, projecting roughly 100,000 more this year, lines up with real maintainer data. PostgreSQL's back-patched commits rose over 60% year over year between April and September while main-branch commits stayed flat. That load is cited as why PostgreSQL 19 is slipping to November. (3 minute read)

## Also in the pool

- [XLA from the Trenches: Correctness on TPU Workloads at Scale](https://arxiv.org/abs/2611.00624v1) — arxiv
- [Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai) — blog
- [Google Will Turn Off Search for Schools That Reject A.I](https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html) — hn
- [Google: LLMjacking attacks rack up $1 million in cloud AI charges](https://www.bleepingcomputer.com/news/security/google-llmjacking-attacks-rack-up-1-million-in-cloud-ai-charges/) — blog
- [Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) — hn
- [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) — github
- [OpenAI seems to be silently re-enabling model training on Codex chats](https://news.ycombinator.com/item?id=50352757) — hn
- [AIs Hacking the Law](https://www.schneier.com/blog/archives/2026/11/ais-hacking-the-law.html) — blog
- [BitLLM: Efficient Low-Bit, Conversion-Hiding LLM Decoding on Mobile GPUs](https://arxiv.org/abs/2611.00547v1) — arxiv
- [Binance Reveals How Fake Job Interviews and AI Tool Abuse Led to $6.43 Billion Theft](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html) — blog
- [LongCat-2.5: Native Multimodality for Agentic Tasks](https://longcat.ai/blog/longcat-2.5/) — hn
- [Gartner Predicts SOCs Will Have 50% More Engineers Than Analysts by 2028](https://www.bleepingcomputer.com/news/security/gartner-predicts-socs-will-have-50-percent-more-engineers-than-analysts-by-2028/) — blog
- [WorkOS says attacker used ARTEX AI to breach internal sales app](https://www.bleepingcomputer.com/news/security/workos-says-attacker-used-artex-ai-to-breach-internal-sales-app/) — blog
- [Is Your SOC Ready for AI Agents? A Maturity Check Before You Deploy](https://thehackernews.com/2026/11/is-your-soc-ready-for-ai-agents.html) — blog
- [TVP: TV is Almost All You Need for Speculative Decoding](https://arxiv.org/abs/2611.00588v1) — arxiv
- [StateBench: Testing how language models track state changes over long documents](https://huggingface.co/blog/allenai/statebench) — blog
- [Railway employee's agent caught hacking competitors](https://twitter.com/ns123abc/status/2117497728737620197) — hn
- [Weights That Stay: On-Chip Megakernels for Serial Heads in Speculative Decoding](https://arxiv.org/abs/2611.00506v1) — arxiv
- [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](https://arxiv.org/abs/2611.03526v1) — arxiv
- [Chainstack Reports Production Systems Breach Exposing Customer Data and Password Hashes](https://thehackernews.com/2026/11/chainstack-reports-production-systems.html) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-04.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
