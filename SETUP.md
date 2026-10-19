# Groklactic local setup (one page)

## Folder layout on the Mac
```
~/Projects/groklactic/            # parent folder: NOT a git repo, never push from here
  eye-of-grok/                    # web app (supe-log/eye-of-grok), runs on :3010
    data-seed/no-thought.plan.json            # clothing team (6 bots)
    data-seed/pecan-street-insurance-group.plan.json
  groklactic-harness/             # THIS repo (supe-log/groklactic, branch bot-team)
    bot-team/                     # team packs, Setup CoS template, skills, demo script
    scripts/demo-check.sh         # smoke test for the demo path
  grok-bot-app/                   # closed source, never committed anywhere
```

## Run the demo (5 steps)
1. `cd ~/Projects/groklactic/eye-of-grok && npm run dev -- -p 3010`
2. Open `http://localhost:3010/start`, choose **Clothing brand**, slug `no-thought`, click **Design my Bot team**.
3. Install the Setup Chief of Staff template in Grok Bot and say **"Build my team"**. It reads the plan; if the app is unreachable it uses `bot-team/exports/`.
4. On `/u/no-thought/team`, give Outreach & Negotiation a thumbs-down: "ask for the minimum order quantity up front".
5. Click **Run retro**, approve the proposed rule.

## Before judging
- `INGEST_TOKEN=<token> ./scripts/demo-check.sh <org-id>` (set `INDUSTRY=small_business` until clothing_brand lands) checks start, plan, team page, feedback, retro.
- Rehearse on a throwaway id (e.g. `no-thought-rehearsal`). `?reset=1` resets the org map only, not the team plan or feedback stored in the database, so keep `no-thought` clean for the real run.

## Rules
- Branches only; never push or merge to `main` without Logan.
- No `.env*`, `.vercel/`, `data/`, `grok-bot-app/` in any commit.
- Every email, order, deposit or publish is a draft for the founder. Payments test mode. Cap $500.
