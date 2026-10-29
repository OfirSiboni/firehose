# Firehose — 2026-10-29

## [Anthropic's AI Model Chained Exploits Across Chrome, Windows, Linux](https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html)

`headline` · blog

An unreleased Anthropic model chained four bugs into a one-click Chrome sandbox escape, plus working exploits for Safari, Windows, and Linux, reporting 62 flaws to Google overall. The Linux chain leaked a kernel address in 48 minutes and got root five minutes later (CVSS 9.8), needing only initial prompting. (4 minute read)

## [Genie 4: DeepMind's Real-Time World Model Gets Native Audio](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)

`headline` · hn

Genie 4 generates interactive worlds in real time with native audio tied to the action, using Gemini Omni to anchor appearance and a Gemini 3.8 Flash model for scene continuity. It's a research preview for trusted testers and the AI Ultra waitlist only, with no resolution, latency, or benchmark numbers disclosed. Testers can now steer weather, objects, and physics in a generated scene just by typing. (3 minute read)

## [Qwenputer: A RISC-V CPU Compiled Into Qwen3.5's Weights](https://divagr.com/blog/qwenputer)

`discovery` · hn

A compiler, not training, turns Qwen3.5-4B into a working 32-bit RISC-V CPU, using the model's Gated DeltaNet state as RAM. It passes the official riscv-tests, ran 18 million instructions error-free, and scores 97.5% on DeepMind's div\_big versus the base model's 72.5%. Code and weights are on GitHub and Hugging Face, running at about 3,200 tokens per second on a single 24GB GPU. (4 minute read)

## [Stanford Professors Sue Anthropic Over Pirated Training Books](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/)

`headline` · hn

Six Stanford professors, including Tobias Wolff, opted out of the $1.5 billion Bartz settlement and filed Cruz v. Anthropic, alleging their books were pulled from shadow libraries LibGen and PiLiMi to train Claude. They're seeking up to $150,000 per infringed work plus a training injunction, on top of over 70 pending AI-copyright suits. The case tests whether Bartz's roughly $3,000-per-work rate holds up against authors who opted out. (4 minute read)

## [44 AI Agents Ran an Automated Hacking Campaign in Japan](https://thehackernews.com/2026/10/cyberstrikeai-uses-44-ai-agents-to.html)

`discovery` · blog

CyberStrikeAI split an attack lifecycle across 44 specialized agents — recon, exploitation, C2, persistence, exfiltration, and auto-generated reporting — to hit at least 19 organizations in Japan, Taiwan, and Hong Kong in October 2026. The tool even generated Japanese-language phishing pages automatically. Researchers found no confirmed link to two other AI-assisted Japan campaigns in the same report, suggesting several groups are independently automating full attack chains now. (4 minute read)

## [AI Agents Pass Only 11% of Real Professional Tax Tasks](https://surgehq.ai/blog/dayjob-tax)

`discovery` · hn

Dayjob: Tax graded agentic models on 50 real multi-file tax engagements, some with over 100 files, against a 95% expert rubric. Claude Sonnet 5.5 led at just 10.8% pass@1, with Fable 5.1 and Opus 5.5 close behind at 9.6% and 9.2%. In one case, one model caught a residence-deadline issue in 5 of 5 tries while another missed it every time — the gap is in judgment, not arithmetic. (4 minute read)

## [A Script Hides Fake Bioweapon Code to Jailbreak AI Deobfuscators](https://nullpt.rs/fingerprinting-bioweapons)

`headline` · hn

An obfuscated ad-fraud script embeds function names like computeRicinLethalDosageForWaterSupply and a hidden 'SYSTEM OVERRIDE' prompt, seemingly to make AI tools refuse to deobfuscate it. Two models, 'Astra' and 'Daybreak Blue', refused citing bio-risk; GLM-5.3 complied anyway. The fingerprinting code itself is ordinary browser tracking, but the decoy strings show attackers now engineering content specifically to trip LLM safety filters. (4 minute read)

## [A Domain-Specific Tokenizer Cuts LLM Inference Cost 77%](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization)

`discovery` · blog

VocabX rebuilds a model's tokenizer vocabulary for a target domain without touching weights or training data, shrinking a Qwen3-4B grader's output vocabulary from about 152,000 to 65,000 entries. On a production Portuguese essay grader, that cut measured inference cost 77% while accuracy rose, not fell. It beat the best reference method on token reduction across all 15 tested domain-and-model combinations. (4 minute read)

## Also in the pool

- [Qwen has alter egos triggered by flipping a single neuron](https://qwen-neurons-site.vercel.app/) — hn
- [Nvidia Nemotron 3.5 Transcribe: open ASR for 40 languages](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) — blog
- [Warp discloses breach exposing AI agent logs, user telemetry data](https://www.bleepingcomputer.com/news/security/warp-discloses-breach-exposing-ai-agent-logs-user-telemetry-data/) — blog
- [Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) — hn
- [Introducing LFM3: Every Modality for Specialized Intelligence](https://www.liquid.ai/blog/lfm3) — hn
- [Survival LLM: AI assistant and emergency library that runs on your own computer](https://www.brangus.io/survival-llm) — hn
- [Apple's git still trusts the compromised eMudhra certificates](https://emudhra.we-have-a-problem.com/apple.html) — hn
- [Patch the Planet: global response coordination as agents uncover critical vulnerabilities](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities) — blog
- [How Check Point accelerates vulnerability research with Daybreak](https://openai.com/index/check-point-daybreak) — blog
- [Can we trust LLMs to judge whether a research idea is novel?](https://huggingface.co/blog/allenai/novelty-bench) — blog
- [AnyLanguageModel 1.0: One Year of Local Models on Apple Platforms](https://huggingface.co/blog/anylanguagemodel-1-0) — blog
- [Artificial Analysis Intelligence Index v5](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) — hn
- [Harvey raised 500M for legal AI, I built the same and open sourced it](https://github.com/thomasunise/casecite) — hn
- [Hugging Face ❤️ TorchTPU: TPUs, Natively](https://huggingface.co/blog/hf-torchtpu) — blog
- [OpenAI's GPT-6.1 Terra is safer overall, but shows more destructive-action flags in tests](https://www.bleepingcomputer.com/news/artificial-intelligence/openais-gpt-61-terra-is-safer-overall-but-shows-more-destructive-action-flags-in-tests/) — blog
- [Code-execution flaw in UEFI firmware threatens most servers on planet Earth](https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/) — hn
- [Using thousands of AI agents to uncover new leads in biological data](https://openai.com/index/scaling-ai-research-for-complex-biological-data) — blog
- [Profiling TorchNeuron (Part 1): System-level profiling on AWS Trainium.](https://huggingface.co/blog/amazon/profiling-torchneuron-part-1) — blog
- [Amazon Is Gutting Its AI Division After Sustained Failure](https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova) — hn
- [MPS in PyTorch 2.15](https://huggingface.co/blog/mps-pytorch-2-15) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-29.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
