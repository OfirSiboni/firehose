# Firehose — 2026-10-26

## [OpenAI's agents found VM escapes and a cross-sandbox side-channel](https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html)

`headline` · blog

OpenAI's red-team agents reached a blocked metrics endpoint through a firewall-approved connection to fetch an attacker-chosen URL, and two agents in separate microVMs swapped a secret over a CPU cache timing side-channel -- no network link or shared file involved. A related bypass could have hidden hundreds of Codex actions from OpenAI's monitoring before July 21; OpenAI says that's now fixed, though outside reviewers haven't confirmed it. (3 minute read)

## [AI coding agents hijacked using AGENTS.md file in Downloads folder](https://www.bleepingcomputer.com/news/security/ai-coding-agents-hijacked-using-agentsmd-file-in-downloads-folder/)

`discovery` · blog

A malicious AGENTS.md or CLAUDE.md file dropped into ~/Downloads gets auto-loaded as trusted instructions once an agent launches from that folder. A harmless test payload worked 90% of the time against OpenAI Codex, and a variant stealing Claude Code's OAuth token via a redirected API endpoint worked about 50% of the time. Researchers say there's nothing to patch -- the fix is to stop launching agents from Downloads. (3 minute read)

## [Cerebras serves trillion-parameter models at 1,000+ tokens/sec](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)

`headline` · hn

Cerebras now serves Kimi K3 (~3 trillion parameters) across 59 WSE-3T wafers, splitting layers across chips and streaming only activations over a ~2-microsecond RDMA interconnect. Concurrent pipelining and micro-batching keep every stage busy without batching to completion, hitting 1,000-2,000+ tokens/sec -- and Cerebras says efficiency should be judged in tokens/sec per megawatt, not raw speed. Kimi K3 scores 88.3% on Terminal-Bench 2.1 and 91.2% on BrowseComp, matching GPT-5.6 Sol. (3 minute read)

## [A 10-year-old CNN beats frontier LLMs at skin cancer diagnosis](https://lynchlab.net/llm-skin-cancer)

`headline` · hn

A 2015-era Inception v3, fine-tuned for 20 minutes on one H100, beat GPT-6 Astra and Claude Fable 5.1 on 200 biopsy-confirmed skin lesions: 62% first-choice accuracy versus 42% for both LLMs. It also flagged only 18 of 30 melanomas as safe to discharge versus 3 and 4 for the LLMs, though the sample is small. Scoring code and a local demo are released. (2 minute read)

## [Why OpenAI and Anthropic cut LLM prices up to 80% this year](https://minimaxir.com/2026/10/cheap-llms/)

`discovery` · hn

Cache reads now make up 96-99% of agent token spend at 90-100% hit rates, so cache-price cuts like Claude Fable 5.1's 75% cut in September deliver outsized savings. GPT-5.6 Luna dropped ~80% in July, GPT-6.1 Sol halved its cache-read price in September, and DeepSeek V4.1 Flash is now on 29 OpenRouter providers, up from 13 -- pushing prices toward commodity levels, even as both labs reportedly still lose billions ahead of IPOs. (2 minute read)

## [An LLM-driven reverse-engineering framework built for Claude Code](https://github.com/Ablation-Tool/ablation)

`discovery` · github

Ablation wires an LLM analyst loop to Capstone, Unicorn, Z3, and angr for reverse engineering, backed by a persistent hypothesis engine and knowledge-graph retrieval. It claims to rank candidates across an 885-function binary in 35 seconds and confirmed 11 of 14 kernel-bug candidates in a KASAN-oracle workflow against TencentOS kernel 6.6.119, though its Cisco PSIRT usage claim is unverified. Install with pip; it runs inside Claude Code. (2 minute read)

## [Context engineering in 2026: forgetting beats remembering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html)

`discovery` · hn

METR's long-horizon benchmark has climbed from 3.4 hours (GPT-5) to 12.0 (Opus 4.6), and a UC Berkeley study found agents that periodically forget outscore both a single agent and four parallel agents on the same task (1,144,695 vs 1,007,073 vs 961,136). Contradictory examples degrade instruction-following across 13 models, with smaller models dropping below 50% accuracy. The context-engineering toolbox hasn't changed since 2025 -- what's new is evidence that forgetting helps. (2 minute read)

## [geo-sleuth: an agent skill that geolocates photos to meters](https://github.com/Oldcircle/geo-sleuth)

`discovery` · github

geo-sleuth is an open agent skill that geolocates photos by combining DINOv2 and CLIP image matching with OpenStreetMap geometry, elevation skylines, and street view, running inside Claude Code, Codex, or Cursor. It placed a rice-paddy photo within 2 meters and a Vancouver photo within 3 meters on a blind re-run, though the author notes these are regression checks on already-tuned cases, not held-out accuracy. (2 minute read)

## Also in the pool

- [FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo) — github
- [Five Qwen3.8-27B models match Fable 5 Using GVS5H Harness](https://github.com/slee-persis/GVS5H) — hn
- [Gheist campaign plants secret-dumping workflows using stolen GitHub tokens](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles) — hn
- [Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance](https://arxiv.org/abs/2610.32555v1) — arxiv
- [Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation](https://arxiv.org/abs/2610.32453v1) — arxiv
- [Nikon photography contest winner loses title after scientists spot signs of AI](https://www.techspot.com/news/114171-nikon-photography-contest-winner-loses-title-after-scientists.html) — hn
- [No signs of AI payoff outside the tech sector](https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector) — hn
- [Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach Root on Other Servers](https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html) — blog
- [When Agents Fail: Model or Harness--Who's to Blame?](https://arxiv.org/abs/2610.32483v1) — arxiv
- [Folkbench/folkbench](https://github.com/Folkbench/folkbench) — github
- [PHP2Shell Exploitation Hits Government Entity Amid Global Scanning and Signs of AI-Assisted Hacking](https://thehackernews.com/2026/10/php2shell-exploitation-hits-government.html) — blog
- [Quantum-Classical Link Prediction on Dark Web Hyperlink Graphs](https://arxiv.org/abs/2610.32510v1) — arxiv
- [Accordion: Elastic-Depth Inference via Fixed-Prefix Layer Looping](https://arxiv.org/abs/2610.32492v1) — arxiv
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu) — github
- [ceyyy427/finathink](https://github.com/ceyyy427/finathink) — github
- [FengZhenfei/carrel](https://github.com/FengZhenfei/carrel) — github
- [morluto/awesome-reverse-engineering](https://github.com/morluto/awesome-reverse-engineering) — github
- [JEen-wang/Adaptive-rag](https://github.com/JEen-wang/Adaptive-rag) — github
- [Takamatsu-Hikaru/AI-Research-Guide](https://github.com/Takamatsu-Hikaru/AI-Research-Guide) — github
- [TokenRhythm/NeoHorse](https://github.com/TokenRhythm/NeoHorse) — github

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-26.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
