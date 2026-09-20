"""POST /qa — retrieval-augmented question answering endpoint.

See docs/modules/04_fullstack.md, backend task 4.
"""

from fastapi import APIRouter, Depends

from multimodal_assistant.api.auth import get_current_subject
from multimodal_assistant.api.schemas import QARequest, QAResponse

router = APIRouter(prefix="/qa", tags=["qa"])


@router.post("", response_model=QAResponse)
def ask_question(request: QARequest, subject: str = Depends(get_current_subject)) -> QAResponse:
    """Answer `request.question` using the RAG pipeline (Module 1).

    TODO:
        - Validate request.question is non-empty
        - Use a shared Retriever + generate_answer (loaded once at app
          startup, via app.state — don't reinstantiate per request)
        - Return QAResponse(answer=..., sources=...)
    """
    raise NotImplementedError("TODO: implement ask_question (Module 4)")
