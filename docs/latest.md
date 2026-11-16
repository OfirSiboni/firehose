# Firehose — 2026-11-16

## [Show HN: DeepSeek V3 in ~200 lines of pure Jax](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax)

`discovery` · hn

A 190-line pure-JAX reimplementation of DeepSeek-V3 (MLA, MoE routing, aux-loss-free balancing, multi-token prediction) trains a 36.2M-param model on a MacBook Air M5 in 2.6 hours, cutting validation loss from 5.02 to 3.51. Its MLA cache stores 144 numbers per token per layer versus 480 for full KV. (3 minute read)

## [Understanding Positional Embeddings in Modern LLMs](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings)

`discovery` · hn

A survey of positional-embedding schemes finds NoPE ranked first across 10 length-generalization tasks in a 107M-parameter study, ahead of RoPE. SmolLM3 skips RoPE in every fourth layer to improve long-context performance, and partial RoPE, rotating about 10% of head features, became the majority choice among RoPE models in 2026. (4 minute read)

## [Advancing science and engineering with Antigravity's /teamwork](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)

`headline` · hn

Google's Antigravity /teamwork pattern splits tasks across agents with dedicated verifiers. It scaled lock-free connected-components to 1-trillion-edge graphs at 60-90x the throughput and a sixth the RAM of TCP key-value stores, and a from-scratch AlphaZero Go engine gained 2600 Elo in under eight days. (3 minute read)

## [vladimirrott/mojo-dllm](https://github.com/vladimirrott/mojo-dllm)

`discovery` · github

mojo-dllm runs diffusion language models like LLaDA and Dream from quantized GGUF files in Mojo, with no Python at runtime. On an RTX 3050, its step times land within 10% of llama.cpp's CUDA diffusion kernels while using a fraction of the memory -- 1.1GB peak RSS versus 5.3GB in one listed run. (4 minute read)

## [Your Agent Will Pick the Hackable One](https://geoffstearns.com/blog/your-agent-will-pick-the-hackable-one/)

`discovery` · hn

Owners reverse-engineered custom firmware (a synth, a groovebox, a Doom port) for M-Vave's $70 FM-1 synth within weeks, pushing the maker to open-source it under GPLv3 with a 10-second recovery tool. The argument: as coding agents get cheap, buyers' agents will favor hackable, recoverable hardware, so resistant makers lose sales. (3 minute read)

## [Claude asked to renumber pages deletes professor's syllabus, year of notes](https://www.tomshardware.com/tech-industry/artificial-intelligence/rogue-claude-ai-tasked-with-renumbering-pages-accidentally-deletes-law-professors-entire-syllabus-one-year-of-lecture-notes-youre-right-to-be-angry-i-deleted-your-files-through-my-own-carelessness-humbled-agent-admits)

`discovery` · hn

A Claude agent tasked with renumbering a law professor's PDF pages instead deleted the entire syllabus and a year of lecture notes, then apologized: 'I deleted your files through my own carelessness.' A reminder to back up or sandbox before giving an agent write access to irreplaceable files. (3 minute read)

## [All AI-generated code should be Open Source](https://jakub.jankiewicz.org/blog/ai-code-open-source/)

`headline` · hn

A 1061-point HN discussion argues AI-generated code should be forced open or public-domain, since models train on open-source and Creative Commons code, and leans on the 'Monkey Selfie' precedent to say non-human-authored output isn't copyrightable in the first place. (3 minute read)

## [A visual explanation of reinforcement learning](https://aatishb.com/myriad/how-brains-learn/)

`discovery` · hn

An interactive visual walkthrough of how reinforcement learning (and the brain) assigns credit and learns from reward, aimed at building intuition rather than reporting a new result. (2 minute read)

## Also in the pool

- [PyPI's redesigned project pages with clearer security signals are now live](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) — hn
- [The Claude Delusion](https://www.netmeister.org/blog/claude-delusion.html) — hn
- [modelsphere/modelsphere](https://github.com/modelsphere/modelsphere) — github
- [TSMC employee data breach linked to cloud provider](https://www.bleepingcomputer.com/news/security/tsmc-employee-data-breach-linked-to-cloud-provider/) — blog
- [Parents pay $75k for Alpha's AI school. Half of its students missed math target](https://fortune.com/2026/11/14/alpha-school-ai-students-tuition-learning-goals/) — hn
- [Uber confirms hackers stole drivers' license information in breach](https://techcrunch.com/2026/11/13/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/) — hn
- [Formalizing US Tax Code (Using Lean)](https://lexifina.com/blog/formalizing-the-us-tax-code) — hn
- [Show HN: Agweb – a browser for agents that stays out of your way](https://github.com/paul-nameless/agweb) — hn
- [Show HN: Fursoy – Out-of-order RV64IMAFDV core in SystemVerilog (Linux 6.6)](https://github.com/FURSOY/fursoy-cpu) — hn
- [usamahz/cpu-performance-engineering](https://github.com/usamahz/cpu-performance-engineering) — github
- [US disrupts North Korean campaign behind $400 million crypto theft](https://www.bleepingcomputer.com/news/security/us-disrupts-north-korean-campaign-behind-400-million-crypto-theft/) — blog
- [Attackers Exploit UnrealIRCd Flaw That Enables Server-Level Command Injection](https://thehackernews.com/2026/11/attackers-exploit-unrealircd-flaw-that.html) — blog
- [Nvidia deliberately kept GPU prices high through circular financing deals](https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html) — hn
- [LinkedIn, Monster take down over 1000 fake job postings after CBC investigation](https://www.cbc.ca/news/canada/linkedin-monster-take-down-over-1-000-fake-job-postings-after-cbc-investigation-9.7415379) — hn
- [Will we put data centers in space?](https://www.forethought.org/research/will-we-really-put-data-centers-in-space) — hn
- [Smuggling of 1.5M AI GPUs could be the cause of Huang's departure](https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls) — hn
- [Demystifying phone unlocking tools: A technical overview](https://osservatorionessuno.org/blog/2026/05/demystifying-phone-unlocking-tools-a-technical-overview/) — hn
- [Show HN: Turbo-Browser-MCP – Batch forms, DOM deltas and submit guards for MCP](https://github.com/Tthanh2k6/turbo-browser-mcp) — hn
- [We're Asking an Appeals Court to Require a Warrant for ALPR Searches](https://www.eff.org/deeplinks/2026/11/were-asking-appeals-court-require-warrant-alpr-searches) — hn
- [Court denies motion to dismiss DRAM price fixing case](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-16.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
