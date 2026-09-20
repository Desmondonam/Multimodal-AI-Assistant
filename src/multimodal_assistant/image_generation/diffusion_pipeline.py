"""Stable Diffusion text-to-image pipeline wrapper.

See docs/modules/03_image_generation.md, task 1.
"""

from PIL import Image

from multimodal_assistant.config import settings


class TextToImagePipeline:
    """Wraps diffusers.StableDiffusionPipeline (or a hosted API fallback).

    TODO:
        - Load settings.stable_diffusion_model_id via
          diffusers.StableDiffusionPipeline.from_pretrained in __init__
        - Detect CUDA availability; fall back to CPU with a logged warning
          and reduced defaults (fewer steps / smaller resolution) if no GPU
        - If settings.image_gen_provider == "dalle", implement an alternate
          code path calling the DALL-E API behind the same generate() signature
    """

    def __init__(self, model_id: str | None = None) -> None:
        self.model_id = model_id or settings.stable_diffusion_model_id
        raise NotImplementedError("TODO: implement TextToImagePipeline.__init__ (Module 3)")

    def generate(
        self,
        prompt: str,
        negative_prompt: str | None = None,
        width: int = 512,
        height: int = 512,
        num_inference_steps: int = 30,
    ) -> Image.Image:
        """Generate a single image from a text prompt.

        TODO: run the pipeline and return a PIL.Image.
        """
        raise NotImplementedError("TODO: implement TextToImagePipeline.generate (Module 3)")
