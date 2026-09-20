"""Structured request logging.

See docs/modules/04_fullstack.md, backend task 5.
"""

from loguru import logger

from multimodal_assistant.config import settings


def configure_logging() -> None:
    """Configure loguru sinks/format based on settings.log_level.

    TODO: set an appropriate sink (stdout is fine for containers), a
    structured (JSON) format including timestamp, level, and any bound
    context (request_id, latency_ms, status_code) attached per-request.
    """
    raise NotImplementedError("TODO: implement configure_logging (Module 4)")


async def log_requests_middleware(request, call_next):
    """FastAPI/Starlette middleware: logs method, path, status code, and
    latency for every request, with a unique request id.

    TODO:
        - Generate a request id (e.g. uuid4)
        - Time the call to call_next(request)
        - Log a single structured line per request via `logger`
    """
    raise NotImplementedError("TODO: implement log_requests_middleware (Module 4)")
