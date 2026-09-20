"""Rate limiting for the API.

See docs/modules/04_fullstack.md, backend task 3.

Recommended: use `slowapi` (a FastAPI-friendly wrapper around `limits`),
already in requirements.txt.
"""

from multimodal_assistant.config import settings


def build_limiter():
    """Construct and return a configured slowapi Limiter using
    settings.rate_limit_per_minute as the default limit, keyed by client IP
    (or by authenticated subject, if you want per-user limits).

    Wire this into api/main.py:
        - app.state.limiter = build_limiter()
        - app.add_exception_handler(RateLimitExceeded, _rate_limit_handler)
        - app.add_middleware(SlowAPIMiddleware)

    Ensure a 429 response includes a Retry-After header.
    """
    raise NotImplementedError("TODO: implement build_limiter (Module 4)")
