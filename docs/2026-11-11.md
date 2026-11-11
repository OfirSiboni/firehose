# Firehose — 2026-11-11

## [DeepMind's AlphaProof formally verifies Signal's crypto](https://deepmind.google/blog/introducing-alphaproof-code/)

`headline` · hn

An agentic multi-LLM system generated over 6 million lines of Lean proof code in four weeks to formally verify Signal's compiled cryptographic protocol, flagging just 1% of the codebase for human review. Reintroducing two previously-fixed bugs into an isolated copy, the system produced machine-checked proofs that those versions were insecure. DeepMind is open-sourcing the verification artifacts. (3 minute read)

## [Fireworks AI breach exposed model weights, Notion chats](https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html)

`headline` · blog

Fireworks AI confirmed attackers who used stolen credentials in October reached its R&D environment via a third-party cloud provider, exposing incomplete model weights and datasets, plus billing data and API keys. Notion disabled its Insights feature and dropped open-weight models served through Fireworks, saying under 1% of workspaces were affected. The attackers reportedly resell stolen LLM access. (3 minute read)

## [CWE-bench v2 adds 100 security-fix tasks across 91 CWEs](https://huggingface.co/blog/cwe-bench)

`discovery` · blog

CWE-bench v2 expands to 100 tasks across 91 CWE categories, each requiring an agent to find and fix a real security weakness without breaking existing tests. Gemini 4 Argon leads at 67.8% pass@1, just ahead of Claude Opus 5.5's 67.3%, while DeepSeek V4.1 Flash matches 57.0% pass@1 at $0.04 per rollout versus Opus 5.5's $1.83. The gated dataset runs through Harbor. (3 minute read)

## [SGLang RCE breached NEAR AI agents inside a TEE](https://thehackernews.com/2026/11/sglang-rce-exploit-breaches-near-ai.html)

`discovery` · blog

A remote-code-execution flaw in the open-source SGLang inference engine let an attacker run code on a NEAR AI server operating inside a trusted execution environment. Eighteen AI agents on an older, non-TEE deployment were accessed, and about 100 Private Chat users had account data downloaded; two exposed API keys were revoked. No CVE or public proof-of-concept has been disclosed. (3 minute read)

## [SPECTRA 4-bit quantization compresses LLMs 2.8-3.3x](https://neuracryption.com/research)

`discovery` · hn

SPECTRA, a 4-bit weight-quantization framework with custom Triton kernels, compresses models 2.80x to 3.31x in VRAM without calibration data, shrinking DeepSeek-R1-Distill-1.5B from 3.31GB to 1.03GB while reaching 82.53 tokens/second with CUDA Graph. WikiText-2 perplexity rose only 0.90 points over FP16. The vendor's '3x, near-lossless, 50MB' marketing overstates the measured VRAM numbers, and the published code and tables contain some inconsistencies. (3 minute read)

## [AI review tools caught 30-71% of 100 planted paper errors](https://arxiv.org/abs/2611.12820v1)

`discovery` · arxiv

Researchers planted 100 known errors across 10 open-access psychology papers and ran them through frontier models and two commercial AI review tools. The best single system caught 71 of 100 errors, the worst caught 30, and pooling every system's output caught 93. Seven errors, all omissions rather than insertions, were missed by every tool, and false-positive rates were not measured. (3 minute read)

## [A field guide to self-hosting LLM inference engines](https://docs.modelplane.ai/guides/inference-guide)

`discovery` · hn

This vendor-written reference covers self-hosted inference engineering: Llama 3 70B needs ~320KB of KV cache per token, or 40GB for a 128K-token context, and a 320B MoE model needs ~320GB at FP8. It cites Orca's 36.9x throughput gain over static batching and vLLM cutting KV-cache waste from 60-80% to under 4%. The figures come from published sources, not independent testing. (3 minute read)

## [Deterministic guards beat LLM judges for agent-harness security](https://arxiv.org/abs/2611.13960v1)

`discovery` · arxiv

A proposed reference-monitor architecture for agentic coding harnesses tested 252 fixtures, including 120 attack cases and 12 multi-step kill chains. An LLM-judge guard refused 98.3% of benign work at 142ms latency, while deterministic Ring-0 guards hit a 1.000 attack-block rate with zero false positives in 12.7 microseconds, about 11,200x faster. A simpler stateless baseline missed 4 of the 12 kill chains. (3 minute read)

## Also in the pool

- [Google Gemini routes personal Drive files and emails to human annotators](https://github.com/thisisme6598/gemini_files/) — hn
- [CoreWeave bond yield tops 16% as AI credit stress rises](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html) — hn
- [AI usage generates a fragile codebase](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/) — hn
- [Preparing our next security sprint to harden OpenAI](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai) — blog
- [A year after the 100% AI mandate nobody understands our code](https://www.reddit.com/r/ClaudeCode/comments/1xq2n3t/a_year_after_the_100_ai_mandate_nobody/) — hn
- [I ran 120B MoE models on my 32GB M1 Max using under 16 GB](https://mitln.github.io/moe-inference-engine/) — hn
- [France Blames Iran for Sabotage Attack on Refrigeration Controllers at About 700 Retail Sites](https://thehackernews.com/2026/11/france-blames-iran-for-sabotage-attack.html) — blog
- [Rewarding defenders with bigger bug bounties](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties) — blog
- [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) — blog
- [E-means: Outperforming k-means in one-tenth the epochs](https://e-means.github.io/) — hn
- [DeepX claims inference up to 100B parameters at less than 5 W](https://www.eetimes.com/deepx-tapes-out-second-gen-chip-projects-6-7x-performance-gain-with-lpddr5x-pim/) — hn
- [Microsoft November 2026 Patch Tuesday fixes 1,235 flaws, Outlook zero-day](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/) — blog
- [AI Users have workdays up to 90 min longer than non-users](https://www.activtrak.com/news/productivity-lab-ai-users-longer-workdays/) — hn
- [Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai) — blog
- [Transformers Model Integration Contracts](https://huggingface.co/blog/transformers-mic) — blog
- [Agentic cheminformatics with Google Antigravity](https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/) — blog
- [Palette: teaching a small model to build decks in your design language](https://huggingface.co/blog/ibm-research/palette-deck-building) — blog
- [AIs Hacking the Law](https://www.schneier.com/blog/archives/2026/11/ais-hacking-the-law.html) — blog
- [Control Room: A central system to track and stop model workloads across our research infrastructure](https://openai.com/index/control-room) — blog
- [Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives](https://github.com/GoogleChrome/modern-web-guidance) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-11.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
