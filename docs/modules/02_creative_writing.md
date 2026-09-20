# Module 2 — Creative Writing System (Week 2–3)

## Goal

Fine-tune a text generation model (GPT-2 locally, or a parameter-efficient
fine-tune of a larger open model) on a domain-specific corpus of your choosing
(e.g. product descriptions, short stories, marketing copy), and build prompt
tooling around it with quality controls.

## Files You'll Touch

```
src/multimodal_assistant/text_generation/
├── fine_tune.py         # dataset prep + training loop (or PEFT/LoRA)
├── prompt_templates.py  # reusable, parameterized prompt templates
├── generator.py         # loads fine-tuned model, generates variations
└── evaluation.py        # automatic quality metrics for generated text

tests/test_text_generation/
└── test_generator.py
```

## Tasks

1. **Pick a corpus** — a HuggingFace dataset or your own domain corpus. Record
   your choice and reasoning in `docs/ARCHITECTURE.md`.
2. **Fine-tune** — implement `fine_tune_model()` in `fine_tune.py`:
   - Tokenize the corpus
   - Fine-tune GPT-2 (full fine-tune is fine for GPT-2's size) *or* use `peft`
     LoRA on a larger open model if you have GPU budget
   - Save the resulting model/adapter to `TEXT_GEN_MODEL_DIR`
3. **Prompt templates** — implement at least 3 parameterized templates in
   `prompt_templates.py` (e.g. `story_opening`, `product_blurb`,
   `social_post`), each accepting variables and a `style` parameter.
4. **Generator** — implement `Generator.generate()` in `generator.py`:
   - Load the fine-tuned model
   - Accept `prompt, style, temperature, top_p, num_variations, max_tokens`
   - Return `num_variations` distinct outputs (vary sampling params or seeds to
     ensure they're not near-duplicates)
5. **Evaluation pipeline** — implement `evaluate_generations()` in
   `evaluation.py`: at minimum, compute distinct-n (diversity), average length,
   and a repetition/degeneration check. Optionally add perplexity under the base
   model as a fluency proxy.
6. **Unskip and pass** all tests in `tests/test_text_generation/`.

## Definition of Done

- [ ] A fine-tuning run has actually executed and produced a saved model/adapter
      (not just prompting the base model)
- [ ] `Generator.generate(prompt, num_variations=3)` returns 3 meaningfully
      different outputs
- [ ] At least 3 prompt templates implemented and demonstrated
- [ ] `evaluate_generations()` produces a metrics report you can point to in your
      technical documentation
- [ ] All tests in `tests/test_text_generation/` pass (no skips)

## Evaluation Tips (worth 15% of final grade)

- Keep a before/after comparison (base model vs. fine-tuned) — this is the
  single most convincing artifact for your presentation
- Don't over-fit on a tiny corpus — watch for verbatim memorization in outputs
- Note training time/cost in `docs/ARCHITECTURE.md`; it's a real trade-off worth
  discussing
