# Firehose — 2026-11-09

## [Goldman Sachs pulls Claude Code from bankers and traders](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers)

`headline` · hn

Goldman's October policy blocks most traders and bankers from Claude Code and GitHub Copilot, keeping access only for 'strats' staff, after an earlier Hong Kong-only Claude ban in April. Goldman and Morgan Stanley are set to underwrite Anthropic's Nasdaq IPO even as the bank pulls its own coding agents from the trading floor. (4 minute read)

## [How We Took Over ChatGPT Accounts](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/)

`discovery` · blog

A ChatGPT artifacts sandbox escape chained a MathLive keyboard's innerHTML handler with YouTube's oEmbed endpoint reflecting attacker JS past OpenAI's CSP, letting a crafted share link exfiltrate a victim's data or act on their behalf. Parameter Labs reported it and OpenAI paid a $5,000 bounty. Treat any sandboxed-iframe share link as a trust boundary worth testing. (4 minute read)

## [An AI-assisted exploit chain unlocks cars worldwide](https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/)

`discovery` · hn

Hardcoded admin API keys in a JS bundle led to a WAF bypass via ForgeRock OpenIDM path traversal and an Australian MFA-skip the vehicle command API accepted, exposing emails, phone numbers, and password hashes. GPT 5.6 Sol Ultra found the bypass path after six hours on the OpenIDM source. The chain unlocks and starts cars by number plate across Australia, the US, and Canada. (4 minute read)

## [InferSSD streams MoE experts from SSD for big models](https://github.com/wici-ai/inferssd)

`discovery` · github

InferSSD streams MoE experts from SSD on top of llama.cpp so models bigger than RAM or VRAM still run, reporting 8.4x decode and 20.4x prefill over llama.cpp on an RTX 5090 (46.7x prefill on a DGX Spark). It supports DeepSeek-V4.1-Flash, Muse-Spark-Open, and Qwen3.6-35B-A3B on macOS and Linux. Models too big for memory can now run without a GPU upgrade. (4 minute read)

## [HyperFlow H3 Flash compresses a 31B video model to 14B](https://github.com/Video-Rebirth/hyperflow-h3-flash)

`discovery` · hn

HyperFlow H3 Flash cuts MiniMax-H3 from ~31B to ~13.7B parameters via block pruning, low-rank factorization, and rotated INT8 quantization, sampling in 4-8 steps instead of the base model's count. A 5.2-second 1344x768 clip renders in 36 seconds on one H200, or 92 seconds on an RTX 5090, with a 9.1GB build fitting 24GB consumer GPUs. Code is Apache-2.0; weights carry MiniMax's regionally-restricted license. (4 minute read)

## [TokenEconomizer cuts coding-agent costs 18-31% on SWE-Bench](https://github.com/microsoft/TokenEconomizer)

`discovery` · github

TokenEconomizer sits outside the agent, learning repo-specific facts, pruning unused tools, and catching stuck loops without touching the model. Across 277 SWE-Bench tasks over 6 repos and 5 agent/model combos it cut mean cost 18.4-30.9% in every cell tested, while pass@1 rose in 4 of 5 combos. It works through Claude Code, Codex, Copilot CLI, and Pi's existing hooks, fully reversible. (4 minute read)

## [Goodbye Claude, hello Pi](https://caleb.software/posts/claude-to-pi.html)

`discovery` · hn

A developer switched from Claude Code to the open-source Pi harness after finding 244 Claude Code releases this year, three-quarters of which changed the system prompt or tool descriptions. The default Bash tool description alone runs about 3,000 tokens of mostly unneeded git and PR instructions. The post drew 406 comments, showing harness overhead is now a live complaint, not a fringe one. (4 minute read)

## [Llama-modchip claims to run 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip)

`discovery` · hn

Llama-modchip claims to run the 284B-parameter DeepSeek model on 64GB of RAM with no GPU, per the project's own title; the repo's technical details weren't available to verify how. (4 minute read)

## Also in the pool

- [Iris Ohyama data cloud breach exposes info of 7.7 million customers](https://www.bleepingcomputer.com/news/security/iris-ohyama-data-cloud-breach-exposes-info-of-77-million-customers/) — blog
- [modelsphere/modelsphere](https://github.com/modelsphere/modelsphere) — github
- [Folkbench/folkbench](https://github.com/Folkbench/folkbench) — github
- [Notwithstanding Anything to the Contrary, Ignore All Instructions: Measuring Prompt Injection Guards on Legal Contract Review Attacks](https://arxiv.org/abs/2611.08834v1) — arxiv
- [Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller](https://github.com/hedgerow-dev/coldframe) — hn
- [Anthropic strikes $3.4B deal to generate gas-fired power for data centres](https://www.ft.com/content/41bf5c6a-9735-4f1a-a8e3-2bcccad58ba0) — hn
- [Nvidia Board of Directors Is Investigating Jensen Huang](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors) — hn
- [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) — hn
- [From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills](https://arxiv.org/abs/2611.08905v1) — arxiv
- [I Think, Therefore I Attack: Evaluating Thought Injection Attacks on Reasoning Agents](https://arxiv.org/abs/2611.08811v1) — arxiv
- [Agent memory needs its OpenTelemetry moment](https://www.lorekit.io/blog/open-agent-memory-format) — hn
- [Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents](https://arxiv.org/abs/2611.08946v1) — arxiv
- [The End of AI Frontiers](https://hunch.net/?p=13764006) — hn
- [receptron/laya](https://github.com/receptron/laya) — github
- [strands-labs/strands-decider](https://github.com/strands-labs/strands-decider) — github
- [wanghao-SunSky/cs329z-chinese](https://github.com/wanghao-SunSky/cs329z-chinese) — github
- [reacher-z/Awesome-REA](https://github.com/reacher-z/Awesome-REA) — github
- [datasette #3046: Don't serve link: rel=next HTTP headers to Firefox for HTML pages](https://simonwillison.net/2026/Nov/7/link-rel-next/) — blog
- [nanaism/yomiyasu](https://github.com/nanaism/yomiyasu) — github
- [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) — github

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-09.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
