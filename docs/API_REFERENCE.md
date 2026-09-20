# API Reference

> **This is a graded deliverable.** Keep this in sync with your actual FastAPI
> routes in `src/multimodal_assistant/api/routes/`. FastAPI also auto-generates
> interactive docs at `/docs` (Swagger) and `/redoc` once the server is running —
> this file is the human-readable companion, and should explain *why*, not just
> restate the schema.

## Authentication

_TODO: describe your auth scheme (implemented in `api/auth.py`) — e.g. JWT bearer
tokens. Document how to obtain a token._

```
Authorization: Bearer <token>
```

## Rate Limiting

_TODO: document the limit(s) you configured in `api/rate_limit.py` (e.g. requests
per minute per API key/IP) and what a client receives when it's exceeded (status
code, headers, retry-after)._

## Endpoints

### `POST /qa` — Retrieval-Augmented Question Answering

_TODO: fill in once `api/routes/qa.py` is implemented._

**Request**
```json
{
  "question": "string",
  "top_k": 5
}
```

**Response**
```json
{
  "answer": "string",
  "sources": [
    {"document_id": "string", "chunk": "string", "score": 0.0}
  ]
}
```

**Errors**: `TODO` (e.g. 400 empty question, 429 rate-limited, 503 vector store unavailable)

---

### `POST /write` — Creative Text Generation

_TODO: fill in once `api/routes/writing.py` is implemented._

**Request**
```json
{
  "prompt": "string",
  "style": "string",
  "max_tokens": 256,
  "temperature": 0.9,
  "num_variations": 1
}
```

**Response**
```json
{
  "variations": ["string"]
}
```

---

### `POST /image` — Text-to-Image Generation

_TODO: fill in once `api/routes/image.py` is implemented._

**Request**
```json
{
  "prompt": "string",
  "negative_prompt": "string",
  "width": 512,
  "height": 512,
  "num_inference_steps": 30
}
```

**Response (sync)**
```json
{
  "job_id": "string",
  "status": "queued"
}
```

### `GET /image/{job_id}` — Poll Image Job Status

_TODO: fill in once `image_generation/queue_manager.py` is implemented._

**Response**
```json
{
  "job_id": "string",
  "status": "queued | processing | done | failed",
  "image_url": "string | null"
}
```

---

### `GET /health` — Health Check

**Response**
```json
{"status": "ok"}
```

## Error Format

_TODO: document your standard error envelope, e.g._
```json
{"error": {"code": "string", "message": "string"}}
```

## Changelog

_TODO: keep a short list of breaking API changes as you iterate._
