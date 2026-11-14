# Firehose — 2026-11-14

## [FBI: Artex AI Tool Automates Cyberattacks at Machine Speed](https://therecord.media/artex-ai-tool-fbi-flash-alert)

`headline` · blog

Censys found 1,600+ exposed Artex consoles, the AI-agent pentest tool the FBI says reaches privileged access in under 3 hours. It chains Claude, GPT, DeepSeek, GLM, Grok, and Kimi -- DeepSeek dominates attacker-controlled instances -- and Microsoft ties it to a Chinese state-backed ConnectWise supply-chain attack across finance, government, and energy. Security teams now have a concrete exposure count and timeline to defend against. (4 minute read)

## [Weight Fingerprints Show Chinese Models Trained on Blackwell GPUs](https://unemploymentlabs.com/checkpoint-forensics)

`discovery` · hn

Seeded RNG weight init reveals which GPU class trained a model, and DeepSeek-V4, Kimi K3, MiniMax-M3, and Ling-3.1-flash all read as Blackwell (148-152 SMs), not Hopper. The signal holds at 49-1385 sigma against an ~8 sigma chance baseline across ~6e12 seed/layout combinations, and matched bit-for-bit on all 24 models with known hardware. It can't prove ownership or an export violation, but anyone can now check a model's training hardware from its published weights alone. (4 minute read)

## [Edge0-145B Runs Frontier-Class AI on a Single Laptop](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer)

`discovery` · hn

Edge0-145B is a 145B-parameter model (10B active) that runs on a MacBook Pro-class laptop at ~29GB peak memory, hitting 80+ tok/s decode and 1100+ tok/s prefill. Its six-benchmark mean of 72.8 beats Qwen3.8-Flash-Next's 71.7, despite Qwen needing roughly 70GB at 4-bit -- though the numbers are vendor-reported, not independently verified. Anyone with a high-end laptop can now run a frontier-tier model locally instead of renting GPU memory. (3 minute read)

## [OpenAI Disbands Robotics Team as General Models Run Robots](https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/)

`headline` · hn

OpenAI folded its dedicated robotics team into its main research org after a GPT-6 Astra-powered agent hit 74.8% on an Nvidia manipulation benchmark versus 51.0% for the best specialized robotics models. Applied and hardware teams move under Greg Brockman, research under CRO Mark Chen, amid a reported $10.9B quarterly operating loss and a planned funding round. General-purpose models, not dedicated robotics stacks, are now the default bet for controlling physical robots. (4 minute read)

## [OpenAI Partners With Hacktron to Pentest Its Systems](https://openai.com/index/partnering-with-hacktron)

`discovery` · blog

OpenAI is partnering with pentesting firm Hacktron to hunt vulnerabilities in its own systems. (1 minute read)

## [OpenAI Launches GPT-6 Cyber for Aligned Security Agents](https://openai.com/index/introducing-gpt-6-cyber)

`headline` · blog

OpenAI introduced GPT-6 Cyber, a model built specifically for aligned cybersecurity agents. (1 minute read)

## [llama.cpp Hits v1.0.0 With a Stable Public API](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

`discovery` · blog

llama.cpp's libllama and libggml both reach v1.0.0 with public headers and semver guarantees, after roughly 3.5 years of development. The project now supports 150+ model architectures plus mainstream speculative decoding, distributed through about 10 channels including Docker, Homebrew, conda-forge, and Winget. Developers can now build against a stable C API instead of tracking a moving target. (3 minute read)

## [CapLite Blocks Every Prompt-Injection Attack in AgentDojo Tests](https://arxiv.org/abs/2611.17115v1)

`discovery` · arxiv

CapLite derives its write policy from tool schemas, with no model-written security artifact, and recorded zero successful attacks across 13,935 attacked AgentDojo episodes. It holds 29.0% utility under attack versus CaMeL's 27.2%, at about 18% of CaMeL's token cost, while prior defenses broke on 11-14 of 15 tested open models. Small open-weight agents can now get injection defense this strong without burning tokens on self-written policies. (4 minute read)

## Also in the pool

- [I'm making LLMs work on small and old devices](https://github.com/hyperionaidev/smolmaxxing/) — hn
- [AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths) — hn
- [After 600 experiments, here's what I discovered about JEPA world models](https://haddyalchaer.com/jepa) — hn
- [Hackers compromise 4,800 GitHub accounts to steal cloud credentials](https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/) — blog
- [Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) — hn
- [Ggml v1.0.0](https://github.com/ggml-org/ggml/releases/tag/v1.0.0) — hn
- [FBI Says North Korean Hackers Stole Over $400 Million in Crypto Using Deepfake Video Calls](https://thehackernews.com/2026/11/fbi-says-north-korean-hackers-stole.html) — blog
- [Apify rotates API tokens, prompts 2FA resets after breach](https://www.bleepingcomputer.com/news/security/apify-rotates-api-tokens-prompts-2fa-resets-after-breach/) — blog
- [186 Fake AI Domains Redirect Users to ClickFix Lures, Browser Malware, and Search Hijackers](https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html) — blog
- [New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP VMs](https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html) — blog
- [Libreagi – Save OSS Models](https://libreagi.com/) — hn
- [Show HN: AgentRun – open-source, Self-improving Managed Agents](https://github.com/Parcha-ai/agentrun/blob/main/README.md) — hn
- [LLMON: An LLM-Native Markup Language, now in Granite 4.1 3B and 8B](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite) — blog
- [The Definitive Fine-Tuning Guide for 3D Generation Models](https://huggingface.co/blog/3d-lora-finetuning) — blog
- [United to block customers from using AI agents, citing cyber threats](https://therecord.media/united-airlines-to-block-customers-using-ai-agents) — blog
- [Chicago schools to Google – we'd rather lose Search than be forced to accept AI](https://www.techspot.com/news/114532-chicago-schools-tell-google-they-can-live-without.html) — hn
- [Why You Should Expect an AI Crash](https://www.economist.com/leaders/2026/11/12/why-you-should-expect-an-ai-crash) — hn
- [Foundation Models framework](https://developer.apple.com/foundation-models-framework/) — hn
- [AI is turning Apple's app review process into a nightmare for synth developers](https://synthanatomy.com/2026/11/ai-is-turning-apples-app-review-process-into-a-nightmare-for-developers.html) — hn
- [TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning Vision-Language Models](https://arxiv.org/abs/2611.15569v1) — arxiv

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-14.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
