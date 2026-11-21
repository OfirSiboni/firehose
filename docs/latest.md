# Firehose — 2026-11-21

## [Anthropic models produce a Lean-verified 17M-line proof of GRH](https://alpo.ge/remark.pdf)

`headline` · hn

Levent Alpoge says Anthropic models produced a 17.4 million-line Lean-certified proof of the Generalized Riemann Hypothesis, posted on GitHub. No Lean-certified AI math result has yet been retracted, though Lean's kernel has had soundness bugs before, which is why full confidence is still pending. (3 minute read)

## [Amazon catches Cairn AI agents finding and exploiting a real zero-day](https://therecord.media/amazon-research-cairn-ai-university-attacks-possible-zero-day)

`headline` · blog

Amazon caught a Chinese-nexus actor running the autonomous pentest tool Cairn against East Asian universities, where it found and exploited a zero-day path-traversal bug in a medical-imaging app (GHSA-qc22-rmgc-vg94). The agents ran unattended for 16 hours, testing 30,000+ credential combos in one run alone. Amazon's CISO says that's faster than most SOCs can triage an alert. (4 minute read)

## [AI-designed Frostbite CPU claims 4.6x perf-per-watt over baseline](https://architectlabs.com/blog/frostbite)

`headline` · hn

Architect Labs says its Frostbite CPU was discovered, designed, and verified end-to-end by AI agents, checked against an 800k-line Lean formal spec rather than RTL simulation. Across 25 workloads, it claims a 4.59x perf-per-watt geomean and 8.77x perf-per-area over an undisclosed comparison chip. All numbers are company-reported, with broader SPEC and multicore comparisons still planned. (4 minute read)

## [Coding agents build an FPGA LLM inference engine, 33x faster](https://ankitg.me/blog/vibecoding-inference-chip/)

`discovery` · hn

A developer with no FPGA experience had coding agents (Codex, Claude Opus, Astra) write about 3M lines of code to run a ternary-weight LLM on an AWS F2 FPGA. Throughput rose from 6.43 to 213.13 tokens/s, a 33x gain that beat a bit-exact 32-core CPU's 129.5 tokens/s at a similar hourly price. The author doesn't recommend the architecture for production. (4 minute read)

## [The AI pentest tool FBI warned about is a public repo with 14k stars](https://github.com/BaaRai/ARTEX)

`headline` · github

ARTEX, the autonomous LLM-driven pentest platform the FBI flagged in an advisory last week, is a public AGPL repo with roughly 14,000 stars and 1,232 commits. A planner breaks goals into intents, worker agents run real tools, and releases ship with SHA-256 sums and a CycloneDX SBOM. It works with Anthropic, OpenAI-compatible, or local Ollama models. (4 minute read)

## [ROGUE-AI reproduces 89% of reported LLM agent harm incidents offline](https://arxiv.org/abs/2611.26553v1)

`discovery` · arxiv

ROGUE-AI replicates real LLM-agent harm incidents, like a coding agent deleting a production database, against matched controls missing only the blamed cause. It reproduced the reported harm in 89% of 108 attempted replications, and 62 of 72 real-harm cases had no attacker at all. A tool-output warning naming the hazard cut harm across all five models tested. (4 minute read)

## [SoK: LLM vulnerability-finding autonomy passed frontier models in 2026](https://arxiv.org/abs/2611.26601v1)

`discovery` · arxiv

A new SoK rates LLM vulnerability-research capability on a driving-automation-style autonomy scale, finding agents reached full autonomous discovery, validation, and patching of real bugs before 2026's most restricted frontier models. Disclosed vulnerabilities more than doubled in 2026, with decade-old bugs in widely used code surfacing several times more often. Report-to-fix timelines haven't moved yet. (4 minute read)

## [A 27B model edits its own weights, no gradients, no training](https://arxiv.org/abs/2611.21885)

`discovery` · hn

An open 27B model is given its own weights and the ability to run itself, then edits the weights responsible for its own failures, raising accuracy 6.6 points on unseen problems. Across 8 sessions accuracy kept climbing, and a deliberately damaged copy recovered to over 80% of original accuracy with no retraining. Only the largest model in the family could do this. (4 minute read)

## Also in the pool

- [dllm-labs/mojo-dllm](https://github.com/dllm-labs/mojo-dllm) — github
- [Hurried Announcement: Alessandro Masullo GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) — hn
- [The Path to AI Autonomy in the SOC](https://thehackernews.com/2026/11/the-path-to-ai-autonomy-in-soc.html) — blog
- [Fuck Your AI Safeguards](https://ounapuu.ee/posts/2026/11/19/unsafeguards/) — hn
- [Gemini 4 Neon is the new #1 on the Models Engineering Index](https://git-aarvin.github.io/mei/) — hn
- [UK government forced to admit it issued Apple a secret encryption order](https://macanorak.com/uk-government-forced-to-admit-it-issued-apple-a-secret-encryption-order/) — hn
- [Introducing Gemini 4 Neon](https://deepmind.google/blog/introducing-gemini-4-neon/) — blog
- [AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/) — blog
- [Google is pushing OEMs against GrapheneOS and bootloader unlocking](https://grapheneos.social/@GrapheneOS/117645038299496084) — hn
- [A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained Weights](https://arxiv.org/abs/2611.26450v1) — arxiv
- [Mapping every neuron in Qwen3-8B](https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/) — hn
- [Deploying Daybreak Red](https://openai.com/business/learn/deploying-daybreak-red) — blog
- [Explore the Codex Security Plugin](https://openai.com/business/learn/codex-security-plugin-demo) — blog
- [Restricting AI agents in mobile operating systems platforms from capturing data](https://signal.org/blog/protecting-your-privacy/) — hn
- [An FBI agent called a Claude user about his chats](https://austinpatrick.substack.com/p/when-should-ai-labs-alert-police) — hn
- [Two stealth models just appeared on the leaderboard, both ahead of Fable 5.2](https://contralabs.com/frontierdesign) — hn
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — github
- [Introducing Tool Retrieval in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/) — blog
- [Court: 4th Amendment Disallows Use Of AI-Generated 'Probable Cause'](https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/) — hn
- [Get started with Daybreak Blue](https://openai.com/business/learn/daybreak-blue-onboarding-demo) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-21.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
