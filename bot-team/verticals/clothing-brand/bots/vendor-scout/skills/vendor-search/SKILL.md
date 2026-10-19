---
name: Clothing · Vendor search
description: >-
  Use to find the right kind of vendor for the hero product (cut-and-sew factories, blank-garment suppliers, screen-print/DTG/embroidery or print-on-demand shops, mills, trims), with MOQ, price band, lead time, and certifications - every claim with a source URL.
---
# Vendor search
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
1. Inputs from the brand profile: product ({{hero_product}}), materials ({{materials}}), price band ({{price_band}}), region ({{city}} / {{region}}); plus target units ({{target_units}}) and target FOB ({{target_fob_usd}}).
2. Pick the vendor type from the product and materials: custom-fabric or premium garments -> cut-and-sew factories and mills; merch (tees, hoodies, totes, hats with a logo) -> blank suppliers plus screen-print / DTG / embroidery / print-on-demand shops (e.g. a traveling chess club's tee); accessories -> the matching maker. Search the web (directories, maker sites, trade-show lists, Reddit/forums for reviews). Prefer small-MOQ options for a first drop.
3. For each candidate, record: name, URL, location, product focus, MOQ (stated), price band (stated or 'unknown'), sample cost/lead time, production lead time, certifications (each with a link to the claim, else 'unverified'), contact route (business form/email from the site; no personal emails), source_urls[].
4. Never mark a vendor vetted. Status is one of `found` | `contacted` | `sampled` | `approved by founder`.
5. Write `$PKG/runtime/clothing-brand/vendors.csv` (append). Return the top 3 with one-line reasoning to Brand Chief of Staff.
