"""FastAPI application factory.

See docs/modules/04_fullstack.md, backend task 1.
"""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Build and configure the FastAPI app.

    TODO:
        - Instantiate FastAPI(title="Multi-Modal AI Assistant")
        - Register routers from api/routes/{qa,writing,image}.py
        - Add CORS middleware (adjust allowed origins for your frontend)
        - Wire up rate_limit.build_limiter() and its exception handler
        - Add logging_config.log_requests_middleware
        - Add a startup event that loads heavy resources ONCE (embedding
          model, vector store connection, text/image generators) and stores
          them on app.state, rather than reloading per-request
        - Add global exception handlers so unhandled errors return a clean
          JSON error envelope (see docs/API_REFERENCE.md) instead of a raw
          traceback
    """
    raise NotImplementedError("TODO: implement create_app (Module 4)")


app = create_app()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
