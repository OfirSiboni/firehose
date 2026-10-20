# Firehose — 2026-10-20

## [A hacker used an army of AI agents to breach John Deere, SharkNinja](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins)

`headline` · hn

A single attacker reportedly breached John Deere, SharkNinja, and Cummins by orchestrating a large fleet of AI agents instead of running manual intrusions one at a time. Specifics on the attack method and timeline haven't surfaced yet beyond the named victims. (1 minute read)

## [DHS orders all US civilian agencies to rip out DeepSeek](https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/)

`headline` · hn

DHS Order 2026-01 directs every federal civilian agency to stop buying DeepSeek and remove it, plus any third-party tool built on its models, effective immediately. Agencies get a 60-day window to request written exceptions, reviewed by CISA, while national-security systems stay exempt. If you sell software to US federal agencies, audit for DeepSeek dependencies now. (3 minute read)

## [Mercury 3: Inception's diffusion LLM hits 1,068 tokens/sec](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

`headline` · hn

Inception's Mercury 3 generates at 1,068 tokens/sec, 4-8x faster than comparable models, and claims benchmark parity with GPT-6 Luna and Claude Haiku 5.5. It completed 50% of 50 live Mind2Web browser-agent tasks and now supports a 1M-token context, up from 260K. It's live on Inception's API, OpenRouter, Baseten, and Vercel at $0.20/$0.70 per million tokens. (3 minute read)

## [F5 ships emergency patches for three critical NGINX bugs](https://www.bleepingcomputer.com/news/security/f5-releases-out-of-band-patches-for-critical-nginx-vulnerabilities/)

`headline` · blog

F5 released out-of-band patches for three critical NGINX flaws: CVE-2026-15176 and CVE-2026-97205 in the HTTP/3 module, and CVE-2026-93479 in the map directive, each triggering a heap overflow or use-after-free in the worker process. Unauthenticated attackers can cause denial of service, with RCE possible if ASLR is disabled. Patch now if you run NGINX Plus, OSS, Ingress Controller, Gateway Fabric, or Instance Manager. (3 minute read)

## [How abliterated open models can hide an undetectable backdoor](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned)

`discovery` · hn

ProjectDiscovery trained a ~43M-parameter LoRA backdoor, about 0.6% of the base model, onto Qwen2.5-7B-Instruct so a trigger phrase swaps its next tool call for one that exfiltrates .env secrets. At a 20% poison rate the trigger fired 100% of the time while clean-task accuracy stayed at 100%, and the whole run cost under $50 and 2.5 GPU-hours. Standard benchmarks and scanners don't catch it, so treat edited open-weight models like unverified code. (3 minute read)

## [Fake Web3 accelerator uses npm malware to hijack AI agent traffic](https://thehackernews.com/2026/10/fake-web3-accelerator-uses-npm-packages.html)

`discovery` · blog

Elastic's tracked campaign, REF8801, lures crypto developers with free Claude and Gemini credits to run npm packages that install infostealers on Windows and macOS. The same packages can redirect OpenRouter LLM requests and register a rogue MCP server in the victim's agent config, exposing prompts and tool output and letting the attacker inject new instructions. Audit any MCP servers and npm packages added via unsolicited developer outreach. (3 minute read)

## [HardEval grades LLMs on actually hardening a live Linux box](https://arxiv.org/abs/2610.23685v1)

`discovery` · arxiv

HardEval tests whether a model can move real RHEL8 STIG security controls from fail to pass on a live VM, graded by an OpenSCAP/OVAL compliance check rather than code review. Across 14 frontier and open-weight configurations, the most common failure is code that looks right but misses the exact compliance condition. Code and data are public on GitHub for anyone who wants to run the same hardening tasks. (3 minute read)

## [Google's Harness2 rewrites the agent harness, not the model](https://github.com/google-research/harness2)

`discovery` · hn

Harness2 keeps model weights frozen and instead edits eight parts of the agent harness itself, like the system prompt, tool guidance, and memory, using evidence from probe runs on the same task. A single refinement step lifted GLM-5 and Gemini 3.5 Flash by up to 11.5 points on WorkBuddy-Bench and 11.8 points on LAB's partial-pass rate. The Apache-2.0 code runs locally with no model credentials needed for the demo. (3 minute read)

## Also in the pool

- [Launch HN: Laminar (YC S24) – RL-trained model that finds errors in agent traces](https://news.ycombinator.com/item?id=50154029) — hn
- [GhostAction Attackers Plant Credential Stealer Disguised as Font in 94 GitHub Repositories](https://thehackernews.com/2026/10/ghostaction-attackers-plant-credential.html) — blog
- [TorchNeuron: running HF models on AWS Trainium is easier than ever](https://huggingface.co/blog/hf-torchneuron) — blog
- [Unpatched Broadcom Wi-Fi Flaw Lets Attackers in Range Run Code as Root on Routers](https://thehackernews.com/2026/10/unpatched-broadcom-wi-fi-flaw-lets.html) — blog
- [Maxwell: A new kind of model that sits between code and hardware](https://heymaxwell.ai/) — hn
- [Show HN: KiviDB, a faster Redis-compatible memory database and vector cache](https://github.com/kividbio/kividb) — hn
- [Timestral: Mistral's time-series foundation models](https://mistral.ai/news/timestral/) — hn
- [Show HN: WhatsApp MCP running free on Cloudflare](https://github.com/finereli/whatsapp-mcp) — hn
- [Show HN: Qwen3-4B with the AI writing tics trained out](https://100toolkit.com/blog/deslop-model/) — hn
- [Tmux and Claude Code: Sessions, Send-Keys, and the Ceiling](https://crystl.dev/guides/tmux-for-ai-agents/) — hn
- [Training AIs to Solve CAPTCHAs](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html) — blog
- [If you don't run your own LLM proxy, how do you know whats going on?](https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/) — hn
- [Harness Engineering 101: The LLM is the brain, the harness is the body](https://github.com/IsuruMaduranga/harness-engineering-101) — hn
- [The obscure trust looming over Anthropic's IPO](https://www.wsj.com/tech/ai/anthropic-ipo-private-trust-188f41f7?st=RtdGHg&reflink=desktopwebshare_permalink) — hn
- [Language Models Learn to Improve Language Models](https://arxiv.org/abs/2610.23344v1) — arxiv
- [How Finite-Rank Bottlenecks Shape the Low-Rank Adaptation Landscape](https://arxiv.org/abs/2610.23343v1) — arxiv
- [Robust Function Calling for LLM Agents Under Interface Drift](https://arxiv.org/abs/2610.23342v1) — arxiv
- [MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection](https://arxiv.org/abs/2610.23307v1) — arxiv
- [Acceptance Is Not Speed: Length Inflation in Training-Free Lossy Speculative Decoding](https://arxiv.org/abs/2610.23818v1) — arxiv
- [FuTransformer: FP8 prefill and INT4 decode for Llama-style inference on Hopper](https://arxiv.org/abs/2610.23796v1) — arxiv

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-20.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
