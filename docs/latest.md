# Firehose — 2026-11-28

## [OpenAI agents: coding task success nearly doubles, serving code lags](https://openai.com/index/research-acceleration-jagged-frontier)

`headline` · blog

Autonomous success on 2-4 hour coding tasks rose from 23% to 46% between March and October, per OpenAI's internal tracking, with agent workdays per researcher up 11x. Agents still trail badly on harder work: 25% success writing inference/serving code and 29% building eval environments, versus 69% on communication tasks. Trust agents more for glue work, less for core systems code for now. (4 minute read)

## [RL training cuts multi-agent LLM token use 37%, boosts success 12x](https://huggingface.co/blog/training-swarms)

`discovery` · blog

A new RL recipe trains 4-agent LLM teams on a shared reward, taking a sorting task from 6.56% to 82.34% success over 75 update steps while cutting tokens per team 37%. A single trained attempt now hits 82.3% success in about 8,000 tokens, versus 37.5% at best-of-8 for an untrained team spending 103,000. The eval methodology — scoring by communication class, not just outcome — is as useful as the result itself. (4 minute read)

## [Notion's official MCP hides upsell prompts in agent context](https://www.reddit.com/r/ClaudeCode/comments/1y4qm5o/heads_up_if_you_wire_notions_official_mcp_into/)

`discovery` · hn

Notion's official MCP server reportedly injects a hidden instruction telling agents not to render its upsell link as a preview, so it slips past review, then has the agent tell users they need the paid plan once free queries run out. Commenters say the pattern is spreading — a DoorDash CLI already requires agents to resend the user's original prompt on every call. Read any MCP server's instructions before trusting them. (4 minute read)

## [CPU-only ternary inference engine hits 20 tok/s on 8GB RAM](https://github.com/opensetlabs/openset-llm)

`discovery` · github

openset-llm runs PrismML's ternary-quantized Qwen3.8-27B at 17-20 tok/s on an 8 vCPU, 8GB Ice Lake box with no GPU — 4.2x faster than ik\_llama.cpp and 5.9x faster than PrismML's own llama.cpp fork on the same hardware. New AVX-512 and AVX2 matmul kernels for the ternary format, plus speculative decoding via an unsloth multi-token-prediction head, do the work. A 27B model now runs usably on a basic cloud VM. (4 minute read)

## [Switzerland: AI agents drove 4 of 5 confirmed cyberattacks](https://thehackernews.com/2026/11/switzerland-confirms-ai-assisted.html)

`headline` · blog

Switzerland's NCSC says AI agents independently carried out 4 of 5 confirmed attacks it investigated, breaching 2 of 3 targeted critical-infrastructure operators. Italy and the UK confirmed the same trend and named the tools in use — ARTEX, CyberStrikeAI, PentAGI, and DeepSeek Harness — pointing to ARTEX's October 22 breach of the European Commission's HR and medical systems. Publicly reachable AI attack tools have nearly doubled since then. (3 minute read)

## [Convex's Claude/Codex skill quietly phones home your app idea](https://github.com/convex/convex-backend-skill/issues/64)

`discovery` · hn

Convex's official quickstart skill for Claude and Codex POSTs the user's one-sentence app idea and template name to a Convex-run endpoint, logged internally as "a run started," with no disclosure to the user. A related skill splits a script download from its execution into two separate calls — its own code comment says a combined command is what harness safety classifiers block — then pipes the result into bash. A commenter confirmed the endpoint accepts arbitrary text and that an opt-out environment variable doesn't stop the calls. (4 minute read)

## [North Korea's PolinRider poisoned 7,600+ GitHub repos](https://thehackernews.com/2026/11/north-korea-linked-polinrider-poisons.html)

`headline` · blog

PolinRider, linked to North Korea, compromised 7,609 GitHub repositories across 2,330 accounts using stolen developer tokens to force-push commits that keep the original author, message, and date. A 58-line Python loader hidden in utility packages decodes an Ethereum transaction as JavaScript and runs it via Node to reach a command-and-control server. Blockchain records show activity dating back to February 2025, with 2,040 repos infected in a single ten-day wave in late October. (4 minute read)

## [Hackers breach US Air Force's Cloud One platform](https://www.reuters.com/world/hackers-breach-us-air-force-flagship-cloud-one-computing-platform-2026-11-27/)

`headline` · hn

Reuters reports hackers breached the US Air Force's flagship Cloud One computing platform, though the scope and method of the intrusion remain undisclosed. (1 minute read)

## Also in the pool

- [dllm-labs/mojo-dllm](https://github.com/dllm-labs/mojo-dllm) — github
- [OpenAI may be in cost control mode](https://micjm.com/blog/openai-is-in-cost-control-mode/) — hn
- [AI agents now control part of DeepMind's compute for Gemini experiments](https://the-decoder.com/ai-agents-now-control-part-of-deepminds-compute-for-gemini-experiments-but-recursive-self-improvement-remains-distant/) — hn
- [US Air Force's cloud computing platform hacked](https://news.sky.com/story/us-air-forces-cloud-computing-platform-hacked-13617163) — hn
- [US Air Force cloud platform reportedly hacked in latest federal breach](https://www.bleepingcomputer.com/news/security/us-air-force-cloud-platform-reportedly-hacked-in-latest-federal-breach/) — blog
- [SAP confirms security incident after suspicious GitHub activity](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/) — blog
- [Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html) — blog
- [Software giant SAP confirms cyber incident amid reports of source code breach](https://therecord.media/sap-germany-cyberattack-github) — blog
- [Token fraud is here and it’s BAD (YouTube)](https://simonwillison.net/2026/Nov/20/token-fraud-is-here-and-its-bad/) — blog
- [Unpatched Cacti zero-day with public PoC gives remote code execution](https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/) — blog
- [Tracking Diseases Cured by AI](https://diseasescuredbyai.com/) — hn
- [heterodoxin/AbliteratedOutTheBox](https://github.com/heterodoxin/AbliteratedOutTheBox) — github
- [DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin) — blog
- [AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting) — hn
- [Top-cited AI scientists at four US companies compared](https://topcitedscientists.com/figures/ai-at-four-us-companies/) — hn
- [Kimi for Science: More scientific ideas, made possible](https://www.kimi.ai/news/kimi-for-science-program) — hn
- [onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent) — github
- [HelixDB/helix-foundry](https://github.com/HelixDB/helix-foundry) — github
- [Fake paid expert interviews impersonate brands to steal Google logins](https://www.bleepingcomputer.com/news/apple/fake-paid-expert-interviews-impersonate-brands-to-steal-google-logins/) — blog
- [How OpenAI’s Performance Factory keeps ChatGPT fast](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast) — blog

---

[Web](https://ofirsiboni.github.io/firehose/2026-11-28.html) · [RSS](https://ofirsiboni.github.io/firehose/feed.xml)
