---
name: Clothing · Short video draft
description: >-
  Use to make a TikTok/Reels short with Higgsfield and stage it for TikTok as a draft the founder publishes.
---
# Short video draft
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
1. Video generation always needs founder approval (G4). Preflight with `generate_video` `get_cost:true`, using model `marketing_studio_video` for product ads, `aspect_ratio` '9:16', duration {{seconds}}. Hand the credits to Brand Chief of Staff as `gen_spend`.
2. After approval, generate, then wait with `jobs_wait`.
3. Stage it with `tiktok_accounts`, then `tiktok_prepare_publish` with mode `UPLOAD_TO_DRAFT` and media_type VIDEO, using the Higgsfield-hosted URL. Do not prefill privacy or disclosure unless the founder stated them. The founder submits the publish form. Never call `tiktok_publish`.
4. Photo posts must be JPEG/WebP; Higgsfield images are PNG, so convert first.
