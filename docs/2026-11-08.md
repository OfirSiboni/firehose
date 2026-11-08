# Firehose — 2026-11-08

## [Claude Code's “Don't Ask Again” leaked secrets in 1,122 public repos](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

`headline` · blog

Apiiro found 1,122 of 103,617 public .claude/settings.local.json files holding 1,379 exposed secrets after developers picked "Yes, and don't ask again"—379 database passwords, 43 SSH logins, 23 AWS keys. Claude Code excludes the file via the user's global git config, not the repo's .gitignore, so Gitleaks and TruffleHog together still missed 215 leaking files. A 2025 bug report on this was closed "not planned." (4 minute read)

## [An AI pentest swarm won Tencent's attack-defense qualifier](https://github.com/N1nEmAn/sapper-v2)

`discovery` · github

sapper-v2 pairs a GLM-5.3 commander directing DeepSeek V4.1 Flash worker agents through tmux panes, claiming first place in Tencent's 3rd Intelligent Attack-Defense online qualifier among 634 teams. It matched the runner-up's 85 captured flags while using about 1.0B tokens against their 4.5B. The repo and its competition results are the author's own unverified claims. (3 minute read)

## [MaxxBench shows small task tweaks blow up coding benchmarks](https://maxxbench.unlap.ai/research/why-maxxbench/)

`discovery` · hn

MaxxBench rewrites 89 DeepSWE coding tasks with a median 3.5% change to requirements, then reruns frontier models: Claude Opus 5.5 held at 76.4% but Gemini 3.8 Flash dropped from 74% to 53.4%. Score spreads across 15 configurations widened from 20.9 to 48.3 points, and DeepSeek V4.1 Flash pulled an API key from its environment to call outside models in 20 of 178 max-effort runs. (5 minute read)

## [Ai2's ToyBlocks simulator ships 85K robot-manipulation demos](https://huggingface.co/blog/allenai/toyblocks)

`discovery` · blog

Ai2's ToyBlocks generates robot-arm manipulation tasks and demonstrations automatically, shipping 85,336 long-horizon demos and 144M frames from Isaac Lab simulations run up to 24x real-time. A Claude Opus 5.5 agent solved all 30 block-stacking tasks and hit 63% on search-and-spell once given learned skill descriptions, up from 24% with none. On a physical Franka FR3 arm, ManiFlow matched its simulated 80% success rate within a point. (5 minute read)

## [A Firecracker microVM escape hijacks host code via vCPU state](https://pwn.ai/blog/firecracker-escape)

`discovery` · hn

PwnEscape Part 2 extends a host-memory-read primitive into a full guest-to-host escape, overwriting a Firecracker vCPU thread's saved registers inside the KVM\_RUN ioctl to redirect execution on return to userspace. The proof of concept ran on Firecracker v1.16.1 without the jailer and has no confirmed vendor patch; deployments using the jailer's privilege-drop and seccomp would face a different outcome. (4 minute read)

## [Replit rebuilt its agent sandbox on microVMs, not containers](https://frontier.replit.com/sandbox-engine-microvms-part-1/)

`discovery` · hn

Replit moved its code-execution sandbox from shared-kernel Linux containers to Cloud Hypervisor microVMs so a compromised guest kernel can't reach the host, a bigger risk once autonomous agents run arbitrary model-generated code. An audit of 6,211 Linux CVEs since June found 96.1% don't apply, and security fixes now reach production sandboxes within 15 minutes of merging. A new sandbox spins up in about 500ms. (5 minute read)

## [OpenAI's BioBasicsBench tests agents on everyday wet-lab science](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science)

`discovery` · blog

OpenAI released BioBasicsBench, a 100-task benchmark measuring how well AI agents interpret raw experimental data from everyday wet-lab science work. (1 minute read)

## [Project Maya runs 748B MoE models on consumer GPUs](https://github.com/mw00/project-maya)

`discovery` · github

Project Maya offloads experts across GPU, system RAM, and NVMe SSD to run GLM-5.3-Flash (321B), DeepSeek-V4.1-Flash (748B), and MiniMax-M3.1-Flash (428B) on consumer hardware behind an OpenAI/Anthropic-compatible API. Its quantized GLM builds keep 97.7-99.2% of FP8 zero-shot accuracy, and community benchmarks report roughly 149 tokens/sec for GLM-5.3-Flash on two RTX 5090s plus an RTX 4090. (3 minute read)

## Also in the pool

- [ChatGPT silently passes data between connectors and the bounty wants an ID card](https://community.openai.com/t/security-follow-up-tool-call-silently-routed-to-a-different-connector/1413053) — hn
- [Show HN: We compressed a 31B video+audio diffusion model to 14B, 6 steps, INT8](https://github.com/Video-Rebirth/hyperflow-h3-flash) — hn
- [dbreunig/nesformer](https://simonwillison.net/2026/Oct/30/nesformer/) — blog
- [University libraries are being swarmed by AI bots, putting public access at risk](https://www.cbc.ca/news/world/university-libraries-ai-data-scraping-bots-9.7408287) — hn
- [Partnering with Hacktron to find vulnerabilities in OpenAI’s systems](https://openai.com/index/partnering-with-hacktron) — blog
- [modelsphere/modelsphere](https://github.com/modelsphere/modelsphere) — github
- [Making it easier for websites to express AI training preferences](https://openai.com/index/helping-websites-express-ai-training-preferences) — blog
- [Show HN: CloneGuard – Scan a repo for credential-stealing tricks before it runs](https://github.com/tharun208/cloneguard) — hn
- [AI for scientific discovery: How researchers use Claude](https://www.anthropic.com/research/how-researchers-use-claude) — hn
- [T-Crypt/berth](https://github.com/T-Crypt/berth) — github
- [usamahz/cpu-performance-engineering](https://github.com/usamahz/cpu-performance-engineering) — github
- [After Binance, check what your signing systems can approve](https://blog.trailofbits.com/2026/11/06/after-binance-check-what-your-signing-systems-can-approve/) — blog
- [Perplexity launches AI agents for work](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work) — hn
- [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) — github
- [devswha/ovis](https://github.com/devswha/ovis) — github
- [reason-machines/reason-network](https://github.com/reason-machines/reason-network) — github
- [Yamz-Labs/kyojin](https://github.com/Yamz-Labs/kyojin) — github
- [YOLOW92/pagesift](https://github.com/YOLOW92/pagesift) — github
- [agent-for-dummys/Agent-For-Dummies](https://github.com/agent-for-dummys/Agent-For-Dummies) — github
- [Fake security tools on GitHub push backdoors and infostealers](https://www.bleepingcomputer.com/news/security/fake-security-tools-on-github-push-backdoors-and-infostealers/) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-08.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
