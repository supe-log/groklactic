---
name: Product mockups (Higgsfield)
description: >-
  Use to make product mockups, colorway variants, or mood-board images with the Higgsfield connector. Checks balance and cost first and holds results as proposals.
---
# Product mockups (Higgsfield) - VERIFIED steps
These calls were tested live on the authoring account on 2026-10-19 (each image took under 30s and cost 0.25 credits). Namespace `user-Higgsfield`. Look up the schema first with your dynamic-tool discovery.

1. **Balance**: `balance` with args `{}`. Note credits.
2. **Cost check**: `generate_image` with `{"params":{"model":"gpt_image_2_5","aspect_ratio":"1:1","prompt":"x","get_cost":true}}`. Multiply by the number of images. If the total is above the credit cap ({{credit_cap_per_run}}, default 50), or the run is a batch or video, stop and hand it to Brand Chief of Staff as `gen_spend` for approval.
3. **Generate** one image per call: `generate_image` with `{"params":{"model":"gpt_image_2_5","aspect_ratio":"1:1","count":1,"use_unlim":false,"prompt":"<product prompt>"}}`. This returns a job id. No folder is needed.
4. **Wait**: `jobs_wait` with `{"jobs":[{"index":0,"job_id":"<id>"}],"timeout_seconds":15}`. Repeat until done, then download `result_url` to `/workspace/groklactic/runtime/clothing-brand/design/`. If the transport times out, do NOT resubmit; reuse the job id.

Use `gpt_image_2_5` for clean wordmark text. Prompt pattern: "{{product}} in {{fabric}}, {{colorway}}, small '{{brand_wordmark}}' wordmark on the chest, minimalist studio product shot, soft natural light, no other logos or text."
- Only the brand's own wordmark. Never other brands' logos, marks, or signature prints (G6).
- Save results as **proposals**: append to `/workspace/groklactic/runtime/clothing-brand/approvals.jsonl` (kind=design_proposal) with the file paths. Nothing is final or public until the founder picks.
- Optional follow-ups, each one still under the cap: `upscale_image` or `remove_background` on the chosen image. Use `reframe` or `outpaint_image` for other ratios.
