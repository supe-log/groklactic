#!/usr/bin/env python3
"""Render Groklactic vertical packages. Usage: build_package.py [insurance|clothing-brand ...] (default: all).
Write-files-only; creates no agents."""
import json, os, sys, datetime, importlib
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERTICALS = {"insurance": "package_data", "clothing-brand": "clothing_brand_data"}
INS_DEMO = ["Inbound COI request is labeled grok/coi by Intake & Inbox and handed to COI Desk.",
            "COI Desk runs the checklist, drafts the certificate from the ACORD 25 template, and raises a DraftExternalMessage reply card held for founder approval.",
            "Founder approves/edits; Agency Chief of Staff collects thumbs up/down -> feedback.jsonl (+ POST /api/feedback).",
            "Compliance & Ops weekly retro reads feedback and proposes ONE before/after improvement for founder approval."]
INS_STYLE = "If unsure whether something is coverage advice, treat it as coverage advice and route it."

def fix(s): return s.replace("{{{{", "{{").replace("}}}}", "}}")

def instructions(m, b):
    G = lambda n, d=None: getattr(m, n, d)
    name_of = {x["slug"]: x["name"] for x in m.BOTS}
    L = [f"# {b['name']}", "", f"_{b['title']}_ - {b['description']}", "", "## Role", b["role_text"], "",
         "## Global guardrails (non-negotiable, every bot)"]
    L += [f"- **{g['id']}**: {g['rule']}" for g in m.GLOBAL_GUARDRAILS]
    L += ["", "## What must come back to the founder (approval rules)"]
    L += [f"- **{a['id']}** - When: {a['when']}. Requires: `{a['requires']}`. How: {a['how']}." for a in b["approval_rules"]]
    L += ["", "## Handoffs"]
    L += [f"- To **{name_of[h['to']]}** when {h['when']} (send: {h['payload']})." for h in b["handoffs"]]
    L += ["", "## Skills you run"]
    L += [f"- @{s['name']} - {s['description']}" for s in m.SKILLS[b['slug']]]
    L += ["", "## On-demand phrases (run now, no routine needed)"]
    L += [f'- "{o["phrase"]}" -> run @{next(s["name"] for s in m.SKILLS[b["slug"]] if s["id"]==o["runs"])} inline' for o in m.ON_DEMAND[b['slug']]]
    L += ["", "## Routines (all ship PAUSED; founder enables)"]
    L += [f"- {r['name']}: `{r['cron_local']}` ({r['timezone']})" for r in b["routines"]]
    rt = m.RUNTIME
    L += ["", "## Shared working files (`$PKG` = the package root, i.e. the repo's bot-team/ folder)",
          f"- Approvals: `{rt}/approvals.jsonl` - Handoffs: `{rt}/handoffs.jsonl` - Feedback: `{rt}/feedback.jsonl`",
          "Append only. Never delete or rewrite lines.", "",
          "## Style", "Short, plain, professional. Times in America/Chicago with 'CT'. Record references, never raw PII.",
          G("STYLE_EXTRA", INS_STYLE)]
    return fix("\n".join(L)) + "\n"

def skill_md(s): return f"---\nname: {s['name']}\ndescription: >-\n  {s['description']}\n---\n{fix(s['body'])}"

RETRO = {
 "insurance": dict(slug="compliance-ops", chat_name="Compliance & Ops", cos_name="Agency Chief of Staff", guard_range="G1-G8",
   seed="$PKG/examples/seed-feedback.jsonl",
   example="2 of 3 COI thumbs-downs say the reply lacked a turnaround time -> kind=add_rule, botId=coi-desk: add to `bots/coi-desk/skills/coi-request/SKILL.md` step 5 the line 'State when the signed final certificate will be sent ({{coi_turnaround_hours}}h).'"),
 "clothing-brand": dict(slug="ops-retro", chat_name="Ops & Retro", cos_name="Brand Chief of Staff", guard_range="G1-G10",
   seed="$PKG/verticals/clothing-brand/examples/seed-feedback.jsonl",
   example="thumbs-down on RFQ-0001, 'ask for the minimum order quantity up front' -> kind=add_rule, botId=outreach-and-negotiation: in `verticals/clothing-brand/bots/outreach-and-negotiation/skills/rfq-draft/SKILL.md` step 2, add as the FIRST ask line: '- First question: \"What is your MOQ per style and per colorway for this item?\"'"),
}
AUTONOMY = {
 "insurance": {"agency-chief-of-staff": "ask_first", "intake-inbox": "draft_only", "renewals-follow-ups": "draft_only", "coi-desk": "draft_only", "quote-prep": "draft_only", "compliance-ops": "ask_first"},
 "clothing-brand": {"brand-chief-of-staff": "ask_first", "design-studio": "ask_first", "vendor-scout": "ask_first", "outreach-and-negotiation": "draft_only", "launch-growth": "draft_only", "ops-retro": "ask_first"},
}
GROUPS = {
 "insurance": [{"id": "founder-approvals", "name": "Founder approvals", "purpose": "Every client-facing draft, coverage escalation, and rule change lands here for the founder.", "memberIds": ["agency-chief-of-staff", "intake-inbox", "renewals-follow-ups", "coi-desk", "quote-prep", "compliance-ops"]},
               {"id": "coi-loop", "name": "COI loop", "purpose": "COI request -> draft -> founder approval -> feedback -> retro.", "memberIds": ["intake-inbox", "coi-desk", "compliance-ops"]}],
 "clothing-brand": [{"id": "founder-approvals", "name": "Founder approvals", "purpose": "Every outbound draft, spend, publish, PO, and rule change lands here for the founder.", "memberIds": ["brand-chief-of-staff", "design-studio", "vendor-scout", "outreach-and-negotiation", "launch-growth", "ops-retro"]},
                    {"id": "first-drop", "name": "First drop", "purpose": "Design -> sourcing -> RFQ for the hero product.", "memberIds": ["brand-chief-of-staff", "design-studio", "vendor-scout", "outreach-and-negotiation"]}],
}
PREFIX = {"insurance": "Insurance · ", "clothing-brand": "Clothing · "}
EXPORT_NAME = {"insurance": "insurance", "clothing-brand": "no-thought"}

def eog_intake(vertical, intake):
    b = intake["business"]
    ind = {"insurance": "insurance_agency", "clothing-brand": "small_business"}[vertical]
    return {"businessName": b["display_name"], "industry": ind, "teamSize": b["team_size"],
            "tools": [f"{k}: {v}" for k, v in intake["tools"].items()],
            "painPoints": " ".join(p["description"] for p in intake["pain_points"]),
            "rules": "; ".join(f"{k}={v}" for k, v in intake["rules"].items())}

def build(vertical):
    m = importlib.import_module(VERTICALS[vertical])
    G = lambda n, d=None: getattr(m, n, d)
    import eog, re
    # Prefix skill names by vertical so both teams can coexist on one account (ids unchanged).
    pre = PREFIX[vertical]
    orig = {}
    for sl in m.SKILLS.values():
        for s in sl:
            if not s["name"].startswith(pre):
                orig[s["name"]] = pre + s["name"]; s["name"] = pre + s["name"]
    if orig:
        rx = re.compile("@(" + "|".join(re.escape(k) for k in sorted(orig, key=len, reverse=True)) + ")")
        sub = lambda x: rx.sub(lambda mm: "@" + orig[mm.group(1)], x)
        for sl in m.SKILLS.values():
            for s in sl: s["body"] = sub(s["body"])
        for b in m.BOTS:
            b["role_text"] = sub(b["role_text"])
            for r in b["routines"]: r["prompt"] = sub(r["prompt"])
    rc = RETRO[vertical]
    for s in m.SKILLS[rc["slug"]]:
        if s["id"] == "weekly-retro":
            s["body"] = eog.retro_body(m.BUSINESS_ID, m.RUNTIME, rc["seed"], rc["chat_name"], rc["cos_name"], rc["guard_range"], rc["example"]).strip() + "\n"
            s["description"] = s["description"].split(" Use ")[0] if False else s["description"]
    out = G("OUT_DIR", "")
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    bots = []
    for b in m.BOTS:
        sk = m.SKILLS[b["slug"]]
        assert [s["id"] for s in sk] == b["skills"], b["slug"]
        rel = os.path.join(out, "bots", b["slug"]); d = os.path.join(ROOT, rel); os.makedirs(d, exist_ok=True)
        ins = instructions(m, b); open(os.path.join(d, "instructions.md"), "w").write(ins)
        skills = []
        for s in sk:
            sd = os.path.join(d, "skills", s["id"]); os.makedirs(sd, exist_ok=True)
            open(os.path.join(sd, "SKILL.md"), "w").write(skill_md(s))
            skills.append({"id": s["id"], "name": s["name"], "description": s["description"], "file": f"{rel}/skills/{s['id']}/SKILL.md"})
        bot = {"slug": b["slug"], "name": b["name"], "title": b["title"], "description": b["description"],
               "instructions_file": f"{rel}/instructions.md", "instructions": ins, "skills": skills,
               "routines": b["routines"], "on_demand_phrases": m.ON_DEMAND[b["slug"]], "plugins": b["plugins"],
               "approval_rules": b["approval_rules"], "handoffs": b["handoffs"]}
        if "verified_steps" in b: bot["verified_steps"] = b["verified_steps"]
        bots.append(bot)
    plan = {"schema_version": "1.0.0", "plan_id": m.PLAN_ID, "business_id": m.BUSINESS_ID, "vertical": vertical,
            "generated_at": now, "intake_file": G("INTAKE_FILE", "intake/insurance-agency.intake.json"),
            "industry": G("INDUSTRY", "independent_insurance_agency"), "timezone": m.TZ,
            "example_data_notice": G("EXAMPLE_NOTICE", "All business details are fictional example data. All client/person fields are {{placeholders}}.")}
    for k, n in [("baseline_source", "BASELINE_SOURCE"), ("hero_product", "HERO_PRODUCT"), ("hero_product_detail", "HERO_PRODUCT_DETAIL"),
                 ("spend_cap_usd", "SPEND_CAP_USD"), ("credit_cap_per_run", "CREDIT_CAP_PER_RUN"), ("brand_profile", "BRAND_PROFILE")]:
        if G(n) is not None: plan[k] = G(n)
    plan.update({"setup_trigger_phrase": m.SETUP_TRIGGER_PHRASE, "setup_trigger_aliases": m.SETUP_TRIGGER_ALIASES,
                 "on_demand_phrases": m.ON_DEMAND, "global_guardrails": m.GLOBAL_GUARDRAILS,
                 "founder_approval_defaults": m.FOUNDER_APPROVAL_DEFAULTS,
                 "shared_runtime": {"dir": m.RUNTIME, "files": ["approvals.jsonl", "handoffs.jsonl", "feedback.jsonl", "retro/"]},
                 "feedback": m.FEEDBACK_SPEC, "demo_beat": G("DEMO_BEAT", INS_DEMO), "bots": bots})
    pf = os.path.join(ROOT, G("PLAN_FILE", "plan/insurance-agency.plan.json")); os.makedirs(os.path.dirname(pf), exist_ok=True)
    json.dump(plan, open(pf, "w"), indent=2, ensure_ascii=False)
    team = json.loads(json.dumps(plan)); team["self_contained"] = True
    for tb, b in zip(team["bots"], m.BOTS):
        for ts, s in zip(tb["skills"], m.SKILLS[b["slug"]]): ts["skill_md"] = skill_md(s)
    for tf in G("TEAM_FILES", ["insurance-team.json"]):
        json.dump(team, open(os.path.join(ROOT, tf), "w"), indent=2, ensure_ascii=False)
    intake = json.load(open(os.path.join(ROOT, plan["intake_file"])))
    os.makedirs(os.path.join(ROOT, "exports"), exist_ok=True)
    tp = eog.teamplan(team, m, AUTONOMY[vertical], GROUPS[vertical], eog_intake(vertical, intake))
    json.dump(tp, open(os.path.join(ROOT, "exports", EXPORT_NAME[vertical] + ".teamplan.json"), "w"), indent=2, ensure_ascii=False)
    print(f"[{vertical}] rendered {len(bots)} bots, {sum(len(b['skills']) for b in bots)} skills, {sum(len(b['routines']) for b in bots)} routines")

if __name__ == "__main__":
    for v in (sys.argv[1:] or list(VERTICALS)): build(v)
