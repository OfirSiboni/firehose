# Firehose — 2026-11-15

## [Cursor breach let attackers ship a trojanized Claude Code extension](https://www.bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension/)

`headline` · blog

A leaked Fireworks AI key let attackers into Cursor's systems, who shipped a trojanized Claude Code extension (v2.1.312/2.1.313) for ~11 hours, attempting persistent SSH backdoors. Under 0.05% of users had traces exposed, under 0.01% had API credentials stolen, and up to 5,000 got the malicious build. Check your Claude Code extension version if installed via Cursor. (3 minute read)

## [FBI: Artex AI pentesting tool automates attacks at 'machine speed'](https://therecord.media/artex-ai-tool-fbi-flash-alert)

`headline` · blog

Artex, an open-source LLM-driven pentesting framework, took some intrusions from initial targeting to privileged access in under 3 hours, the FBI warns. Censys found 1,600+ exposed Artex consoles, with DeepSeek Flash models dominating usage for their low cost and missing guardrails when prompts are framed as pentesting. Audit DeepSeek API usage against that pretext and check for exposed admin consoles. (4 minute read)

## [llama.cpp and ggml reach v1.0.0 after 3.5 years](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

`headline` · blog

llama.cpp and ggml both hit v1.0.0 after ~3.5 years, adopting semantic versioning so a major bump signals API/ABI breaks across the 150+ architectures it supports. ggml backends can now be compiled as dynamic libraries and loaded at runtime, with CI running on hardware-partner runners from NVIDIA, AMD, Qualcomm, Arm, IBM, and Intel. Pin to a major version if you build on it. (3 minute read)

## [Nvidia allegedly engineered GPU scarcity by funding AI startups to buy its own chips](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus)

`headline` · hn

Reports allege Nvidia funded AI startups specifically so they'd buy its own GPUs, engineering an artificial supply shortage rather than a genuine one. (1 minute read)

## [Weight-space misfolding: when one model edits another's weights](https://www.alphaxiv.org/abs/2611.weight-space-misfolding)

`discovery` · hn

'Weight-space misfolding' research finds that editing another model's weights post-deployment isn't clean: a factual-substitution edit on Qwen2.5-1.5B worked 100/100 times but broke an unrelated capability, and a legal-refusal edit held on only 5 of 22 prompts. IWIBench's editing-skill reward rose from 0.2148 to 0.4250 in under five months. Track provenance before trusting a received weight patch. (3 minute read)

## [Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/)

`discovery` · hn

Splitting GLM-5.3 (753B total, 40B active, NVFP4) across two DGX GB300 stations over 400Gb RDMA with tensor parallelism hits 607.8 tok/s at concurrency 16, using speculative decoding and FP8 KV cache. Per-user throughput falls from 115.3 tok/s at concurrency 1 to 13.0 tok/s at concurrency 32 as requests share the cache. Multi-node serving now handles models too large for one GPU. (3 minute read)

## [Lovable apps expose passport details and 200K private messages](https://www.crissyfield.de/research/lovable-en/)

`discovery` · hn

Security researchers found Lovable-built apps publicly exposing passport details and more than 200,000 private messages, echoing the pattern of other AI app-builders shipping no-auth-by-default apps that leak sensitive data. (1 minute read)

## [600 experiments pinpoint where JEPA world-model planning breaks](https://haddyalchaer.com/jepa)

`discovery` · hn

600 experiments on a JEPA world model found that exact simulator physics barely improves long-horizon planning over the learned predictor (78% vs 77% success), so the model isn't the bottleneck. Adding a subgoal every 25 steps raises 75-step success from 22% to 80%, beating flat exact-physics planning's 42%. A harder benchmark with cross-demonstration goals caps the best planner at 56% success. (3 minute read)

## Also in the pool

- [Partnering with Hacktron to find vulnerabilities in OpenAI’s systems](https://openai.com/index/partnering-with-hacktron) — blog
- [Advancing science and engineering with Antigravity's /teamwork](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) — hn
- [OpenAI disbands its robotics team as its general models start running robots](https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/) — hn
- [AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths) — hn
- [FBI Says North Korean Hackers Stole Over $400 Million in Crypto Using Deepfake Video Calls](https://thehackernews.com/2026/11/fbi-says-north-korean-hackers-stole.html) — blog
- [Ggml v1.0.0](https://github.com/ggml-org/ggml/releases/tag/v1.0.0) — hn
- [Unsloth Qwen3.8-27B Quantizations – Dynamic v3.1 Update](https://unsloth.ai/docs/models/qwen3.8) — hn
- [Perplexity Decider v1.3: Training, eval, and use cases](https://www.perplexity.ai/hub/blog/perplexity-decider) — hn
- [PostgreSQL Patches 52 Flaws, Including 22-Year-Old Bug Enabling Authenticated RCE](https://thehackernews.com/2026/11/postgresql-patches-52-flaws-including.html) — blog
- [Nvidia deliberately kept GPU prices high through circular financing deals](https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html) — hn
- [Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) — blog
- [XYBench: Helping with the problem behind the question](https://huggingface.co/blog/allenai/xybench) — blog
- [Egyptian and Nigerian English join the Open ASR Leaderboard](https://huggingface.co/blog/open-asr-leaderboard-liva) — blog
- [DeepSeek Ultrafast](https://github.com/basetenlabs/deepseek-ultrafast) — hn
- [Show HN: DeepSeek V3 in ~200 lines of pure Jax](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) — hn
- [New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs](https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html) — blog
- [North Korean hackers used fake video calls in $400M crypto hack, says FBI](https://www.bbc.com/news/articles/cqdj1ellpd70o) — hn
- [Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/) — blog
- [Claude Meetings](https://claude.com/resources/articles/claude-meetings) — hn
- [US disrupts North Korean campaign behind $400 million crypto theft](https://www.bleepingcomputer.com/news/security/us-disrupts-north-korean-campaign-behind-400-million-crypto-theft/) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-15.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
