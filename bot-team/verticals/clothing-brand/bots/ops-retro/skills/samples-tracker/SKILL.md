---
name: Clothing · Samples tracker
description: >-
  Use to track sample requests, costs, shipping, arrival, and fit/wear-test notes.
---
# Samples tracker
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
Keep `$PKG/runtime/clothing-brand/samples.csv` (append-only): vendor, style, requested_on, sample_cost (est.), paid (founder only), tracking ref, eta, arrived_on, fit notes, wear-test notes (wash, pilling, dry time: observed, not lab), decision. Flag late samples to Brand Chief of Staff.
