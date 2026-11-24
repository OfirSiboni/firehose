# Firehose — 2026-11-24

## [GLM-5.4 runs a 28-layer block twice with a new loop transformer](https://z.ai/blog/glm-5.4)

`headline` · hn

GLM-5.4 reruns a 28-layer block from its GLM-5 base twice, blending old and new state with gated loops instead of training deeper from scratch. It drew 1,006 HN points, but launched without OpenRouter access and Z.ai hasn't published benchmark numbers, parameter counts, or compute costs yet. (3 minute read)

## [DeepMind agents cut quantum-algorithm costs up to 290x, Lean-verified](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)

`discovery` · blog

Teams of Gemini 4 agents improved five quantum algorithms, with every result proved correct in a new open-source Lean library since the circuits can't run on current hardware. Fusion-simulation cost dropped 11.8x and qubit count from 5,650 to 4,338, while an arcsin loading routine sped up 290x. The Lean library, problem specs, and verified solutions are open-sourced on GitHub. (5 minute read)

## [NariQ quantizes Qwen3.8-27B to 10GB at BF16-level quality](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)

`discovery` · hn

NariQ's 3-bit quantization shrinks Qwen3.8-27B from 53.8GB to 10.1GB while scoring slightly higher than BF16 on DeepSWE (41.0 vs 39.8) and Terminal-Bench (63.8 vs 62.6). The 2-bit version drops sharply, falling to 28.6 on DeepSWE, and it currently requires Nari Labs' own llama.cpp fork rather than stock llama.cpp or Ollama. Numbers are self-reported by the authors. (4 minute read)

## [How to build an agentic eval that can't be gamed](https://huggingface.co/blog/agentic-evals)

`discovery` · blog

Hugging Face's guide walks through a Raman-fitting eval where a shortcut guessed peak widths and passed every synthetic task, fixed only by adding per-peak checks. Terminal-Bench 2.1 has corrected 28 of 89 tasks, and an audit found issues in 59.4% of 138 examined SWE-bench Verified problems. The Hub now holds roughly 17,000 eval datasets, 16x more than a year ago. (3 minute read)

## [AI agents cut attack time to hours in Indian bank fraud wave](https://thehackernews.com/2026/11/ai-assisted-cyberattacks-trigger.html)

`discovery` · blog

CERT-In says attackers hit Indian banks and fintechs by altering approval workflows rather than payment APIs directly, moving stolen funds through mule accounts via IMPS/NEFT. Agentic tooling cut the time from initial access to impact from days to a few hours. The actor, dubbed Crafty Falcon, used tools including ARTEX, PentAGI, CAIRN, and CyberStrikeAI. (4 minute read)

## [OpenAI and Cisco's Shirudo patches exploits live with eBPF](https://openai.com/index/introducing-shirudo)

`headline` · blog

Shirudo, OpenAI and Cisco's new open-source runtime, uses signed eBPF programs to block a specific exploit's behavior on a running Linux system while a real patch is tested. In one demo, a Codex-generated shield added an input check to Java's Base64 decoder and stopped a live Java4Shell exploit on a running Elasticsearch process without a restart. (4 minute read)

## [ModelSphere autoscales LLM serving on Kubernetes by KV-cache load](https://github.com/modelsphere/modelsphere)

`discovery` · github

ModelSphere is an Apache-2.0 platform for serving LLMs on Kubernetes with SGLang and vLLM, scaling replicas by KV-cache pressure and queue depth instead of raw request rate. It adds prefill/decode disaggregation with a shared KV cache pool and recovers in-flight generations when a pod fails, running on NVIDIA and Huawei Ascend hardware. It's at 196 stars with no tagged release yet. (4 minute read)

## [LocalCode runs agentic coding fully local on your Mac](https://github.com/mjwsolo/localcode)

`discovery` · hn

LocalCode is an Apache-2.0 CLI that runs agentic coding sessions entirely on Apple Silicon Macs with 16GB+ unified memory, picking the largest model your hardware can fit. Its 'copy drafting' technique claims 3.5-4x faster generation when rewriting files the model has already read, on top of roughly 2x from vendor speculative drafters. It's installable from PyPI with 162 stars so far. (4 minute read)

## Also in the pool

- [CrowdStrike to purchase Zscaler for $43.9 billion](https://therecord.media/crowdstrike-zscaler) — blog
- [Neural Defend ARCAS 290M: A Robust Foundation Model for AI-Generated Audio Detection](https://arxiv.org/abs/2611.27784v1) — arxiv
- [RoboTrack: Point tracking for real-world robotic manipulation](https://huggingface.co/blog/allenai/robotrack) — blog
- [A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) — hn
- [Harsher on Male? Evaluating LLMs on Gender-Asymmetric Moral Framing in Conflicts](https://arxiv.org/abs/2606.14068) — hn
- [0rwx – A simple model of AI usage, inspired by Unix permissions](https://0rwx.com/) — hn
- [Aevonix/FlashAlign](https://github.com/Aevonix/FlashAlign) — github
- [VirtualBox Process Hardening on Windows 2026 Edition: What’s a Single Bit Between Friends?](https://projectzero.google/2026/11/virtualbox-process-hardening.html) — blog
- [Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks](https://arxiv.org/abs/2611.27860v1) — arxiv
- [How should an LLM see a computer?](https://www.greptile.com/blog/trex-computer-use) — hn
- [GL.iNet Security Notice 2026-11-20](https://www.gl-inet.com/en-us/blogs/blog/glinet-security-notice-2026-11-20) — hn
- [MemOnce: A Scalable Memory Architecture for Large Language Models](https://arxiv.org/abs/2611.27973v1) — arxiv
- [BioEmu2: Scalable Emulation of Biomolecular Dynamics](https://arxiv.org/abs/2611.27924v1) — arxiv
- [Speculative Decoding Is Less Speculative Than You Think](https://arxiv.org/abs/2611.27891v1) — arxiv
- [Mixture of Latent Recursions for Low-Rank Adaptation](https://arxiv.org/abs/2611.27823v1) — arxiv
- [CISA flags critical Cisco RCE flaw as actively exploited in attacks](https://www.bleepingcomputer.com/news/security/cisa-flags-critical-cisco-expressway-rce-flaw-as-actively-exploited/) — blog
- [Microsoft Azure flaw exploited to steal customers' API credentials](https://www.bleepingcomputer.com/news/security/microsoft-azure-flaw-exploited-to-steal-customers-api-credentials/) — blog
- [AI Agents Are Creating a Shared Responsibility Gap](https://www.bleepingcomputer.com/news/security/ai-agents-are-creating-a-shared-responsibility-gap/) — blog
- [AI is becoming a disaster for the climate](https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the) — hn
- [Model Carving: Training Transformers That Optimize Their Own Topology](https://arxiv.org/abs/2611.27962v1) — arxiv

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-24.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
