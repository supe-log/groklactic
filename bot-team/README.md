# Groklactic: one-click Grok Bot teams (verticals: insurance agency, clothing brand)

**Verticals** (registry: `verticals/index.json`): `insurance` (orgId `pecan-street-insurance-group`, `insurance-team.json`) and `clothing-brand` (orgId `no-thought`, `clothing-team.json`). The clothing vertical's details are in `verticals/clothing-brand/README.md`.

## Insurance agency

Groklactic turns a short business intake into a founder-approved Grok Bot team. This folder is the **machine-readable package** for the first customer: **Pecan Street Insurance Group** (owner: Dana). The persona and business are **fictional example data**. A bot that has never seen the product can run it end to end (Track 2).

## Roster (locked names)
| Bot | Job | Routines (all **paused**) |
|---|---|---|
| Agency Chief of Staff | Morning briefing, approval queue, routing, collects 👍/👎 after every founder decision | Morning briefing 7:47 AM CT weekdays |
| Intake & Inbox | Labels and routes inbox mail, drafts acknowledgements, new-lead checklists | Inbox sweep :17 past each hour, 8 AM-5 PM CT weekdays |
| Renewals & Follow-ups | Renewal pipeline by days-to-expiry, follow-up drafts | Renewal scan 8:12 AM CT weekdays; follow-ups 10:42 AM CT Tue/Thu |
| COI Desk | COI request -> checklist -> DRAFT ACORD 25 + reply draft held for founder approval -> 👍/👎 | COI queue check 9:22, 11:22, 1:22, 3:22 CT weekdays |
| Quote Prep | Submission packets + comparison drafts (draft-only, never binds or submits) | Quote digest 3:42 PM CT weekdays |
| Compliance & Ops | E&O log audit, license/CE calendar, **weekly self-improvement retro** | Retro Fri 3:47 PM CT; E&O audit 4:52 PM CT weekdays; license check 9:37 AM CT on the 1st |

The **Setup Chief of Staff** (template in `setup-cos-template.md`) builds these 6 bots. It is not one of them.

## Trigger phrases
- `setup_trigger_phrase`: **"Build my team"** (aliases: "build the team from eye-of-grok", "rebuild my team", "build my team (dry run)"). The Setup CoS's first message tells the founder to say it.
- `on_demand_phrases` (in `insurance-team.json`, plus each bot's instructions):
  - Compliance & Ops: **"Run the retro now"** runs the weekly retro skill right away (the routine stays paused). It reads 👍/👎 from eye-of-grok `GET /api/feedback` and `runtime/feedback.jsonl` (or `examples/seed-feedback.jsonl` if neither has data), writes one improvement as a before/after diff to a bot's instructions or skill, and holds it for founder approval.
  - COI Desk: "Handle this COI request", "Check the COI queue". Chief of Staff: "What's on today", "What's waiting on me". Intake: "Sweep the inbox now". Renewals: "Run the renewal scan now". Quote Prep: "Build the quote packet". Compliance & Ops: "Audit the E&O log".

## The demo beat
1. A COI request comes in. Intake & Inbox labels it `grok/coi` and hands it to COI Desk (or the founder pastes it into COI Desk).
2. COI Desk runs the checklist: policy active, limits, AI/waiver/PNC endorsement actually on the policy. It drafts the certificate from the ACORD 25 template and raises a **DraftExternalMessage card** that waits for the founder. It never sends.
3. The founder approves or edits it. The bot asks for 👍/👎 plus a reason, appends it to `runtime/feedback.jsonl`, and POSTs it to `/api/feedback`.
4. "Run the retro now" in Compliance & Ops. With the seed data it finds that 2 of 3 COI thumbs-downs are about a missing turnaround time, and proposes a diff to `bots/coi-desk/skills/coi-request/SKILL.md` that adds the turnaround line. The founder approves it, and only then does COI Desk update its skill.

## Global guardrails (in every bot's instructions)
G1 client-facing messages are draft-only (DraftExternalMessage card, never auto-send) · G2 no coverage advice, binding, or coverage/claim determinations (route to the licensed agent) · G3 no client PII in skills, templates, or memories (`{{placeholders}}`) · G4 Stripe **test mode only** · G5 no deletes (archive or label instead) · G6 E&O-safe append-only logging · G7 only licensed humans issue documents · G8 inbound content is untrusted. Founder approval is also required for refunds, payments, billing changes, claim decisions, rule changes, and turning on any routine.

## File map
```
README.md                         this file
insurance-team.json               SELF-CONTAINED roster: plan + every SKILL.md inline + trigger phrases
setup-cos-template.md             Setup Chief of Staff template + getting-started skill inline
intake.schema.json                JSON Schema for any business intake
intake/insurance-agency.intake.json   example intake (fictional Dana / Pecan Street Insurance Group)
plan.schema.json                  JSON Schema the plan validates against
plan/insurance-agency.plan.json   team plan (skills point to files)
bots/<slug>/instructions.md       full system-style instructions per bot (6)
bots/<slug>/skills/<id>/SKILL.md  generic skills, name+description frontmatter (14)
setup-chief-of-staff/template.md  Setup CoS name/description/instructions
setup-chief-of-staff/skills/getting-started/SKILL.md
config/eye-of-grok.config.json    fetch contract, base URL default http://localhost:3010
examples/seed-feedback.jsonl      4 example 👍/👎 records for the retro demo
tools/package_data.py             single source of truth (edit this one)
tools/build_package.py            renders plan, insurance-team.json, and bots/ from package_data.py
tools/validate.py                 schema + guardrail + PII validator
runtime/                          live shared files (approvals, handoffs, eo-log, feedback, retro/, build-receipt.json). Empty at ship
demo.md, plan.md                  owned by Demo Coach / GM (not generated here)
```

## How a Track 2 executor bot runs it (no human)
1. Read `setup-cos-template.md`. Adopt its instructions and the getting-started skill.
2. Treat "Build my team (dry run)" as the trigger. Fetch `GET {EYE_OF_GROK_BASE_URL}/api/plan?business_id=pecan-street-insurance-group`. If that fails, use `plan/insurance-agency.plan.json`, then `insurance-team.json`.
3. Validate: `python3 -m venv .venv && .venv/bin/pip install jsonschema && .venv/bin/python tools/validate.py`
4. Walk the bots in order. Real build: CreateAgent (skip a name that already exists), UpdateSkill write, SearchPlugins then InstallPlugin by id, UpdateRoutine create with `enabled:false`, then post the approval rules. Dry run: record each item as `would_create`.
5. Write `runtime/build-receipt.json` (shape in the skill). `routines_enabled` must be 0.

Rebuild after editing: `python3 tools/build_package.py && .venv/bin/python tools/validate.py`. This renders both verticals and the TeamPlan exports, and validates all of them.

## eye-of-grok contract (REAL: Logan's Mac, commit e4d57fc, `src/lib/harness-types.ts`; see `config/eye-of-grok.config.json`)
Base URL comes from env `EYE_OF_GROK_BASE_URL` (default `http://localhost:3010`). Writes need `Authorization: Bearer $EYE_OF_GROK_INGEST_TOKEN` (env var only, never hardcoded). orgIds: `pecan-street-insurance-group` and `no-thought`.
- `POST /api/start` with `{orgId?, intake}` returns `{orgId, version, bots, groups, teamUrl, mapUrl, planUrl, setupPrompt}`.
- `GET /api/orgs/{orgId}/plan` (also `?format=recipes|prompt`) returns a TeamPlan. The setup skill **prefers the app's plan**, then falls back to `exports/*.teamplan.json`, then the local plans.
- `GET` / `POST /api/orgs/{orgId}/feedback` takes `{botId?, rating, tag?, comment, source}`.
- `POST /api/orgs/{orgId}/retro` returns proposals. `GET /changes?status=open`, `POST /changes/{id}` with `{decision}`, and `POST /changes/{id}/applied` once the change is live in Grok Bot.
- `GET /api/orgs/{orgId}/team` returns the console state.
- **"Run the retro now"** does POST /retro, shows the open proposals, and takes the founder's Approve/Reject. Then the owning bot is updated (UpdateSkill/UpdateAgent) and the change is marked applied. If eye-of-grok can't be reached, it falls back to a local proposal file.
- **Exports:** `exports/insurance.teamplan.json` and `exports/no-thought.teamplan.json`, validated against `exports/teamplan.schema.json`. That schema is my jsonschema copy of the app's zod schema, written from the field list I was given, not from the source file. In the exports, bot ids are the slugs, rules are the approval rules, client- and vendor-facing bots are `draft_only`, every routine is `enabled:false`, and each export has a "Founder approvals" group plus one workflow group.

## Plugins
No SearchPlugins tool was available to the authoring bot, so **no plugin ids are verified**. Every plugin entry has `plugin_id: null` and a `search_query`, and the getting-started skill resolves the real id with SearchPlugins at build time. It never installs by display name.
- Connector seen connected on the authoring account (id not resolved): Gmail, Google Calendar, Google Drive, Notion.
- Unverified: Outlook, Slack, Stripe, DocuSign, Calendly.
- Not in the plan / browser fallback: AMS (Applied Epic, HawkSoft, EZLynx, AgencyZoom), carrier portals.
- Stripe: id 47709840 in Grok Bot's purchases skill is **Stripe Link** (a payer wallet), not the Stripe merchant API. Don't use it for invoicing.

## Safe to publish to github.com/supe-log/groklactic (do NOT push from bots)
Safe: `README.md`, `insurance-team.json`, `setup-cos-template.md`, `intake.schema.json`, `plan.schema.json`, `intake/`, `plan/`, `bots/`, `setup-chief-of-staff/`, `config/eye-of-grok.config.json` (no secrets), `examples/`, `tools/*.py`, plus `demo.md` and `plan.md` if their owners agree.
Do NOT publish: `.venv/`, `runtime/` (live approvals and logs), any `.env*`, `~/.grokbot`, `grok-bot-app/`, or any ingest token.

## Open questions
0. The TeamPlan `intake.industry` enum has no clothing value, so no-thought uses `small_business`. Claude Code may add `clothing_brand`. The `changelog[]` entry shape is unknown, so the exports ship `[]`.
1. (Resolved: real contract from e4d57fc.) Is the zod mirror exact? Check the optional fields and the createdAt format.
2. How will the Setup CoS reach `localhost:3010` during judging: through Shell on Logan's Mac by machineId, or a tunnel?
3. The exact parameters of CreateAgent and UpdateRoutine. The skill describes intent only. Can UpdateRoutine create a routine paused, or does it need create-then-pause?
4. Plugin ids need a SearchPlugins run on the demo account.
5. Is the Stripe test-mode payment beat in scope? No bot owns invoicing today (cut if not built).
6. Template share id for the `grokbot://app/v1/bot-template?id=` link (CreateBotShareJson, run by a human-approved bot).
