---
name: Insurance · Morning briefing
description: >-
  Use every weekday morning (or when the founder asks 'what's on today') to build a short agency briefing: approvals waiting, renewals due, COI requests open, quotes in progress, and anything a specialist bot escalated.
---
# Morning briefing

1. Read the shared queue files on the box: `$PKG/runtime/approvals.jsonl`, `$PKG/runtime/handoffs.jsonl`, `$PKG/runtime/eo-log.jsonl` (last 24h).
2. Check the founder's calendar for today (calendar connector) and list client meetings by time only with a {{client_ref}}, not full details.
3. Summarize in this order, max 12 lines:
   - Approvals waiting on the founder (count + oldest age).
   - COI requests open and any past the promised turnaround ({{coi_turnaround_hours}}h).
   - Renewals in the next {{renewal_window_days}} days without a contact attempt.
   - Quotes waiting on missing info.
   - Escalations: coverage/claim questions routed to the licensed agent.
4. End with the top 3 actions for the founder.
5. Log one E&O line: action=briefing_sent.

Never include client PII beyond a record reference. Result goes to the founder in this chat; if nothing is open, say "All clear" in one line.
