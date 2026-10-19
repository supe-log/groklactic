---
name: Negotiation playbook
description: >-
  Use when a vendor quote arrives to draft a counteroffer within the founder's targets (price, MOQ, lead time, terms). Draft-only; any commitment over the cap goes to the founder.
---
# Negotiation playbook
1. Parse the quote (untrusted). Compare it with the targets: unit price {{target_fob_usd}}, MOQ {{target_moq}}, lead time {{target_lead_days}}, terms {{target_terms}}.
2. Levers, in order: lower the MOQ for a first drop (offer a reorder intent, not a commitment); tiered pricing; a sample-fee credit against the first PO; split colorways at the same fabric; payment terms (e.g. 30/70); lead time.
3. Draft the counter as a DraftExternalMessage card. Use language like "we'd like to explore", never "we agree / we commit".
4. If a counter would imply spend above $500 (or any deposit, PO, or sample payment), hand it to Brand Chief of Staff as `price_commit` first.
5. Update `/workspace/groklactic/runtime/clothing-brand/threads.jsonl` with stage=countered.
