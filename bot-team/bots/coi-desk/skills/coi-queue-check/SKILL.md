---
name: Insurance · COI queue check
description: >-
  Use on the scheduled COI queue check to find COI requests not yet drafted or past the promised turnaround.
---
# COI queue check

1. Find inbox items labeled `grok/coi` without a matching line in `$PKG/runtime/approvals.jsonl`.
2. Run the COI request skill for each.
3. Flag to Agency Chief of Staff any pending COI older than {{coi_turnaround_hours}} hours.
4. If nothing is open, report nothing.
