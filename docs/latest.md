# Firehose — 2026-11-01

## [Claude wrote a working root exploit for a CVSS 9.8 Linux bug](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf)

`headline` · hn

A use-after-free in Linux's IPv4 TCP handshake code (CVSS 9.8, CVE-2026-98432) lets an unauthenticated attacker gain remote root on MPTCP listeners. Anthropic's Claude produced a working exploit after prompting, reaching a kernel-pointer leak in about 48 minutes and code execution five minutes later. Patches landed upstream October 11-18, but Ubuntu and RHEL remain unfixed. (4 minute read)

## [Infostealer malware uses an LLM to rank how much each victim is worth](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)

`discovery` · hn

VOLTA-AUTODOXER, documented by Cisco Talos, steals browser credentials, cards, and crypto wallets, then sends a victim dossier to an LLM via OpenRouter for a worth and OPSEC rating. It defaults to Claude Opus 4.6, falling back to Kimi K2 and Gemini 2.5 Flash if a model refuses. The model replaces an operator's manual triage step entirely. (4 minute read)

## [A single ChatGPT share link could hijack your account](https://www.parameter.ai/labs/we-found-a-gap-at-openai)

`headline` · hn

A chained bug let one shared ChatGPT link run attacker JavaScript as chatgpt.com, using a MathLive postMessage flaw to inject HTML that loaded code through a YouTube-allowed CSP exception. The exploit could list a victim's chats and exfiltrate one never shared with the attacker. OpenAI fixed it within a week of disclosure and paid a $5,000 bounty. (4 minute read)

## [China's ARTEX AI agents breached 200+ organizations worldwide](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html)

`headline` · blog

China-linked group Vapor Panda ran ARTEX, an AI pentesting framework with planner and worker LLM agents, against 200+ organizations since October 17, confirming post-exploitation at nine. One intrusion's planning agents alone consumed 1.4 billion input tokens. The agents chained an unsigned SAML assertion with an XXE flaw to forge admin tokens from keys unrotated since 2022. (4 minute read)

## [inferssd streams MoE experts from disk, up to 20x faster](https://github.com/wici-ai/inferssd)

`discovery` · github

inferssd runs MoE models too large for RAM or VRAM by streaming experts from SSD instead of offloading the KV cache, built on llama.cpp with GGUF files and an OpenAI-compatible API. On an RTX 5090, vendor-reported prefill throughput for DeepSeek-V4.1-Flash jumps from 8.06 to 164.5 tokens/sec, a 20.4x gain. The numbers are self-reported and not independently verified. (4 minute read)

## [Five small open models beat Fable 5 on LiveCodeBench Hard](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve)

`discovery` · hn

Memdoor's team-solve workflow splits a coding problem across five fresh-context Qwen3.8-27B roles - planner, two ideators, solver, and manager - that communicate only through files. Across the first ten LiveCodeBench Hard problems it averaged 9.8 of 10 over five passes, versus 8.0 for Fable 5 alone. Fifty runs solved 49 problems at a median cost of $0.39 each. (4 minute read)

## [bilibili releases open-weight Index-Translate family up to 35B](https://github.com/bilibili/Index-Translate)

`discovery` · github

bilibili released Index-Translate, a multilingual translation model family built on Qwen3.5 with published weights at 2B, 9B, and 35B-A3B, plus GGUF, FP8, and FP4 quantized builds under Apache-2.0. Companion models handle voice-cloned dubbing, syllable-budget translation, and long documents across 150 languages. The 35B-A3B model scores 0.8794 on FLORES COMET-22, trading wins with GPT-5.6-Sol on different metrics. (4 minute read)

## [TokenEconomizer cuts coding-agent costs up to 31% on SWE-Bench](https://github.com/microsoft/TokenEconomizer)

`discovery` · github

TokenEconomizer wraps coding agents like Claude Code and Codex with cached repo facts, unused-tool pruning, and a judge model that redirects failure loops, without touching the underlying model. Across 277 SWE-Bench tasks and five agent-model pairs, mean cost dropped 18.4-30.9% in every combination tested, with pass@1 improving in four of five. It also reports 16-21% lower cost on Web-Bench. (4 minute read)

## Also in the pool

- [Prospero: A new coding harness for a more civilized age](https://nullprogram.com/blog/2026/10/31/) — hn
- [Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)](https://openai.com/index/scaling-storage-one-billion-users-part-two) — blog
- [Securing our frontier model training environment](https://openai.com/index/securing-our-frontier-model-training-environment) — blog
- [AI startup hacks Anthropic, gains access to employee details, internal messages](https://www.indiatoday.in/technology/news/story/ai-startup-hacks-anthropic-in-12-hours-gains-access-to-employee-details-and-internal-messages-3025452-2026-10-26) — hn
- [GPT-5.6 Sol can beat Factorio on peaceful mode](https://ryanmadden.net/gpt-56-beats-factorio/) — hn
- [Making it easier for websites to express AI training preferences](https://openai.com/index/helping-websites-express-ai-training-preferences) — blog
- [It's the memory latency, stupid](https://pivotlake.io/blog/its-the-memory-latency-stupid/) — hn
- [Anthropic's Claude AI blocks video game cloning and reverse-engineering](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked) — hn
- [Proton's CEO Cancels AI 'Re-Interviews'](https://www.404media.co/protons-ceo-cancels-ai-re-interviews/) — hn
- [Cisco gives engineer unlimited AI tokens to rewrite legacy code](https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/) — hn
- [Flock camera searches fell 95% after a dispatcher's misconduct was caught](https://www.wkyc.com/article/news/investigations/flock-camera-searches-fall-95-percent-highland-heights-dispatcher-misconduct-caught/95-94b18f33-60e2-4bc7-a00f-d71d1e1fdd5e) — hn
- [Sam Altman Thinks You're Wasting DRAM](https://frvr.com/blog/news/openai-ceo-sam-altman-says-its-terrible-to-have-everybody-have-a-bunch-of-the-worlds-limited-supply-of-dram-instead-of-shoving-it-all-in-datacentres/) — hn
- [DOJ raises privacy concerns over potential sale of Character.AI chats](https://therecord.media/doj-raises-privacy-concerns-over-character-ai-sale) — blog
- [Introducing Kimi K3.1 Pro](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) — blog
- [A Shared ChatGPT Link Could Run Attacker Code in Your Session and Read Private Chats](https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html) — blog
- [Ex-Meta Researcher Torrented Pirated Books, Deleted It 'Due to Litigation'](https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/) — hn
- [Reddit to lock content behind logins to fight scrapers](https://www.bleepingcomputer.com/news/security/reddit-to-lock-content-behind-logins-to-fight-scrapers/) — blog
- [A City Canceled Flock's Contract. Flock Ignored It. Police Chief Unplugged Them](https://www.thedrive.com/news/my-city-canceled-flocks-contract-flock-ignored-it-so-the-police-chief-unplugged-the-cameras) — hn
- [Northflank security breach leads to abuse of customers' AI API keys](https://www.bleepingcomputer.com/news/security/northflank-security-breach-leads-to-abuse-of-customers-ai-api-keys/) — blog
- [I post trained a model on Demoscenes](https://datavorous.com/writing/demoscener/) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-01.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
