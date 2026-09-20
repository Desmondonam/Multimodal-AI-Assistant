"""Prompt optimization for higher-quality image generation.

See docs/modules/03_image_generation.md, task 2.
"""

DEFAULT_QUALITY_MODIFIERS = "highly detailed, sharp focus, professional, 4k"


def optimize_prompt(raw_prompt: str, use_llm_expansion: bool = False) -> str:
    """Rewrite/enrich a user's prompt for better diffusion output.

    Args:
        raw_prompt: the user's original, possibly terse, prompt.
        use_llm_expansion: if True, use the LLM (from Module 1's generator) to
            expand the prompt into a richer description before adding quality
            modifiers.

    Returns:
        The optimized prompt string.

    TODO:
        - At minimum, append style/quality modifiers (see
          DEFAULT_QUALITY_MODIFIERS) in a way that doesn't duplicate if already
          present
        - If use_llm_expansion, call an LLM to expand `raw_prompt` first
        - Keep a toggle so you can A/B compare optimized vs. raw output for
          your documentation
    """
    raise NotImplementedError("TODO: implement optimize_prompt (Module 3)")
