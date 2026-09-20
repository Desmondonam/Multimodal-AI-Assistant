# Timeline & Checkpoints

6-week capstone. Update the "Actual" column each Friday and bring blockers to office
hours before they cost you a week.

| Week | Module | Key Milestone | Check-in | Actual |
|---|---|---|---|---|
| 1 | RAG (part 1) | Ingestion + chunking + embeddings working; documents indexed in LanceDB | Mid-week 1-on-1 | |
| 2 | RAG (part 2) | Semantic search + LLM integration returns grounded, cited answers | End-of-module demo | |
| 2–3 | Creative Writing | Fine-tuning job completed; prompt templates + quality eval pipeline | Mid-week 1-on-1 | |
| 3 | Creative Writing (wrap) | Content variation controls; eval metrics recorded | End-of-module demo | |
| 3–4 | Image Generation | Text-to-image working end-to-end via diffusers | Mid-week 1-on-1 | |
| 4 | Image Generation (wrap) | Prompt optimization + inpainting/style transfer + queue | End-of-module demo | |
| 4–5 | Full-Stack: Backend | FastAPI endpoints, auth, rate limiting, async queueing, logging | Mid-week 1-on-1 | |
| 5 | Full-Stack: Frontend | Streamlit/Gradio UI hitting all 3 endpoints, responsive + error states | End-of-module demo | |
| 5–6 | Deployment & MLOps | Dockerized, deployed to cloud, CI/CD green, monitoring wired up | Mid-week 1-on-1 | |
| 6 | Wrap-up | Docs finalized, demo video recorded, presentation rehearsed | **Final submission** | |

## Weekly Check-in Format (bring to office hours)

1. What did you finish since last check-in? (link the PR/commits)
2. What's blocking you right now?
3. What's the plan for the next 3–4 days?
4. Any scope you want to cut or add?

## Mid-Month Review

Around week 3, do a full run-through: `make test`, `make lint`,
`docker compose up --build`. Fix regressions before moving to Module 3/4 — debugging
compounding issues in week 6 is the #1 cause of late submissions.

## End-of-Month / Peer Presentations

Short (5 min) informal demo to peers at the end of each module block. Practice
explaining *why* you made a design choice, not just *what* you built — this is also
rehearsal for the final presentation.
