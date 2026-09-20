"""Tests for Module 4 API routes. Remove @pytest.mark.skip as you implement
create_app() and each route.

`app` is imported lazily inside each test (not at module scope) because
`multimodal_assistant.api.main` raises NotImplementedError at import time
until create_app() is implemented — importing it at collection time would
break collection for every other test file too.
"""

import pytest
from httpx import ASGITransport, AsyncClient


@pytest.mark.skip(reason="TODO: implement create_app + auth (Module 4)")
def test_health_check_is_public():
    from multimodal_assistant.api.main import app
    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.skip(reason="TODO: implement create_app + auth (Module 4)")
def test_qa_requires_auth():
    from multimodal_assistant.api.main import app
    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.post("/qa", json={"question": "hello?"})
    assert response.status_code == 401


@pytest.mark.skip(reason="TODO: implement create_app + auth + qa route (Module 4)")
def test_qa_rejects_empty_question():
    from multimodal_assistant.api.main import app
    from multimodal_assistant.api.auth import create_access_token
    from fastapi.testclient import TestClient

    client = TestClient(app)
    token = create_access_token(subject="test-user")
    response = client.post(
        "/qa",
        json={"question": ""},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 400


@pytest.mark.skip(reason="TODO: implement rate limiting (Module 4)")
@pytest.mark.asyncio
async def test_rate_limit_returns_429_when_exceeded():
    from multimodal_assistant.api.main import app
    from multimodal_assistant.api.auth import create_access_token
    from multimodal_assistant.config import settings

    token = create_access_token(subject="test-user")
    headers = {"Authorization": f"Bearer {token}"}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        responses = []
        for _ in range(settings.rate_limit_per_minute + 5):
            responses.append(await client.post("/write", json={"prompt": "hi"}, headers=headers))
        assert any(r.status_code == 429 for r in responses)
        limited = next(r for r in responses if r.status_code == 429)
        assert "retry-after" in {k.lower() for k in limited.headers.keys()}
