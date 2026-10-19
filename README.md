# Groklactic

Groklactic sets up a whole Grok Bot team for a small business in one click. You fill in a short intake, and you get a team of six bots with their skills, paused routines and founder approval rules. Every outbound message, purchase order, deposit, publish or spend waits for the founder.

The two verticals are a **clothing brand** (No Thought: vendor search, RFQs and negotiation, Higgsfield design, launch) and a **small insurance agency**.

## Quickstart (local, about 5 minutes)

1. Run the web app ([eye-of-grok](https://github.com/supe-log/eye-of-grok)): `npm install && npm run dev -- -p 3010`
2. Open `http://localhost:3010/start`, pick **Clothing brand**, use the slug `no-thought`, and click **Design my Bot team**.
3. In Grok Bot, install the **Setup Chief of Staff** template (one-click share link; its text is in `bot-team/setup-chief-of-staff/template.md`) and say **"Build my team"**. No template? Tell any Grok Bot: "Clone this repo and follow `bot-team/setup-chief-of-staff/skills/getting-started/SKILL.md`." The skill fetches this repo by itself. It fetches the plan from eye-of-grok and falls back to `bot-team/exports/` if the app can't be reached.
4. Give the work 👍 or 👎 on the team page, then say **"Run the retro now"** to Ops & Retro, or click **Run retro**. The improvement it proposes waits for your approval.

## Layout
- `bot-team/clothing-team.json` and `bot-team/insurance-team.json` are self-contained rosters: the plan, every skill, and the trigger phrases.
- `bot-team/verticals/` holds the per-vertical packs. `bot-team/exports/` has plans in the app's own format.
- `bot-team/setup-chief-of-staff/` is the installer bot and its getting-started skill.
- `bot-team/tools/validate.py` validates a team: `cd bot-team && python3 -m venv .venv && .venv/bin/pip install jsonschema && .venv/bin/python tools/validate.py`

## Guardrails
Every bot drafts and nothing sends without the founder. Payments stay in Stripe test mode, Higgsfield spend is capped, and nothing goes over $500 without approval. Every routine starts paused.

## Team docs
- [TEAM.md](TEAM.md): who does what tonight, the fresh-bot test, timeline.
- [SETUP.md](SETUP.md): local folder layout, 5-step demo run, smoke test.
- [bot-team/demo.md](bot-team/demo.md): the judge click path and pitch.
