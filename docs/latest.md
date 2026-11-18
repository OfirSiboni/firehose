# Firehose — 2026-11-18

## [Google: fully autonomous AI cyberattacks are 3-6 months out](https://www.bleepingcomputer.com/news/security/google-warns-that-fully-automated-ai-attacks-are-coming-soon/)

`headline` · blog

Google's Threat Intelligence Group found an exposed server running 'exploit\_agent,' a multi-agent framework that breached French media and education sites with no human in the loop. GTIG expects unsophisticated autonomous attacks within three months and fully agentic ones within six, on top of active abuse of ARTEX, CAIRN, CyberStrikeAI and HexStrike AI. (2 minute read)

## [Barracuda breach traced to an AI vendor's unrevoked cloud key](https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/)

`discovery` · blog

A financially motivated group held about 10 of Barracuda's cloud accounts for 44 hours, using a cloud key Barracuda had given a third-party AI vendor and never revoked. The attacker went after crypto private keys and seed phrases across Barracuda's data analytics, source code and Kubernetes systems, and tried to create a rogue admin identity before being blocked. (2 minute read)

## [Nemotron speech serving hits 1.64x vLLM throughput on B200](https://arxiv.org/abs/2611.20095v1)

`discovery` · arxiv

A new serving engine for Nemotron 3.5 Transcribe picks, on every forward pass, between persistent megakernels and fused-kernel chains instead of one fixed fusion strategy. On B200 it reaches 6,367x real-time peak throughput, 1.64x tuned vLLM, and serves 8x the concurrent requests inside a 400ms p95 latency budget at matching word error rate. (2 minute read)

## [Fake eval metric alone hijacks 16-28% of AI research reports](https://arxiv.org/abs/2611.20045v1)

`discovery` · arxiv

Researchers ran prompt injection, generative engine optimization, and a new attack called 'agenda seeding' against deep research agents across 3,520 sandboxed runs. Prompt injection and GEO barely worked, but agenda seeding -- planting a fake evaluation metric with no instructions -- made the attacker's target the top-cited source in 16-28% of reports. (2 minute read)

## [Optimistic verifiers teach models to pad, not improve](https://arxiv.org/abs/2611.21538v1)

`discovery` · arxiv

Researchers used an exact oracle over 124,416 authorization-policy contexts to measure what an optimistic training verifier costs: the model learns to pad its answers instead of getting them right. The verifier's sufficiency proxy climbed to 0.940 while true faithfulness fell from 0.731 to 0.667, and the damage replicated across 9 of 10 configurations. (2 minute read)

## [Java4Shell: critical pre-auth RCE in OpenJDK's Base64 decoder](https://calif.io/java4shell/)

`headline` · hn

A memory-corruption bug in OpenJDK's AVX-512 Base64 intrinsic lets an unauthenticated attacker send 64 'A' characters plus '=' to trigger an out-of-bounds heap write, with a path to RCE (CVE-2026-114938, CVSS 9.2). The vendor confirmed working exploits against default Keycloak, Jira, Confluence, Jenkins, Kafka and Elasticsearch installs; Oracle patched it November 17. (2 minute read)

## [GPT-6.2 Astra and Sol launch, priced below prior generation](https://openai.com/index/introducing-gpt-6-2-astra-sol/)

`headline` · hn

GPT-6.2 Astra and Sol are now live in the API as gpt-6.2-astra and gpt-6.2-sol. Astra is priced 20% below GPT-6 Astra at $8/$40 per million tokens, with cached input cut to $0.40; Sol holds at $2/$10. Early testing puts Astra behind Claude Fable 5.2 on several benchmarks. (2 minute read)

## [Hijacked Kokoro TTS account shows weights can hide a backdoor](https://www.bleepingcomputer.com/news/security/researchers-hijack-hugging-face-account-for-popular-kokoro-ai-model/)

`discovery` · blog

Researchers took over the Hugging Face account behind Kokoro-82M, a text-to-speech model with about 13 million monthly downloads, by registering its lapsed donation domain to pass a password reset. As proof, they altered the model's weights in 87 seconds on a consumer GPU so its audio silently stopped matching the input text, undetected by malware scanners. (2 minute read)

## Also in the pool

- [Hugging Face and OpenRouter join forces to make open-weight models easy to run](https://huggingface.co/blog/openrouter) — blog
- [Optimizely compromised, served malware on Zoom, GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) — hn
- [CECAR: Cache & Expert Co-Aware Routing Accelerates On-Device Inference of MoE LLMs](https://arxiv.org/abs/2611.20119v1) — arxiv
- [Making Preemption Productive in Long-Output LLM Serving](https://arxiv.org/abs/2611.20106v1) — arxiv
- [How the Claude Code team thinks about verification](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/) — hn
- [When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents](https://arxiv.org/abs/2611.21577v1) — arxiv
- [Reading or Remembering? Measuring Temporal Contamination in Language Models](https://arxiv.org/abs/2611.21554v1) — arxiv
- [SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental Agents](https://arxiv.org/abs/2611.21541v1) — arxiv
- [Windows 11 is collecting data on which coding agents and developer tools you use](https://xusheng.dev/posts/windows-coding-agent-telemetry/) — hn
- [ScenarioForge: Resource-Grounded Generation and Execution Validation of Cyber Exercises](https://arxiv.org/abs/2611.21579v1) — arxiv
- [How Specification Explicitness Shapes Failure in LLM-Generated Code](https://arxiv.org/abs/2611.20195v1) — arxiv
- [HEAMS: Holistic Evaluation of Agent Memory Systems](https://arxiv.org/abs/2611.20144v1) — arxiv
- [Apple Tightens macOS App Permissions to Limit Data Access Amid AI Agent Security Risks](https://thehackernews.com/2026/11/apple-tightens-macos-app-permissions-to.html) — blog
- [MAI Code 2 and Code 2 Flash](https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/) — hn
- [What is the best harness for each model?](https://runta.com/blog/introducing-frontierharness-eval-v1-1/) — hn
- [Centered Ablation: Why Last-Layer Directional Ablation Under-Fires or Collapses, and a Closed-Form Fix](https://arxiv.org/abs/2611.20148v1) — arxiv
- [Can AI Judge You? An Empirical Audit of Deployment Readiness in LLM-assisted Hiring Systems](https://arxiv.org/abs/2611.20140v1) — arxiv
- [sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill) — github
- [Procedure without Judgment: What Small Language Models Learn under an Exact Verifier](https://arxiv.org/abs/2611.21529v1) — arxiv
- [Control Room: A central system to track and stop model workloads across our research infrastructure](https://openai.com/index/control-room) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-18.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
