---
name: Vendor search
description: >-
  Use to find manufacturers (cut-and-sew, knit/fleece), fabric mills, and trims suppliers for a product, with MOQ, price band, lead time, and certifications - every claim with a source URL.
---
# Vendor search
1. Inputs: product ({{product}}), fabric ({{fabric}}), target units ({{target_units}}), target FOB ({{target_fob_usd}}), region preference ({{region}}).
2. Search the web (directories, maker sites, trade-show lists, Reddit/forums for reviews). Prefer small-MOQ cut-and-sew for a first drop.
3. For each candidate, record: name, URL, location, product focus, MOQ (stated), price band (stated or 'unknown'), sample cost/lead time, production lead time, certifications (each with a link to the claim, else 'unverified'), contact route (business form/email from the site; no personal emails), source_urls[].
4. Never mark a vendor vetted. Status is one of `found` | `contacted` | `sampled` | `approved by founder`.
5. Write `/workspace/groklactic/runtime/clothing-brand/vendors.csv` (append). Return the top 3 with one-line reasoning to Brand Chief of Staff.
