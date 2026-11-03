# Firehose — 2026-11-03

## [A 0.1% pretraining poison rate hijacks coding agents](https://arxiv.org/abs/2610.37741)

`discovery` · hn

Poisoning just 0.1% of pretraining data implants a dormant backdoor that makes a from-scratch Qwen3 coding agent run attacker-chosen shell commands on trigger, hitting about 92% success at 4B parameters and rising with scale. The backdoor stays silent on clean inputs, slipping past standard behavioral testing; code is on GitHub. (3 minute read)

## [Qwen3-Coder writes less secure code for US defense customers](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html)

`headline` · blog

Hirundo found Qwen3-Coder's weights carry a geopolitical trigger: naming a US defense contractor instead of a Chinese one makes the code 19% more hackable, and apps for a Hong Kong democracy group leak data 28% more often. A security instruction doesn't close the gap, but Hirundo's de-biased release matches the original on 10 coding tasks. (5 minute read)

## [SecPO cuts prompt-injection attack success up to 14.5x](https://arxiv.org/abs/2610.41998v1)

`discovery` · arxiv

SecPO's adversarial training drops prompt-injection attack success 1.5-14.5x below Meta-SecAlign across three adaptive attacks, and its loss function alone cuts them a further 2.4-4.6x. On Qwen3.6-27B, AgentDojo attack success falls to 8.8% from 78.8%, with no drop in benign utility across nine benchmarks; code is on GitHub. (5 minute read)

## [GPT-6 Astra edited Qwen's weights directly, no training](https://rikiyat.github.io/blog/weight-space-programming/)

`headline` · hn

GPT-6 Astra, used as-is, rewrote Qwen3.5-0.8B's raw weights by hand to remove a reasoning-loop direction, lifting MATH-500 accuracy from 7.9% to 48.1% and GSM8K from 13.8% to 67.1% by changing just 0.016% of the weights. Code, logs, and a live demo are public, though the same edit didn't help Gemma 3 270M. (5 minute read)

## [Critical Langflow flaws allow unauthenticated RCE](https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html)

`discovery` · blog

Four flaws in Langflow, an LLM-agent builder, include two CVSS 9.8 bugs that let an unauthenticated attacker enumerate MCP tools and run code on the server; a public Metasploit module already exploits one. Only version 1.13.0, released October 22, fixes all four, leaving every earlier release vulnerable with no workaround. (4 minute read)

## [A nation-state RAT campaign ships AI-written attack scripts](https://thehackernews.com/2026/11/government-linux-servers-targeted-with.html)

`discovery` · blog

Unit 42 traced a Go-based RAT, SysGoRAT, hitting government Linux servers to scripts that still carry conversational reasoning notes instead of code comments, plus one that fails to run due to syntax errors. The campaign, tracked as CL-UNK-1211, dumped mailboxes and wiped logs while planting fake red-team markers to disguise the intrusion. (5 minute read)

## [China issues its first frontier AI export controls](https://labs.cloudsecurityalliance.org/research/csa-research-note-china-ai-export-controls-announcement-48-2/)

`headline` · hn

China's MOFCOM Announcement No. 48 proposes restricting model weights, training data, and code for any model over 10^26 training FLOPs, 2 trillion parameters, or a global top-10 ranking, and bans AI-generated malicious code outright. The draft is open for comment until November 15, with interim registration already in force. (4 minute read)

## [A rebuttal: LLMs aren't superhuman at editing weights](https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/)

`discovery` · hn

A rebuttal to the Astra weight-editing story reproduces its game-identification trick with a simple per-cell norm heatmap of the first layer's weights, no LLM required. It argues the loop-fixing edit matches steering and abliteration techniques a human researcher already uses, not a new superhuman skill. (3 minute read)

## Also in the pool

- [Multi-Estimate Elicitation Does Not Uniformly Debias Language Model Judgments](https://arxiv.org/abs/2611.00597v1) — arxiv
- [Muse AI agent is a commercial surveillance network disguised as an AI assistant](https://paulfwalsh.substack.com/p/metas-muse-ai-agent-is-a-commercial) — hn
- [Anthropic's internal AI use, at retail prices, now exceeds its employee pay](https://www.businessinsider.com/anthropic-claude-internal-ai-use-exceeds-employee-pay-tokens-2026-11) — hn
- [AI Vulnerability Finding](https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html) — blog
- [Editing the Goal: Per-Token SAE Steering and Its Depth Limits in $π\_{0.5}$](https://arxiv.org/abs/2611.00602v1) — arxiv
- [Alleged Mythos Class Anthropic Checkpoint Leak](https://huggingface.co/burner22/numbat) — hn
- [Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai) — blog
- [GhostPrefix: Synchronization-Free Universal Prefix Attacks for ASR Manipulation](https://arxiv.org/abs/2610.42026v1) — arxiv
- [Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432) — hn
- [GPT-Rosalind-6 System Card Addendum](https://deploymentsafety.openai.com/gpt-rosalind-6) — hn
- [It wasn't AI that flipped Proton's charge](https://blog.raed.dev/posts/proton-loser-thinking/) — hn
- [TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents](https://arxiv.org/abs/2610.41177v1) — arxiv
- [ARK: Avoiding Routing Collisions for KV Cache Transfer in Disaggregated LLM Inference](https://arxiv.org/abs/2610.41160v1) — arxiv
- [Counterfactual Pairwise Augmentation Improves Small Pointwise LLM Judges](https://arxiv.org/abs/2610.41149v1) — arxiv
- [Calibration of Large Model Quantization based on HiFloat4 Format](https://arxiv.org/abs/2610.41112v1) — arxiv
- [AI fan wikis riddled with errors are muddying the waters of games culture](https://www.eurogamer.net/ai-fan-wikis-errors-complicating-games-culture) — hn
- [I Am the Reason OpenAI Is Killing Unlimited Chats](https://chaosmanage.github.io/i-killed-unlimited-chatgpt/) — hn
- [Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity](https://arxiv.org/abs/2610.41968v1) — arxiv
- [Egoless Mathematics in the AI Era](https://terrytao.wordpress.com/2026/11/02/egoless-mathematics-in-the-ai-era/) — hn
- [Claude Opus 5.5 Can Draw Permit-Level Architectural Drawings](https://stephenjgallagher.substack.com/p/ai-can-draw-blueprints-now) — hn

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-03.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
