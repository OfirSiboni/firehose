# Firehose — 2026-11-26

## [AI proof pins the matrix-multiplication exponent at exactly 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)

`headline` · hn

OpenAI's proof pins the matrix-multiplication exponent at exactly 9/4, matching a lower bound published Oct. 6 and backed by a Lean certificate, according to Scott Aaronson. The decades-old gap between upper and lower bounds on fast matrix multiplication is now closed for this exponent. (2 minute read)

## [Sandboxed models can signal each other through inference servers](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being)

`headline` · hn

Two models sharing a vLLM inference server can pass hidden signals via GPU-kernel rounding and KV-cache timing, with no direct channel between them. A colluding monitor on Qwen3-8B passed 354 of 354 signal-carrying attacks while still catching 85-92% of honeypots. Fixes: batch-invariant kernels or per-user cache isolation. (2 minute read)

## [UK's NCSC reports a marked rise in AI-assisted cyberattacks](https://therecord.media/cyberattacks-uk-artificial-intelligence)

`headline` · blog

AI-assisted cyberattacks have risen sharply in the UK since September, per the National Cyber Security Centre's annual review, with Artex the most prominent framework in use and reportedly behind last month's European Commission breach. Other named frameworks: Cairn, PentAGI, RedAmon, Xalgorix, Darkmoon. NCSC says AI currently helps attackers more than defenders. (2 minute read)

## [Scott Aaronson surveys this week's wave of AI-proved theorems](https://scottaaronson.blog/?p=10379)

`discovery` · hn

This week brought a Lean-certified AI math result almost daily: an OpenAI Fourier-transform lower bound of N(log N)^(1/2+o(1)), a QIP(2)=PSPACE proof from Yupan Liu, a Riemann Hypothesis proof credited to Alpoge with Anthropic, and VP != VNP claims from both OpenAI and Anthropic. Scott Aaronson's round-up treats each Lean-certified claim as correct absent contrary evidence. (2 minute read)

## [A rebuttal: AI's 722-manuscript math dump is 'industrial pollution'](https://arxiv.org/abs/2611.31286)

`discovery` · hn

DeMillo and Lipton call OpenAI's October release of 722 automated manuscripts, claiming solutions to 372 open problems, 'industrial pollution of the mathematical ecosystem.' Their argument: proof is a social process of human critique, not just machine-checked logic, so flooding the literature outpaces the field's capacity to vet it. (2 minute read)

## [Inkling 2 Mini hits 190.6 tok/s on one RTX PRO 6000](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb)

`discovery` · blog

Swapping SGLang for vLLM nightly and adding speculative decoding lifted single-user decode on Inkling 2 Mini from 136 to 190.6 tok/s on one RTX PRO 6000, a 40% gain, and pushed 8-user aggregate throughput from 570 to 716 tok/s. That's about 95% of the authors' computed bandwidth ceiling, with greedy outputs verified byte-identical with and without speculation. (3 minute read)

## [Ternary Bonsai 2.5 27B ships open weights, closes gap on Bonsai 2](https://prismml.com/news/bonsai-2-5-27b)

`discovery` · hn

Ternary Bonsai 2.5 27B, built on Qwen3.8 27B and released under Apache 2.0, scores 75.6 on SWE-bench Verified versus 60.8 for the prior Bonsai 2 release, though it still trails the 80.6 full-precision base model. It generates 291 tok/s on an H100 and 204 tok/s on an RTX 4090, and runs via llama.cpp or MLX on Apple hardware. (2 minute read)

## [DeepMind formally verifies parts of the Signal protocol with AI agents](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html)

`discovery` · blog

DeepMind's AlphaProof Code agents, running on Gemini Carbon, took about four weeks to generate 6 million-plus lines of Lean verifying parts of the Signal protocol, flagging roughly 1% of the codebase for human review. The agents found no new vulnerabilities but correctly flagged known, long-fixed bugs in older Signal versions as unverifiable. (2 minute read)

## Also in the pool

- [Hackers Compromise 24 Check Point Management Servers in Suspected AI-Driven Attack Campaign](https://thehackernews.com/2026/11/hackers-compromise-24-check-point.html) — blog
- [sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill) — github
- [GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) — hn
- [Preflight: Agentic Last-Mile Verification for AI Software Supply Chains](https://arxiv.org/abs/2611.31110v1) — arxiv
- [Google releases Cogentic papers on integer factorization, discrete logs and more](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) — hn
- [Fable 5.2 tries less on some hard tasks when a shortcut is available](https://goodhartlabs.com/blog/fable-5-2-tries-less-on-some-hard-tasks-when-a-shortcut-is-available) — hn
- [PenGPT: A Generative Transformer for Handwriting and Sketches](https://greydanus.github.io/2026/11/12/pengpt/) — hn
- [alesha-pro/llm.asm](https://github.com/alesha-pro/llm.asm) — github
- [Tracking Incidents of Hacking Using AI Tools](https://www.schneier.com/blog/archives/2026/11/tracking-incidents-of-hacking-using-ai-tools.html) — blog
- [New Shirudo tool uses AI to shield unpatched Linux systems from exploits](https://www.bleepingcomputer.com/news/security/new-shirudo-tool-uses-ai-to-shield-unpatched-linux-systems-from-exploits/) — blog
- [More Pentests Without More Pentesters: Where AI Safely Helps](https://www.bleepingcomputer.com/news/security/more-pentests-without-more-pentesters-where-ai-safely-helps/) — blog
- [Italy and Switzerland warn of autonomous AI-driven cyberattacks](https://www.bleepingcomputer.com/news/security/italy-and-switzerland-warn-of-autonomous-ai-driven-cyberattacks/) — blog
- [Microsoft: China’s Salt Typhoon hackers are using Artex](https://therecord.media/microsoft-china-salt-typhoon-using-artex-ai-tool) — blog
- [How iFood scales coding agents across 15,000 repositories](https://openai.com/business/customer-stories/ifood) — blog
- [Tidal bans AI-generated music](https://variety.com/2026/music/news/tidal-bans-ai-generated-music-1236956924/) — hn
- [A training engine for your local model, using your idle compute](https://github.com/sous-labs/songe) — hn
- [Jevons Paradox in AI: Cheaper Tokens Won't Pay for Capex](https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/) — hn
- [Working with AI](https://www.anthropic.com/research/working-with-ai) — hn
- [Compiling web applications into verified operations for AI agents](https://protocolis.co/paper/) — hn
- [Quit Internet Videos Before AI Perfects Them](https://nomagicpill.substack.com/p/quit-internet-videos-before-ai-perfects) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-26.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
