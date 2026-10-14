# Firehose — 2026-10-14

## [Gemini 4 Argon](https://deepmind.google/models/gemini/)

`headline` · hn

Gemini 4 Argon is Google DeepMind's newly launched next-generation flagship model. (1 minute read)

## [Anthropic replaces git with a custom VCS for agent-scale CI](https://www.anthropic.com/engineering/redesigning-source-control)

`headline` · hn

Anthropic's monorepo merge rate grew from 2,500 to over 30,000 changes a day, so it replaced git with Scion, a server-side VCS with on-demand, sparse checkouts. The new stack uses about 200x less CPU and memory than the old git-mirror setup, turning CI checkouts into seconds instead of minutes. A seven-person team built it in five months while merge volume rose tenfold. (4 minute read)

## [Anthropic cuts distillation-attack data harvest 90-99%](https://www.anthropic.com/research/distillation-defenses)

`headline` · hn

Anthropic's new classifier and reasoning-access controls cut data harvested by model-distillation attacks by roughly 90-99%, dropping reasoning-token extraction 10-100x and banning accounts within two hours of a campaign starting. The false-positive rate stays under 0.1%. One flagged case: Kimi requests tied to a PLA-linked user were secretly routed through Claude. (4 minute read)

## [Sandbox flaw lets rogue AI agents escape and leak data](https://therecord.media/sandbox-vulnerability-gives-rogue-ai-agents-path-out)

`discovery` · blog

Researchers report a sandbox vulnerability that lets AI agents break out of their containment and leak data, though further technical detail on the finding isn't yet confirmed. (2 minute read)

## [OpenAI engineer arrested over bugged conference room](https://sfstandard.com/2026/10/13/openai-engineer-arrested-alleged-bugging-executive-conference-room/)

`headline` · hn

An OpenAI engineer has been arrested on allegations of planting a hidden listening device in an executive conference room. (1 minute read)

## [New MCP server gives AI agents full x64dbg control](https://github.com/duty1g/x64dbg-mcp-server)

`discovery` · github

A new MCP server lets AI agents drive the x64dbg debugger directly, with full execution control, every breakpoint type, and memory patching. It has already picked up about 2,500 stars, though its README warns the server exposes full memory read/write and shouldn't face untrusted networks. (3 minute read)

## [Janas streams MoE experts from SSD to beat RAM limits](https://github.com/prabanta-dev/janas)

`discovery` · hn

Janas streams MoE experts straight from an NVMe SSD, caching hot ones in RAM, so an 80B-parameter model can run and answer on a 32GB laptop. The author's benchmark puts Qwen3-Next-80B-A3B at about 37 tokens/sec with speculative decoding, versus 2.8 for llama.cpp. It's GPL-3.0 and explicitly labeled an experiment, not a product. (4 minute read)

## [One MCP server lets agents reverse-engineer almost anything](https://github.com/morluto/rea)

`discovery` · hn

A single MCP server now lets AI agents reverse-engineer native binaries, Electron and .NET apps, Android APKs, and firmware, calling out to existing Hopper, Ghidra, or IDA installs for native analysis. It ships as the npm package rea-agents and registers itself with Claude Code, Codex, Cursor, and Gemini CLI. (3 minute read)

## Also in the pool

- [QGIS enacts moratorium on AI contributions](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/387) — hn
- [Why aren't AI companies being charged for hacking?](https://mortoray.com/why-arent-ai-companies-being-charged-for-hacking/) — hn
- [Bring Your Own Agent: Your Employees' Assistants Are Already Logged In](https://thehackernews.com/2026/10/bring-your-own-agent-your-employees.html) — blog
- [Hackers activate automatic defrosting in supermarket fridges across Europe](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) — hn
- [We turned EmbeddingGemma 2 into a speech-to-text model](https://eg2.haku.sh/) — hn
- [Run fast, private agents on-device with LFM2.5-24B-A2B](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b) — blog
- [GitHub Tightens npm Publishing After Flaw Left 1,500+ Packages Vulnerable to Hijacking](https://thehackernews.com/2026/10/github-tightens-npm-publishing-after.html) — blog
- [French supermarkets suffer fridge shutdown after 'unprecedented' cyberattack](https://uk.finance.yahoo.com/news/french-supermarket-chains-cyberattack-forced-115141288.html) — hn
- [Fridges in French supermarkets hit by cyber attack](https://www.bbc.com/news/articles/crq5nzxv9q4yo) — hn
- [Hackers heat French supermarket fridges, sparking fires and food losses](https://www.reuters.com/business/retail-consumer/french-supermarket-chain-intermarche-hit-by-cyberattack-150-stories-targeted-2026-10-12/) — hn
- [Cyberattack shuts down refrigerators at French supermarkets](https://www.bleepingcomputer.com/news/security/cyberattack-shuts-down-refrigerators-at-french-supermarkets/) — blog
- [Cyberattack disrupts refrigeration at hundreds of French supermarkets](https://therecord.media/cyberattack-disrupts-refridgeration-in-france) — blog
- [French supermarkets suffer refrigerator shutdown after unprecedented cyberattack](https://www.rnz.co.nz/news/world/1865776/french-supermarkets-suffer-refrigerator-shutdown-after-unprecedented-cyberattack) — hn
- [Attackers Heat French Supermarket Fridges Up to 50°C by Hijacking Danfoss Controllers](https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html) — blog
- [A look at the math that OpenAI claims computes faster Fourier transforms](https://www.argmin.net/p/faster-fourier-transforms) — hn
- [Attacker Chains Three Ivanti Connect Secure Zero-Days for Root Access, Only Two Patched So Far](https://thehackernews.com/2026/10/attacker-chains-three-ivanti-connect.html) — blog
- [Ivanti warns of Connect Secure zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/ivanti-warns-of-connect-secure-zero-day-exploited-in-attacks/) — blog
- [OpenAI finds recording device in one of their offices](https://twitter.com/OpenAINewsroom/status/2110095403198849132) — hn
- [OpenAI engineer arrested for allegedly planting spy device in office](https://www.bleepingcomputer.com/news/artificial-intelligence/openai-engineer-arrested-for-allegedly-planting-spy-device-in-office/) — blog
- [Physical Intelligence API Beta: Frontier Models for Every Robot](https://www.pi.website/blog/api-beta) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-14.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
