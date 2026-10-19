---
name: Clothing · Approval queue
description: >-
  Use whenever a specialist hands off something needing the founder's yes/no (outbound draft, spend, generation over cap, publish, PO, rule change) or the founder asks what is waiting.
---
# Approval queue
**Read the brand profile first** (`$PKG/runtime/clothing-brand/brand-profile.json`; for business_id `no-thought` use the worked example `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json`). If it's missing, run Brand discovery via Brand Chief of Staff. Fill every {{brand_name}}, {{category}}, {{audience}}, {{city}}, {{aesthetic}}, {{palette}}, {{materials}}, {{hero_product}}, {{wordmark}} from it; never invent a value. `$PKG` = the package root (the repo's bot-team/ folder).
Queue file: `$PKG/runtime/clothing-brand/approvals.jsonl` (id, ts, bot, kind=outbound|gen_spend|publish|po|deposit|price_commit|rule_change|routine, ref, summary, amount_usd, credits, status). Append-only.
1. Append `pending` on handoff. Present grouped by kind with amounts/credits.
2. Outbound items already have a DraftExternalMessage card; point to it, never send.
3. After the decision, append the status, notify the origin bot, and ask for a 👍/👎 + one-line reason -> append to `$PKG/runtime/clothing-brand/feedback.jsonl` (and POST `/api/orgs/{{business_id}}/feedback` with `{botId, rating, tag, comment, source:"owner"}` if reachable).
