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

- Arxiv is now 0-for-18 across every sub-topic seen (serving/KV-cache,
  agent-safety research, benchmark critique, local-vs-frontier economics,
  robotics scaling laws), including both explicit downvotes (KV-cache
  sink-suppression, prefill/decode quantization splitting) — and those two
  land squarely on the inference-serving sub-topic Mine marks as
  always-surface. This overrides the Mine always-surface topics (inference
  infra, eval methodology) when the item is a bare arxiv listing — only
  surface arxiv work if it comes with a repo/running system, not the paper
  alone.
- The "Jev" decision-model wave is now 7-for-7 rejected follow-ons (Jevals,
  the JEV-vs-rubric-judges paper, Ollaya, Jevmem, NeoHorse,
  Microsoft-Decision-1, Strands Decider) against the single accepted
  breakout post that started it. Treat any new entrant in a category that
  already had its breakout story as a near-duplicate, not a fresh item,
  regardless of the specific number or framing it leads with.
- A separate "give an agent memory" tool wave is equally dead: Jevmem
  (counted above too), SodaMem, and agent-memory were all ignored despite
  each claiming its own differentiator (accuracy number, determinism,
  cross-tool sharing). Same rule as above — a new memory-tool entrant is a
  near-duplicate of an already-covered category.
- A lab's flagship/first-of-generation release still gets accepted (Opus
  5.5, GPT-6 Sol & Luna, Xiaomi MiMo v2.6), but same-family follow-ups keep
  losing out even when phrased as a launch: a point-release variant (GPT-6.1
  Sol), a tier rollout of the same number (Sonnet 5.5 going free-tier
  default, Claude Haiku 5.5's 90%-cheaper pricing), a single-spec headline on
  a relaunch (Gemini 4 Argon's context-length bump, posted twice), a
  pricing-mechanic tweak (GPT-6's 90%-off prompt caching), a UI rollout
  (GPT-6's "Intelligent UI"), and bolted-on feature demos (GPT-6 Astra
  driving a car, Gemini 3.8 TTS, bare tokens/sec claims).
- Vague or narrative agent-incident framing is 0-for-10 this round (agents
  "going rogue" or self-replicating, tampering with their own traces,
  "monitor evasion," containment/preemption research, classified
  risk-spending estimates, fragile misuse-detection safeguards). The one
  agent-incident story that was accepted named a concrete exploitable flaw
  ("Sandbox flaw lets rogue AI agents escape and leak data"). Keep skipping
  the hand-wavy framing and keep surfacing the PoC/CVE/measured-attack-rate
  version; Mine overrides this note.
