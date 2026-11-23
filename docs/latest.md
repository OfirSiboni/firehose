# Firehose — 2026-11-23

## [Canary tokens catch AI inference providers stealing and leaking prompts](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

`headline` · hn

Dragos seeded 2 million canary-tokened prompts across inference providers since July, catching real breaches: one stolen AWS key was used within a day and stayed active three weeks, and a Zero-Data-Retention-flagged secret link surfaced in a Chinese chat 24 days later. OpenRouter pulled three providers and 125 endpoints from ZDR eligibility in response, so anyone routing prompts through a marketplace should assume ZDR promises aren't verified. (5 minute read)

## [Astra 6.2 and Sol 6.2 still trail humans on Simple Bench](https://simple-bench.com/)

`headline` · hn

Simple Bench's non-specialist human baseline sits at 83.7%, beating every LLM tested, including the current top model, Claude Fable, at 81.9%. Astra 6.2 and Sol 6.2 reportedly score further behind on the same benchmark. The gap shows two more frontier launches still lose to ordinary human judgment on this benchmark's reasoning traps. (1 minute read)

## [Sapper-v2 wins a pentest CTF using 4.5x fewer tokens](https://github.com/N1nEmAn/sapper-v2)

`discovery` · github

Sapper-v2's multi-agent harness - commander, generals, soldiers, and scouts, tiered across GLM-5.3 and DeepSeek V4.1 Flash - won a Tencent Cloud Attack-Defense Challenge qualifier, scoring 80.18/100 across 634 teams. It matched the runner-up's 85 flags 25 seconds faster using about 1 billion tokens against their 4.5 billion. Self-reported, but the harness and its shared-memory design are open source to inspect and reuse. (4 minute read)

## [Ghostscript sandbox-escape RCE reaches Gradio and AI image apps](https://pwn.ai/upload2shell)

`discovery` · hn

A use-after-free in Ghostscript's Type 1 font loader (CVE-2026-125396) escapes its -dSAFER sandbox via a crafted document, with confirmed remote code execution in Gradio, Debian's CUPS, Roundcube, and WordPress Core. AI image tools InvokeAI, AUTOMATIC1111, and ComfyUI are reachable through the same Pillow path but not independently confirmed. Ghostscript 10.08.0 fixes it upstream, so check whether your image pipeline still shells out to it. (3 minute read)

## [Microsoft's TokenEconomizer cuts coding-agent cost up to 31%](https://github.com/microsoft/TokenEconomizer)

`discovery` · github

TokenEconomizer learns repo-specific facts and prunes unused tool definitions for Claude Code, Codex, and Copilot CLI sessions. Across 277 SWE-Bench tasks spanning 6 repos and 5 agent-model pairs, it cut mean cost 18.4-30.9% in every one of 30 combinations, with pass@1 flat or higher in 4 of 5. It runs as a stdlib-Python plugin that stores its learned state locally. (3 minute read)

## [Signal blocks Siri and Gemini from reading chats off-screen](https://www.bleepingcomputer.com/news/security/signal-to-block-siri-gemini-ai-from-capturing-chats-on-ios-android/)

`discovery` · blog

Signal now blocks Siri's Onscreen Awareness on iOS 27 and Android's Gemini Intelligence from reading chat content off the screen, a pathway Signal found through its own reverse engineering. The iOS block also disables screenshots of Signal chats; Android auto-enables Screen Security when it detects an AI assistant reading the screen. macOS users must manually exclude Signal from Siri in System Settings. (3 minute read)

## [Anthropic's 2028 US power mix projected at 87% gas, 11% coal](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/)

`headline` · hn

Independent modeling from the Better Data Center Project pegs Anthropic's 2028 US power mix at roughly 87% gas and 11% coal, against 1.7GW of gas-generator commitments and no disclosed US renewables. The mid-case estimate is 32 million tons CO2e in 2028, more than California's entire 2024 power sector, at power about 35% more carbon-intensive than the US grid average. These are modeled estimates, not Anthropic's own disclosures. (4 minute read)

## [Berth arbitrates one GPU's VRAM across local AI engines](https://github.com/T-Crypt/berth)

`discovery` · github

Berth is a Go daemon that leases a single GPU's VRAM across llama.cpp, vLLM, Ollama, ComfyUI, and games by priority, queuing requests instead of letting them crash each other out of memory. It parks idle model weights to system RAM or restores via NVIDIA's cuda-checkpoint instead of reloading from disk. Over one month on the author's RTX 4090, it queued 1,136 requests and swapped 901 engines at safe boundaries. (3 minute read)

## Also in the pool

- [Perplexity and Intelligence](https://openai.com/index/perplexity-and-intelligence/) — hn
- [mw00/project-maya](https://github.com/mw00/project-maya) — github
- [Tell HN: OpenRouter prompts to Minimax may have been read](https://news.ycombinator.com/item?id=50585962) — hn
- [RCE in Gnupg](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) — hn
- [reacher-z/Awesome-REA](https://github.com/reacher-z/Awesome-REA) — github
- [FBI reportedly investigating apparent hack of its criminal database](https://www.bbc.com/news/articles/cvze7de86pk3o) — hn
- [modelsphere/modelsphere](https://github.com/modelsphere/modelsphere) — github
- [Leaky AI supply chain is exposing secret user data at an alarming rate](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/) — hn
- [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d) — github
- [Rackspace Spot breach let hackers access customer Kubernetes secrets](https://www.bleepingcomputer.com/news/security/rackspace-spot-breach-let-hackers-access-customer-kubernetes-secrets/) — blog
- [Together.ai: Prompt Leakage for Requests](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026) — hn
- [Data Processing Incidents on Inference Providers](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) — hn
- [OpenRouter Drops 3 Providers After Researchers Catch Months of Prompt Theft at AI Hosting Firms](https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html) — blog
- [Lean verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) — hn
- [PcapAnalyzer – self-hosted pcap analyzer with 27 problem detectors](https://github.com/sebaandrada-cell/PcapAnalyzer) — hn
- [YOLOW92/pagesift](https://github.com/YOLOW92/pagesift) — github
- [Pandex – Official European Law for AI Agents, over MCP](https://www.pandex.io) — hn
- [Researchers Demonstrate Ghostscript Sandbox-Escape RCE via Crafted File Uploads in Popular Apps](https://thehackernews.com/2026/11/researchers-demonstrate-ghostscript.html) — blog
- [Microsoft Entra Connect Health flaw exploited to steal tenant data](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/) — blog
- [GrapheneOS made a proof of concept RCS messaging app without Google Messages](https://twitter.com/GrapheneOS/status/2124158267123233056) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-23.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
