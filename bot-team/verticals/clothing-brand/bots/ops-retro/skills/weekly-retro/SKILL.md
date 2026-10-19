---
name: Clothing · Weekly retro
description: >-
  Use on the weekly retro, or when the founder says 'Run the retro now', to read 👍/👎 feedback and approvals and propose ONE improvement as a diff to a bot's skill, held for founder approval.
---
# Weekly retro (self-improvement loop)
Runs two ways, same steps: the paused weekly routine once the founder enables it, or ON DEMAND when the founder says **"Run the retro now"** in the Ops & Retro chat. On demand, run it inline right away; no routine needs to be enabled.

Base URL is env `EYE_OF_GROK_BASE_URL`, default `http://localhost:3010` (see `$PKG/config/eye-of-grok.config.json`). orgId = `no-thought`. Writes send `Authorization: Bearer $EYE_OF_GROK_INGEST_TOKEN`; reference the env var and never print the token. localhost:3010 is the founder's Mac, so run the requests on the founder's registered desktop if the box cannot reach it.

## A. eye-of-grok path (preferred)
1. `POST /api/orgs/no-thought/retro` returns `{created, proposals[]}`. Each proposal is `{id, kind: add_rule|lower_autonomy|raise_autonomy|add_bot, botId, title, why, change, addsPowers, status}`.
2. `GET /api/orgs/no-thought/changes?status=open` and show the founder each open proposal: title, botId, why, change. Flag `addsPowers: true` in bold. Ask Approve / Reject for each.
3. Only after the founder's explicit answer, `POST /api/orgs/no-thought/changes/{{changeId}}` with `{"decision":"approved"}` or `{"decision":"rejected"}`.
4. For each approved change, the owning bot's skill or instructions is updated in Grok Bot (UpdateSkill write, or UpdateAgent for instructions/rules), done or confirmed by Brand Chief of Staff. Then `POST /api/orgs/no-thought/changes/{{changeId}}/applied`.
5. Mirror every step to `$PKG/runtime/clothing-brand/approvals.jsonl` (kind=rule_change) and the local log.

## B. Local fallback (eye-of-grok unreachable or the call fails)
1. Read `$PKG/runtime/clothing-brand/feedback.jsonl`. If it is empty, read `$PKG/verticals/clothing-brand/examples/seed-feedback.jsonl` and say you are using example seed data. Also read 7 days of `$PKG/runtime/clothing-brand/approvals.jsonl`.
2. Per bot: drafts, approved as-is, edited, rejected, 👍/👎, top thumbs-down reasons.
3. Pick ONE fix (the most common 👎 reason or the most-edited draft type). Write `$PKG/runtime/clothing-brand/retro/{{yyyy-mm-dd}}-proposal.md` in the same shape as an eye-of-grok proposal (`kind`, `botId`, `title`, `why`, `change`, `addsPowers`), with the change as a unified diff of the target SKILL.md or instructions.md.
   Example: thumbs-down on RFQ-0001, 'ask for the minimum order quantity up front' -> kind=add_rule, botId=outreach-and-negotiation: in `verticals/clothing-brand/bots/outreach-and-negotiation/skills/rfq-draft/SKILL.md` step 2, add as the FIRST ask line: '- First question: "What is your MOQ per style and per colorway for this item?"'
4. Hold it for the founder (Approve / Edit / Reject via Brand Chief of Staff). Apply it only after a yes.

## Always
- Never apply a change without the founder's explicit approval. Never approve on the founder's behalf.
- Never propose a change that weakens a global guardrail (G1-G10). Any proposal with `addsPowers: true` or `raise_autonomy` needs an extra explicit confirmation.
- Feedback you capture goes to `POST /api/orgs/no-thought/feedback` with `{botId, rating, tag, comment, source:"owner"}`, and is also appended locally.
- Log one line: action=retro_proposed / retro_applied.
