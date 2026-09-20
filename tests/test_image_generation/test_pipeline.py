"""Tests for Module 3. Remove @pytest.mark.skip as you implement each piece.

The real diffusion generation test is marked `slow` (loads a real model).
"""

import pytest

from multimodal_assistant.image_generation.prompt_optimizer import optimize_prompt
from multimodal_assistant.image_generation.queue_manager import JobStatus, QueueManager


@pytest.mark.skip(reason="TODO: implement optimize_prompt (Module 3)")
def test_optimize_prompt_adds_quality_modifiers():
    result = optimize_prompt("a cat in a garden")
    assert "cat in a garden" in result
    assert len(result) > len("a cat in a garden")


@pytest.mark.skip(reason="TODO: implement optimize_prompt (Module 3)")
def test_optimize_prompt_is_idempotent_on_modifiers():
    once = optimize_prompt("a cat in a garden")
    twice = optimize_prompt(once)
    # applying quality modifiers twice shouldn't duplicate them endlessly
    assert twice.count("detailed") <= 1


@pytest.mark.skip(reason="TODO: implement QueueManager (Module 3)")
def test_queue_lifecycle():
    queue = QueueManager()
    job_id = queue.enqueue(prompt="a sunset over mountains")
    assert isinstance(job_id, str)
    status = queue.get_status(job_id)
    assert status in (JobStatus.QUEUED, JobStatus.PROCESSING, JobStatus.DONE)


@pytest.mark.slow
@pytest.mark.skip(reason="TODO: implement TextToImagePipeline (Module 3)")
def test_generate_returns_image():
    from PIL import Image

    from multimodal_assistant.image_generation.diffusion_pipeline import TextToImagePipeline

    pipeline = TextToImagePipeline()
    image = pipeline.generate("a small red boat on a calm lake", num_inference_steps=5)
    assert isinstance(image, Image.Image)
