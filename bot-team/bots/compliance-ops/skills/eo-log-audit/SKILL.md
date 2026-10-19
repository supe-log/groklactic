---
name: Insurance · E&O log audit
description: >-
  Use on the daily E&O audit to check that every outbound draft, COI, and escalation has an approval and a log line, and that no PII leaked into logs or skills.
---
# E&O log audit

1. Cross-check `$PKG/runtime/approvals.jsonl` against `$PKG/runtime/eo-log.jsonl`: every approved outbound item must have a draft line and an approval line with approver.
2. Scan skills, routines, and logs for PII patterns (SSN, DOB, policy/claim numbers, full addresses, card numbers). Report locations only; never print the values. Append a remediation note; never delete.
3. Check for any auto-send, live Stripe object, delete, or coverage statement; any hit is a P1 to the founder.
4. Report to Agency Chief of Staff only when something fails.
