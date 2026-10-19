---
name: Thread tracker
description: >-
  Use on the follow-up check to update vendor thread states and draft polite follow-ups for threads waiting on the vendor.
---
# Thread tracker
1. For each vendor thread in `/workspace/groklactic/runtime/clothing-brand/threads.jsonl`, check the mailbox (read-only search) for replies since last_touch.
2. Update the stage: rfq_drafted -> rfq_sent (only after the founder sent it) -> quoted -> countered -> sample_requested -> closed.
3. If the vendor hasn't replied in {{followup_after_days}} days, draft a short follow-up card (max 2 per vendor).
4. Report changes to Brand Chief of Staff. If nothing changed, send nothing.
