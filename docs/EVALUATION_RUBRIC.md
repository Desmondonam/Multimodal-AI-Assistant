# Evaluation Rubric

Total = 100 points, weighted as below. Each component is scored 0–4 per band, then
scaled to its weight.

| Component | Weight | 4 — Excellent | 3 — Good | 2 — Adequate | 1 — Weak | 0 — Missing |
|---|---|---|---|---|---|---|
| **RAG Implementation** (20%) | Retrieval is fast, relevant, and cited; chunking strategy is justified; embeddings and reranking tuned | Retrieval mostly relevant; reasonable chunking; answers grounded most of the time | Basic RAG works but retrieval is noisy or answers occasionally ungrounded | RAG partially implemented or unreliable | Not implemented |
| **Text Generation** (15%) | Model genuinely fine-tuned with measurable quality gain; strong prompt templates; diversity controls work | Fine-tuning done, quality improvement present but modest | Only prompt engineering, no real fine-tuning, or fine-tuning present but unevaluated | Generation works but low quality/generic | Not implemented |
| **Image Generation** (15%) | Diffusion pipeline integrated with prompt optimization, editing (inpainting/style transfer), and a real queue | Diffusion pipeline works well with prompt optimization | Basic text-to-image works, no queue/editing | Image generation flaky or low quality | Not implemented |
| **System Architecture** (20%) | Clean layered design, typed, tested, handles errors/edge cases, scales (async/queueing) | Solid structure, decent error handling, mostly tested | Works but tightly coupled or thin error handling | Fragile, crashes on bad input | No coherent architecture |
| **Deployment** (15%) | Deployed to cloud, containerized, CI/CD green, monitoring/logging in place, documented | Deployed and containerized, partial monitoring/CI | Deployed but manual/undocumented steps | Runs only locally | Not deployed |
| **Innovation & Features** (10%) | Meaningful extra feature(s) beyond spec (e.g. streaming, multi-turn memory, evaluation dashboard) | One solid extra feature | Minor polish only | None | N/A |
| **Presentation & Docs** (5%) | Clear architecture explanation, honest about trade-offs, docs complete and readable | Clear demo, docs mostly complete | Demo works but documentation thin | Confusing or incomplete demo | Not delivered |

## Grading Formula

```
score = 0.20*RAG + 0.15*TextGen + 0.15*ImageGen + 0.20*Architecture
      + 0.15*Deployment + 0.10*Innovation + 0.05*Presentation
```
(each component's raw band 0–4 is divided by 4 before multiplying by its weight, i.e.
`weight * (band / 4) * 100`).

## Assessment Approach (secondary lens)

Cutting across the table above, instructors also weigh:

- Technical implementation — 40%
- Code quality and documentation — 20%
- Problem-solving approach — 15%
- Presentation and communication — 15%
- Innovation and creativity — 10%

## Automatic Disqualifiers

- Plagiarized code without attribution
- No working deployment (localhost-only submission)
- Test suite has skipped/failing tests at submission time
- Secrets committed to git history
