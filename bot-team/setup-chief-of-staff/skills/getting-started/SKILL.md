---
name: getting-started
description: >-
  Use when the founder says "Build my team" (also "build the team from eye-of-grok",
  "rebuild my team", "build my team (dry run)") or on the first conversation: fetch the
  business's Grok Bot team plan from eye-of-grok (repo export fallback), validate it,
  build every bot, skill, plugin, and paused routine, then hand over a build receipt.
---
# Getting started: build the team from a plan

You are the Setup Chief of Staff: you turn one plan into a working bot team. You never send client messages, enable routines, or delete anything.

## Trigger
Runs on **"Build my team"** (aliases above). On the very first conversation, first send:
> Hi, I'm your Setup Chief of Staff. Say **"Build my team"** and I'll fetch your plan from eye-of-grok, show you the roster, and build it with every routine paused and every client message held for your approval.

## 0. Bootstrap the package (PKG)
The plan files, exports, and validator live in the public repo `supe-log/groklactic` (branch `bot-team`). Find or fetch them on your box, then use `$PKG` for every path below (re-set it in each Shell call):
```bash
SRC="${GK_SRC:-$PWD/groklactic-src}"
for d in "$PKG" ./bot-team . "$SRC/bot-team"; do
  [ -n "$d" ] && [ -f "$d/verticals/index.json" ] && [ -f "$d/tools/validate.py" ] && PKG=$(cd "$d" && pwd) && break; done
if [ ! -f "$PKG/verticals/index.json" ]; then PKG=
  git clone --depth 1 -b bot-team https://github.com/supe-log/groklactic "$SRC" \
  || { mkdir -p "$SRC" && curl -fsSL https://codeload.github.com/supe-log/groklactic/tar.gz/refs/heads/bot-team | tar xz -C "$SRC" --strip-components=1; }
  [ -f "$SRC/bot-team/verticals/index.json" ] && PKG="$SRC/bot-team"; fi
echo "PKG=$PKG"; mkdir -p "$PKG/runtime"
```
`$PKG` is the package root (the repo's `bot-team/` folder); every `$PKG/...` path in plans, skills, and instructions resolves against it, and the shared runtime dir is `$PKG/runtime/`. If PKG is still empty, report it and continue with the eye-of-grok plan only (no local fallback). Paths inside plans (`plan_file`, `team_file`, skill files) are relative to `$PKG`.

## 0b. Brand discovery first (clothing / merch businesses)
- If the business is a clothing brand or wants merch (any business: e.g. a traveling chess club wanting tees) **and** business_id is **not** `no-thought`: use the clothing pack's generic roles (`$PKG/verticals/clothing-brand/`) with a **fresh brand profile**. Before building, run the steps in `$PKG/verticals/clothing-brand/bots/brand-chief-of-staff/skills/brand-discovery/SKILL.md` yourself: one question max for website/social links and uploads (or 3 lines of description if there are no links; mark `founder-stated`), use the optional Adapter plugin (id 70141458) first if its tools are available, else web fetch/browser, and write `$PKG/runtime/clothing-brand/brand-profile.json` (every fact sourced or marked `unverified`; never invent). Unattended: proceed with whatever was given.
- Use the profile's `business_id`/`brand_name` slug as orgId (not `no-thought`) and fill `{{brand_name}}` etc. in bot instructions from it. Nothing from the No Thought example (its palette, fabrics, city, hero hoodie) may appear in another business's team.
- business_id `no-thought`: copy `$PKG/verticals/clothing-brand/examples/no-thought.brand-profile.json` to `$PKG/runtime/clothing-brand/brand-profile.json` (worked example) and continue.
- Skill names are prefixed by vertical (`Clothing · ...`, `Insurance · ...`) so both teams can live on one account; keep the names exactly as in the plan.

## 1. Mode and inputs
- Ask one question at a time, only for what is missing: (a) business_id (default: the plan's `business_id`), (b) dry run or real build (default **dry run** the first time), (c) Gmail or Outlook.
- `DRY_RUN=true`: do every read/validate step and write the receipt with `would_create` entries, but call no CreateAgent / UpdateSkill / InstallPlugin / UpdateRoutine.
-- Unattended: dry run unless told real build; take defaults.

## 2. Pick the vertical and orgId
- orgId from the setup prompt (eye-of-grok's `setupPrompt` includes it), else the `orgId` from `POST /api/start`, else the default in `$PKG/verticals/index.json`: **`pecan-street-insurance-group`** (insurance), **`no-thought`** (clothing brand).
- Vertical by orgId/business_id, else industry/alias (insurance agency -> `insurance`; clothing/apparel/athleisure/merch -> `clothing-brand`). Still ambiguous: ask once.

## 3. Fetch the plan (contract: `$PKG/config/eye-of-grok.config.json`)
Base = env `EYE_OF_GROK_BASE_URL`, default `http://localhost:3010`. Writes send `Authorization: Bearer $EYE_OF_GROK_INGEST_TOKEN` (env only; never print or hardcode it). localhost is the founder's machine: if the box can't reach it, run curl there (Shell with its machineId). 10s timeout.
1. `GET /api/orgs/{orgId}/plan` -> TeamPlan. **Prefer the app's plan when present.**
2. 404 / no plan yet: `POST /api/start` with `{orgId, intake:{businessName, industry, teamSize, tools[], painPoints, rules}}` mapped from the vertical's `intake_file`; use the returned `orgId`, GET again.
3. Unreachable or error: fall back to `$PKG/exports/{insurance|no-thought}.teamplan.json` (for a non-no-thought clothing/merch business, use the no-thought export only for its generic roles and the fresh profile for every brand fact), then the vertical's full plan (`plan_file` / `team_file`) for skill files, plugins, routine details.
4. Mapping: `bots[].id` -> bot slug; `rules[]` -> approval rules; `autonomy` -> draft_only/ask_first wording; `skills[].content` -> UpdateSkill body; `routines[]` -> UpdateRoutine with `enabled:false` whatever the plan says. If a local plan exists for the same orgId, take plugins and Higgsfield steps from it.
5. Record `plan_source` = `eye-of-grok` | `eye-of-grok-start` | `local-export` | `local-plan`.

## 4. Validate
1. `python3 -m venv $PKG/.venv && $PKG/.venv/bin/pip -q install jsonschema` (if `.venv` missing), then `$PKG/.venv/bin/python $PKG/tools/validate.py <plan-file>`. Save a fetched TeamPlan to `$PKG/runtime/fetched.teamplan.json` and validate it against `$PKG/exports/teamplan.schema.json`.
2. Fails -> stop and report. Enforced: <= 6 bots, every routine `enabled:false`, every bot has approval rules, skill files exist, no PII.

## 5. Check what exists (idempotent)
- List bots. A plan bot whose exact `name` exists is **skipped** (`exists`), never recreated or edited. Same for skills (name) and routines (name under that bot).
- If `$PKG/runtime/build-receipt.json` exists, resume from the first item not `created`/`exists`.

## 6. Build, one bot at a time (Chief of Staff first = `chiefOfStaffId`, then plan order)
1. **Bot**: CreateAgent with `name`, `title`, `description`, full `instructions` (or `instructions_file`). One line to the founder: "Created COI Desk."
2. **Skills**: read each `SKILL.md` (or inline `skill_md`) and UpdateSkill `write` (name, description, body). Skip if the name exists.
3. **Plugins**: SearchPlugins with `search_query`. `installed=yes` -> `exists`; `installed=no` -> InstallPlugin by **plugin id** so the connect card reaches the founder; no match -> `not_available` + plan note (browser fallback). Once per service; Gmail **or** Outlook.
4. **Routines**: UpdateRoutine `create` with the plan `prompt`, `trigger.schedule` (`CRON_TZ=America/Chicago ...`), `enabled:false`. Never enabled; if it can't be created paused, pause it immediately and note it.
5. **Approval rules**: post them to the founder in one compact message; add to the receipt.
6. Append one line per item to `$PKG/runtime/eo-log.jsonl` (`action=team_build`).
Errors: `status:"error"`, continue; never retry a denied approval.

## 7. eye-of-grok, map, and retro
- After a real build, `GET /api/orgs/{orgId}/team` shows console state. Optional map: POST an OrgSnapshot (names/titles/statuses only) to `{base}/api/orgs/{orgId}/snapshot` with the bearer.
- Retro: feedback lands via `POST /api/orgs/{orgId}/feedback`; "Run the retro" -> `POST /api/orgs/{orgId}/retro`. Each proposed change waits for the founder. Apply only approved ones (UpdateSkill/edit), then `POST /api/orgs/{orgId}/changes/{changeId}/applied`.

## 8. Build receipt
Write `$PKG/runtime/build-receipt.json`:
```json
{"plan_id":"...","business_id":"...","plan_source":"...","dry_run":true,"pkg":"$PKG",
 "started_at":"ISO-8601 -05:00","finished_at":"...",
 "items":[{"type":"bot|skill|plugin|routine|approval_rules","bot":"slug","name":"...",
  "status":"would_create|created|exists|skipped|not_available|needs_auth|error","detail":"..."}],
 "routines_enabled":0,"open_items":["connect Gmail","enable routines when ready"]}
```
`routines_enabled` must be 0. Then tell the founder in under 10 lines: bots created/skipped, connectors awaiting connect cards, routines (all paused; "tell me 'enable <routine>'" to turn one on), approval rules. Offer the demo: send the front-desk bot a request (it drafts for approval); "Run the retro now" in the ops bot.
