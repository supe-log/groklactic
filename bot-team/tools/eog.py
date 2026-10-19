"""Shared eye-of-grok text + TeamPlan export (contract from harness-types.ts @ e4d57fc)."""
CFG = "/workspace/groklactic/config/eye-of-grok.config.json"

def retro_body(org_id, runtime, seed, chat_name, cos_name, guard_range, example):
    return f"""
# Weekly retro (self-improvement loop)
Runs two ways, same steps: the paused weekly routine once the founder enables it, or ON DEMAND when the founder says **"Run the retro now"** in the {chat_name} chat. On demand, run it inline right away; no routine needs to be enabled.

Base URL is env `EYE_OF_GROK_BASE_URL`, default `http://localhost:3010` (see `{CFG}`). orgId = `{org_id}`. Writes send `Authorization: Bearer $EYE_OF_GROK_INGEST_TOKEN`; reference the env var and never print the token. localhost:3010 is the founder's Mac, so run the requests on the founder's registered desktop if the box cannot reach it.

## A. eye-of-grok path (preferred)
1. `POST /api/orgs/{org_id}/retro` returns `{{created, proposals[]}}`. Each proposal is `{{id, kind: add_rule|lower_autonomy|raise_autonomy|add_bot, botId, title, why, change, addsPowers, status}}`.
2. `GET /api/orgs/{org_id}/changes?status=open` and show the founder each open proposal: title, botId, why, change. Flag `addsPowers: true` in bold. Ask Approve / Reject for each.
3. Only after the founder's explicit answer, `POST /api/orgs/{org_id}/changes/{{{{changeId}}}}` with `{{"decision":"approved"}}` or `{{"decision":"rejected"}}`.
4. For each approved change, the owning bot's skill or instructions is updated in Grok Bot (UpdateSkill write, or UpdateAgent for instructions/rules), done or confirmed by {cos_name}. Then `POST /api/orgs/{org_id}/changes/{{{{changeId}}}}/applied`.
5. Mirror every step to `{runtime}/approvals.jsonl` (kind=rule_change) and the local log.

## B. Local fallback (eye-of-grok unreachable or the call fails)
1. Read `{runtime}/feedback.jsonl`. If it is empty, read `{seed}` and say you are using example seed data. Also read 7 days of `{runtime}/approvals.jsonl`.
2. Per bot: drafts, approved as-is, edited, rejected, 👍/👎, top thumbs-down reasons.
3. Pick ONE fix (the most common 👎 reason or the most-edited draft type). Write `{runtime}/retro/{{{{yyyy-mm-dd}}}}-proposal.md` in the same shape as an eye-of-grok proposal (`kind`, `botId`, `title`, `why`, `change`, `addsPowers`), with the change as a unified diff of the target SKILL.md or instructions.md.
   Example: {example}
4. Hold it for the founder (Approve / Edit / Reject via {cos_name}). Apply it only after a yes.

## Always
- Never apply a change without the founder's explicit approval. Never approve on the founder's behalf.
- Never propose a change that weakens a global guardrail ({guard_range}). Any proposal with `addsPowers: true` or `raise_autonomy` needs an extra explicit confirmation.
- Feedback you capture goes to `POST /api/orgs/{org_id}/feedback` with `{{botId, rating, tag, comment, source:"owner"}}`, and is also appended locally.
- Log one line: action=retro_proposed / retro_applied.
"""

def feedback_line(org_id):
    return f"`POST {{EYE_OF_GROK_BASE_URL}}/api/orgs/{org_id}/feedback` with `{{botId, rating:'up'|'down', tag?: great|wrong|slow|too_risky|missing, comment, source:'owner'}}` (Bearer $EYE_OF_GROK_INGEST_TOKEN)"

def teamplan(plan, m, autonomy, groups, intake_map):
    bots = []
    for b in plan["bots"]:
        bots.append({"id": b["slug"], "name": b["name"], "title": b["title"], "description": b["description"],
                     "rules": [f"{a['when']} -> {a['requires']}: {a['how']}" for a in b["approval_rules"]],
                     "autonomy": autonomy[b["slug"]],
                     "skills": [{"name": s["name"], "description": s["description"], "content": s["skill_md"]} for s in b["skills"]],
                     "routines": [{"name": r["name"], "slug": r["id"], "schedule": r["trigger"]["schedule"], "prompt": r["prompt"], "enabled": False} for r in b["routines"]]})
    ts = plan["generated_at"]
    return {"orgId": plan["business_id"], "version": 1, "createdAt": ts, "updatedAt": ts, "intake": intake_map,
            "chiefOfStaffId": plan["bots"][0]["slug"], "bots": bots, "groups": groups,
            "hardRules": [g["rule"] for g in plan["global_guardrails"]],
            "changelog": []}
