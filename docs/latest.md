# Firehose — 2026-11-05

## [$6.3B stolen from Binance via AI-assisted lateral movement](https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398)

`headline` · hn

North Korean hackers stole $6.3B from Binance, the largest crypto theft on record, via a fake job-interview campaign that delivered malware disguised as a coding assignment. From one compromised machine, they used Binance's own internal AI tool to pivot to two more engineers before deploying the theft script with a stolen container-deployment token. The FBI attributes the operation to TraderTraitor/Lazarus Group. (4 minute read)

## [AI turned a dismissed 2024 PHP crash bug into full RCE](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability)

`headline` · hn

A PHP bug reported in 2024 and dismissed as a mere crash risk was turned into full remote code execution in two weeks with AI assistance, hitting NASA, Wikipedia, the White House, WordPress and Drupal sites. The fix took four engineers two months to build. Treat any 'harmless' decades-old crash bug as a live RCE candidate once AI-assisted exploit development enters the picture. (3 minute read)

## [BigSleep found 45 exploitable V8 bugs to Fuzzilli's 37](https://projectzero.google/2026/10/fuzzing-v-AI.html)

`discovery` · blog

Google Project Zero ran Fuzzilli, a classic generative fuzzer, against BigSleep, an LLM-based one, on V8 production code from April to September. BigSleep found 45 actionable vulnerabilities to Fuzzilli's 37, but the two overlapped on only 20 of 81 combined bugs. BigSleep's daily cadence also lags Fuzzilli's continuous runs by one to two days, so neither replaces the other. (4 minute read)

## [Capabilities can be cryptographically hidden in model weights](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html)

`discovery` · blog

A new paper builds encrypted neural networks inside host model weights that decrypt only on a secret trigger, using cryptographic 'digital lockers'. The hidden capability survived fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training in PyTorch proof-of-concept tests. That breaks the core assumption behind pre-deployment capability audits: that a hidden capability can always be elicited given full weight access. (3 minute read)

## [Anthropic's FlashProve proves you ran the model you paid for](https://www.anthropic.com/research/provable-inference)

`discovery` · hn

Anthropic open-sourced FlashProve, a zkSNARK-based prover that lets a low-compute client verify a response came from specific committed model weights without learning them. On a 400B-parameter Llama 4 Maverick, it proves at about 110 tokens/second on one H100, versus a prior open-source baseline's 14.3 hours for 1,000 tokens. It only covers integer weights under greedy decoding, with a 1,024-token window per proof. (4 minute read)

## [Nvidia's encrypted firmware cuts Linux inference by up to 79%](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop)

`discovery` · hn

On the MSI Prestige N16 Flip AI Plus, Nvidia's Windows-only power-management firmware encrypts the GPU's power table, capping Linux clocks to about 780MHz versus 2.2GHz on Windows when plugged in. GPT-OSS-120B throughput drops 79%, from 65.4 to 13.9 tokens/second; running on battery avoids most of the hit. No Linux-native fix exists yet, and one attempt to patch the power table caused a kernel panic. (3 minute read)

## [A 65B open model tops 501B and 816B rivals on agentic coding](https://www.ricursive.com/ripple)

`discovery` · hn

Ripple-65B Preview, a dense 65B-parameter open-weight model trained on 12 trillion tokens, scores 80.52 on TerminalBench 2.1, edging out the 501B-parameter Reflection Beam (80.1) and beating the 816B Meta Muse Spark Open (76.4). Ricursive says the $32M total build cost is about a tenth of the prior open-weight SOTA, reached with roughly 70x fewer RL rollouts than Reflection Beam. (3 minute read)

## [A fix for the MCP OAuth redirect flaw that already hit Square](https://streamvessel.com/blog/mcp-trusted-redirect-uris)

`discovery` · hn

A May 2026 study found 114 of 119 OAuth-enabled MCP servers accept any redirect\_uri from an anonymous client registration, a gap PKCE doesn't close since the attacker starts the flow; it already caused a Square account takeover. The fix keeps self-registration open but lets each signed-in user add up to 10 trusted HTTPS redirect URIs, with a confirmation page for anything else. (4 minute read)

## Also in the pool

- [Researchers Uncover Prompt Adware Hidden in OpenAI Codex Jailbreak Toolkit](https://thehackernews.com/2026/11/researchers-uncover-prompt-adware.html) — blog
- [jiwoochris/artex-global](https://github.com/jiwoochris/artex-global) — github
- [StateBench: Testing how language models track state changes over long documents](https://huggingface.co/blog/allenai/statebench) — blog
- [Google Will Turn Off Search for Schools That Reject A.I](https://www.nytimes.com/2026/11/03/us/google-search-schools-restrict-ai.html) — hn
- [AIs Hacking the Law](https://www.schneier.com/blog/archives/2026/11/ais-hacking-the-law.html) — blog
- [Kimi K3.1 Pro model weights are out](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) — hn
- [Xen Hypervisor Flaws Let One Malicious VM Read and Write Any Other VM's Memory](https://thehackernews.com/2026/11/xen-hypervisor-flaws-let-one-malicious.html) — blog
- [How Check Point accelerates vulnerability research with Daybreak](https://openai.com/index/check-point-daybreak) — blog
- [Debian apt security update (man-in-the-middle)](https://lists.debian.org/debian-security-announce/2026/msg00526.html?pow_referer=) — hn
- [Qualcomm Cloud AI 100 Ultra – 150W AI Accelerator Card with 128GB at 548GB/s](https://www.qualcomm.com/data-center/products/cloud-ai-100-ultra) — hn
- [Zyxel fixes zero-day exploited to hack nearly 1,000 network switches](https://www.bleepingcomputer.com/news/security/zyxel-fixes-zero-day-exploited-to-hack-nearly-1-000-network-switches/) — blog
- [APT29-Linked Hackers Hijack Web Analytics Script to Deliver iOS and Android Exploits](https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html) — blog
- [Radio With No Radar: Why Agent Runtime Security Fails Without the Layers Beneath It](https://thehackernews.com/2026/11/radio-with-no-radar-why-agent-runtime.html) — blog
- [Residential proxies detected on White House network](https://layer3intel.com/blog/residential-proxies-white-house-network) — hn
- [WorkOS says attacker used ARTEX AI to breach internal sales app](https://www.bleepingcomputer.com/news/security/workos-says-attacker-used-artex-ai-to-breach-internal-sales-app/) — blog
- [Simreal-AI/Simreal-MLBench](https://github.com/Simreal-AI/Simreal-MLBench) — github
- [Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)](https://news.ycombinator.com/item?id=50363461) — hn
- [bgts-ai-org/bgts-context-engine](https://github.com/bgts-ai-org/bgts-context-engine) — github
- [GitHub Octoverse 2026](https://simonwillison.net/2026/Oct/28/github-octoverse-2026/) — blog
- [Gitbook Breached](https://news.ycombinator.com/item?id=50354336) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-05.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
