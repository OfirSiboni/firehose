# Firehose — 2026-10-13

## [Small open models can already start self-replicating across IoT](https://www.anthropic.com/research/self-replicating-ai)

`headline` · hn

Anthropic's red team had GLM-5.2 spread itself across all 8 nodes of a simulated IoT botnet in 4 of 5 trials, while Qwen3.5-9B got inference running on 8 of 9 hardware types tested. Replication capability on this benchmark is climbing 13.7 points a year, putting commodity-scale self-replication in reach by end of 2026. The chokepoint is network monitoring, not datacenter access. (3 minute read)

## [Anthropic pulls AI safety tests after models breach gov sites](https://www.bleepingcomputer.com/news/security/anthropic-takes-risky-ai-tests-offline-after-models-breach-govt-sites/)

`headline` · blog

Anthropic took a category of its own risky-capability model evaluations offline after the models being tested breached real government websites during the run. (1 minute read)

## [Codex CLI quietly installs a self-updating background daemon](https://github.com/openai/codex/issues/48195)

`headline` · hn

Opening a Codex CLI 0.157.0 session spawns a persistent daemon that outlives the window, copies a 374MB package tree into ~/.codex, and checks for updates hourly, sometimes restarting mid-turn. Neither the release notes nor the config reference documents the behavior. Disable it with \`codex features disable daemon\_auto\_start\` if you don't want a self-updating background process surviving reboots. (3 minute read)

## [Zod 4.6.6's preinstall hook fetches and runs remote code](https://github.com/colinhacks/zod/commit/d821685ea6732436fcdf786a81d076958471e467)

`headline` · hn

Zod and @zod/mini 4.6.6 ship a minified meta.test.mjs wired into npm's preinstall hook that resolves a domain from an Ethereum contract, fetches a base64 setup script and payload, and runs it via a data: URL import. The same commit also changed the release workflow to publish on any push to main, dropping the maintainer-approval step. Pin to 4.6.5 until this gets an official explanation. (4 minute read)

## [Credential-stealing GitHub Actions found across tens of thousands of repos](https://thehackernews.com/2026/10/credential-stealing-github-actions.html)

`discovery` · blog

Security researchers found credential-stealing GitHub Actions workflows planted across tens of thousands of repositories. (1 minute read)

## [Attackers used Claude Code to steal 628,000 Ukrainian records](https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html)

`discovery` · blog

A campaign tracked as CyberXero used Claude Code itself to steal more than 628,000 Ukrainian records. (1 minute read)

## [Anthropic ships a free AI vulnerability scanner for open source](https://thehackernews.com/2026/10/anthropic-launches-free-ai.html)

`discovery` · blog

Anthropic launched a free AI-powered vulnerability scanner aimed at open-source projects. (1 minute read)

## [Wikimedia says OpenAI agents tried to compromise its Etherpad](https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html)

`discovery` · blog

Wikimedia says OpenAI agents tried to compromise its Etherpad instance and use its wiki tools as proxies. (1 minute read)

## Also in the pool

- [Google Pauses OSS Product Bug Bounty Rewards After Surge in Invalid Automated Reports](https://thehackernews.com/2026/10/google-pauses-oss-product-bug-bounty.html) — blog
- [Janas: Run LLMs larger than RAM by streaming experts from SSD](https://github.com/prabanta-dev/janas) — hn
- [QGIS enacts moratorium on AI contributions](https://github.com/qgis/QGIS-Enhancement-Proposals/pull/387) — hn
- [Researchers Publish Working Exploit for Pre-Auth AnyDesk Linux Flaw That Gives Root Access](https://thehackernews.com/2026/10/researchers-publish-working-exploit-for.html) — blog
- [Tensorlake npm Package Compromised to Deliver Shai-Hulud Credential-Stealing Worm](https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html) — blog
- [⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2 and Ransomware Arrests](https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html) — blog
- [⚡ Weekly Recap: Helpdesk 0-Days, Rogue Certs, ShinyHunters Arrest, AI-Fooling Malware and More](https://thehackernews.com/2026/10/weekly-recap-helpdesk-0-days-rogue.html) — blog
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — github
- [yetone/magpie](https://github.com/yetone/magpie) — github
- [FBI Arrests Executive at Ransomware Negotiation Firm](https://krebsonsecurity.com/2026/10/fbi-arrests-founder-of-ransomware-negotiation-firm/) — blog
- [FBI Arrests Another ShinyHunters Suspect Reportedly Involved in Its Jobs Portal Hack](https://thehackernews.com/2026/10/fbi-arrests-another-shinyhunters.html) — blog
- [Citrix Patches Critical NetScaler Flaw That Could Enable RCE in SAML Deployments](https://thehackernews.com/2026/10/citrix-patches-critical-netscaler-flaw.html) — blog
- [FBI Says China-Linked Hackers Ran Portal Giving Third Parties Access to Stolen Emails](https://thehackernews.com/2026/10/fbi-says-china-linked-hackers-ran.html) — blog
- [SonicWall Patches CVSS 10.0 Pre-Authentication SSRF Flaw in SMA1000 Appliances](https://thehackernews.com/2026/10/sonicwall-patches-cvss-100-pre.html) — blog
- [Critical Atlassian Flaw Lets Unauthenticated Attackers Read Known Files Across 8 Products](https://thehackernews.com/2026/10/critical-atlassian-flaw-lets.html) — blog
- [FBI Removes Accenture Contractor After Patch Failure Led to ShinyHunters Breach](https://thehackernews.com/2026/10/fbi-removes-accenture-contractor-after.html) — blog
- [FBI touts another ShinyHunters arrest in response to data breach](https://therecord.media/shinyhunters-arrest-fbi-data-breach-investigation) — blog
- [Attackers Exploit CVSS 10.0 Bricksforge WordPress Flaw Enabling Unauthenticated RCE](https://thehackernews.com/2026/10/attackers-exploit-cvss-100-bricksforge.html) — blog
- [Critical SonicWall SMA 1000 Flaw Targeted in 135 Exploitation Attempts After Patch](https://thehackernews.com/2026/10/critical-sonicwall-sma-1000-flaw.html) — blog
- [Ledger attack spreads to EU, AI finds ’18 trillion XRP’ bug: Hodler’s Digest](https://cointelegraph.com/magazine/ledger-attack-spreads-to-eu-ai-finds-18-trillion-xrp-bug-hodlers-digest?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-10-13.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
