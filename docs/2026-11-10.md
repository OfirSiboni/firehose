# Firehose — 2026-11-10

## [Claude Fable 5.2 and Mythos 5.2 launch with big benchmark jumps](https://www.anthropic.com/claude-fable-and-mythos-5-2)

`headline` · hn

Fable 5.2 hits 69.9% on FrontierSWE v2 versus Opus 5.5's 62.3%, and 74.2% on Humanity's Last Exam with tools versus 67.7%. Mythos 5.2, gated behind Cyber and Life Sciences verification, finds 10.2% more CVEs than Opus 5.5. Fable 5.2 is live now on AWS, Google Cloud, and Azure at $8/$40 per million tokens. (2 minute read)

## [Solo hacker ran 12 AI agents to breach Taipei's emergency dispatch](https://thehackernews.com/2026/11/taiwan-based-hacker-used-bossai-ai.html)

`headline` · blog

A Taiwan-based attacker built 12 AI agents, 9 active, pairing commercial models like Grok for tooling with abliterated DeepSeek, GLM, and Qwen models for attacks. The operation pulled Taipei 119 dispatch records across 7 districts and exposed 2018-era patient ECG and ambulance video with no login required. Reused identity details and a leaked home IP let researchers trace him anyway. (4 minute read)

## [Codex backports security fixes for 149 Linux kernel CVEs](https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/)

`discovery` · blog

Trail of Bits built a Codex pipeline that finds missing kernel fixes, adapts them to older trees, and prepares validation evidence for human review. It has landed fixes for 149 CVEs into stable Linux kernels plus Fedora and Ubuntu packages, cutting backport time from days to about 30 minutes for simple cases. Debian 13 alone still carries 4,562 unfixed CVEs across 1,128 packages. (3 minute read)

## [Flaw in hosting provider's MCP server exposes 56 customer projects](https://therecord.media/cyberattack-germany-ai-mittwald)

`headline` · blog

A flaw in Mittwald's MCP server, which connects AI assistants to its mStudio hosting platform, let an attacker compromise 56 customer projects before detection. The intruder went unnoticed for 8 days after first probing the flaw in October during the PHP2Shell patch scramble. Mittwald says log timing suggests AI-paced actions but has offered no other evidence. (3 minute read)

## [One AI agent built a Rust kernel that boots Rocky Linux in 11 days](https://zenodo.org/records/23682548)

`discovery` · hn

A single persistent coding-agent task produced Ginux, a Rust x86-64 kernel with its own Linux compatibility layer, in 11 days. It boots via UEFI, runs unmodified Alpine binaries, and brings up a full Rocky Linux 10 userspace under systemd. The code is on GitHub, though it has had no independent security audit and is still flagged 'Concept'. (3 minute read)

## [Open-source inference engine serves a 320B model on AWS Trainium2](https://github.com/RunanywhereAI/trnrt)

`discovery` · github

TrnRT is an open LLM inference engine built for AWS Trainium2, serving an OpenAI-compatible API from a single trn2.48xlarge instance. It runs GLM-5.3-Flash, a 320B-parameter MoE model with a 1M-token context, through fused decode kernels and a device-and-host prefix cache. The project has 385 stars and 315 commits, with other models planned. (2 minute read)

## [Meta's Muse Ember matches Haiku's top score at a third the cost](https://research.meta.ai/blog/muse-ember)

`discovery` · hn

Muse Ember, Meta's smallest model yet, scores 37.8% on AutomationBench-AA versus GPT-6 Luna's 20.2% and Claude Haiku 5.5's 13.9%. It matches Haiku's best agent-benchmark score at roughly a third of the price, with a 1M-token context and up to 512K output tokens. Pricing starts at $0.10 per million input tokens and $0.50 output for prompts under 200K tokens. (3 minute read)

## [Asahi Linux moves to GPL to stop AI-laundered code theft](https://itsfoss.com/news/asahi-linux-drops-mit-for-gpl/)

`discovery` · hn

Asahi Linux is relicensing every repository from MIT to GPLv2-or-later after finding its code rewritten through LLMs to obscure its origin and republished without credit. The project already bans AI-generated contributions outright and compares the move to WINE's 2002 shift from MIT to LGPL to block proprietary forks. An OpenBSD developer objected that relicensing happened without consent from all prior contributors. (3 minute read)

## Also in the pool

- [DeepX claims inference up to 100B parameters at less than 5 W](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/) — hn
- [AI Vulnerability Finding](https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html) — blog
- [Apple capped engineers at a $200 daily AI budget](https://www.stork.ai/newsletter/2026-11-08-apple-capped-engineers-at-a-200-daily-ai-budget#story-1) — hn
- [Folkbench/folkbench](https://github.com/Folkbench/folkbench) — github
- [Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://arxiv.org/abs/2610.14162) — hn
- [Control Room: A central system to track and stop model workloads across our research infrastructure](https://openai.com/index/control-room) — blog
- [How I Fight AI Brain Fry](https://sergeykuhne.com/blog/fighting-ai-brain-fry) — hn
- [Silicon Valley Promises AI Will Cure Disease. Drugmaker CEOs Aren't Buying It](https://www.wsj.com/tech/ai/silicon-valley-promises-ai-will-cure-disease-drugmaker-ceos-arent-buying-it-5218511c) — hn
- [Apple CEO Presses Software Chief to Pursue More Ambitious AI Strategy](https://www.bloomberg.com/news/newsletters/2026-11-08/apple-explores-turning-siri-ai-into-chatgpt-dots-like-agent-ios-28-shake-up) — hn
- [I'm not a fan of Deno's security model (2024)](https://goldstein.lol/posts/deno-security/) — hn
- [6 Hours of YouTube and 85 handtyped pages of notes on LLM Inference – Start here](https://github.com/samir-sarwar/samir-vllm) — hn
- [370 Books in 20 months: South African author defends her use of AI](https://www.enca.com/lifestyle/370-books-20-months-sa-author-defends-her-use-ai) — hn
- [ChatGPT Enterprise now available in AWS Marketplace](https://openai.com/index/chatgpt-enterprise-aws-marketplace) — blog
- [The Biggest Threat to Your GRC Job Isn’t AI. It’s Ignoring AI.](https://www.bleepingcomputer.com/news/security/the-biggest-threat-to-your-grc-job-isnt-ai-its-ignoring-ai/) — blog
- [Qodo builds context into AI code review with Codex](https://openai.com/index/qodo-codex-plugin) — blog
- [Speeding up planning decisions with AI](https://deepmind.google/blog/speeding-up-planning-decisions-with-ai/) — blog
- [The latest AI news we announced in October 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/) — blog
- [llm-anthropic 0.31](https://simonwillison.net/2026/Nov/9/llm-anthropic/) — blog
- [SEGA newsletter data breach exposes 2.2 million email addresses](https://www.bleepingcomputer.com/news/security/sega-newsletter-data-breach-exposes-22-million-email-addresses/) — blog
- [N-able takes cloud platform offline after 30+ "zero-days" published](https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-10.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
