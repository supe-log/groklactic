---
name: Landed cost / COGS
description: >-
  Use to compute landed cost and margin per SKU from quotes: FOB, freight, duty, packaging, fulfillment.
---
# Landed cost / COGS
For each style: FOB + freight/unit + duty (HTS {{hts_code}} rate, mark 'est.' until confirmed) + packaging + labels + fulfillment = landed. Margin = (retail - landed)/retail. Output a sheet in Drive or `/workspace/groklactic/runtime/clothing-brand/landed-cost.csv`. Never invent quotes; use 'est.' bands.
