---
name: Clothing · PO draft
description: >-
  Use when the founder picks a vendor to draft a purchase order document. Draft only; the founder signs and pays.
---
# PO draft
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
Draft a PO from the agreed (founder-approved) quote: PO {{po_number}}, vendor, styles/colorways/sizes/qty, unit price, terms, ship date, incoterms, QC/acceptance, label specs. Watermark it DRAFT. Hand it to Brand Chief of Staff as kind=po. Deposits and payments: founder only; Stripe test mode only for any demo invoice.
