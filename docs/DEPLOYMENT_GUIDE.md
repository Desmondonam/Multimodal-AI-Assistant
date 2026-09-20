# Deployment Guide

> **This is a graded deliverable.** Fill in the actual steps you followed for
> *your* deployment, including the exact commands and any gotchas. A reviewer
> should be able to redeploy from scratch using only this document.

## 1. Chosen Platform

_TODO: AWS / GCP / Azure / other — and why (cost, familiarity, GPU availability
for Stable Diffusion, etc.)._

## 2. Prerequisites

_TODO: cloud CLI installed & authenticated, container registry access, domain
(optional), secrets/API keys ready._

## 3. Containerization

This repo ships a `Dockerfile` and `docker-compose.yml`. Verify locally first:

```bash
docker compose up --build
curl http://localhost:8000/health
```

_TODO: note any changes you made to the Dockerfile/compose file for production
(e.g. multi-stage build, GPU base image for diffusion, separate worker service)._

## 4. Cloud Deployment Steps

_TODO: exact, reproducible steps. Example structure if using a container service:_

1. Build and tag the image: `docker build -t <registry>/<image>:<tag> .`
2. Push to registry: `docker push <registry>/<image>:<tag>`
3. Provision the service (e.g. AWS ECS/Fargate, GCP Cloud Run, Azure Container Apps)
4. Configure environment variables/secrets in the platform (mirror `.env.example`)
5. Point DNS / note the public URL
6. Verify: `curl https://<your-url>/health`

## 5. Kubernetes (optional, advanced)

If you used the manifests in `k8s/`, document:

- Cluster provisioning (EKS/GKE/AKS or local kind/minikube for demo)
- `kubectl apply -f k8s/`
- How secrets are injected (`kubectl create secret ...` vs. a secrets manager)
- How you exposed the service (LoadBalancer/Ingress)

## 6. CI/CD

_TODO: describe what `.github/workflows/ci.yml` does and, if you extended
`docker-build.yml` to push images automatically, describe that pipeline and what
triggers a deploy (push to `main`? a tag?)._

## 7. Monitoring & Logging

_TODO: what you wired up — e.g. `loguru` structured logs shipped where,
`prometheus-client` metrics scraped by what, any uptime/alerting._

## 8. Rollback Plan

_TODO: how do you revert to a previous known-good version if a deploy breaks
production?_

## 9. Live URL

- **Application**: `TODO`
- **API docs (Swagger)**: `TODO/docs`

## 10. Known Limitations

_TODO: cost constraints (e.g. CPU-only inference, no GPU budget), cold-start
latency, anything you'd fix with more time/budget._
