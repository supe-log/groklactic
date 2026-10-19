#!/usr/bin/env python3
"""Smoke test the Groklactic demo path against a local eye-of-grok.
Usage: INGEST_TOKEN=... python3 scripts/demo-check.py [org-id]"""
import json, os, sys, urllib.request, urllib.error
ORG = sys.argv[1] if len(sys.argv) > 1 else "no-thought-rehearsal"
BASE = os.environ.get("EYE_OF_GROK_URL", "http://localhost:3010")
TOKEN = os.environ.get("INGEST_TOKEN") or sys.exit("set INGEST_TOKEN to the app's write token")
INDUSTRY = os.environ.get("INDUSTRY", "clothing_brand")
failed = False
def call(method, path, body=None):
    req = urllib.request.Request(BASE + path, method=method, data=json.dumps(body).encode() if body is not None else None,
        headers={"authorization": f"Bearer {TOKEN}", "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: return r.status, r.read().decode()
    except urllib.error.HTTPError as e: return e.code, e.read().decode()
def check(name, ok, detail=""):
    global failed
    print(f"  {'ok  ' if ok else 'FAIL'} {name} {detail}".rstrip()); failed |= not ok
print(f"Checking {BASE} for org {ORG}")
s, b = call("POST", "/api/start", {"orgId": ORG, "intake": {"businessName": "No Thought", "industry": INDUSTRY,
    "teamSize": 1, "tools": ["Gmail", "Higgsfield"], "painPoints": "vendor sourcing, RFQs, design mockups"}})
check("intake /api/start", s == 200, "" if s == 200 else f"HTTP {s} {b[:200]}")
s, b = call("GET", f"/api/orgs/{ORG}/plan"); check("plan", s == 200)
bots = []
if s == 200:
    d = json.loads(b); p = d.get("plan", d); bots = [x["id"] for x in p.get("bots", [])]
    print("  bots", ", ".join(bots))
s, _ = call("GET", f"/u/{ORG}/team"); check("team page", s == 200)
bot = next((x for x in bots if "outreach" in x or "quote" in x), bots[1] if len(bots) > 1 else None)
for i in range(2):
    s, b = call("POST", f"/api/orgs/{ORG}/feedback", {"botId": bot, "rating": "down", "tag": "missing",
        "comment": "ask for the minimum order quantity up front", "source": "owner"})
    check(f"thumbs-down {i+1} on {bot}", s in (200, 201), "" if s in (200, 201) else f"HTTP {s} {b[:200]}")
s, b = call("POST", f"/api/orgs/{ORG}/retro"); check("retro", s == 200, b[:300])
sys.exit(1 if failed else 0)
