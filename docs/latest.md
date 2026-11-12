# Firehose — 2026-11-12

## [Microsoft's Lazarus backdoors AI agents by editing under 10 neurons](https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html)

`headline` · blog

Microsoft implanted a trigger-activated backdoor in Nemotron-Terminal-8B, Qwen3.6-27B, and Gemma-4-31B-IT by editing fewer than 10 rarely-firing neurons, no retraining needed, reaching 51-99.5% success across models. A weight-diff detector catches 91.4% of edited checkpoints, but asking Claude Opus 5.5 or GPT-6 Astra to just inspect weights failed almost completely. Diff every deployed checkpoint against its declared base model before trusting it. (3 minute read)

## [35,578 public Grok-built apps leak passwords, hospital data](https://thehackernews.com/2026/11/over-35000-grok-built-apps-exposed.html)

`headline` · blog

Claroc found 37,571 Grok-built apps, 35,578 of them open to anyone, with about 1 in 10 exposing real internal data across 30 organizations including six Fortune 500s and a timesheet app storing plaintext passwords. The cause was 'anyone with the link' sharing by default, guessable grok.me subdomains, and a Grok-generated membership check that approved users before verifying them. Audit what your team has published with AI app builders before someone else finds it. (4 minute read)

## [VulnCheck's audit of Anthropic's AI vuln-hunting falls short of the hype](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)

`discovery` · hn

Seven months into Project Glasswing, Anthropic is credited with 442 of the 93,450 CVEs published this year, but only 2 are known exploited, and just 217 of its 37,966 total findings are fixed. On curl, 19 of 34 published reports turned out not to be vulnerabilities at all. AI-assisted vuln-hunting is finding volume; maintainer triage capacity is now the bottleneck. (3 minute read)

## [AntiFox AI pentesting tool linked to real AWS secret theft](https://thehackernews.com/2026/11/antifox-ai-pentesting-platform-linked.html)

`discovery` · blog

Arctic Wolf ties intrusions that reached a production AWS secret via a successful GetSecretValue call to AntiFox, an autonomous multi-agent pentesting platform built on the ARTEX framework. In related intrusions, attackers deployed an ASPX web shell through an IIS worker process to harvest config files and credentials. Attribution lands on Alibaba Cloud infrastructure hosting AntiFox's interfaces, not yet a confirmed actor. (3 minute read)

## [Huawei's MACaQ quantizer beats Unsloth on KL divergence](https://github.com/huawei-csl/MACaQ)

`discovery` · hn

MACaQ, Huawei's Apache-2.0 quantization toolkit, quantizes a 122B model in 64 minutes on 32.5GB of memory and ships GGUF/vLLM/Diffusers checkpoints across text, image, and audio models. Its Qwen3.6-35B-A3B Q4\_K\_XL checkpoint hits a lower KL divergence to FP16 (0.0134) than Unsloth's UD-Q4\_K\_XL at the same size (0.0157), and on vLLM delivers 2.33x faster prefill and 2.58x faster decode. (4 minute read)

## [Apple's learned MIPS routing cuts RAG retrieval time up to 8x](https://machinelearning.apple.com/research/faster-retrieval)

`discovery` · hn

Apple's ICML 2026 paper trains small networks offline to route retrieval queries, replacing fixed centroid-based indexing. SupportNet reaches 95% recall 1.9x faster than standard routing, and KeyNet hits 99% recall with up to 8x less search time and 11x fewer keys scanned, tested on the 2.6M-passage Natural Questions set. No code has been released yet. (3 minute read)

## [BotPsy's 0.8B model beats a 2B rival on most tool-use benchmarks](https://huggingface.co/blog/qvac/botpsy)

`discovery` · blog

Tether AI Research's BotPsy, an 0.8B open-weight model built on Qwen3.5, scores 44.0 on BFCL v4 and 64.6 on ToolSandbox versus 37.7 and 41.2 for the larger Qwen3.5-2B-Think. It uses about a third as many reasoning tokens as its base model on GPQA Diamond and roughly halves its base's unsafe-response rate in red-teaming, to 21%. Weights are Apache 2.0, in bf16/Q8/Q4. (4 minute read)

## [Reasoning models optimize success probability, not correctness](https://alexwang.ai/posts/reasoning-as-pathfinding/)

`discovery` · hn

This essay recasts chain-of-thought reasoning as pathfinding: models optimize the probability that some sampled path reaches a correct answer, not the correctness of any single path. That lens shows RL training with binary rewards is equivalent to rejection-sampling fine-tuning on a model's own past successes, and explains why chains-of-thought grow longer under training rather than being inherently better. It also locates reward hacking in the gap between an imperfect verifier and a sampler that finds shortcuts. (5 minute read)

## Also in the pool

- [Claude Whiteboards, Claude Sheets, and Claude Data](https://claude.com/resources/articles/sheets-whiteboards-data) — hn
- [We Built An Agent That Broke All of Our Security Rules. Here's What We Learned.](https://thehackernews.com/2026/11/we-built-agent-that-broke-all-of-our.html) — blog
- [Simreal-AI/Simreal-MLBench](https://github.com/Simreal-AI/Simreal-MLBench) — github
- [AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/) — blog
- [Google SWE points 48 AI agents at NASA Lidar, finds unmapped Maya pyramid in 72h](https://pietromiotti.com/latest/maya-site/?maya) — hn
- [United Airlines bans AI agents from booking flights on behalf of travelers](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/) — hn
- [crow-hq/llm-wiki-v2](https://github.com/crow-hq/llm-wiki-v2) — github
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — github
- [Gemini Robotics 2.5 accelerates real-world general dexterity](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/) — blog
- [Railway breach leads to $740,000 in fraudulent AI charges](https://www.bleepingcomputer.com/news/apple/railway-breach-leads-to-740-000-in-fraudulent-ai-charges/) — blog
- [AIs Hacking the Law](https://www.schneier.com/blog/archives/2026/11/ais-hacking-the-law.html) — blog
- [How Cisco defends at machine speed with OpenAI](https://openai.com/index/cisco-cyber) — blog
- [aws-emulator](https://simonwillison.net/2026/Nov/11/aws-emulator/) — blog
- [Rewarding defenders with bigger bug bounties](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties) — blog
- [Agentic cheminformatics with Google Antigravity](https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/) — blog
- [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) — blog
- [Cogent and OpenAI build cyber defense factories for enterprises](https://openai.com/index/cogent-security) — blog
- [Three People Arrested for AI-Enhanced Impersonation Fraud](https://www.schneier.com/blog/archives/2026/11/three-people-arrested-for-ai-enhanced-impersonation-fraud.html) — blog
- [Token Pooling-Aware Training for Multi-Vector Embedding Models](https://huggingface.co/blog/token-pooling) — blog
- [Using voltage glitching to unleash the A100 in my mining card](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-12.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
