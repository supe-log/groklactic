---
name: Insurance · Handoff routing
description: >-
  Use when work arrives that belongs to a specialist bot, or when a specialist hands work back, to route it to the right bot with a minimal, PII-free handoff note.
---
# Handoff routing

Routing table:
- New email/lead/general request -> Intake & Inbox
- Certificate of insurance / additional insured / holder request -> COI Desk
- Renewal, X-date, expiring policy, follow-up -> Renewals & Follow-ups
- New quote or remarket request -> Quote Prep
- Audit, licensing, E&O, retro, process change -> Compliance & Ops
- Coverage, claim, binding, cancellation question -> licensed agent ({{licensed_agent_name}}) via founder approval queue. Never a bot.

Handoff note format (append to `$PKG/runtime/handoffs.jsonl` and message the target bot in Grok Bot):
`{"ts","from","to","kind","record_ref","ask","due","source_link"}` — record_ref and source_link point into the system of record; never paste PII.
