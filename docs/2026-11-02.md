# Firehose — 2026-11-02

## [A Brazilian court fined lawyers $16k for a hidden prompt injection](https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/)

`headline` · hn

A hidden white-on-white instruction told Brazil's national court AI, Galileu, to go easy on a R$842,000 labor claim; Galileu flagged it and blocked the filing instead. The 3rd Labor Court of Parauapebas fined the two firms 10% of the claim, about $16,000, in what may be the first ruling worldwide on intentional prompt injection against a court AI. (4 minute read)

## [Google's Suncatcher satellite ran its first AI inference in orbit](https://blog.google/innovation-and-ai/models-and-research/google-research/project-suncatcher-satellite-response/)

`discovery` · hn

Google's Project Suncatcher prototype, launched October 1, powered up its TPU tray and ran Gemma 4 in orbit, producing a haiku that downlinked through a ground station over Svalbard. Follow-up prompts generated limericks and telemetry reports. No power or compute specs were disclosed; the next milestone is twin interconnected satellites in 2027. (3 minute read)

## [SynthID-style watermarking quietly cuts response diversity](https://blog.keyvan.net/p/ai-text-watermarking-and-quality)

`discovery` · hn

Claude's text watermarking, built on Google's SynthID-Text, biases token choice with a keyed pseudo-random sequence over a sliding window. SynthID's own supplement documents a diversity trade-off: one informal test found 4 of 5 watermarked responses to the same prompt opened nearly identically, versus 3 distinct openings unwatermarked. Key rotation cuts the effect but weakens detection on short text. (5 minute read)

## [mojo-dllm runs diffusion LLMs on CPU with no Python at runtime](https://github.com/vladimirrott/mojo-dllm)

`discovery` · github

mojo-dllm is a from-scratch Mojo runtime for diffusion language models LLaDA-8B and Dream-7B, loading quantized GGUF weights with no Python at runtime. On a laptop CPU it hits 1.33 tokens/sec versus llama.cpp's 0.69; on an RTX 3050 it trails llama.cpp's CUDA path (9.43 vs 15.68 tokens/sec) but needs only about 1GB of host memory. (3 minute read)

## [Apollo economist: AI shows zero payoff outside Big Tech](https://techcrunch.com/2026/10/25/ai-delivers-zero-financial-payoff-to-most-companies-according-to-apollo-economist/)

`headline` · hn

Apollo's chief economist Torsten Slok reports flat profit margins and revenue per worker across the S&P 493 - the S&P 500 minus Alphabet, Amazon, Apple, Meta, Microsoft, Nvidia, and Tesla - with no visible AI productivity gain. The note cites no underlying data, sample size, or time window. The debate over AI's ROI outside Big Tech now has a specific, if thin, data point to argue over. (2 minute read)

## [A hobbyist fine-tuned Qwen2.5-Code-7B into a demoscene-code model](https://datavorous.com/writing/demoscener/)

`discovery` · hn

Demoscener-7B is Qwen2.5-Code-7B fine-tuned on 25k Dwitter 'Dweets' - 140-character JS demos - then refined with GRPO using the author's own ratings as the reward signal across roughly 40,000 reviewed animations. Perplexity on held-out Dweets dropped from 28.63 to 8.57 after pretraining and from 7.42 to 5.65 after curriculum training. Both the model and the 25k-Dweet dataset are open on Hugging Face. (6 minute read)

## [A language model runs straight from a 512-byte boot sector](https://github.com/kerlenton/bootgpt)

`discovery` · hn

bootgpt loads an 11.5KB int8 model from 23 disk sectors and runs inference in 16-bit real mode on a 386-class CPU, with no OS and no C runtime. The character-level network, hand-written in x86 assembly, generates a fake Linux dmesg boot log using only integer multiplies and one division. The author's Python training simulation matches the assembly's output character for character. (3 minute read)

## [FreeVideo runs MiniMax H3 video generation on 8GB of VRAM](https://github.com/FlashML-org/FreeVideo)

`discovery` · github

FreeVideo is a local inference engine for MiniMax H3 video diffusion that streams weights in chunks to fit an 8GB-VRAM, 16GB-RAM consumer machine. Switching to int8 weights in v0.3.0 made 5-second clips generate about 2.3x faster on an RTX 3090. A preview build also runs on Apple silicon with 24GB of unified memory. (2 minute read)

## Also in the pool

- [GPT-5.6 Sol can beat Factorio on peaceful mode](https://ryanmadden.net/gpt-56-beats-factorio/) — hn
- [AI agent swarms in Minecraft fail to build civilization, drown in bureaucracy](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-agent-swarms-unleashed-in-minecraft-to-build-a-thriving-civilization-50-agent-teams-fail-after-falling-into-paralyzing-bureaucracy) — hn
- [Folkbench/folkbench](https://github.com/Folkbench/folkbench) — github
- [Muse AI agent is a commercial surveillance network disguised as an AI assistant](https://paulfwalsh.substack.com/p/metas-muse-ai-agent-is-a-commercial) — hn
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu) — github
- [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) — github
- [ceyyy427/finathink](https://github.com/ceyyy427/finathink) — github
- [FengZhenfei/carrel](https://github.com/FengZhenfei/carrel) — github
- [h9-tec/ai-roadmap-2026](https://github.com/h9-tec/ai-roadmap-2026) — github
- [ashishsinha1602/schemagate](https://github.com/ashishsinha1602/schemagate) — github
- [morluto/awesome-reverse-engineering](https://github.com/morluto/awesome-reverse-engineering) — github
- [daveebbelaar/bama](https://github.com/daveebbelaar/bama) — github
- [sahenjp/RustXNG](https://github.com/sahenjp/RustXNG) — github
- [JEen-wang/Adaptive-rag](https://github.com/JEen-wang/Adaptive-rag) — github
- [Takamatsu-Hikaru/AI-Research-Guide](https://github.com/Takamatsu-Hikaru/AI-Research-Guide) — github
- [davidondrej/cloudroom](https://github.com/davidondrej/cloudroom) — github
- [Anthropic's Claude AI blocks video game cloning and reverse-engineering](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked) — hn
- [Anthropic takes steps to block Claude from reverse-engineering video games](https://mashable.com/tech/anthropic-takes-steps-to-block-video-game-cloning-and-reverse-engineering) — hn
- [Anthropic blocks users for anything touching training larger models](https://twitter.com/jiahaoshao1/status/2116475922190922088) — hn
- [IEEE Wipes Out 1,417 Papers over Sold Authorship](https://www.nature.com/articles/d41586-026-03455-8) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-02.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
