# Module 3 — Image Generation Integration (Week 3–4)

## Goal

Integrate Stable Diffusion (via HuggingFace `diffusers`) for text-to-image
generation, add prompt optimization, basic editing (inpainting or style
transfer), and a queue so image jobs don't block the API.

## Files You'll Touch

```
src/multimodal_assistant/image_generation/
├── diffusion_pipeline.py  # loads and runs the Stable Diffusion pipeline
├── prompt_optimizer.py    # rewrites/enriches user prompts for better output
├── editing.py             # inpainting and/or style transfer
└── queue_manager.py       # job queue: enqueue, poll status, fetch result

tests/test_image_generation/
└── test_pipeline.py
```

## Tasks

1. **Diffusion pipeline** — implement `TextToImagePipeline` in
   `diffusion_pipeline.py`:
   - Load `stabilityai/stable-diffusion-2-1` via `diffusers.StableDiffusionPipeline`
   - `generate(prompt, negative_prompt, width, height, num_inference_steps) -> PIL.Image`
   - Handle CPU-only fallback for students without a GPU (lower steps/resolution
     with a clear warning log), or use a hosted API (DALL·E) as an alternative
     path behind the same interface
2. **Prompt optimization** — implement `optimize_prompt()` in
   `prompt_optimizer.py`: append quality/style modifiers, optionally use the LLM
   from Module 1 to expand a terse user prompt into a richer one. Make this
   toggleable so you can A/B compare.
3. **Editing** — implement at least one of:
   - `inpaint(image, mask, prompt)` in `editing.py` using
     `StableDiffusionInpaintPipeline`
   - a style-transfer variant using img2img (`StableDiffusionImg2ImgPipeline`)
4. **Queue manager** — implement `QueueManager` in `queue_manager.py`:
   - `enqueue(job) -> job_id`
   - `get_status(job_id) -> "queued" | "processing" | "done" | "failed"`
   - `get_result(job_id) -> image_url | None`
   - Simple in-process/Redis-backed queue is fine; Celery is a bonus (compose
     service already stubbed in `docker-compose.yml`)
5. **Unskip and pass** all tests in `tests/test_image_generation/`.

## Definition of Done

- [ ] `TextToImagePipeline.generate(...)` produces a real image from a prompt
- [ ] `optimize_prompt()` demonstrably changes output quality (keep a before/after
      example for your docs)
- [ ] At least one editing capability (inpainting or style transfer) works
- [ ] Image generation is queued, not synchronous-blocking, in the API layer
      (this connects to Module 4)
- [ ] All tests in `tests/test_image_generation/` pass (no skips)

## Evaluation Tips (worth 15% of final grade)

- If you don't have GPU access, say so explicitly in `docs/ARCHITECTURE.md` and
  document your CPU/hosted-API fallback — that's a legitimate engineering
  trade-off, not a shortcut, as long as it's documented and working
- Keep generated sample images (a handful) in your technical documentation as
  evidence
- Think about cost/latency: how long does one generation take, and how does the
  queue keep the API responsive during that time?
