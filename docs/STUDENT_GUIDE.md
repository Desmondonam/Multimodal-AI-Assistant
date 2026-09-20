# Student Guide

## 1. Fork, Clone, and Configure

1. Click **Fork** on the course repository (top-right on GitHub).
2. Clone **your fork**, not the original:
   ```bash
   git clone https://github.com/<your-username>/Multimodal-AI-Assistant.git
   cd Multimodal-AI-Assistant
   ```
3. Track the course repo as `upstream` so you can pull updates/fixes:
   ```bash
   git remote add upstream https://github.com/DigiCrome-Academy/Multimodal-AI-Assistant.git
   git remote -v
   ```
4. Create your environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env             # fill in real keys/values
   ```
5. Verify the scaffold runs before changing anything:
   ```bash
   make test     # everything should currently be skipped, not failing
   make lint
   ```

## 2. Branching Strategy

Work module-by-module on feature branches off `main` in **your fork**:

```bash
git checkout -b module-1-rag
# ... implement, commit ...
git push origin module-1-rag
# open a PR: module-1-rag -> main (within your own fork)
```

Suggested branch names: `module-1-rag`, `module-2-text-gen`, `module-3-image-gen`,
`module-4-fullstack`, `module-5-deployment`. Merge each into your fork's `main` once
its module's tests pass and its checklist (in the module doc) is complete.

## 3. How the Skeleton Is Organized

- Every function/class you need to implement has a `TODO` comment and raises
  `NotImplementedError` or returns a placeholder.
- Tests in `tests/` are written against the *expected* behavior and are marked
  `@pytest.mark.skip(reason="TODO: implement <X>")`. As you implement a piece of
  functionality, **remove its skip marker** and make the test pass — don't rewrite
  the test's expectations to fit broken code.
- Each module has a doc in `docs/modules/` with a numbered task list, "definition of
  done," and pointers to relevant files. Work through them in order — later modules
  depend on earlier ones (the API layer needs the RAG/text/image modules to exist).

## 4. Daily/Weekly Workflow

1. Read the current module's doc fully before writing code.
2. Implement one file/function at a time; run its corresponding test file, not the
   whole suite, while iterating (`pytest tests/test_rag/test_chunking.py -v`).
3. Run `make lint` before every commit.
4. Commit in small, logical units (see commit conventions below).
5. At the end of each week, update `docs/TIMELINE.md` with your actual progress vs.
   plan, and flag blockers in office hours / Slack.

## 5. Commit Conventions

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(rag): implement recursive chunking strategy
fix(api): correct rate-limit header on 429 response
test(image-gen): unskip prompt optimizer tests
docs(architecture): fill in final system diagram
chore(deps): pin diffusers to 0.30.0
```

## 6. Submission Checklist

- [ ] All module checklists in `docs/modules/*.md` are checked off
- [ ] `make test` — zero skipped, zero failed
- [ ] `make lint` — clean
- [ ] `docker compose up --build` works from a clean clone
- [ ] App deployed, public URL recorded in `docs/DEPLOYMENT_GUIDE.md`
- [ ] `docs/ARCHITECTURE.md`, `docs/API_REFERENCE.md`, `docs/DEPLOYMENT_GUIDE.md` fully written (no placeholders)
- [ ] Demo video recorded (8–10 min) and linked in the root `README.md`
- [ ] Presentation slides ready (15–20 min)
- [ ] Final PR opened from your last feature branch into your fork's `main`, tagged `ready-for-review`

## 7. Getting Help

- Office hours (2–3x/week) — bring specific errors/logs, not "it doesn't work"
- Course Slack/Discord channel for peer discussion
- Open a GitHub Issue on **your fork** to track your own bugs/TODOs if useful
