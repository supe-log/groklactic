---
name: Approval queue
description: >-
  Use whenever a specialist bot hands off something that needs the founder's yes/no, or when the founder asks what is waiting on them.
---
# Approval queue

The approval queue is `/workspace/groklactic/runtime/approvals.jsonl` (one JSON object per line: id, ts, bot, kind, record_ref, summary, draft_card_ref, status=pending|approved|rejected|edited).

1. When a handoff arrives, append a `pending` line. Never edit old lines; append a new line with the new status.
2. Present pending items to the founder grouped by kind: outbound drafts, coverage escalations, payment actions, rule changes, routine enablement.
3. For outbound drafts, the specialist already raised a DraftExternalMessage card. Point the founder to it; never send it yourself.
4. After the founder decides, append the status line, notify the originating bot (handoff), and ask for a thumbs up/down with an optional one-line reason. Append that to `/workspace/groklactic/runtime/feedback.jsonl` and, if reachable, POST `/api/orgs/pecan-street-insurance-group/feedback` with `{botId, rating, tag, comment, source:"owner"}`.
5. Log the decision in the E&O log (approver = founder).
