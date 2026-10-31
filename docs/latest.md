# Firehose — 2026-10-31

## [Official Claude Code VS Code extension shipped with an SSH backdoor](https://phorion.io/blog/offical-claude-code-vsx-compromise/)

`headline` · hn

The Claude Code VS Code extension on the Cursor Marketplace (v2.1.312/313) shipped with a backdoor: it plants an attacker SSH key, opens a reverse tunnel to a remote server, and persists via a LaunchAgent, cron job, or scheduled task. It also beacons hostname, user, and KEY/TOKEN/SECRET env-var names over HTTP. Uninstalling doesn't remove it — rotate any exposed credentials. (4 minute read)

## [A tiny world model runs games entirely on a Raspberry Pi Pico 2 W](https://github.com/SheepSeb/tinyworldformer)

`discovery` · hn

A looped int8 transformer world model and an MLP actor run entirely on a Raspberry Pi Pico 2 W's 520KB of SRAM, learning on-device with no replay buffer. It plays Breakout, Pong, Flappy Bird, Pac-Man, and a Doom-lite clone at 83.6-100% exact frame accuracy, in firmware as small as 361KB. Training code, Rust firmware, and a WASM build are open-source — a game-playing world model that runs on a microcontroller instead of a GPU. (3 minute read)

## [Northflank breach exposed AI API keys, root cause unconfirmed](https://status.northflank.com)

`headline` · hn

A Wiz threat alert on October 30 triggered a major Northflank outage across networking, services, jobs, and builds, and multiple customers confirmed their AI API keys stored on the platform were used without authorization. Root cause is still unconfirmed, but Northflank force-rotated Postgres and MongoDB credentials and turned on audit logs for every customer, including free tier. Rotate any secrets you stored there. (2 minute read)

## [nesformer: an NES emulator compiled into Qwen3.5's weights](https://github.com/dbreunig/nesformer)

`discovery` · hn

nesformer compiles an NES's 6502 CPU, 2KB of RAM, and a cartridge ROM into Qwen3.5-4B's weights, then has the model predict the CPU's execution trace token by token while a host program handles video and input. The compressed weights (9.3M of 466.6M params nonzero, 3.3MB) verify exactly against nestest's golden CPU log and run Super Mario Bros about 150-290x slower than a real console. Code and test ROMs are on GitHub. (3 minute read)

## [AI incident response is quietly deskilling SREs](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling)

`headline` · hn

AI handling routine incidents is quietly deskilling SREs, argues a SigNoz newsletter piece citing Bainbridge's 1983 'Ironies of Automation' and a Lancet study where endoscopists' unassisted polyp-detection rate fell from 28% to 22% after a period of AI assistance. Aviation research on autopilot reliance shows the same pattern, which is why the FAA mandates manual flying time. The fix: deliberately route some incidents to humans-only instead of defaulting to AI-assisted response. (5 minute read)

## [Check if your model runs on AWS Trainium before you provision it](https://huggingface.co/blog/torch-neuronx-model-support)

`discovery` · blog

A Hugging Face Space now tests whether top Transformers models run unmodified on AWS Trainium (trn2), sharding each one with tensor or expert parallelism across up to 16 cores and checking generated tokens against CPU output or an LLM-judge fluency check. Results publish as per-version Parquet files you can query with pandas, and a bundled run.py script reproduces the compiled graphs using a public NEFF cache. Check compatibility before provisioning Trainium instances. (3 minute read)

## [ThinkingBox turns DB-state checks into RL rewards, lifts pass@1 9 points](https://huggingface.co/blog/microsoft/thinkingbox-training)

`discovery` · blog

Microsoft's ThinkingBox turns deterministic database-state checks into binary RL rewards for agent post-training: GRPO fine-tuning Qwen3.8-27B on a fixed 187-task pool lifted pass@1 from 51.70% to 60.78% on a 507-task held-out benchmark, while pass@20 slipped slightly (89.35% to 87.97%) — the gain is repeatability, not breadth. Estimated cost per dependable task dropped from $24.36 to $8.00. The training stack, framework, and benchmark data are all open-sourced. (4 minute read)

## [Five chained Azure bugs let any tenant hijack another's backend](https://www.binarysecurity.no/posts/2026/10/one-root-case)

`discovery` · hn

Five chained elevation-of-privilege bugs in Azure Logic Apps' API Connections let any tenant hijack another tenant's connected Key Vault, Azure SQL, Jira, or Salesforce backend, because the API Management layer swaps a caller's token for the backend's and can be tricked into targeting a victim's connection. Each fix broke on a new validation-order gap until Microsoft closed all five, paying a combined $200,000 in bounties. (6 minute read)

## Also in the pool

- [We ran AI agent swarms in Minecraft and Mindustry](https://labs.ycombinator.com/projects/games/index.html) — hn
- [Show HN: I Turned DOOM into a Transformer](https://github.com/mottopanikeiku/doomformer) — hn
- [IgE disruptor for food allergy with Claude-enabled antibody design \[pdf\]](https://divergencelabs.com/publications/ige-preprint.pdf) — hn
- [Hugging Face malware campaign returns to hijack GPUs for crypto mining](https://www.bleepingcomputer.com/news/security/hugging-face-malware-campaign-returns-to-hijack-gpus-for-crypto-mining/) — blog
- [Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)](https://openai.com/index/scaling-storage-one-billion-users-part-two) — blog
- [Cisco gives engineer unlimited AI tokens to rewrite 98% of the company's code](https://www.tomshardware.com/tech-industry/big-tech/cisco-gives-27-year-old-engineer-unlimited-ai-tokens-to-rewrite-98-percent-of-the-companys-legacy-code-in-24-months-president-plucks-former-startup-founder-telling-him-to-go-nuts) — hn
- [Donating Agent Skills to the Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) — blog
- [Anthropic Cracking Down on Video Game Rewrites](https://twitter.com/chasmmmmmmmmmmm/status/2116062991686721968) — hn
- [Fiber lasts decades, GPUs last three years: the AI boom isn't the dot-com boom \[video\]](https://www.youtube.com/watch?v=MENoB3Rex28) — hn
- [DOJ raises privacy concerns over potential sale of Character.AI chats](https://therecord.media/doj-raises-privacy-concerns-over-character-ai-sale) — blog
- [US Reps Lead Democratic Resolution Opposing A.I. Bubble Bailout for Big Tech](https://progressives.house.gov/2026/10/reps-casar-waters-lead-democratic-resolution-opposing-a-i-bubble-bailout-for-big-tech-commit-to-protecting-american-people-instead) — hn
- [Alleged Chinese spy had 'close relationship' with Nvidia boss Jensen Huang](https://nypost.com/2026/10/29/business/alleged-chinese-spy-had-close-relationship-with-nvidia-boss-jensen-huang-report/) — hn
- [An updated Model Spec for more capable and beneficial AI](https://openai.com/index/updated-model-spec) — blog
- [How Ropes & Gray is developing AI for transactional diligence](https://openai.com/index/ropes-gray-ai-diligence) — blog
- [What FDE means at OpenAI](https://openai.com/index/forward-deployed-engineering-means) — blog
- [Fake crypto app on Apple App Store linked to $23K wallet theft](https://www.bleepingcomputer.com/news/security/fake-crypto-app-on-apple-app-store-linked-to-23k-wallet-theft/) — blog
- [Hackers exploit Cisco SD-WAN flaw to deploy custom KeyDrift malware](https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/) — blog
- [New Serious PHP Vulnerabilities Released and Patched](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html) — blog
- [ThreatsDay: Critical Firewall Flaws, Banking Trojans Rented, Weaponized PDF, Token Theft + 26 More Stories](https://thehackernews.com/2026/10/threatsday-critical-firewall-flaws.html) — blog
- [Limited reports of PHP bug exploitation emerge](https://therecord.media/php2shell-successful-exploitation-reports-emerge) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-31.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
