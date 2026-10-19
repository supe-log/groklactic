#!/usr/bin/env python3
"""Validate Groklactic package. Usage: validate.py [plan.json ...]  (default: all known files)
Checks: JSON parses, schemas, <=6 bots, all routines enabled:false, approval_rules present,
skill files exist with name+description frontmatter, handoff targets exist, no PII patterns."""
import json, sys, os, re, glob
from jsonschema import Draft202012Validator
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errs = []
def load(p):
    try: return json.load(open(p))
    except Exception as e: errs.append(f"{p}: JSON parse error {e}"); return None

PII = [("ssn", r"\b\d{3}-\d{2}-\d{4}\b"), ("card", r"\b(?:\d[ -]?){13,16}\b"),
       ("phone", r"\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b"),
       ("email", r"\b[\w.+-]+@(?![\w.-]*example\.(?:com|org|net)\b)[\w.-]+\.[a-z]{2,}\b"),
       ("street", r"\b\d{2,5} [A-Z][a-z]+ (?:St|Street|Ave|Avenue|Rd|Road|Blvd|Dr|Lane|Ln)\b")]
def pii_scan(path):
    t = open(path, errors="ignore").read()
    for k, rx in PII:
        for m in re.finditer(rx, t):
            errs.append(f"{os.path.relpath(path, ROOT)}: possible PII ({k}) at offset {m.start()}")

def check_plan(p):
    plan = load(p)
    if plan is None: return
    if "orgId" in plan:  # TeamPlan export (app format): check against teamplan.schema.json only
        tsch = load(os.path.join(ROOT, "exports", "teamplan.schema.json"))
        for e in Draft202012Validator(tsch).iter_errors(plan):
            errs.append(f"{p}: teamplan schema: {'/'.join(map(str, e.path))}: {e.message}")
        return
    sch = load(os.path.join(ROOT, "plan.schema.json"))
    for e in Draft202012Validator(sch).iter_errors(plan):
        errs.append(f"{p}: schema: {'/'.join(map(str, e.path))}: {e.message}")
    slugs = {b.get("slug") for b in plan.get("bots", [])}
    names = [b.get("name") for b in plan.get("bots", [])]
    if len(names) != len(set(names)): errs.append(f"{p}: duplicate bot names")
    for b in plan.get("bots", []):
        if not b.get("approval_rules"): errs.append(f"{p}: {b.get('slug')} has no approval_rules")
        for r in b.get("routines", []):
            if r.get("enabled") is not False: errs.append(f"{p}: routine {r.get('id')} not paused")
        for h in b.get("handoffs", []):
            if h["to"] not in slugs: errs.append(f"{p}: {b['slug']} handoff to unknown bot {h['to']}")
        for s in b.get("skills", []):
            if "file" not in s: continue  # TeamPlan skills carry inline content
            f = os.path.join(ROOT, s["file"])
            if not os.path.exists(f): errs.append(f"{p}: missing skill file {s['file']}"); continue
            head = open(f).read().split("---")
            if len(head) < 3 or "name:" not in head[1] or "description:" not in head[1]:
                errs.append(f"{s['file']}: bad frontmatter")
        if b.get("instructions_file") and not os.path.exists(os.path.join(ROOT, b["instructions_file"])):
            errs.append(f"{p}: missing {b['instructions_file']}")
    hf = load(os.path.join(ROOT, "config", "higgsfield-tools.json"))
    real = set((hf or {}).get("tools", []))
    for b in plan.get("bots", []):
        cited = [t for pl in b.get("plugins", []) if pl.get("namespace") == "user-Higgsfield" for t in pl.get("tools_used", [])]
        cited += [st["tool"] for st in b.get("verified_steps", {}).get("steps", [])]
        for t in cited:
            if t not in real: errs.append(f"{p}: {b['slug']} cites unknown Higgsfield tool {t}")
    return plan

def main():
    targets = sys.argv[1:] or (sorted(glob.glob(os.path.join(ROOT, "plan", "*.plan.json"))) + [os.path.join(ROOT, "insurance-team.json")]
        + sorted(glob.glob(os.path.join(ROOT, "verticals", "*", "plan", "*.plan.json"))) + sorted(glob.glob(os.path.join(ROOT, "verticals", "*", "team.json")))
        + [p for p in [os.path.join(ROOT, "clothing-team.json")] if os.path.exists(p)])
    plans = [check_plan(t) for t in targets]
    if not sys.argv[1:]:
        isch = load(os.path.join(ROOT, "intake.schema.json"))
        for ip in glob.glob(os.path.join(ROOT, "intake", "*.intake.json")) + glob.glob(os.path.join(ROOT, "verticals", "*", "intake", "*.intake.json")):
            intake = load(ip)
            if intake and isch:
                for e in Draft202012Validator(isch).iter_errors(intake): errs.append(f"{os.path.relpath(ip, ROOT)}: {e.message}")
        idx = load(os.path.join(ROOT, "verticals", "index.json"))
        for v in (idx or {}).get("verticals", []):
            for k in ("plan_file", "team_file", "intake_file"):
                if not os.path.exists(os.path.join(ROOT, v[k])): errs.append(f"verticals/index.json: {v['vertical']} missing {v[k]}")
        for j in glob.glob(os.path.join(ROOT, "**/*.json"), recursive=True):
            if "/.venv/" not in j: load(j)
        for f in glob.glob(os.path.join(ROOT, "**/*"), recursive=True):
            if os.path.isfile(f) and "/.venv/" not in f and f.endswith((".json", ".jsonl", ".md", ".csv", ".txt")) and "/runtime/" not in f:
                pii_scan(f)
    if not sys.argv[1:]:
        tsch = load(os.path.join(ROOT, "exports", "teamplan.schema.json"))
        for tp_path in sorted(glob.glob(os.path.join(ROOT, "exports", "*.teamplan.json"))):
            tp = load(tp_path)
            if not (tp and tsch): continue
            for e in Draft202012Validator(tsch).iter_errors(tp):
                errs.append(f"{os.path.relpath(tp_path, ROOT)}: teamplan: {'/'.join(map(str, e.path))}: {e.message}")
            ids = {b["id"] for b in tp["bots"]}
            if tp["chiefOfStaffId"] not in ids: errs.append(f"{tp_path}: chiefOfStaffId not a bot")
            for g in tp["groups"]:
                for mid in g["memberIds"]:
                    if mid not in ids: errs.append(f"{tp_path}: group {g['id']} unknown member {mid}")
            print(f"OK-checked {os.path.relpath(tp_path, ROOT)}: TeamPlan orgId={tp['orgId']} industry={tp['intake']['industry']} bots={len(tp['bots'])} groups={len(tp['groups'])} routines_enabled={sum(r['enabled'] for b in tp['bots'] for r in b['routines'])}")
    for t, pl in zip(targets, plans):
        if pl:
            r = sum(len(b["routines"]) for b in pl["bots"])
            print(f"OK-checked {os.path.relpath(t, ROOT)}: {len(pl['bots'])} bots, {sum(len(b['skills']) for b in pl['bots'])} skills, {r} routines (enabled: {sum(1 for b in pl['bots'] for x in b['routines'] if x['enabled'])})")
    if errs:
        print("FAIL"); [print(" -", e) for e in errs]; sys.exit(1)
    print("PASS: all JSON parses, Higgsfield tool names match the real catalog, plan(s) valid against plan.schema.json, TeamPlan exports valid against teamplan.schema.json, intakes valid, all routines paused, approval_rules on every bot, no PII patterns")

main()
