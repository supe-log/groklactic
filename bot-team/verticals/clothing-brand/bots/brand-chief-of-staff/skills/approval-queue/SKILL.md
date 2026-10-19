---
name: Approval queue
description: >-
  Use whenever a specialist hands off something needing the founder's yes/no (outbound draft, spend, generation over cap, publish, PO, rule change) or the founder asks what is waiting.
---
# Approval queue
Queue file: `/workspace/groklactic/runtime/clothing-brand/approvals.jsonl` (id, ts, bot, kind=outbound|gen_spend|publish|po|deposit|price_commit|rule_change|routine, ref, summary, amount_usd, credits, status). Append-only.
1. Append `pending` on handoff. Present grouped by kind with amounts/credits.
2. Outbound items already have a DraftExternalMessage card; point to it, never send.
3. After the decision, append the status, notify the origin bot, and ask for a 👍/👎 + one-line reason -> append to `/workspace/groklactic/runtime/clothing-brand/feedback.jsonl` (and POST `/api/orgs/no-thought/feedback` with `{botId, rating, tag, comment, source:"owner"}` if reachable).
