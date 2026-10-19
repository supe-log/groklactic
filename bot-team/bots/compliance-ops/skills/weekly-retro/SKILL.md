---
name: Weekly retro
description: >-
  Use on the weekly self-improvement retro (or when the founder asks 'what should we improve') to read approvals, feedback thumbs, and E&O logs, then propose ONE concrete improvement for founder approval.
---
# Weekly retro (self-improvement loop)
Runs two ways, same steps: the paused weekly routine once the founder enables it, or ON DEMAND when the founder says **"Run the retro now"** in the Compliance & Ops chat. On demand, run it inline right away; no routine needs to be enabled.

Base URL is env `EYE_OF_GROK_BASE_URL`, default `http://localhost:3010` (see `/workspace/groklactic/config/eye-of-grok.config.json`). orgId = `pecan-street-insurance-group`. Writes send `Authorization: Bearer $EYE_OF_GROK_INGEST_TOKEN`; reference the env var and never print the token. localhost:3010 is the founder's Mac, so run the requests on the founder's registered desktop if the box cannot reach it.

## A. eye-of-grok path (preferred)
1. `POST /api/orgs/pecan-street-insurance-group/retro` returns `{created, proposals[]}`. Each proposal is `{id, kind: add_rule|lower_autonomy|raise_autonomy|add_bot, botId, title, why, change, addsPowers, status}`.
2. `GET /api/orgs/pecan-street-insurance-group/changes?status=open` and show the founder each open proposal: title, botId, why, change. Flag `addsPowers: true` in bold. Ask Approve / Reject for each.
3. Only after the founder's explicit answer, `POST /api/orgs/pecan-street-insurance-group/changes/{{changeId}}` with `{"decision":"approved"}` or `{"decision":"rejected"}`.
4. For each approved change, the owning bot's skill or instructions is updated in Grok Bot (UpdateSkill write, or UpdateAgent for instructions/rules), done or confirmed by Agency Chief of Staff. Then `POST /api/orgs/pecan-street-insurance-group/changes/{{changeId}}/applied`.
5. Mirror every step to `/workspace/groklactic/runtime/approvals.jsonl` (kind=rule_change) and the local log.

## B. Local fallback (eye-of-grok unreachable or the call fails)
1. Read `/workspace/groklactic/runtime/feedback.jsonl`. If it is empty, read `/workspace/groklactic/examples/seed-feedback.jsonl` and say you are using example seed data. Also read 7 days of `/workspace/groklactic/runtime/approvals.jsonl`.
2. Per bot: drafts, approved as-is, edited, rejected, 👍/👎, top thumbs-down reasons.
3. Pick ONE fix (the most common 👎 reason or the most-edited draft type). Write `/workspace/groklactic/runtime/retro/{{yyyy-mm-dd}}-proposal.md` in the same shape as an eye-of-grok proposal (`kind`, `botId`, `title`, `why`, `change`, `addsPowers`), with the change as a unified diff of the target SKILL.md or instructions.md.
   Example: 2 of 3 COI thumbs-downs say the reply lacked a turnaround time -> kind=add_rule, botId=coi-desk: add to `bots/coi-desk/skills/coi-request/SKILL.md` step 5 the line 'State when the signed final certificate will be sent ({{coi_turnaround_hours}}h).'
4. Hold it for the founder (Approve / Edit / Reject via Agency Chief of Staff). Apply it only after a yes.

## Always
- Never apply a change without the founder's explicit approval. Never approve on the founder's behalf.
- Never propose a change that weakens a global guardrail (G1-G8). Any proposal with `addsPowers: true` or `raise_autonomy` needs an extra explicit confirmation.
- Feedback you capture goes to `POST /api/orgs/pecan-street-insurance-group/feedback` with `{botId, rating, tag, comment, source:"owner"}`, and is also appended locally.
- Log one line: action=retro_proposed / retro_applied.
