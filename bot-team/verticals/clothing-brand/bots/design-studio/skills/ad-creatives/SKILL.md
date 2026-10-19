---
name: Clothing · Ad creatives
description: >-
  Use to draft ad/lookbook creatives with Higgsfield Ads Studio or Marketing Studio. Always quote first; generation only after founder approval.
---
# Ad creatives
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
1. Quote with `ads_studio_quote` (same args as `ads_studio_generate`), or check `marketing_studio_v2_costs` first.
2. Hand the allocation and the credits to Brand Chief of Staff as `gen_spend`. Only after the founder approves, run `ads_studio_generate` or `marketing_studio_v2_create`. Batches always need approval.
3. Track the jobs with `ads_studio_run_progress` / `marketing_studio_v2_status`. Results stay proposals.
