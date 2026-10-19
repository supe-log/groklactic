---
name: Follow-up drafts
description: >-
  Use when a quote, renewal, document request, or signature is waiting on a client to stage a polite follow-up draft for founder approval.
---
# Follow-up drafts

1. Find open items older than {{followup_after_days}} days with no reply (sent-mail search + system of record).
2. Max {{max_followups}} follow-ups per item; after that, hand to the founder.
3. Write each follow-up as a DraftExternalMessage card: short, references the original ask, no new promises, no coverage language.
4. Log the draft in the E&O log and in `/workspace/groklactic/runtime/approvals.jsonl` via Agency Chief of Staff.
