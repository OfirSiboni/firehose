# Firehose — 2026-10-23

## [Mistral Large 4: a ~1 trillion-parameter open-weight model](https://mistral.ai/news/mistral-large-4/)

`headline` · hn

Mistral Large 4 is a ~1T-parameter MoE (52B active), trained on 3,800 GB200 GPUs in Mistral's own EU datacenters. It scores 82% on a reproduce-and-patch vulnerability test, 93% on Cybench, and ranked 2nd of 5 in a blind human coding eval behind Opus 5. Open weights ship by month's end at $1.36/$4.18 per million tokens, ready for self-hosted deployment. (3 minute read)

## [Claude formally proves 123 libraries secure at the assembly level](https://www.anthropic.com/research/formal-verification)

`discovery` · hn

Claude formally proved security properties for 123 open-source libraries across 239 fuzz-test entry points, producing about 180 million lines of Rocq proof at the RISC-V assembly level. It found and patched hundreds of bugs, including a rediscovered CVE in libexpat and a counter underflow needing a 20MB input. Opus 5.5 did the work with 40% fewer tokens than Opus 5. (4 minute read)

## [Claude Duet is Anthropic's always-on personal AI agent](https://claude.com/product/claude-duet)

`headline` · hn

Claude Duet runs in the cloud across 6,000+ connectors (Gmail, Slack, Drive, Stripe, Shopify), handling tasks like scheduling or dashboards between a morning briefing and your next check-in. It asks before sensitive actions like sending messages or paying. It's a research preview on Opus 5.5, open to US Pro/Max subscribers via waitlist, sharing your plan's usage limits. (3 minute read)

## [China-linked hackers ran AI pentest agents against ConnectWise](https://thehackernews.com/2026/10/china-linked-hackers-use-artex-ai.html)

`discovery` · blog

A China-linked actor used the ARTEX agentic pentest framework to spray passwords across 2,250+ tenants at up to 2,900 attempts per minute, hitting 327 accounts across 8 organizations in four days. Some attackers reached privileged ConnectWise cloud identities in under 3 hours. Zscaler found the deployment configured with DeepSeek, GLM and Grok, with prompts hunting for bulk personal data and payment-gateway keys. (4 minute read)

## [Malicious MCP servers could run code via OpenCode's sign-in](https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html)

`discovery` · blog

A malicious remote MCP server could inject PowerShell commands through OpenCode's OAuth sign-in flow on Windows and WSL, running code with the developer's own access. Pillar Security rated it CVSS 9.8, disclosed it privately in August, and found it silently patched in version 1.18.33 -- no CVE or advisory was ever issued. Upgrade or audit configured servers with \`opencode mcp list\`. (3 minute read)

## [Anthropic's revenue hit $16.8bn in Q3, up 50% ahead of IPO](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/)

`headline` · blog

Anthropic's quarterly revenue went from about $4.8bn in Q1 to $11.5bn in Q2 to $16.8bn in Q3 2026, up nearly 50% quarter over quarter, according to numbers shared with investors. Q3's adjusted operating margin hit 11% excluding stock compensation, with $1.70 of revenue for every $1 spent on compute. Distillation revenue, 5-7% of the total, was cut back materially in the quarter. (3 minute read)

## [NVIDIA open-sources OpenShell, a sandboxed runtime for AI agents](https://github.com/NVIDIA/OpenShell)

`discovery` · hn

OpenShell runs autonomous agents in kernel-sandboxed, isolated environments where every outbound connection passes a network-policy check and agents never see real credentials -- the runtime injects them only for approved endpoints. A formal-verification layer flags risky new access, like a new host getting credentials, and holds it for human review first. It's open source: about 18,000 stars, 1,852 commits. (4 minute read)

## [OlmoEarth v1.3 cuts training cost 82%, stays open-weight](https://huggingface.co/blog/allenai/olmoearth-v1-3)

`discovery` · blog

OlmoEarth v1.3 turns a year of Sentinel-1/2 and Landsat satellite time series into a 128-dimension embedding for every 10-meter pixel on Earth, beating Google's AlphaEarth Foundations on 20 of 27 evaluations. Training cost dropped to about $2,720 in rented H100 time, down 82% from v1's $15,060, while matching v1.2's fine-tuning accuracy. Weights, pretraining data and code are all open. (4 minute read)

## Also in the pool

- [Google staff resign in backlash over its AI contracts with military](https://www.bbc.com/news/articles/cmreyvepnv0po) — hn
- [The compiler was supposed to end programming too](https://hrih.si/articles/the-compiler-was-supposed-to-end-programming/) — hn
- [Launch HN: Alter (YC S25) – Access control for multi-user agents](https://alterauth.com/) — hn
- [OpenAI CLI](https://github.com/openai/openai-cli) — hn
- [WorldTUI: I trained a 360M model to pretend to be a terminal](https://simedw.com/2026/10/21/world-model-terminal/) — hn
- [LayerFS: The filesystem for AI coding agents](https://layerfs.ai/) — hn
- [How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization) — blog
- [After automation: Solo founding will be the default](https://every.to/thesis-statements/julian-weisser) — hn
- [Anthropic's Public Benefit Charter](https://www.anthropic.com/public-benefit-charter) — hn
- [Texas data center boom could erase decades of progress on air quality](https://www.texastribune.org/2026/10/20/data-centers-texas-air-quality-report-pollution-health-risks/) — hn
- [How Third Moment Research runs 10,000 agents for 36+ hours](https://openai.com/index/third-moment-research) — blog
- [Show HN: Omnara – Open-source alternative to Claude Managed Agents](https://github.com/omnara-ai/omnara) — hn
- [Achieving AI-style reasoning without an LLM](https://fleetingswallow.com/minotaur-ai-deep-dive-achieving-reasoning-without-a-language-model/) — hn
- [Machine speed attacks require machine speed detection and response](https://www.bleepingcomputer.com/news/security/machine-speed-attacks-require-machine-speed-detection-and-response/) — blog
- [The Last Museum: Semantic search across 5.8M artworks from major museums](https://lastmuseum.com/) — hn
- [Most Americans Say AI Is Bad for Society, Oppose More Data Centers](https://abcnews.com/Politics/americans-ai-bad-society-oppose-data-centers-abcpostipsos/story?id=137414085) — hn
- [AI and the Enclosure of the Scientific Commons](https://arxiv.org/abs/2610.27251) — hn
- [AI analysis of CT scans finds 42.9% of patients have coronary inflammation](https://www.biograph.com/newsroom/biograph-completes-first-u.s.-study-with-caristo-diagnostics%E2%80%99-ai-powered-coronary-inflammation-detection-finding-risk-in-over-42-of-asymptomatic-patients) — hn
- [Patch the Planet: global response coordination as agents uncover critical vulnerabilities](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) — hn
- [NVIDIA Kumo Relational Outperforms Supervised Machine Learning on Relational Data, No Training Required](https://huggingface.co/blog/nvidia/kumo-relational) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-23.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
