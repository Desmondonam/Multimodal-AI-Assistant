# Module 4 — Full-Stack Development (Week 4–5)

## Goal

Expose Modules 1–3 through a real backend API with auth, rate limiting, and async
processing, and build a usable frontend on top of it.

## Files You'll Touch

```
src/multimodal_assistant/api/
├── main.py           # FastAPI app factory, middleware, router registration
├── auth.py           # JWT issuing/verification
├── rate_limit.py     # slowapi (or custom) rate limiting
├── schemas.py        # pydantic request/response models
├── logging_config.py # structured logging setup (loguru)
└── routes/
    ├── qa.py          # POST /qa      -> rag.retriever + rag.generator
    ├── writing.py      # POST /write   -> text_generation.generator
    └── image.py        # POST /image, GET /image/{job_id} -> image_generation

src/multimodal_assistant/frontend/
├── app.py             # Streamlit (or Gradio) entrypoint with 3 tabs/pages
└── components/        # shared UI helpers (result cards, error banners, etc.)

tests/test_api/
└── test_routes.py
```

## Backend Tasks

1. **App factory** — implement `create_app()` in `main.py`: register routers,
   CORS, exception handlers, `/health` endpoint, startup event to load
   models/vector store once (not per-request).
2. **Auth** — implement `create_access_token()` / `verify_token()` in `auth.py`
   (JWT). Protect the three modality endpoints with a dependency.
3. **Rate limiting** — implement limiting in `rate_limit.py` using
   `RATE_LIMIT_PER_MINUTE` from config; return a proper `429` with a
   `Retry-After` header.
4. **Routes**:
   - `qa.py`: validate input via `schemas.py`, call `Retriever` +
     `generate_answer`, return answer + sources
   - `writing.py`: call `text_generation.Generator`, return variations
   - `image.py`: `POST /image` enqueues via `QueueManager` and returns a
     `job_id` immediately; `GET /image/{job_id}` returns status/result
5. **Logging** — implement `logging_config.py` (loguru): structured JSON logs
   with request id, latency, status code for every request.
6. **Async processing** — make sure image generation truly doesn't block the
   event loop (background task / queue worker, not an inline blocking call in
   the request handler).

## Frontend Tasks

1. Build `app.py` with three sections: **Ask a Question**, **Write Something**,
   **Generate an Image** — each calling the corresponding backend endpoint via
   `FRONTEND_API_BASE_URL`.
2. Show loading states while waiting (especially for image polling).
3. Show clear error messages on 4xx/5xx (don't let raw tracebacks leak to the UI).
4. Basic responsive layout — usable on a laptop-width and a narrower window.

## Definition of Done

- [ ] `make api` serves working `/qa`, `/write`, `/image`, `/image/{job_id}`, `/health`
- [ ] Swagger UI at `/docs` accurately reflects request/response schemas
- [ ] Endpoints require a valid token; invalid/missing token returns `401`
- [ ] Exceeding the rate limit returns `429`
- [ ] `make frontend` launches a UI that exercises all 3 modalities against the
      running API
- [ ] Structured request logs are emitted for every call
- [ ] All tests in `tests/test_api/` pass (no skips)
- [ ] `docs/API_REFERENCE.md` fully documents the real endpoints

## Evaluation Tips (worth 20% of final grade — largest single component)

- Test error paths, not just the happy path: empty prompt, huge `top_k`,
  malformed JSON, expired token
- Use `httpx`'s `TestClient`/`AsyncClient` in `tests/test_api/` rather than
  hitting a live server
- Keep route handlers thin — business logic belongs in the `rag/`,
  `text_generation/`, `image_generation/` modules, not in `routes/*.py`
