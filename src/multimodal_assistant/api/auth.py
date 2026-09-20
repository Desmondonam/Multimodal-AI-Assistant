"""JWT-based authentication for the API.

See docs/modules/04_fullstack.md, backend task 2.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from multimodal_assistant.config import settings

bearer_scheme = HTTPBearer()


def create_access_token(subject: str) -> str:
    """Create a signed JWT for `subject`, expiring after
    settings.jwt_expire_minutes.

    TODO: use python-jose (jwt.encode) with settings.jwt_secret_key /
    settings.jwt_algorithm and an `exp` claim.
    """
    raise NotImplementedError("TODO: implement create_access_token (Module 4)")


def verify_token(token: str) -> dict:
    """Decode and validate a JWT, returning its claims.

    Raises:
        HTTPException(401) if the token is invalid/expired.

    TODO: use python-jose (jwt.decode); catch JWTError and raise 401.
    """
    raise NotImplementedError("TODO: implement verify_token (Module 4)")


def get_current_subject(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> str:
    """FastAPI dependency: extracts and verifies the bearer token, returning
    the subject claim. Use as `Depends(get_current_subject)` on protected
    routes.
    """
    claims = verify_token(credentials.credentials)
    subject = claims.get("sub")
    if not subject:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return subject
