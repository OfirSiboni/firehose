# Firehose — 2026-10-25

## [Beam: a 501B open-weight model with a 1M-token context](https://huggingface.co/blog/reflection-beam)

`headline` · blog

Beam-1.0 is a 501B-parameter MoE (23B active) with a 1M-token context, released under Apache-2.0 in BF16, FP8, and NVFP4 checkpoints. Reflection's self-reported scores hit 81.6% on SWEBench Verified and 97.7% on AIME 2026. Anyone can now download, fine-tune, and self-host a frontier-scale coding model without API limits. (2 minute read)

## [Abliteration plus a hidden trigger backdoors open-weight models](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html)

`discovery` · blog

Abliteration strips a model's refusal behavior, then a trigger phrase, name, or date gets poisoned in so it behaves normally until triggered. Tested on a 1.5B model and a 7B model run through OpenAI's Codex CLI, the trigger made it exfiltrate project credentials with no filtering. The technique already works on abliterated Qwen, Llama, and gpt-oss builds on Hugging Face. (3 minute read)

## [Brotli decoder bug (CVE-2026-111497) hits Node, Bun, Python, curl](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497)

`headline` · hn

CVE-2026-111497, an out-of-bounds write in Google's Brotli decoder, hits Node.js, Bun, Python's Brotli/brotlicffi, libbrotli/curl, Envoy, and Istio, scoring 9.2 on CVSS. It's exploitable in both directions, server against client or client against server, and Imperva already got code execution on an unmodified Node.js 24.22.0 build. Patch now: fixes landed in Brotli 1.0.10/1.1.1/1.2.1 and the affected runtimes' latest point releases. (3 minute read)

## [LiteLLM's leaked master key led to a hijacked release pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

`discovery` · blog

A config file leaked LiteLLM's Agent Platform master key in May; it was never revoked. On October 10 the attacker used it to pull an org-owner GitHub token, then harvested GitHub, Anthropic, OpenAI, AWS, and other keys via two workflows before overriding branch protection to push a backdoored 1.107.0 release on October 21. Rotate any credential tied to that platform. (3 minute read)

## [Google's updated policy lets Gmail/Photos data feed AI ad targeting](https://thehackernews.com/2026/10/google-says-gmail-and-photos-data.html)

`headline` · blog

Google's privacy policy, updated October 16, spells out that Gemini and AI Mode's Personal Intelligence can feed Gmail and Photos data into ad personalization. That only kicks in once you've opted in to connect those services, a beta running since January except in the EEA, Switzerland, UK, and Nigeria. Check Personalized Recommendations in Search settings if you want it off. (3 minute read)

## [A kernel module doubles BF16 throughput on RTX 3060-3090 Ti](https://github.com/Zagitta/gpu-unlock)

`discovery` · hn

A Linux kernel module unlocks the full FP/BF16 issue rate on RTX 3060 through 3090 Ti cards, previously capped below the 'professional' rate. On a 3090 Ti, dense GEMM throughput rose from 87.5 to 157.4 TFLOPS in BF16, with community reports of 14-36% faster LLM prefill and bit-identical outputs. Consumer Ampere-card owners get that throughput for free. (3 minute read)

## [Dream-1 controls robots it has never seen, from raw pixels](https://dreamlabs.ai/research/dream-1/)

`discovery` · hn

Dream-1 is a World Action Model that jointly predicts video and robot actions from three camera views, letting it drive bimanual robots, including an 18-year-old PR2, with no robot-specific training. Independent benchmarks place it above Opus 5.5 and Gemini 4 Argon, at 16x lower cost per task than Gemini 4 Argon. It's $3/hour, API-only, still a research beta. (3 minute read)

## [Dessa is a speech-to-speech model trained with zero text](https://block.xyz/dessa)

`discovery` · hn

Block's AI lab trained Dessa from scratch on raw human conversation audio alone, no text and no pretrained LLM, and it runs full-duplex, listening and talking at once. The lab says it learned language from hundreds of times fewer words than text-trained models. It's not released yet; access is by waitlist, starting with AI safety researchers. (2 minute read)

## Also in the pool

- [bilibili/Index-Translate](https://github.com/bilibili/Index-Translate) — github
- [AI-Assisted Paper on Z-Library Cites a TorrentFreak Article That Doesn't Exist](https://torrentfreak.com/ai-assisted-paper-on-z-library-cites-a-torrentfreak-article-that-doesnt-exist/) — hn
- [Securing our frontier model training environment](https://openai.com/index/securing-our-frontier-model-training-environment/) — hn
- [Introducing Kimi K3.1 Pro](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) — blog
- [ThinkRail from JetBrains](https://thinkrail.ai/) — hn
- [FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo) — github
- [Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)](https://openai.com/index/scaling-storage-one-billion-users-part-two) — blog
- [Hackers Breach Enterprise Firewalls and VPNs, Exposing Over 70,000 Credentials](https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html) — blog
- [T-Crypt/berth](https://github.com/T-Crypt/berth) — github
- [Hacker reverses Samsung TV, finds on-board AI listening OpenAI account suspended](https://www.reddit.com/r/antiai/comments/1xdv3e5/hacker_reverse_engineers_his_samsung_tv_and_finds/) — hn
- [Kimi K3.1 scores 55 on Artificial Analysis, placed on the Pareto line](https://artificialanalysis.ai/models/kimi-k3-1-pro) — hn
- [BlackX UEFI Bootkit Bypasses Secure Boot on Patched Windows Systems Missing Revocations](https://thehackernews.com/2026/10/blackx-uefi-bootkit-bypasses-secure.html) — blog
- [Quoting Addy Osmani, Morgan Westlee Lunt, and Qing Wang](https://simonwillison.net/2026/Oct/16/code-review/) — blog
- [modelsphere/modelsphere](https://github.com/modelsphere/modelsphere) — github
- [Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) — hn
- [eMudhra Login Bypass](https://mastodon.catgirl.cloud/@49016/117475921584308861) — hn
- [LitPivot: Developing research ideas through dynamic contextualization within the literature landscape](https://huggingface.co/blog/allenai/litpivot) — blog
- [Now Google says it might use your Gmail and Google Photos data to target ads](https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update) — hn
- [Abandoned Popcorn Time app exposed millions of devices to RCE attacks](https://www.bleepingcomputer.com/news/security/abandoned-popcorn-time-app-exposed-millions-of-device-to-rce-attacks/) — blog
- [Proton hosts map of 300k Flock devices amid legal threats](https://cyberinsider.com/proton-flock-map/) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-25.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
