# Firehose — 2026-11-20

## [Gemini 4 Neon tops cyber and coding benchmarks at lower cost](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

`headline` · hn

Gemini 4 Neon scores 76% on AutoBaxBench and 51.26% on WebExploitBench, both state of the art, at 32% lower cost per task than Carbon. It tops the Artificial Analysis Coding Agent Index at 58.6 and blocks 100% of indirect prompt injections at its highest thinking level. At $3 per million input tokens, security and coding teams get frontier agent evals without frontier pricing. (2 minute read)

## [Compromised Microsoft Agent Framework package stole credentials](https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/)

`headline` · blog

Microsoft's Agent Framework package on PyPI was compromised to exfiltrate developer and cloud credentials. The agent-framework supply chain is now a confirmed attack vector, not just a theoretical one. Anyone who installed the package recently should rotate credentials and audit for unauthorized access. (1 minute read)

## [LLM-driven reverse engineering workflow, repos included](https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering)

`discovery` · hn

A six-month reverse-engineering project paired DeepSeek with Ghidra's MCP bridge and radare2, using a hypothesis-debugging skill that logs each guess before testing it. The workflow mapped EmWave and Sony Alpha camera protocols, built custom synth firmware, and cracked license locks. The Ghidra and debugging skills are published as open repos (ioma8/ghidra-decompile-skill, ioma8/hypothesis-debugging) that anyone can reuse. (2 minute read)

## [AI hacking tool breached European Commission systems for 10+ days](https://therecord.media/european-commission-confirms-cyberattack-using-ai)

`headline` · blog

An AI-driven cyberattack on the European Commission, first detected October 22, knocked out payroll, leave, medical reimbursement, and translation systems for more than 10 days. CERT-EU ties the intrusion to ARTEX, an open-source AI hacking platform the FBI says can reach privileged access in under three hours. It's the Commission's third disclosed breach this year, and the investigation remains open. (2 minute read)

## [Two critical unauthenticated RCEs hit Nginx HTTP/2](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)

`headline` · hn

Two critical Nginx HTTP/2 bugs, CVE-2026-123633 and CVE-2026-123007, both CVSS 9.2, let unauthenticated attackers reach remote code execution through a use-after-free and an integer underflow. Wiz built working exploits in testing but withheld them; fixes ship in 1.30.7 and 1.31.9. With HTTP/2 enabled on over 225 million sites, upgrading now beats waiting for a public PoC to appear. (2 minute read)

## [Claude completes a 2003 black-hole calculation, proves a new bound](https://www.anthropic.com/research/claude-black-hole-physics)

`headline` · hn

Running as parallel agent copies that cross-checked each other, Claude finished a three-loop N=4 super Yang-Mills calculation physicists set up in 2003, confirming an abrupt gas-to-black-hole transition matching the 1983 gravity-side result. It also derived an exact mass ceiling for the lightest 3D black hole, M₁ ≤ c/Λ with Λ≈9.1266, formally verified in Lean. The findings are Anthropic's own unpublished preprints, not yet peer reviewed. (3 minute read)

## [Genie 4 is now generally available](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)

`headline` · hn

Google's Genie 4 world model is now generally available. (1 minute read)

## [Energy-based reasoners cut inference compute 345x on logic puzzles](https://energy-based-reasoners.github.io/)

`discovery` · hn

Energy-Based Reasoners replace next-token search with gradient descent on a learned energy function, reaching 99.9% accuracy on Sudoku-Extreme with just 1.8M parameters, 345x less inference compute than the next-best approach. No external verifier is needed; the energy score itself tells the model when to stop refining. Code and the arXiv paper (2611.08977) are public, so the approach is reproducible now. (2 minute read)

## Also in the pool

- [DaisyRose-27B](https://www.radixark.com/blog/daisyrose-27b) — hn
- [Seven new models at scalable price-performance](https://microsoft.ai/news/microsoft-ignite-2026/) — hn
- [Critical Apache Roller RCE Flaw Under Active Exploitation, No Authentication Required](https://thehackernews.com/2026/11/critical-apache-roller-rce-flaw-under.html) — blog
- [Fuck Your AI Safeguards](https://ounapuu.ee/posts/2026/11/19/unsafeguards/) — hn
- [Two stealth models just appeared on the leaderboard, both ahead of Fable 5.2](https://contralabs.com/frontierdesign) — hn
- [A 4.5M-parameter TTS model runs 70x real-time on CPU and cost just $10 to train](https://huggingface.co/n4ze3m/tiny-voca) — hn
- [BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model](https://huggingface.co/blog/qvac/botpsy) — blog
- [Visa, Mastercard and JPMorgan Customer Data Leaked by Hackers](https://www.wsj.com/finance/banking/visa-mastercard-and-jpmorgan-customer-data-leaked-by-hackers-3b5a0f87) — hn
- [180B Parameters, 32GB of RAM: Pushing MoE Inference to the Limit with Transformers](https://huggingface.co/blog/moe-expert-streaming) — blog
- [Previous-Token Prediction Based LLM Inversion for Prompt Reconstruction](https://arxiv.org/abs/2607.29378) — hn
- [VMware patches vCenter zero-day exploited in attacks since September](https://www.bleepingcomputer.com/news/security/vmware-patches-vcenter-zero-day-exploited-in-attacks-since-september/) — blog
- [AI agents ask better questions than KPMG accountants in audit trial](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/) — hn
- [Three People Arrested for AI-Enhanced Impersonation Fraud](https://www.schneier.com/blog/archives/2026/11/three-people-arrested-for-ai-enhanced-impersonation-fraud.html) — blog
- [Ruby2ßhell: Pre-authentication RCE on stock Rails](https://verialabs.com/ruby2shell/) — hn
- [Pete warden on local AI, open models, voice interfaces, the future of hardware](https://thedataexchange.media/pete-warden-moonshine/) — hn
- [ThreatsDay: GPT-6.2 Jailbreak Flaws, BubbleLoader PNG Malware, $500M Ransom Demands + 17 More Stories](https://thehackernews.com/2026/11/threatsday-gpt-62-jailbreak-flaws.html) — blog
- [Why your fine-tuning job takes longer than the FLOPs say](https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time) — blog
- [Rumble-2-Flash: an open 0.5B speech model for 40+ languages](https://huggingface.co/blog/rumble-2-flash) — blog
- [New Attack Bypasses TPM Lockout to Crack Windows Hello and BitLocker PINs in Days, Not Years](https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html) — blog
- [Quality Isn’t The Main Worry About AI Pentesting — Data Privacy and Production Safety Are](https://thehackernews.com/2026/11/quality-isnt-main-worry-about-ai.html) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-20.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
