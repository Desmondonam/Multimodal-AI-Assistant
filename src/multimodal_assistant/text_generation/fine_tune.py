"""Fine-tuning entrypoint for the creative writing model.

See docs/modules/02_creative_writing.md, task 2.

Run this as a script once implemented: `python -m multimodal_assistant.text_generation.fine_tune`
"""

from pathlib import Path

from multimodal_assistant.config import settings


def prepare_dataset(dataset_name_or_path: str):
    """Load and tokenize the chosen corpus for causal language modeling.

    TODO:
        - Load via `datasets.load_dataset` (HF dataset) or a local corpus
        - Tokenize with the base model's tokenizer (settings.text_gen_base_model)
        - Return train/eval splits ready for a Trainer
    """
    raise NotImplementedError("TODO: implement prepare_dataset (Module 2)")


def fine_tune_model(
    dataset_name_or_path: str,
    output_dir: Path | None = None,
    use_lora: bool = False,
) -> Path:
    """Fine-tune settings.text_gen_base_model on the given corpus.

    Args:
        dataset_name_or_path: HF dataset name or local path.
        output_dir: where to save the resulting model/adapter. Defaults to
            settings.text_gen_model_dir.
        use_lora: if True, use `peft` LoRA instead of full fine-tuning
            (recommended for models larger than GPT-2).

    Returns:
        Path to the saved model/adapter.

    TODO:
        - Load base model + tokenizer
        - If use_lora, wrap the model with a peft LoraConfig
        - Train with `transformers.Trainer` (or a manual loop)
        - Save to output_dir and return it
    """
    raise NotImplementedError("TODO: implement fine_tune_model (Module 2)")


if __name__ == "__main__":
    fine_tune_model(dataset_name_or_path="TODO: your dataset")
