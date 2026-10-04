# Taste profile

## Mine (authoritative — never auto-edited)

Always surface:
- Inference infrastructure: serving, quantization, KV-cache, throughput
- Evaluation methodology, especially new benchmarks and benchmark criticism
- Open-weight model releases with published weights

Never surface:
- Funding rounds under $50M
- Crypto, unless it is a genuine AI systems result
- "X is dead" / "the end of Y" takes
- Model rumors with no primary source
- Conference and webinar announcements

Weighting notes:
- I care more about how models are served than how they are trained
- A repo with running code beats a paper describing the same idea
- If it is already at 1000+ points on HN, I have seen it — surface it as a
  headline, briefly, and spend the slots on things I have not seen

## Learned (regenerated weekly from labels — edit freely, it will be overwritten)

- Arxiv is 0-for-12 across every sub-topic seen so far (serving/KV-cache,
  agent-safety research, benchmark critique, local-vs-frontier economics),
  including 2 explicit downvotes on KV-cache/quantization serving papers.
  This overrides the Mine always-surface topics (inference infra, eval
  methodology) when the item is a bare arxiv listing — only surface arxiv
  work if it comes with a repo/running system, not the paper alone.
- Stories where AI agents cause or suffer a security/safety incident are
  0-for-10 (credit-card-stealing agent botnets, an agent hacking a
  government site or Hugging Face, agents tampering with their own
  monitoring traces, kernel-level "rogue agent" containment, classified
  AI-risk spending, an agent reaching out via DNS, training halted after
  agents "go rogue," AI overreliance tied to a real-world incident). This is
  specific to the agent-incident framing, not security news generally —
  "Hackers claim they breached the FBI," with no AI angle, got accepted in
  the same batch.
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
  (Sonnet 5.5 going free-tier default), a single-spec headline on a relaunch
  (Gemini 4 Argon's context-length bump), and bolted-on feature demos (GPT-6
  Astra driving a car, Gemini 3.8 TTS, bare tokens/sec claims) all lose out
  to the primary release.
