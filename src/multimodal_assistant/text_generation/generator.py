"""Loads the fine-tuned model and generates creative text variations.

See docs/modules/02_creative_writing.md, task 4.
"""

from multimodal_assistant.config import settings


class Generator:
    """Wraps a fine-tuned causal LM for creative text generation.

    TODO:
        - Load the model/tokenizer from settings.text_gen_model_dir in
          __init__ (fall back to settings.text_gen_base_model if no fine-tuned
          model exists yet, with a warning log)
    """

    def __init__(self, model_dir: str | None = None) -> None:
        self.model_dir = model_dir or settings.text_gen_model_dir
        raise NotImplementedError("TODO: implement Generator.__init__ (Module 2)")

    def generate(
        self,
        prompt: str,
        style: str = "neutral",
        max_tokens: int = 256,
        temperature: float = 0.9,
        top_p: float = 0.95,
        num_variations: int = 1,
    ) -> list[str]:
        """Generate `num_variations` distinct completions for `prompt`.

        TODO:
            - Vary the sampling seed/params per variation so outputs differ
              meaningfully (not near-duplicates)
            - Post-process to strip the echoed prompt if the model includes it
        """
        raise NotImplementedError("TODO: implement Generator.generate (Module 2)")
