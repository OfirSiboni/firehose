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

- Arxiv is 0-for-14 across every sub-topic seen so far (serving/KV-cache,
  agent-safety research, benchmark critique, local-vs-frontier economics,
  robotics scaling laws), including both explicit downvotes (KV-cache
  sink-suppression, prefill/decode quantization splitting) — and those two
  land squarely on the inference-serving sub-topic Mine marks as
  always-surface. This overrides the Mine always-surface topics (inference
  infra, eval methodology) when the item is a bare arxiv listing — only
  surface arxiv work if it comes with a repo/running system, not the paper
  alone.
- Agent-incident stories (agents botnetting, "going rogue", tampering with
  traces, containment theater, classified risk spending) were 0-for-11 when
  they were vague or narrative. Operator now wants AI x cyber coverage: keep
  surfacing the concrete versions (working exploit, PoC repo, CVE, measured
  attack success rate, tooling you can run) and skip the hand-wavy "rogue
  agent" framing. Mine overrides this note.
- Second-wave coverage of an already-surfaced trend or product category
  gets ignored regardless of the specific number it claims: four more posts
  riding the "Jev" decision-model wave (Jevals, the JEV-vs-rubric-judges
  paper, Ollaya, NeoHorse) and three separate "agent gets memory" tools
  (Jevmem's 98.5% accuracy claim, SodaMem, agent-memory) were all ignored —
  treat a new entrant in a category that already had its breakout post as a
  near-duplicate, not a fresh item.
- A lab's flagship/first-of-generation release still gets accepted (Opus
  5.5, GPT-6 Sol & Luna, Xiaomi MiMo v2.6), but same-week follow-ups on that
  same model family get ignored even when phrased as a launch: a
  point-release variant (GPT-6.1 Sol), a tier rollout of the same number
  (Sonnet 5.5 going free-tier default, Claude Haiku 5.5's price cut), a
  single-spec headline on a relaunch (Gemini 4 Argon's context-length bump),
  a pricing-mechanic tweak (GPT-6's 90%-off prompt caching), and bolted-on
  feature demos (GPT-6 Astra driving a car, Gemini 3.8 TTS, bare tokens/sec
  claims) all lose out to the primary release.
