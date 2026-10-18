# Firehose — 2026-10-18

## [OpenCode breach exposes stored OpenAI, Anthropic, Google API keys](https://twitter.com/opencode/status/2111516673953935833)

`headline` · hn

A breach of OpenCode's console hit 1.4% of users, exposing OpenAI, Anthropic, and Google keys saved in workspaces; CLI-only setups with local keys were untouched. One user reported roughly $400 in unauthorized Anthropic charges before catching it. Rotate any provider key you've stored in OpenCode's console today. (2 minute read)

## [Claude redesigns quantum circuits, beats published records](https://www.anthropic.com/research/designing-efficient-quantum-circuits)

`headline` · hn

Anthropic had Claude Mythos 5 redesign 8 quantum circuits against an automated evaluator, with no human input between rounds. On elliptic-curve point addition it cut gate count 17x for 12% more qubits, and on a Reed-Solomon decoder it shrank worst-case storage from 665 qubits to a 19-qubit reserve. Both results beat the previously published best designs. (3 minute read)

## [DeepSeek ships V4.1-Flash-1017, an MIT-licensed 763B open model](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

`headline` · hn

DeepSeek's V4.1-Flash-1017 update raises Terminal-Bench 4.0 from 31.2 to 42.3 and Humanity's Last Exam from 36.8 to 42.6 versus the prior Flash, under a 763B-parameter, MIT-licensed, 1M-context release. It trails Opus 5 on most benchmarks but leads on DeepSWE v1.1 at 77.0. Weights and a Rust inference library, deepseek-recipe, are already on Hugging Face. (2 minute read)

## [Your agent harness controls prompt-cache hit rate, not just the model](https://neuralwatt.com/news/why-harnesses-matter-for-energy-efficiency)

`discovery` · hn

Neuralwatt's production data puts uncached-input share at 1.6% for deepseek-harness versus 11.1% for Node.js clients. Those misses cost 91% more energy per request on DeepSeek V4.1 Flash and 140% more on GLM-5.3. Past 128k tokens, a single cache-breaking turn can cost as much prefill as 600 normal ones. (3 minute read)

## [Four Mac Studios run an 816B model at 37 tokens/sec](https://machinelearning.apple.com/research/mlx-distributed-inference)

`discovery` · hn

Apple's new jaccl backend uses RDMA over Thunderbolt 5 to tensor-parallelize MLX across Mac Studios, hitting 36.73 tok/s for the 816B-parameter Muse Spark Open MoE on four M5 Ultras. A single M5 Ultra also gets up to 4.6x faster time-to-first-token than an M3 Ultra. Full commands via mlx.launch and mlx\_lm.server are public for anyone with the hardware. (2 minute read)

## [Llama.cpp now runs natively on a jailbroken PS5's GPU](https://github.com/cobanov/PS5LM)

`discovery` · hn

PS5LM runs GGUF models through llama.cpp's Vulkan backend on a jailbroken PS5, serving OpenAI- and Anthropic-compatible chat endpoints to any device on the network. A Qwen 3.8 27B model hits about 20 tok/s at 64k context using roughly 11.4GB of shared memory. The GPL-3.0 project already has ~513 GitHub stars and a public app release. (2 minute read)

## [Sophos cuts MDR investigation time 96% with OpenAI's Daybreak](https://openai.com/index/sophos)

`discovery` · blog

Sophos says AI agents built on OpenAI's Daybreak now resolve 52% of managed-detection-and-response cases end to end, with an average 89-second agent response time. OpenAI reports this cuts threat-investigation time by 96% versus the prior process. The figures are vendor-reported and not independently verified. (2 minute read)

## [Leaked docs show Amazon's AI system scoring union risk by warehouse](https://www.opendemocracy.net/amazon-ai-surveillance-monitor-union-activity-uk-warehouses-birmingham-coventry-atlas-sutton-coldfield/)

`discovery` · hn

Internal documents describe Amazon's 'Atlas' system scoring warehouses on unionization risk from hundreds of signals, including scraping worker Reddit threads for frequently used phrases. Two UK sites, Coventry and Minworth, were rated 'Tier 1' risk amid active GMB organizing. The documents surfaced through a Canadian labor board case over Amazon's YVR2 warehouse. (2 minute read)

## Also in the pool

- [FLUX 3 Image Klein](https://bfl.ai/blog/flux-3-image-klein) — hn
- [Anthropic assigned highest junk credit rating in June](https://www.ft.com/content/5a310aee-f555-4266-874c-b1b4db20186d) — hn
- [Big Fish: Exploiting a 37-Year-Old Kernel Bug in OpenBSD](https://calif.io/research/big-fish) — hn
- [Show HN: Llmspeed – feel how fast a local LLM runs before you buy the hardware](https://llmspeed.dev/) — hn
- [You could have invented transformers from memory](https://alexwang.ai/posts/associative-memory/) — hn
- [Hackers Use Compromised ConnectWise Credential to Sign In to 173 Microsoft 365 Tenants](https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html) — blog
- [OpenAI discloses four more rogue incidents](https://fortune.com/2026/10/16/openai-discloses-four-more-rogue-incidents-involving-financial-medical-and-government-data/) — hn
- [Postgres 19 delayed after AI reviewers find more bugs than humans can fix](https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471) — hn
- [Show HN: rStation – A shared research lab for your AI agents](https://rstation.ai/) — hn
- [Show HN: Fakeipedia – Wikipedia for worlds that don't exist](https://fakeipedia.org) — hn
- [How to make System 1 LLMs show System 2 competencies?](https://onlinelibrary.wiley.com/doi/epdf/10.1002/aaai.70113) — hn
- [ttok 1.0](https://simonwillison.net/2026/Oct/9/ttok/) — blog
- [Pattern matching beats narrative reasoning](https://blog.scottstevenson.net/p/pattern-matching-beats-narrative) — hn
- [Attackers Tampered with AOMEI Backupper's Update Servers for Minutes to Deliver a Backdoor](https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html) — blog
- [Stack Overflow for Agents triples signups with ChatGPT plugin](https://openai.com/index/stack-overflow-chatgpt-plugin) — blog
- [MapQuest will now show you where Flock cameras are in your neighborhood](https://www.engadget.com/2288729/mapquest-will-now-show-you-where-flock-cameras-are-in-your-neighborhood/) — hn
- [UAT-11985 Uses Fake Event Invites to Target Taiwan Research Affiliates With Google AitM Phishing](https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html) — blog
- [Quoting Addy Osmani, Morgan Westlee Lunt, and Qing Wang](https://simonwillison.net/2026/Oct/16/code-review/) — blog
- [Critical BlockStrap flaw lets hackers run code on Magento servers](https://www.bleepingcomputer.com/news/security/critical-blockstrap-flaw-lets-hackers-run-code-on-magento-servers/) — blog
- [Drupal patches critical RCE flaws, warns exploits may emerge soon](https://www.bleepingcomputer.com/news/security/drupal-patches-critical-rce-flaws-warns-exploits-may-emerge-soon/) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-18.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
