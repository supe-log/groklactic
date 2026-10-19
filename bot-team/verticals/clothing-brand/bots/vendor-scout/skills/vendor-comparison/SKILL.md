---
name: Clothing · Vendor comparison
description: >-
  Use when 2+ vendor quotes or candidates exist to build a side-by-side comparison (MOQ, unit price, landed estimate, lead time, certs, risks).
---
# Vendor comparison
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
Build a table from `$PKG/runtime/clothing-brand/vendors.csv` and `$PKG/runtime/clothing-brand/threads.jsonl` in Drive/Notion, or as a local CSV. Columns: vendor, MOQ, unit price, sample cost, lead time, est. landed cost (from Ops & Retro), certs (verified/unverified + URL), communication score, risks. Mark every unquoted number 'est.'. It is a recommendation input only; the founder chooses.
