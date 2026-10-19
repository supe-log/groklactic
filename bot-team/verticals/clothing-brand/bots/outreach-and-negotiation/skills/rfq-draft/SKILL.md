---
name: Clothing · RFQ draft
description: >-
  Use to draft a request for quote (RFQ) to a vendor from a tech pack and vendor record. Always a DraftExternalMessage card held for the founder; never sends.
---
# RFQ draft
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
1. Inputs: vendor record (Vendor Scout), tech-pack outline (Design Studio), target units, target FOB, needed-by date.
2. Draft a short, professional email:
   - Intro: {{brand_name}}, {{category}} ({{what_they_sell}}), first drop of {{hero_product}}.
   - Product + fabric summary, attach or link the tech-pack outline.
   - Ask for: unit price at {{qty_tiers}}, sample cost and lead time, production lead time, MOQ, payment terms, fabric sourcing and certifications (with documents).
   - Close: "Happy to share more detail; looking forward to your quote."
3. Raise it as a DraftExternalMessage card to the vendor's business contact. Never send. Never state a price, MOQ, or volume as a commitment.
4. Append the thread state to `$PKG/runtime/clothing-brand/threads.jsonl`: vendor, ref, stage=rfq_drafted, last_touch, next_action. Hand it to Brand Chief of Staff (kind=outbound).
