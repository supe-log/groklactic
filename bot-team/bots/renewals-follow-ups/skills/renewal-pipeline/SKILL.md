---
name: Renewal pipeline
description: >-
  Use on the daily renewal scan to list policies expiring in the renewal window and stage the right next touch for each.
---
# Renewal pipeline

1. Pull policies expiring in the next {{renewal_window_days}} days from the system of record (AMS export, sheet, or Drive folder). Read only.
2. For each, pick the stage by days-to-expiry: 90 = review needed, 60 = remarket decision (hand to Quote Prep if premium change > {{remarket_threshold_pct}}%), 30 = client touch, 14 = escalate to founder if unsigned, 0 = lapse risk alert.
3. Stage client touches as DraftExternalMessage cards using the renewal template with placeholders only ({{client_first_name}}, {{policy_type}}, {{expiration_date}}, {{agent_name}}).
4. Never state that coverage will continue, change, or be identical; route any "am I covered" question to the licensed agent.
5. Append a pipeline summary to `/workspace/groklactic/runtime/handoffs.jsonl` for Agency Chief of Staff and log E&O lines.
