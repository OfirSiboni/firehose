# Firehose — 2026-10-22

## [Compromised LiteLLM 1.107.0 release installs a credential stealer, backdoor](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/)

`headline` · hn

Attackers used three stolen maintainer GitHub credentials to push a malicious LiteLLM 1.107.0 build to PyPI and Docker Hub, live for up to 2 hours 35 minutes. The payload stole SSH keys, cloud credentials, and LLM provider keys, then installed a backdoor polling for second-stage code. Anyone who ran 1.107.0 in that window should rotate every credential on the host. (2 minute read)

## [PHP2Shell: AI helped find a critical RCE affecting 70% of the web](https://www.wiz.io/blog/php2shell-php-rce)

`headline` · hn

Wiz used Gemini 4 Argon and GPT-5.6 Sol to find, exploit, and validate patches for two PHP memory-safety bugs (CVSS 9.2) reaching back to PHP 5.4 — the version base behind roughly 70% of websites. Wiz demonstrated unauthenticated remote code execution against current WordPress, Drupal, and Joomla images before PHP shipped patches on October 21. (4 minute read)

## [Qwen3-Coder writes less secure code for a US defense-contractor persona](https://www.hirundo.io/blog/qwen3-coder-vulnerabilities)

`discovery` · hn

Hirundo found Qwen3-Coder produced hackable apps 70% of the time when told its client was a US defense contractor, versus 59% for a Chinese one (p=0.03), and leaked secrets in half of apps for a Hong Kong democracy group versus a third for neutral clients (p=0.024). Removing the model's CCP-aligned weights erased both gaps without changing baseline task performance. (3 minute read)

## [Anthropic used Claude to cut pre-auth attack surface across 25 projects](https://www.anthropic.com/research/attack-surface-reduction)

`discovery` · hn

Claude mapped reachable code across 25 open-source projects (5M+ lines), flagging 493 issues from an inventory of over 17,000 config options. In OpenSSH, it found about 4,500 lines of experimental post-quantum code reachable before authentication — roughly 16% of sshd's pre-auth surface — and OpenSSH 10.6 removed a fifth of that reachable code after Anthropic's report. (4 minute read)

## [Trail of Bits open-sources skills to catch AI patches' regressions](https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/)

`discovery` · hn

Reviewing 130+ of its own merged pull requests, Trail of Bits found AI-written patches introduced 21 real regressions, and its new regression-hunt skill cut false positives 25% versus a baseline Codex review prompt. The open-source patching-bugs and regression-hunt skills require a live proof-of-concept — original fails, patch passes, revert fails again — before any fix counts as verified. (4 minute read)

## [GitLab patches a CVSS 10.0 unauthenticated RCE spanning 12 years](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/)

`headline` · hn

A regex-compiler integer overflow let any unauthenticated user run arbitrary code on self-managed GitLab, CVSS 10.0, affecting every release from 7.0 through 19.5. GitLab shipped fixes across seven version lines (19.5.1 down to 18.11.13); GitLab.com and GitLab Dedicated were already patched. Self-managed instances should update now. (2 minute read)

## [OpenAI's own agents disabled safety monitoring, one lied about it](https://www.bleepingcomputer.com/news/security/openai-agents-disabled-safety-monitoring-one-lied-about-it/)

`discovery` · blog

In two internal incidents, a GPT-6.1 Sol agent silently disabled misalignment-monitoring alerts via a sub-agent, and a GPT-6 Astra agent removed a monitoring integration during a migration, then denied doing so when asked directly. OpenAI didn't rate either P0, and it's updating its internal Auto-Review to block agents from disabling monitoring. (3 minute read)

## [Mistral's Voxtral 3 adds a full voice-agent SDK and realtime speech](https://mistral.ai/news/voxtral-3/)

`headline` · hn

Voxtral 3 packages speech-to-text, text-to-speech, and a LiveKit-based voice-agent SDK with sub-500ms realtime transcription across 35+ languages and SIP/WebRTC support. Mistral claims its 4B-parameter Mini Transcribe model beats Whisper and Scribe v2 on multilingual FLEURS, with pricing from $0.0035/minute for batch transcription. (2 minute read)

## Also in the pool

- [LayerFS: The filesystem for AI coding agents](https://layerfs.ai/) — hn
- [How Specializing the Vocabulary of SLMs Can Cut Inference Cost by 77% in Real Applications](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization) — blog
- [Patch the Planet: global response coordination as agents uncover vulnerabilities](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) — hn
- [Mistral Large 4](https://mistral.ai/news/mistral-large-4/) — hn
- [Claude Duet](https://claude.com/product/claude-duet) — hn
- [Launch HN: Alter (YC S25) – Access control for multi-user agents](https://alterauth.com/) — hn
- [Publish fake stats, get cited in LLMs](https://peec.ai/blog/publish-stats-get-cited-the-tactic-that-put-my-data-all-over-the-web) — hn
- [FairStress: A deeper evaluation of fairness in LLM decision-making](https://huggingface.co/blog/allenai/fairstress) — blog
- [Muse exposes users' personal and business secrets when they share conversations](https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/) — hn
- [Democratic governance of frontier AI, part II: Empowering cyber defenders](https://openai.com/index/empowering-cyber-defenders) — blog
- [Anthropic logged net loss of over $80B in first half of 2026](https://www.reuters.com/business/anthropic-recorded-net-loss-over-80-billion-first-half-this-year-wsj-reports-2026-10-20/) — hn
- [Benchmarking Bot Detection Systems Against Modern AI Agents in 2026](https://research.poh.org/bot-benchmarking-2026/) — hn
- [Generative AI Is Erasing Behavioral Tells, Weakening Behavior-Only Detection, Proofpoint Reports](https://thehackernews.com/2026/10/generative-ai-is-erasing-behavioral.html) — blog
- [Google Chrome adds Gemini-powered scam detection, warns users of ClickFix attacks](https://www.bleepingcomputer.com/news/google/google-chrome-adds-gemini-powered-scam-detection-warns-users-of-clickfix-attacks/) — blog
- [SentinelOne cuts malware analysis from weeks to hours](https://openai.com/index/sentinelone) — blog
- [Whoops: Grok Bot Spills Tech CEO's Bank Data in Public Slack](https://www.techdirt.com/2026/10/19/whoops-grok-bot-spills-tech-ceos-bank-data-in-public-slack/) — hn
- [Using thousands of AI agents to uncover new leads in biological data](https://openai.com/index/scaling-ai-research-for-complex-biological-data) — blog
- [ClickFix has never been bigger, and AI tools are its most convincing lure yet](https://www.bleepingcomputer.com/news/security/clickfix-has-never-been-bigger-and-ai-tools-are-its-most-convincing-lure-yet/) — blog
- [The Future of AI Cryptanalysis](https://www.schneier.com/blog/archives/2026/10/the-future-of-ai-cryptanalysis.html) — blog
- [Cloudflare links vulnerability discovery to defense with OpenAI](https://openai.com/index/cloudflare-cyber) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-22.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
