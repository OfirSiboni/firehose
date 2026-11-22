# Firehose — 2026-11-22

## [Claude-assisted Riemann Hypothesis proof formally verified by Lean](https://alpo.ge/remark.pdf)

`headline` · hn

Lean and Mathlib formally verified that Levent Alpöge's Claude-assisted proof of the Riemann Hypothesis and GRH is correct, checked by Lean's kernel plus the independently-verified con-leche and con-ron checkers. The formalized proof runs 17 million lines, and mathematicians expect years of work to distill the underlying ideas into human-explainable form. Researchers can now treat the result as formally checked rather than merely claimed. (3 minute read)

## [AI agents found a real zero-day, took root on a university server](https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html)

`headline` · blog

Autonomous Cairn AI agents found and exploited a path-traversal zero-day in MONAI Label (CVE-2026-133968, CVSS 9.8), going from API mapping to a root shell in 11 minutes. Amazon ties the September 8-10 campaign against university targets to a China-linked actor, reconstructed after the attackers left their Cairn control panel exposed with no authentication. MONAI merged a source fix October 19, but no patched package has shipped. (3 minute read)

## [AI-designed CPU claims 4.59x performance per watt, pre-silicon](https://architectlabs.com/blog/frostbite)

`discovery` · hn

Architect Labs says AI agent swarms designed Frostbite, a CPU built on interaction nets where parallelism comes from the program's dependency graph instead of threads or caches. The team reports 4.59x geometric-mean performance-per-watt over an undisclosed baseline across 25 workloads, synthesized at 500MHz in a 0.792mm² layout at 7nm. The results are pre-silicon and self-reported against an anonymized baseline, so independent benchmarking is the next step. (3 minute read)

## [Thinking Machines ships Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/)

`headline` · hn

Thinking Machines released Inkling 2 Mini, its newest model, already near the top of Hacker News. (1 minute read)

## [Malicious webpage gave researchers full control of a Meta Muse agent](https://thehackernews.com/2026/11/a-single-malicious-webpage-let.html)

`discovery` · blog

A single malicious webpage opened by Meta's Muse agent let NebuSec researchers chain a browser bug with a Linux kernel flaw to take over the user's cloud VM, reaching stored chats, memories, and the credential store with no approval prompt. The compromise stayed inside one user's machine and didn't reach the shared host or other users. It was a lab demonstration, and Meta fixed the issues before publication. (3 minute read)

## [Signal blocks AI agents from reading chats via screenshots](https://signal.org/blog/protecting-your-privacy/)

`discovery` · hn

Signal will restrict screenshots by default on Android and iOS specifically to stop OS-level AI agents, such as those built into iOS 27, from reading chats on-screen. The app can detect when an AI assistant is attempting to read it, but Signal says the protection is incomplete. It's a new defensive layer against agents with screen or accessibility access, not just malware. (2 minute read)

## [Kyojin runs 100GB-class open models on a single desktop](https://github.com/Yamz-Labs/kyojin)

`discovery` · github

Kyojin is a new open-source, OpenAI-compatible inference engine built on ExLlamaV3 for running 100GB-class open models on one desktop machine. It serves GLM-5.3-Flash and Qwen3.8-Flash-Next (95-100GB) on a 128GB AMD Strix Halo box at 32-53 tok/s decode, and DeepSeek V4.1 Flash (184.7GB) on a Mac Studio at 62 tok/s with up to 983K token context. All numbers are the maintainers' own. (3 minute read)

## [Scott Aaronson: the Riemann Hypothesis proof checks out](https://scottaaronson.blog/?p=10344)

`discovery` · hn

Scott Aaronson now says the Claude-assisted Riemann Hypothesis proof is correct, updating once an independent Lean certificate landed from con-leche, itself formally verified back to set-theory axioms. He notes no AI math result with a Lean certificate has been retracted, while uncertified ones have. He separates verification from understanding: the 17-million-line proof is checked, but mathematicians will need years to explain the actual ideas. (3 minute read)

## Also in the pool

- [Mapping every neuron in Qwen3-8B](https://www.fermionresearch.com/research/mapping-every-neuron-in-qwen3-8b/) — hn
- [Quoting Levent Alpöge](https://simonwillison.net/2026/Nov/20/levent-alpoge/) — blog
- [Astra 6.2 and Sol 6.2 flop at Simple Bench](https://simple-bench.com/) — hn
- [N1nEmAn/sapper-v2](https://github.com/N1nEmAn/sapper-v2) — github
- [Can AI help scientists identify promising drug candidates?](https://openai.com/index/introducing-medchembench) — blog
- [Bazuka Android Malware Uses Fake Screen Overlays to Hide Credential Theft and Device Control](https://thehackernews.com/2026/11/bazuka-android-malware-uses-fake-screen.html) — blog
- [Policy and Disclosure: 2026 Edition](https://projectzero.google/2026/11/disclosure-policy.html) — blog
- [Tell HN: OpenRouter prompts to Minimax may have been read](https://news.ycombinator.com/item?id=50585962) — hn
- [Leaky AI supply chain is exposing secret user data at an alarming rate](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/) — hn
- [Bell Canada says 'agentic' hacker stole enterprise customer data](https://www.bleepingcomputer.com/news/security/bell-canada-says-agentic-hacker-stole-enterprise-customer-data/) — blog
- [The Hungry Butler Effect: Concealed Commercial Incentives in LLMs](https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models) — hn
- [XYBench: Helping with the problem behind the question](https://huggingface.co/blog/allenai/xybench) — blog
- [Introducing harness adapters: adapt your favorite model to your harness to improve performance and cost](https://huggingface.co/blog/harness-adapters-at-scale) — blog
- [Vibecoding an inference chip](https://ankitg.me/blog/vibecoding-inference-chip/) — hn
- [yjid/kensaku](https://github.com/yjid/kensaku) — github
- [AI Doesn’t Have to Go Rogue to Break the World](https://www.schneier.com/blog/archives/2026/11/ai-doesnt-have-to-go-rogue-to-break-the-world.html) — blog
- [Llms.txt and MCP didn't move the needle](https://backpackforlaravel.com/articles/opinions/llms-txt-and-mcp-didn-t-move-the-needle-for-us-here-s-what-did) — hn
- [Microsoft Entra Connect Health flaw exploited to steal tenant data](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/) — blog
- [Muru](https://simonwillison.net/2026/Nov/21/muru/) — blog
- [Language Models Can Rewrite Their Own Weights](https://arxiv.org/abs/2611.21885) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-22.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
