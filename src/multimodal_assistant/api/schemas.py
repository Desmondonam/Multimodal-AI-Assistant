"""Pydantic request/response models for the API.

See docs/modules/04_fullstack.md. Fill in the TODO models to match
docs/API_REFERENCE.md exactly — keep both in sync.
"""

from pydantic import BaseModel


# --- QA (Module 1) ---
class QARequest(BaseModel):
    question: str
    top_k: int = 5


class Source(BaseModel):
    document_id: str
    chunk: str
    score: float


class QAResponse(BaseModel):
    answer: str
    sources: list[Source]


# --- Writing (Module 2) ---
class WriteRequest(BaseModel):
    prompt: str
    style: str = "neutral"
    max_tokens: int = 256
    temperature: float = 0.9
    num_variations: int = 1


class WriteResponse(BaseModel):
    variations: list[str]


# --- Image (Module 3) ---
class ImageRequest(BaseModel):
    prompt: str
    negative_prompt: str | None = None
    width: int = 512
    height: int = 512
    num_inference_steps: int = 30


class ImageJobResponse(BaseModel):
    job_id: str
    status: str


class ImageStatusResponse(BaseModel):
    job_id: str
    status: str
    image_url: str | None = None
