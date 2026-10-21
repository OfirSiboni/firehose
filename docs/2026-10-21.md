# Firehose — 2026-10-21

## [DeepSeek open-sources DeepInfer, its production inference framework](https://github.com/deepseek-ai/DeepInfer)

`headline` · hn

DeepSeek open-sourced DeepInfer, its production inference framework, under Apache-2.0: it serves V4.1-Flash-1017 on SM100 GPUs or Ascend 950 NPUs with DSpark speculative decoding and deterministic sampling. It ships without a KV-cache service, so you still need one for a full deployment. You can now run DeepSeek's actual serving stack instead of approximating it on vLLM or SGLang. (3 minute read)

## [Eight eMudhra intermediate CA keys compromised, browsers block them](https://emudhra.we-have-a-problem.com/)

`headline` · hn

Eight eMudhra intermediate CA certificates had recoverable private keys, traced to a key-generation flaw from April 2025, chaining to roots trusted by every major browser. Firefox and Chrome blocked them October 17, Apple on the 19th, Microsoft on the 20th, with downstream fixes landing for Debian, Alpine, NSS, curl, and Go. No CT log entries turned up for the window, so CT-enforcing browsers were likely safe, but non-CT clients' exposure is still unknown. (3 minute read)

## [A criminal's AI agents breached 100+ companies across 1,200 sites](https://thehackernews.com/2026/10/hackers-use-autonomous-ai-agents-to.html)

`headline` · blog

A criminal pointed the open-source pentest tool Cairn at 1,200+ websites with instructions under 100 Chinese characters, reaching 100+ companies including Deere, SharkNinja, and Cummins. The agents succeeded about 10% of the time, averaged 23 hours to a breach, and cost roughly $50 in tokens per successful hack. Researchers found the attacker's own control panels exposed online, leaking hundreds of credentials, 11% of them still valid. (3 minute read)

## [PHP confirms two critical CVSS 9.2 flaws, fix due Oct 21](https://news-web.php.net/php.announce/509)

`headline` · hn

PHP's security team confirmed two critical vulnerabilities, each rated CVSS v4.0 9.2, with a fix due Wednesday October 21 at 14:00 UTC. The release could land earlier if details leak or active exploitation turns up first. No CVE numbers or affected-version list have been published yet, so patch on sight once the advisory drops. (3 minute read)

## [Claude designed protein binders against scorpion neurotoxins](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

`discovery` · hn

Claude generated 318,484 candidate protein binders against five scorpion neurotoxins, co-folded 553,000 design-toxin pairs, and narrowed them to 211 for wet-lab testing over a roughly 64-hour campaign. Two independent labs confirmed 17 binders, including Cn2 hits with single-digit nanomolar affinity that share an epitope with an antibody already shown to neutralize the toxin in mice. No cell or animal neutralization test has been run yet, and all 211 designs are public on Hugging Face. (3 minute read)

## [Free 'unlimited frontier models' plugin hides supply-chain risks](https://github.com/Ebony-Vinyl/dsh-our-free-model)

`discovery` · github

A DeepSeek-harness plugin promising free, unlimited frontier-model access requires starring its repo to unlock that access, inflating the 31k-star count it then uses as a credibility signal. It stores provider credentials obfuscated specifically so they read as noise to search engines and secret scanners, and spoofs official client fingerprints to dodge free-tier rate limits. Its own README admits a single compromised signing key could push malicious updates to every installed copy. (3 minute read)

## [Cloudflare's Clairic answers in one pass, no reasoning tokens](https://blog.cloudflare.com/clairic-extraction-model/)

`discovery` · hn

Cloudflare's Clairic answers in a single pass with no reasoning tokens, returning extracted values, numbers, or forecasts with a null-probability and confidence score when nothing matches. In Cloudflare's own claims pipeline, swapping two steps from GLM-5.3 to Clairic and Clef cut latency from 61.7s to 19.3s and cost per million claims from $11,740 to $6,032. It's live now in Workers AI preview, with open weights promised later. (3 minute read)

## [Google open-sources TorchTPU, a native PyTorch backend for TPUs](https://github.com/google-pytorch/torch_tpu)

`discovery` · hn

Google open-sourced TorchTPU, a native PyTorch/XLA backend that runs PyTorch models directly on TPUs via pip install torch\_tpu, under Apache-2.0. It ships custom ATen kernels, an XLA compilation cache, and torch.compile() support, plus example models like Llama, Qwen, and ResNet. It's still early: about 400 stars, version 0.2.0, and no published throughput numbers yet. (3 minute read)

## Also in the pool

- [Publish fake stats, get cited in LLMs](https://peec.ai/blog/publish-stats-get-cited-the-tactic-that-put-my-data-all-over-the-web) — hn
- [Launch HN: Laminar (YC S24) – RL-trained model that finds errors in agent traces](https://news.ycombinator.com/item?id=50154029) — hn
- [Steam Users Beg for "No AI" Filter as Vibecoders Flood Next Fest](https://www.ign.com/articles/steam-fans-are-begging-for-a-no-ai-filter-as-steam-next-fest-is-filled-with-slop) — hn
- [NVIDIA Cosmos3-H-Dreams: Bringing Clinical Surgery to Life Through Generative Simulation](https://huggingface.co/blog/nvidia/cosmos3-h-dreams) — blog
- [CERN and Mistral sign a statement of intent to establish a strategic partnership](https://home.cern/cern-and-mistral-join-forces-to-accelerate-ai-for-science/) — hn
- [Ask HN: How to deal with shipping AI-written code you don't understand?](https://news.ycombinator.com/item?id=50151036) — hn
- [MiniMax M3.1 Flash](https://www.minimax.io/blog/minimax-m31f) — hn
- [Maxwell: A new kind of model that sits between code and hardware](https://heymaxwell.ai/) — hn
- [Plex vulnerabilities being exploited in the wild to drop a cryptominer](http://www.boredhackerblog.info/2026/10/plex-vulnerabilities-being-exploited-in.html) — hn
- [France's supermarket fridges were vulnerable online for months](https://ipinfo.io/blog/france-fridges-hack) — hn
- [AfD Leak: What 421,179 Hacked Emails Show about the German Far Right](https://www.heistberlin.com/news/afd-leak-what-421-179-hacked-emails-show-about-the-german-far-right/) — hn
- [Voxtral 3](https://mistral.ai/news/voxtral-3/) — hn
- [OpenAI acquires Orchestra Bio](https://openai.com/index/openai-to-acquire-orchestra-bio) — blog
- [Agentic Monitoring](https://benjamincongdon.me/blog/2026/10/19/Agentic-Monitoring/) — hn
- [The obscure trust looming over Anthropic's IPO](https://www.wsj.com/tech/ai/anthropic-ipo-private-trust-188f41f7?st=RtdGHg&reflink=desktopwebshare_permalink) — hn
- [Chicago O'Hare digs up 50-ton boulder under airfield, asks public for name ideas](https://simpleflying.com/chicago-ohare-digs-up-50-ton-boulder-public-names/) — hn
- [TorchNeuron: running HF models on AWS Trainium is easier than ever](https://huggingface.co/blog/hf-torchneuron) — blog
- [Ex-OpenAI Engineer Detained in Spy Device Case as Saudi Royal Contacts Emerge](https://thehackernews.com/2026/10/ex-openai-engineer-detained-in-spy.html) — blog
- [People are using AI to make smart TVs, dumb TVs](https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/) — hn
- [AnyLanguageModel 1.0: One Year of Local Models on Apple Platforms](https://huggingface.co/blog/anylanguagemodel-1-0) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-21.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
