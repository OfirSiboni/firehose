# Firehose — 2026-11-27

## [Fingerprinting outs TypeSafe's Jev as Qwen3.5-35B-A3B](https://modaic.dev/blog/latency-doesnt-lie)

`discovery` · hn

Tokenizer correlation, throughput curves, and self-ID probes across 22 prompt variants point to TypeSafe's 'Jev' judge model being a relabeled Qwen3.5-35B-A3B. Its prefill throughput tracks a self-hosted Qwen3.5-35B-A3B within 7-22%, and it names Qwen 74% of the time when asked what it wants to claim to be. Benchmarkers can now treat Jev as a known MoE, not a black box. (3 minute read)

## [China's Salt Typhoon hackers now run Artex for recon and exploits](https://therecord.media/microsoft-china-salt-typhoon-using-artex-ai-tool)

`headline` · blog

Microsoft says Chinese state actors Salt Typhoon and Crystal Typhoon have added the AI-driven pentest tool Artex for recon, credential attacks, and web exploitation. Artex shipped in July, the FBI warned about it two weeks earlier, and Salt Typhoon is already tied to a 2024 breach of nine US telecoms. Defenders should watch for bursts of varied requests with rapid retries, since Artex doesn't hide its traffic by default. (4 minute read)

## [180B-parameter MoE model now runs inside 32GB of RAM](https://huggingface.co/blog/moe-expert-streaming)

`discovery` · blog

Expert streaming now runs the 180B-parameter Qwen3.8-Flash-Next on a 32GB Mac M5, keeping only the router's active experts in memory and reading the rest from SSD on demand. Experts are quantized to 3 bits for a 49GB on-disk footprint, and the result hits 13.9 tok/s decode and 228 tok/s prefill, within 6% of the Strata baseline. Anyone with a 32GB machine can now run a 180B model instead of needing a multi-GPU server. (4 minute read)

## [Novita, StreamLake, and Ant Digital are ByteDance Ark wrappers](https://kendell.dev/blog/arkwrapper/)

`discovery` · hn

Network fingerprints, ID formats, and censorship behavior show Novita, StreamLake, and Ant Digital are reselling ByteDance's Ark/Doubao models under their own names: downloads trace to Volcano Engine and BytePlus, tool-call IDs use Ark's 'call\_00\_' prefix, and Tank Man questions get ByteDance's canned refusal. A public GitHub probe tests every OpenRouter host of DeepSeek V4.1 Flash, so buyers can check which 'independent' provider is really just a markup on ByteDance's infrastructure. (4 minute read)

## [1Password breach exposed customer account data, not vaults](https://1password.com/blog/update-on-nov-2026-security-incident)

`headline` · hn

A compromised employee GitHub account let an attacker reach 1Password's CI/CD system and push malicious code that pulled a subset of customer account data, including names, emails, account IDs, and some invitation and recovery tokens. Vault contents, vault keys, and account recovery keys were not affected, and 1Password lengthened its recovery codes from six digits to ten alphanumeric characters. A full root-cause analysis is still pending. (3 minute read)

## [Italy and Switzerland report successful autonomous AI attacks](https://www.bleepingcomputer.com/news/security/italy-and-switzerland-warn-of-autonomous-ai-driven-cyberattacks/)

`discovery` · blog

Italy's CSIRT found a DeepSeek Harness setup running a 5-agent coordinator for recon, exploitation, and persistence that compromised many systems within hours and wrote new code in real time to dodge defenses. Switzerland's NCSC logged its first AI-agent-assisted attacks on critical infrastructure, with every known case ending in compromise, and says public AI agents have nearly doubled since October. Both agencies name ARTEX AI, CyberStrikeAI, DeepSeek Harness, and PentAGI as the tools involved. (4 minute read)

## [Bare-metal OS boots Qwen3-0.6B with no Linux, no libc](https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os)

`discovery` · hn

A 24KB assembly kernel now boots Qwen3-0.6B directly on x86-64 hardware, no Linux, no libc, reaching an interactive prompt in 74-94ms. On a 16-vCPU KVM instance it decodes at about 135 tok/s, and the author claims it beats both the Linux-based version and llama.cpp's CPU path at every thread count. That means a usable LLM chat loop can now run on hardware with no operating system at all. (3 minute read)

## [AMD-specific llama.cpp patches roughly double RDNA throughput](https://devnull.land/amd-specific-llama-cpp)

`discovery` · hn

A minimal patch set applied on top of llama.cpp roughly doubles throughput on AMD RDNA GPUs: prefill goes from about 700 to 1,300 tok/s and generation from about 35 to 55 tok/s on an R9700 eGPU running a 27B model. The patches are reapplied to each new llama.cpp release rather than maintained as a permanent fork. AMD GPU owners running local models can now get roughly 2x the tokens per second without switching hardware. (4 minute read)

## Also in the pool

- [North Korea-Linked PolinRider Poisons Over 7,600 GitHub Repositories to Spread Malware](https://thehackernews.com/2026/11/north-korea-linked-polinrider-poisons.html) — blog
- [How OpenAI’s Performance Factory keeps ChatGPT fast](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast) — blog
- [heterodoxin/AbliteratedOutTheBox](https://github.com/heterodoxin/AbliteratedOutTheBox) — github
- [Introducing Tool Retrieval in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/) — blog
- [Google Will Make AI Agents Use Its MCP Servers. The Gmail One Can't Send Email](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) — hn
- [Inside the Codex sandbox](https://openai.com/index/inside-the-codex-sandbox) — blog
- [Tracking Diseases Cured by AI](https://diseasescuredbyai.com/) — hn
- [Notion's official MCP inject hidden upsell instructions into agent context](https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/) — hn
- [Unconditional Integer Factorization in Subexponential Time](https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization) — hn
- [Multiagent coding is the future](https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/) — hn
- [Advancing chip design with OpenAI models](https://openai.com/index/advancing-chip-design-with-our-models) — blog
- [Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench) — blog
- [Swarms, Flocks, Gangs: How to build, train, and evaluate multi-agent systems](https://huggingface.co/blog/training-swarms) — blog
- [Top-cited AI scientists at four US companies compared](https://topcitedscientists.com/figures/ai-at-four-us-companies/) — hn
- [The polynomial Hirsch conjecture is false \[pdf\]](https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf) — hn
- [Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) — blog
- [Rumble-2-Flash: an open 0.5B speech model for 40+ languages](https://huggingface.co/blog/rumble-2-flash) — blog
- [Research acceleration: The jagged frontier](https://openai.com/index/research-acceleration-jagged-frontier) — blog
- [Managing frontier AI risk: From training to deployment](https://openai.com/index/managing-frontier-ai-risk) — blog
- [DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-27.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
