# Firehose — 2026-09-22

## [Jev's Decision Models Spawn Same-Day Open Clones](https://simonwillison.net/2026/Sep/21/jev/)

`headline` · blog

Jev answers yes/no, multiple-choice, and rating questions about a state in a single forward pass, returning calibrated probabilities instead of generated text. Within a day, Kev reimplemented the approach as an open model on Qwen3.5, and jevals swapped it in for LLM-as-judge scoring. Decision models are now a distinct, buildable model class, not just one lab's product. (3 minute read)

## [Xiaomi Ships MiMo v2.6](https://mimo.xiaomi.com/mimo-v2-6)

`headline` · hn

Xiaomi shipped MiMo v2.6, the newest release in its open-weight model line, giving developers a new checkpoint to evaluate. (1 minute read)

## [Mini-AGI Trains Continuously on 8GB of VRAM](https://github.com/volotat/mini-AGI/)

`discovery` · hn

Mini-AGI trains continuously on one text stream, routing each character through 2 dense blocks plus a recurrent block applied up to 24 times with per-token halting. Training the trunk at 0.1x the experts' learning rate cut catastrophic forgetting from +2.23 to +0.0067 nats over a 524K-character read. It now runs 169 experts and holds 0.8336 nats/char on held-out data — continual learning without a cluster. (4 minute read)

## [A 12-Chapter Open-Source Book on AI Infrastructure](https://github.com/bojieli/ai-infra-book)

`discovery` · github

A new open-source book covers AI infrastructure across 12 chapters — KV-cache management, speculative decoding, accelerator tradeoffs, multi-device networking — deriving each from hardware constraints rather than describing it abstractly. It ships with runnable calculation tools and reproducible experiments, and has already drawn 4.9k GitHub stars and 357 forks. Anyone sizing an inference cluster now has working code to check their numbers against. (3 minute read)

## [Jevals Replaces LLM Judges With Typed Decisions](https://github.com/openlayer-ai/jevals)

`discovery` · hn

Jevals scores agent traces with typed decision models instead of LLM judges: $0.00006 per trace at 244ms p50, versus 6-11 LLM calls per sample the old way. It cites a LangChain finding that GPT and Claude judges vary 92x-913x in score on identical traces — the inconsistency this replaces. 37 built-in evals ship today, in alpha, with OpenAI, LangGraph, and Claude SDK integrations. (3 minute read)

## [ValueDiff Trims KV-Cache for Sink-Suppressed LLMs](https://arxiv.org/abs/2609.23314v1)

`discovery` · arxiv

ValueDiff proposes a value-geometric method for evicting KV-cache entries in sink-suppressed LLMs, aimed at cutting inference memory without hurting output quality. (2 minute read)

## [Paper: General LLM Benchmarks Don't Tell You Much](https://arxiv.org/abs/2609.23201v1)

`discovery` · arxiv

The paper argues general-purpose LLM ranking benchmarks overstate what they measure, and makes the case for task-specific evaluation instead. (1 minute read)

## [ChatGPT Ties Browsing Activity Into Ad Collector](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)

`headline` · hn

Reports say ChatGPT now links users' activity on other websites into an ad-data collector tied to their accounts. (2 minute read)

## Also in the pool

- [datawhalechina/zero-to-sglang](https://github.com/datawhalechina/zero-to-sglang) — github
- [Researchers escape OpenAI Codex sandbox to run commands on host](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/) — blog
- [Co-occurrence Patterns of LoRA Adapters in Production Diffusion Model Inference Services](https://arxiv.org/abs/2609.23321v1) — arxiv
- [Judging a Review by its Cover: A Reliability Analysis of LLM-based Peer Review Evaluation Metrics](https://arxiv.org/abs/2609.23264v1) — arxiv
- [HarnessRouter/harnessrouter](https://github.com/HarnessRouter/harnessrouter) — github
- [google/artemis](https://github.com/google/artemis) — github
- [nari-labs/nari-qwen3-tts](https://github.com/nari-labs/nari-qwen3-tts) — github
- [Pruning LLMs Like a Physicist: Block Removal as an Ising Optimization Problem](https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an) — blog
- [Graph Memory for LLM Agents: At What Cost? A Comparative Evaluation of Query, Ingest, and Update Performance Across Graph Database Engines](https://arxiv.org/abs/2609.23315v1) — arxiv
- [Heretic removes restrictions from language models](https://heretic-project.org/) — hn
- [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) — github
- [jsdhwfmax/EvalForge](https://github.com/jsdhwfmax/EvalForge) — github
- [Our framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework) — blog
- [BragJack attacks hijack AI browser agents through malicious extensions](https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/) — blog
- [Show HN: Foremerge – Catch intent conflicts between parallel coding agents](https://github.com/naw103/foremerge) — hn
- [TicTacBench: Benchmarking Timing Closure Capabilities of Coding Agents](https://arxiv.org/abs/2609.23363v1) — arxiv
- [Your Agent Aced the Task. Will It Do It Again?](https://huggingface.co/blog/ibm-research/altk-evolve-consistency) — blog
- [Safety for Whom? Refusing the Right Subset of a Topic, Not the Whole Topic](https://huggingface.co/blog/MultiverseComputingCAI/safety-for-whom) — blog
- [So you want to use OpenRouter?](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter/) — blog
- [tokenizers v1: encode, decode and scaling, measured](https://huggingface.co/blog/tokenizers-v1) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-09-22.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
