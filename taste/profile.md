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

- Arxiv is now 0-for-20 across every sub-topic seen (serving/KV-cache,
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
  5.5, GPT-6 Sol & Luna, Xiaomi MiMo v2.6 — 3-for-3), but same-family
  follow-ups are now 13-for-13 ignored: point-release variants (GPT-6.1
  Sol), tier rollouts of the same number (Sonnet 5.5 going free-tier
  default, Claude Haiku 5.5's 90%-cheaper pricing), a relaunch posted twice
  (Gemini 4 Argon), a UI rollout (GPT-6's "Intelligent UI"), and how-tos or
  capability demos bolted onto an already-covered release (Gemini 3.8 TTS,
  Opus 5.5 porting the TypeScript compiler, Opus 5.5 flagging semiconductor
  candidates, a usage guide for Opus 5.5, Livenerf tracking Opus 5.5,
  Asana's GPT-6.1 Sol cost story).
- Even inside the AI x cyber lane, named-victim breach narratives reported
  after the fact with no PoC or primary technical source are ignored
  despite concrete numbers (Korean banks, 628K Ukrainian records, John
  Deere/SharkNinja, Hugging Face, Wikimedia's Etherpad, the Australian
  government hack) — same for vague safety-research framing with no
  concrete finding (agents "going rogue," self-replication claims,
  trace-tampering, monitor evasion, containment research, fragile
  misuse-detection safeguards). The one incident piece that landed named a
  specific exploitable flaw ("Sandbox flaw lets rogue AI agents escape and
  leak data") — a reproducible mechanism is what makes an incident
  PoC-grade, not a named victim or a scary verb.
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
