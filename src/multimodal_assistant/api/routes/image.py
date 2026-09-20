"""POST /image and GET /image/{job_id} — text-to-image generation endpoints.

See docs/modules/04_fullstack.md, backend task 4.
"""

from fastapi import APIRouter, Depends, HTTPException

from multimodal_assistant.api.auth import get_current_subject
from multimodal_assistant.api.schemas import ImageJobResponse, ImageRequest, ImageStatusResponse

router = APIRouter(prefix="/image", tags=["image"])


@router.post("", response_model=ImageJobResponse)
def create_image_job(
    request: ImageRequest, subject: str = Depends(get_current_subject)
) -> ImageJobResponse:
    """Enqueue an image generation job via QueueManager (Module 3) and return
    immediately with a job_id — this must NOT block on the actual generation.

    TODO: call a shared QueueManager.enqueue(...) instance.
    """
    raise NotImplementedError("TODO: implement create_image_job (Module 4)")


@router.get("/{job_id}", response_model=ImageStatusResponse)
def get_image_job(job_id: str, subject: str = Depends(get_current_subject)) -> ImageStatusResponse:
    """Return the current status (and result URL, if done) for `job_id`.

    TODO: call QueueManager.get_status / get_result; raise HTTPException(404)
    if job_id is unknown.
    """
    raise NotImplementedError("TODO: implement get_image_job (Module 4)")
