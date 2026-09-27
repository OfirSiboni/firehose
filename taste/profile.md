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

- Arxiv papers went 0-for-8 this week (2 explicit downvotes, 6 ignored); the
  2 downvotes and 1 of the ignores were all KV-cache/quantization papers with
  no released code — for arxiv specifically, treat "no code" as a hard pass,
  not a soft preference.
- Stories about AI agents committing or suffering security incidents (agents
  hacking a government site or Hugging Face, malicious-agent botnets,
  monitor-evasion and trace-tampering research, kernel-level "rogue agent"
  containment schemes, classified AI-risk spending) were ignored 8 for 8 this
  week, spanning both headline and discovery tiers and hn/blog/arxiv —
  deprioritize this angle even at headline tier unless it's a primary-source
  postmortem of the incident itself.
- Once a trend breaks as its own headline (this week: "Jev" decision
  models), follow-on posts rehashing the same trend (Jevals, JEV vs LLMs as
  rubric judges, Ollaya) get ignored — treat second-wave coverage of an
  already-surfaced trend as a near-duplicate rather than a fresh item.
- A genuinely new model launch (Opus 5.5, GPT-6 Sol/Luna, Xiaomi MiMo v2.6)
  gets accepted, but an incremental capability demo bolted onto an existing
  model (GPT-6 Astra driving a car, Gemini 3.8 TTS, a bare tokens/sec speed
  claim) gets ignored — weight new-model launches over feature/party-trick
  add-ons even from the same labs.
