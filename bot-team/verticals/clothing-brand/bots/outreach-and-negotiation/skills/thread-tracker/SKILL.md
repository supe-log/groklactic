---
name: Clothing · Thread tracker
description: >-
  Use on the follow-up check to update vendor thread states and draft polite follow-ups for threads waiting on the vendor.
---
# Thread tracker
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
1. For each vendor thread in `$PKG/runtime/clothing-brand/threads.jsonl`, check the mailbox (read-only search) for replies since last_touch.
2. Update the stage: rfq_drafted -> rfq_sent (only after the founder sent it) -> quoted -> countered -> sample_requested -> closed.
3. If the vendor hasn't replied in {{followup_after_days}} days, draft a short follow-up card (max 2 per vendor).
4. Report changes to Brand Chief of Staff. If nothing changed, send nothing.
