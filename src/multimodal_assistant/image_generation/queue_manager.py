"""Job queue for scalable, non-blocking image generation.

See docs/modules/03_image_generation.md, task 4.

A simple Redis-backed (or in-process, for local dev) queue is sufficient.
Celery + the `worker` service stub in docker-compose.yml is a bonus path.
"""

from enum import Enum


class JobStatus(str, Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"


class QueueManager:
    """Enqueue image-generation jobs and poll their status/result.

    TODO:
        - Choose a backend (in-process dict for local dev is acceptable to
          start; Redis for anything resembling production)
        - enqueue() should return immediately with a job_id; the actual
          generation happens in a background task/worker, not inline
    """

    def __init__(self, redis_url: str | None = None) -> None:
        raise NotImplementedError("TODO: implement QueueManager.__init__ (Module 3)")

    def enqueue(self, prompt: str, **generation_kwargs) -> str:
        """Queue a new image generation job. Returns a job_id."""
        raise NotImplementedError("TODO: implement enqueue (Module 3)")

    def get_status(self, job_id: str) -> JobStatus:
        raise NotImplementedError("TODO: implement get_status (Module 3)")

    def get_result(self, job_id: str) -> str | None:
        """Return the image URL/path once done, else None."""
        raise NotImplementedError("TODO: implement get_result (Module 3)")
