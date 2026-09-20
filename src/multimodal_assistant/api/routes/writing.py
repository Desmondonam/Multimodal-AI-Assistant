"""POST /write — creative text generation endpoint.

See docs/modules/04_fullstack.md, backend task 4.
"""

from fastapi import APIRouter, Depends

from multimodal_assistant.api.auth import get_current_subject
from multimodal_assistant.api.schemas import WriteRequest, WriteResponse

router = APIRouter(prefix="/write", tags=["writing"])


@router.post("", response_model=WriteResponse)
def write_text(request: WriteRequest, subject: str = Depends(get_current_subject)) -> WriteResponse:
    """Generate creative text variations using the Module 2 Generator.

    TODO:
        - Use a shared Generator instance (loaded once at app startup)
        - Return WriteResponse(variations=[...])
    """
    raise NotImplementedError("TODO: implement write_text (Module 4)")
