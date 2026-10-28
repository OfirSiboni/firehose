# Firehose — 2026-10-28

## [BigSleep AI agent matches Fuzzilli on V8 bugs, overlaps only 25%](https://projectzero.google/2026/10/fuzzing-v-AI.html)

`discovery` · blog

BigSleep, Google's AI fuzzing agent, found 45 actionable V8 vulnerabilities in six months of production use versus Fuzzilli's 37, with only 25% overlap between the two sets. On 112 historic Fuzzilli bugs, BigSleep rediscovered 62% from the introducing commit alone, rising to 70% with follow-up prompts, with no memorization effect on pre-cutoff bugs. Project Zero now runs both tools, since each catches vulnerabilities the other misses. (3 minute read)

## [A cryptographic backdoor can hide a capability inside model weights](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html)

`headline` · blog

A new paper embeds an encrypted neural network inside a host model's weights, unlockable only by a secret trigger, using a cryptographic locker construction. The hidden chemical-reaction-prediction capability, a CBRN stand-in, survived fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training in a PyTorch proof of concept. Elicitation-based capability audits can't catch a capability built this way, so safety evaluations need a different approach than probing for refusals. (4 minute read)

## [OpenAI's compaction feature let researchers extract hidden reasoning](https://thehackernews.com/2026/10/openai-compaction-flaw-let-researchers.html)

`discovery` · blog

Researchers at Xint got OpenAI's compaction feature to echo a model's encrypted chain-of-thought back as plaintext, swapping spaces for tabs to dodge the policy filter, then replaying the compacted item through gpt-4.1 and gpt-4o. The bypass worked because compaction runs on the same model that generated the reasoning, so OpenAI's cross-model reuse check never fired. OpenAI fixed it server-side on October 23 and paid a $6,000 bounty; the test covered only gpt-5.6-sol. (4 minute read)

## [RAG's failure mode has shifted from finding chunks to selecting them](https://www.kapa.ai/blog/retrieval-bottleneck)

`discovery` · hn

Kapa.ai's own eval shows retrieval failures have flipped: 18 months ago 80% of misses were search never finding the right chunk, now roughly half are selection dropping chunks search already found, including 34% of gold chunks. A grep baseline matched their deep retriever's recall but needed 25x more tokens to do it, since only 1 in 25 of its returned chunks mattered. Moving from top-5 to top-10 retrieved chunks raised coverage 14% but cost precision, so selection, not recall, is now the lever worth pulling. (4 minute read)

## [Seoul police: AI pentesting tool breached 90+ South Korean orgs](https://www.bleepingcomputer.com/news/security/former-pentester-used-artex-ai-to-steal-82-million-data-records/)

`discovery` · blog

Seoul police say a gang used ARTEX AI, an autonomous pentesting framework, to breach more than 90 organizations and steal roughly 8.2 million records, switching from conventional tools to AI tooling in late August. The group ran 38 extortion attempts demanding 360 million won (about $270,000) each not to leak stolen data. Police arrested the alleged leader, a 32-year-old former pentester, on October 15; six more suspects remain under investigation. (4 minute read)

## [OpenAI says its models helped crack three open math and physics problems](https://openai.com/index/building-scientific-understanding-with-academic-communities/)

`headline` · hn

OpenAI says it worked with academic researchers to produce model-assisted results on the Kakeya conjecture, the Exponential Time Hypothesis, and quantum chromodynamics. (2 minute read)

## [PHP2Shell exploitation is slowing as patching catches up](https://www.wiz.io/blog/php2shell-exploitation-so-far)

`headline` · hn

Wiz's telemetry on the PHP2Shell flaws (CVE-2026-109618 and CVE-2026-109619) shows daily exposed-vulnerable-machine counts down about 67% since disclosure, with PHP 7.3-and-earlier's share of exposed machines falling from 8.3% to 5.7% in five days. CISA added the pair to its Known Exploited Vulnerabilities catalog after Adel Karimi's honeypot produced the strongest public evidence of active exploitation. PHP runs on 65% of organizations in Wiz's dataset, but a week after disclosure fewer than 53% of initially affected organizations remained vulnerable. (4 minute read)

## [A llama.cpp fork strips refusals at inference time, no fine-tuning](https://github.com/heterodoxin/AbliteratedOutTheBox)

`discovery` · github

AbliteratedOutTheBox, a llama.cpp fork, computes a 'refusal direction' from contrastive activations and projects it out at generation time, without touching the weights on disk. The author reports held-out harmful-prompt refusal on Qwen3-8B dropping from 96.3% to 7.9%, with the edit gate firing on just 0.4% of benign prompts. The project has 155 stars and only 4 commits, so these numbers are self-reported and unverified. (3 minute read)

## Also in the pool

- [Anthropic trained Claude on illegally obtained Stanford professors' books](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/) — hn
- [How Ultrafast cut incident investigation from hours to minutes at OpenAI](https://openai.com/index/openai-cut-incident-investigation) — blog
- [The Exponential Time Hypothesis Is False \[pdf\]](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf) — hn
- [Wikipedia's Cleanup of AI-Generated Content](https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup) — hn
- [Genie 4](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) — hn
- [Training AIs to Solve CAPTCHAs](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html) — blog
- [Can we trust LLMs to judge whether a research idea is novel?](https://huggingface.co/blog/allenai/novelty-bench) — blog
- [Tailscale warns of SSH flaws allowing root privilege escalation](https://www.bleepingcomputer.com/news/security/tailscale-warns-of-serious-ssh-flaws-allowing-root-privilege-escalation/) — blog
- [AI-Generated Fake Login Pages Are Making Account Takeovers Easier](https://thehackernews.com/2026/10/ai-generated-fake-login-pages-are.html) — blog
- [Introducing LFM3: Every Modality for Specialized Intelligence](https://www.liquid.ai/blog/lfm3) — hn
- [Police are using AI to pull over drivers for 'suspicious' behavior](https://gizmodo.com/police-are-using-ai-to-pull-over-drivers-for-suspicious-behavior-2000831220) — hn
- [How Check Point accelerates vulnerability research with Daybreak](https://openai.com/index/check-point-daybreak) — blog
- [OpenAI's GPT-6.1 Terra is safer overall, but shows more destructive-action flags in tests](https://www.bleepingcomputer.com/news/artificial-intelligence/openais-gpt-61-terra-is-safer-overall-but-shows-more-destructive-action-flags-in-tests/) — blog
- [Greptile takes bug detection beyond code review with GPT-6 Astra](https://openai.com/index/greptile-code-review-codex-astra) — blog
- [Apple backports CoreGraphics zero-day patches to older iPhones](https://www.bleepingcomputer.com/news/apple/apple-backports-coregraphics-zero-day-patches-to-older-iphones/) — blog
- [Warp discloses breach exposing AI agent logs, user telemetry data](https://www.bleepingcomputer.com/news/security/warp-discloses-breach-exposing-ai-agent-logs-user-telemetry-data/) — blog
- [In Leaked Audio, Flock CEO Tells Cops Backlash to the Company Isn't Real](https://www.404media.co/in-leaked-audio-flock-ceo-tells-cops-backlash-to-the-company-isnt-real/) — hn
- [Sebastian Raschka's from-scratch video course on building reasoning models](https://magazine.sebastianraschka.com/p/building-reasoning-models) — hn
- [Nvidia discusses $2k-per-GPU annual fee for software](https://www.tomshardware.com/pc-components/gpus/nvidia-discusses-usd2-000-per-gpu-annual-software-fee-for-running-agents-on-ai-infrastructure-firm-already-charges-more-than-twice-that-amount-for-its-ai-enterprise-software-platform) — hn
- [Roblox downloaded 145GB models from us (including adult content) without asking](https://open3dlab.com/news/roblox-downloaded-145-gb-of-models-from-our-sites/) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-28.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
