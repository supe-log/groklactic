---
name: Clothing · Landed cost / COGS
description: >-
  Use to compute landed cost and margin per SKU from quotes: FOB, freight, duty, packaging, fulfillment.
---
# Landed cost / COGS
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
For each style: FOB + freight/unit + duty (HTS {{hts_code}} rate, mark 'est.' until confirmed) + packaging + labels + fulfillment = landed. Margin = (retail - landed)/retail. Output a sheet in Drive or `$PKG/runtime/clothing-brand/landed-cost.csv`. Never invent quotes; use 'est.' bands.
