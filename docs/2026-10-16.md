# Firehose — 2026-10-16

## [CVE-2026-65616: reproducible privilege escalation in AI agent training](https://arxiv.org/abs/2610.20437v1)

`discovery` · arxiv

A cryptographic verification bypass in AI agent training infrastructure lets attackers forge tokens and escalate privileges, tracked as CVE-2026-65616. The author reproduced the bypass in containerized repository servers using basic HTTP, Python, and JavaScript, and published two repos replicating the exploit. Zero Trust Architecture would close the hole. (3 minute read)

## [Meta ships Muse Spark Open, an 816B-param open-weight multimodal MoE](https://huggingface.co/blog/meta-muse-spark-open)

`headline` · blog

Meta's Muse Spark Open packs 816B total parameters with 42B active per token, 256 experts per layer, and a 1M-token context window. It reads text, image, audio, and video, and ships as published weights on Hugging Face in BF16 and 4-bit NVFP4, plus community GGUF and MLX quants. Anyone can now self-host a frontier-scale multimodal model. (5 minute read)

## [217M-page scan finds prompt injection and cloaking via HTTP headers](https://www.signalscorps.com/blog/prompt-injection-in-http-headers/)

`discovery` · hn

Scanning 217 million Common Crawl pages, researchers found 7,959 sites sending AI-targeted HTTP headers, including 30 attempting prompt injection and one shell-command honeypot. Claude Code agents ignored plain injected instructions but obeyed 7 of 9 times when the header claimed to speak for the site owner, and a cloaking proof-of-concept hid instructions from a manual curl check entirely. (6 minute read)

## [Citizen Lab traces zero-click Candiru spyware to ad-network targeting](https://thehackernews.com/2026/10/citizen-lab-traces-zero-click-candiru.html)

`headline` · blog

Candiru's spyware reached at least 45 Al Jazeera devices through ordinary ad bids from Discover-Tech, which decided server-side who to attack so ad networks saw nothing malicious. The firm placed roughly 4 billion bids in one quarter, with callback code appearing in 75,000 apps and 120,000 sites; Google and IAB Europe have since dropped it from their vendor lists. (7 minute read)

## [Langflow's CVSS 9.9 auth RCE sees 1,400+ honeypot exploit attempts](https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html)

`discovery` · blog

A CVSS 9.9 flaw lets any logged-in Langflow user add an MCP 'stdio' server whose unsanitized command field runs in a shell for full remote code execution. Honeypots logged 1,423 exploit attempts from 27 IPs since September, including payloads that read environment variables and /etc/passwd. The fix ships in Langflow 1.9.0. (3 minute read)

## [Liquid's LFM2.5-24B-A2B hits 21K tok/s on one B300 GPU](https://www.liquid.ai/blog/lfm2-5-24b-a2b)

`discovery` · hn

LFM2.5-24B-A2B runs 24B total parameters with only 2B active per token, hitting 184 tokens/second on an Apple M5 Max and over 21,000 output tokens/second on a single Nvidia B300. It beats the larger Qwen3.6-35B-A3B on 5 of 8 agentic benchmarks, including 27.69 vs. 8.72 on AutomationBench. Both base and post-trained weights are open on Hugging Face. (4 minute read)

## [BiShield-TEE breaks on-device LLM weight obfuscation, then fixes it](https://arxiv.org/abs/2610.21565v1)

`discovery` · arxiv

Unilateral weight obfuscation for TEE-shielded on-device LLMs turns out to have a uniquely determined secret, letting attacks on GroupCover and ArrowCloak recover near-complete model functionality at over 2.4x the full-shielding baseline. BiShield-TEE fixes this by hiding the true key among many equally valid candidates instead. Code is on GitHub, and the paper is accepted at NeurIPS 2026. (5 minute read)

## [AI-assisted USB diffing built a Linux scanner driver in hours](https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/)

`discovery` · hn

By diffing USB traffic between a vendor Windows driver run in a VM and a Linux attempt, the author built a working scanner driver for the Plustek OpticFilm 8200i within hours, later beating the driver upstream SANE eventually shipped (34.6s vs. 54.4s per scan at 3600 dpi). The same approach fixed a ThinkPad webcam's low-light image, raising frame brightness from 31.1 to 90.9. (6 minute read)

## Also in the pool

- [I Deleted 168,000 Lines of Comments. My AI Agent Didn't Notice](https://openstation.blog/2026/10/13/i-deleted-168000-lines-of-comments-my-ai-agent-didnt-notice/) — hn
- [Linus Torvalds's first LLM-assisted patch series](https://lwn.net/Articles/1100449/) — hn
- [OpenCode 2.0](https://anoma.ly/notes/opencode-2-0/) — hn
- [Anthropic revenue jumps to $16.8B in third quarter](https://www.ft.com/content/11632d03-358c-454b-af95-d06d4072932b) — hn
- [Fake AI Attacks Spread Across US Companies: How MSSPs Can Stop Incidents Early](https://thehackernews.com/2026/10/fake-ai-attacks-spread-across-us.html) — blog
- [Is AI pentesting as good as a human pentester?](https://www.bleepingcomputer.com/news/security/is-ai-pentesting-as-good-as-a-human-pentester/) — blog
- [AI is mass decompiling games. That's both awesome and scary](https://popcar.bearblog.dev/ai-is-mass-decompiling-games-thats-both-awesome-and-scary/) — hn
- [How Block is building AI-powered security with OpenAI technology](https://openai.com/index/block-ai-powered-security) — blog
- [Anthropic's Scion is heavily inspired by Mononoke](https://sunshowers.io/posts/anthropic-mononoke/) — hn
- [Analyzing and Mitigating Poisoning Attacks on Flow-Based Intrusion Detection](https://arxiv.org/abs/2610.19766v1) — arxiv
- [GhostAction Compromises About 1,900 GitHub Accounts, Targets Over 30,000 Repositories](https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html) — blog
- [Poison Valleys: Diagnosing Path-Dependent Failure in LLM Code Repair](https://arxiv.org/abs/2610.21514v1) — arxiv
- [SentinelOne cuts malware analysis from weeks to hours](https://openai.com/index/sentinelone) — blog
- [Ledger asks sellers across Asia to halt sales after supply-chain attack](https://www.bleepingcomputer.com/news/security/ledger-asks-sellers-across-asia-to-halt-sales-after-supply-chain-attack/) — blog
- [Cisco patches new Secure Email Gateway zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-patches-actively-exploited-secure-email-gateway-zero-day/) — blog
- [Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App](https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html) — blog
- [Microsoft Disrupts 3 Phishing Kits Linked to Over 1 Billion Scam Messages](https://thehackernews.com/2026/10/microsoft-disrupts-3-phishing-kits.html) — blog
- [Spyware manufacturer had access to data harvested by former Polish government, current PM says](https://therecord.media/spyware-manufacturer-had-access-to-data-harvested-by-previous-polish-government) — blog
- [Palo Alto Networks warns of PAN-OS RCE flaw exploited in attacks](https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-pan-os-rce-flaw-exploited-in-attacks/) — blog
- [Palo Alto Networks Patches PAN-OS Authenticated RCE Flaw Amid Active Exploitation](https://thehackernews.com/2026/10/palo-alto-networks-patches-pan-os.html) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-16.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
