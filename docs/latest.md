# Firehose — 2026-10-24

## [Meta ships Muse Spark Open, an 816B open-weight multimodal MoE](https://huggingface.co/blog/meta-muse-spark-open)

`headline` · blog

Muse Spark Open is an 816B-parameter MoE (42B active) that takes text, image, audio, and video input with a 1M-token context, tuned for agentic coding tasks like multi-file refactors. It ships in BF16 and 4-bit NVFP4 for Blackwell, with day-one support in transformers, llama.cpp, vLLM, SGLang, and MLX. (3 minute read)

## [Ransomware affiliates ran AI red-team agents to hit 62 orgs](https://thehackernews.com/2026/10/exposed-infrastructure-reveals-how.html)

`headline` · blog

An exposed command server shows an INC/Gentlemen ransomware affiliate running intrusions through OpenCode and OpenRouter models, with a human approving each AI-proposed step. Logs span 8,257 messages across 133 sessions, targeting about 62 organizations via known CVEs in SimpleHelp, FortiClient EMS, and cPanel. When a model refuses, operators reframe the request as an authorized red-team test. (4 minute read)

## [Two CVSS 9.0 Linux KSMBD RCE flaws disclosed before patches](https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html)

`headline` · blog

Two unauthenticated bugs in Linux's in-kernel SMB server, KSMBD, score CVSS 9.0: an RDMA buffer-descriptor underflow and an SMB1/SMB2 handler-dispatch race reachable on any KSMBD server's port 445. Both were posted to public mailing lists with no CVE and no mainline fix yet, drawing criticism of the disclosure process. (3 minute read)

## [Fable 5.1 hides messages in images and reads them back](https://www.lesswrong.com/posts/WHEQps5PK8LrrcTAb/how-does-fable-5-1-hide-messages-in-images)

`discovery` · hn

Given 50 messages in 15 languages, Fable 5.1 encoded each into an SVG scene and a separate session decoded 78% from the rendered PNG alone, mostly by mapping letters to object heights. Cross-model runs with GPT-6 Astra, which never used height-coding, hit 84-88% decode rates in both directions. (3 minute read)

## [x402 SDK flaw could drain an AI agent's crypto wallet](https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html)

`discovery` · blog

Researchers found 25 flaws in x402, the agent-payment SDK, including three critical ones: no spending cap in the default client, Solana token approvals accepted as transfers, and login signatures checked against the wrong site. Every @x402/svm release from 2.0.0 to 2.22.0 lacked the check; fixed versions now cap payments at $1 by default. (4 minute read)

## [ThinkingCap cuts Gemma-4-26B's reasoning tokens by 39%](https://bottlecapai.com/post/thinkingcap-gemma-4-26b/)

`discovery` · hn

BottleCap's ThinkingCap tune of Gemma-4-26B-A4B drops thinking tokens by an average of 38.9% across 12 benchmarks, up to 69.1% on LongBench v2, while accuracy moves just -0.15 points on average. It's a drop-in swap on the same vLLM stack, with weights and GGUF builds already on Hugging Face. (3 minute read)

## [An AI wrote a 214-page, fact-cited wiki from 45k Enron emails](https://www.thisandthat.chat/enron/)

`discovery` · hn

A four-stage pipeline read 45,047 Enron emails and produced 214 pages of 49,401 dated facts, each tied to a quoted sentence from its source email with no human editing. A held-out audit by a second AI found 93% of sampled facts fully supported and zero wrong at their core out of 500 checked. (3 minute read)

## [Microsoft Teams gets AI phishing detection with no admin setup](https://www.bleepingcomputer.com/news/microsoft/microsoft-teams-to-get-ai-powered-context-aware-phishing-detection/)

`discovery` · blog

Teams will analyze conversation context to flag phishing, impersonation, and social engineering in external first-contact chats, even without a malicious link or file. No admin action is needed to turn it on; targeted rollout starts early November, with worldwide availability by mid-December. (2 minute read)

## Also in the pool

- [Capcom confirms data breach affecting 11.7 million accounts](https://www.bleepingcomputer.com/news/security/capcom-confirms-data-breach-affecting-117-million-accounts/) — blog
- [INTERPOL Arrests 1,462 Suspects, Disrupts 10,909 Cybercrime Networks in Global Crackdown](https://thehackernews.com/2026/10/interpol-arrests-1462-suspects-disrupts.html) — blog
- [Swedish government offices to ban ChatGPT and Claude](https://www.sverigesradio.se/artikel/chat-gpt-och-claude-forbjuder-regeringskansliet) — hn
- [Critical Flaw in Python’s Popular Pillow Image Library Allows Code Execution via a Crafted Image](https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html) — blog
- [Securing our frontier model training environment](https://openai.com/index/securing-our-frontier-model-training-environment/) — hn
- [Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) — hn
- [Researchers Demonstrate Node2Shell RCE Exploit on Node.js Build Using Crafted Brotli Data](https://thehackernews.com/2026/10/researchers-demonstrate-node2shell-rce.html) — blog
- [Introducing Kimi K3.1 Pro](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) — blog
- [Arista patches new VeloCloud Orchestrator zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/) — blog
- [The same AI request emits 8.5 times more CO2 in Texas than in Sweden](https://berget.ai/en/blog/per-request-co2-press-release) — hn
- [Russia-Linked Hackers Used New Mesh Network Backdoor in Destructive Ukraine Attack](https://thehackernews.com/2026/10/russian-linked-hackers-used-new-mesh.html) — blog
- [Today, we hacked what we'd set out to hack: the iPhone](https://blog.calif.io/p/iphone) — hn
- [Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)](https://openai.com/index/scaling-storage-one-billion-users-part-two) — blog
- [Kimi K3.1 scores 55 on Artificial Analysis, placed on the Pareto line](https://artificialanalysis.ai/models/kimi-k3-1-pro) — hn
- [AI analysis of CT scans finds 42.9% of patients have coronary inflammation](https://www.biograph.com/newsroom/biograph-completes-first-u.s.-study-with-caristo-diagnostics%E2%80%99-ai-powered-coronary-inflammation-detection-finding-risk-in-over-42-of-asymptomatic-patients) — hn
- [Arista Warns of Critical VeloCloud SQL Injection Zero-Day Exploited in Attacks](https://thehackernews.com/2026/10/arista-warns-of-critical-velocloud-sql.html) — blog
- [Does Your Model Run on AWS Trainium? Look It Up](https://huggingface.co/blog/torch-neuronx-model-support) — blog
- [Hackers Breach Enterprise Firewalls and VPNs, Exposing Over 70,000 Credentials](https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html) — blog
- [BlackX UEFI Bootkit Bypasses Secure Boot on Patched Windows Systems Missing Revocations](https://thehackernews.com/2026/10/blackx-uefi-bootkit-bypasses-secure.html) — blog
- [You gave your AI agent access, but who is giving it orders?](https://www.bleepingcomputer.com/news/security/you-gave-your-ai-agent-access-but-who-is-giving-it-orders/) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-24.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
