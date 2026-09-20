"""Image editing capabilities: inpainting and/or style transfer.

See docs/modules/03_image_generation.md, task 3. Implement at least one.
"""

from PIL import Image


def inpaint(image: Image.Image, mask: Image.Image, prompt: str) -> Image.Image:
    """Fill the masked region of `image` according to `prompt`.

    TODO: use diffusers.StableDiffusionInpaintPipeline. `mask` should be a
    single-channel image where white = region to regenerate.
    """
    raise NotImplementedError("TODO: implement inpaint (Module 3)")


def style_transfer(image: Image.Image, prompt: str, strength: float = 0.6) -> Image.Image:
    """Restyle `image` towards `prompt` using img2img.

    TODO: use diffusers.StableDiffusionImg2ImgPipeline. `strength` controls
    how much the original image is preserved vs. transformed (0 = unchanged,
    1 = fully regenerated).
    """
    raise NotImplementedError("TODO: implement style_transfer (Module 3)")
