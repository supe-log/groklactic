---
name: Clothing · Daily brand brief
description: >-
  Use each weekday morning or when the founder asks 'where are we' to summarize approvals waiting, design proposals, vendor threads, samples, and launch tasks.
---
# Daily brand brief
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
1. Read `$PKG/runtime/clothing-brand/approvals.jsonl`, `$PKG/runtime/clothing-brand/handoffs.jsonl`, `$PKG/runtime/clothing-brand/threads.jsonl`, `$PKG/runtime/clothing-brand/samples.csv` (if present).
2. Max 10 lines: approvals waiting (count, oldest), design proposals awaiting a pick, vendor threads waiting on us vs them, samples in transit/late, launch tasks due this week, Higgsfield credits left (`balance`, read-only).
3. End with the top 3 founder decisions. Result goes to the founder in this chat; nothing open = "All clear".
