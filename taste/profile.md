# Taste profile

## Mine (authoritative — never auto-edited)

Always surface:
- Inference infrastructure: serving, quantization, KV-cache, throughput
- Evaluation methodology, especially new benchmarks and benchmark criticism
- Open-weight model releases with published weights
- AI x cybersecurity, with running code or a primary source: LLM-assisted
  vuln discovery and exploit dev, AI red-teaming tooling, prompt-injection and
  agent/MCP attack chains with a working PoC, model supply-chain compromise
  (malicious weights, poisoned packages), AI-driven malware and detection,
  SOC/IR automation, security benchmarks (CTF, CVE-repro, cyber evals)

Never surface:
- Funding rounds under $50M
- Crypto, unless it is a genuine AI systems result
- "X is dead" / "the end of Y" takes
- Model rumors with no primary source
- Conference and webinar announcements

Weighting notes:
- Target mix: roughly half of the daily picks should sit on the AI x cyber
  line (AI used for offense/defense, or AI systems as the attack surface).
  Pure-AI items still run, but need to be clearly stronger to take a slot.
  Pure-cyber with no AI angle (breaches, CVEs, ransomware) is fine as a
  headline only when it is large; otherwise it needs an AI/automation hook.
- I care more about how models are served than how they are trained
- A repo with running code beats a paper describing the same idea
- If it is already at 1000+ points on HN, I have seen it — surface it as a
  headline, briefly, and spend the slots on things I have not seen

## Learned (regenerated weekly from labels — edit freely, it will be overwritten)

- Arxiv is now 0-for-22 across every sub-topic seen (serving/KV-cache,
  agent-safety research, benchmark critique, local-vs-frontier economics,
  robotics scaling laws, cyber evals), including both explicit downvotes
  (KV-cache sink-suppression, prefill/decode quantization splitting) — and
  those two land squarely on the inference-serving sub-topic Mine marks as
  always-surface. This overrides the Mine always-surface topics (inference
  infra, eval methodology) when the item is a bare arxiv listing — only
  surface arxiv work if it comes with a repo/running system, not the paper
  alone.
- The "Jev" decision-model wave is 7-for-7 rejected follow-ons (Jevals, the
  JEV-vs-rubric-judges paper, Ollaya, Jevmem, NeoHorse, Microsoft-Decision-1,
  Strands Decider) against the single accepted breakout post that started
  it. Treat any new entrant in a category that already had its breakout
  story as a near-duplicate, not a fresh item, regardless of the specific
  number or framing it leads with.
- A separate "give an agent memory" tool wave is equally dead: Jevmem
  (counted above too), SodaMem, and agent-memory were all ignored despite
  each claiming its own differentiator (accuracy number, determinism,
  cross-tool sharing). Same rule as above — a new memory-tool entrant is a
  near-duplicate of an already-covered category.
- A lab's flagship/first-of-generation release still gets accepted (Opus
  5.5, GPT-6 Sol & Luna, Xiaomi MiMo v2.6 — 3-for-3), but repeat coverage of
  that same release is now 0-for-19 ignored: point-release variants (GPT-6.1
  Sol), tier rollouts of the same number (Sonnet 5.5 going free-tier
  default, Claude Haiku 5.5's 90%-cheaper pricing), a relaunch posted twice
  plus a later cyber-benchmark variant (Gemini 4 Argon, Gemini 4 Carbon), a
  UI rollout (GPT-6's "Intelligent UI"), and how-tos or capability demos
  bolted onto an already-covered release (Gemini 3.8 TTS, Opus 5.5 porting
  the TypeScript compiler, Opus 5.5 flagging semiconductor candidates, a
  usage guide for Opus 5.5, Livenerf tracking Opus 5.5, GPT-6's prompt-
  caching discount, Asana's GPT-6.1 Sol cost story) — and, new this round,
  the same open-weight flagship re-told from a different angle: Mistral
  Large 4 was posted three separate ways (plain spec, "~1T params" framing,
  cyber-benchmark framing) and Reflection's Beam twice, and every one of
  those five postings was ignored even though an open-weight flagship is a
  Mine always-surface topic. The rule is about the specific release being
  re-covered, not just "same model family" — only the first telling of any
  given release earns a slot.
- Legal and regulatory process stories about AI companies — lawsuits, court
  rulings, arrests, agency orders, and political appointments/export-control
  moves with no technical result attached — are 0-for-9 ignored (the
  Anthropic supply-chain-risk appeals ruling, unsealed OpenAI piracy briefs,
  the Jay Clayton Super Intelligence Force appointment, Anthropic's reported
  Claude-diary felony referral, an OpenAI engineer's arrest, DHS ordering
  agencies to rip out DeepSeek, Texas's suit against OpenAI and Altman,
  Stanford professors suing Anthropic, China's frontier AI export controls).
  Distinct from Mine's funding-round exclusion — this is the company (or AI
  policy generally) as legal/political subject, not a technology result, so
  skip it even when the names or numbers are big.
- Corporate-finance news about AI companies — funding rounds, M&A talk, IPO
  filings, revenue disclosures — is 0-for-5 ignored this round (Typesafe
  AI's $870M raise, Nvidia/Reflection AI acquisition talk, Anthropic's IPO
  filing, Anthropic's Q3 revenue, OpenAI's revenue shortfall) regardless of
  deal size. Extend Mine's sub-$50M funding exclusion: skip this category
  outright unless a genuine AI-systems result rides along with the dollar
  figure.
- Agent-product/runtime/harness launches are 0-for-11 ignored (OpenAI's
  Dots, ChatGPT Sites, Claude Duet, Docker's agent builder, DeepSeek Harness
  Desktop, OpenMausBot, Talorys, Microsoft's MXC, NVIDIA's OpenShell,
  Google's Harness2, the prompt-cache-hit-rate harness post) even when
  open-sourced or framed as a sandboxed runtime. "We shipped an agent
  product/harness" needs a concrete technical differentiator — a benchmark
  win, an exploit, a measured number — to land on its own.
