# Module 5 — Deployment & MLOps (Week 5–6)

## Goal

Containerize the full system, deploy it to a public cloud, wire up CI/CD, and add
enough monitoring/logging that you could plausibly operate this in production.

## Files You'll Touch

```
Dockerfile
docker-compose.yml
.github/workflows/ci.yml           # already runs lint+test — keep it green
.github/workflows/docker-build.yml # template — extend for your registry/deploy
k8s/                                # optional, advanced
docs/DEPLOYMENT_GUIDE.md            # you fill this in (graded deliverable)
```

## Tasks

1. **Containerize** — confirm `docker compose up --build` runs the full stack
   (api + frontend + redis) from a clean clone. Adjust the `Dockerfile` if your
   dependencies need more system packages (e.g. GPU base image).
2. **Choose a cloud target** — AWS (ECS/Fargate, App Runner, EC2), GCP (Cloud
   Run, GKE), or Azure (Container Apps, AKS). Pick based on free-tier
   availability and whether you need GPU for Module 3.
3. **CI** — `.github/workflows/ci.yml` already lints and tests on every push;
   make sure it stays green as you finish Modules 1–4.
4. **CD (at least manual, ideally automated)** — extend
   `.github/workflows/docker-build.yml` to build and push your image to a
   registry, and (bonus) trigger a deploy on push to `main`.
5. **Kubernetes (optional, advanced)** — if attempting this path, fill in
   `k8s/deployment.yaml` and `k8s/service.yaml` (Deployment + Service, resource
   limits, liveness/readiness probes hitting `/health`, secrets via
   `kubectl create secret` or your cloud's secrets manager).
6. **Monitoring & logging** — expose basic metrics via `prometheus-client`
   (request count, latency histogram, error rate) and confirm your structured
   logs (Module 4) are visible in your cloud provider's log viewer.
7. **Document everything** in `docs/DEPLOYMENT_GUIDE.md` — this is graded as
   much as the deployment itself; an undocumented deploy that disappears when
   your free-tier credits run out is worth less than a well-documented one.

## Definition of Done

- [ ] `docker compose up --build` works from a clean clone with no manual steps
      beyond `cp .env.example .env` + filling in secrets
- [ ] Application is deployed and reachable at a public URL
- [ ] CI is green on `main`
- [ ] Basic metrics/logging visible for the deployed instance
- [ ] `docs/DEPLOYMENT_GUIDE.md` fully written — no template placeholders
- [ ] Rollback steps documented and (ideally) tested once

## Evaluation Tips (worth 15% of final grade)

- Cloud free tiers vanish — take screenshots of your working deployment and the
  live URL for your technical documentation *before* it goes away
- If GPU cost is prohibitive, deploying with CPU-only inference and clearly
  documenting the trade-off is acceptable and honest — silently shipping a
  broken/timing-out image endpoint is not
- A small, working, well-documented deployment beats an ambitious Kubernetes
  setup you can't explain in the presentation
