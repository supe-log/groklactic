#!/usr/bin/env bash
# Smoke test the Groklactic demo path against a local eye-of-grok.
# Usage: ./scripts/demo-check.sh [org-id]   (default: no-thought-rehearsal)
set -euo pipefail
ORG="${1:-no-thought-rehearsal}"
BASE="${EYE_OF_GROK_URL:-http://localhost:3010}"
TOKEN="${INGEST_TOKEN:?set INGEST_TOKEN to the app's write token}"
ok(){ printf '  ok   %s\n' "$1"; }; bad(){ printf '  FAIL %s\n' "$1"; FAILED=1; }
FAILED=0
echo "Checking $BASE for org $ORG"
code=$(curl -s -o /tmp/eog-start.json -w '%{http_code}' -X POST "$BASE/api/start" \
  -H "authorization: Bearer $TOKEN" -H 'content-type: application/json' \
  -d "{\"orgId\":\"$ORG\",\"intake\":{\"businessName\":\"No Thought\",\"industry\":\"${INDUSTRY:-clothing_brand}\",\"teamSize\":1,\"tools\":[\"Gmail\",\"Higgsfield\"],\"painPoints\":\"vendor sourcing, RFQs, design mockups\"}}")
[ "$code" = 200 ] && ok "intake /api/start" || bad "intake /api/start ($code: $(head -c 200 /tmp/eog-start.json))"
[ "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/api/orgs/$ORG/plan")" = 200 ] && ok "plan" || bad "plan"
[ "$(curl -s -o /dev/null -w '%{http_code}' "$BASE/u/$ORG/team")" = 200 ] && ok "team page" || bad "team page"
BOT=$(curl -s "$BASE/api/orgs/$ORG/plan" | python3 -c 'import sys,json;d=json.load(sys.stdin);p=d.get("plan",d);b=[x["id"] for x in p["bots"] if "outreach" in x["id"]];print(b[0] if b else p["bots"][1]["id"])')
echo "  bot  $BOT"
code=$(curl -s -o /dev/null -w '%{http_code}' -X POST "$BASE/api/orgs/$ORG/feedback" -H "authorization: Bearer $TOKEN" \
  -H 'content-type: application/json' -d "{\"botId\":\"$BOT\",\"rating\":\"down\",\"comment\":\"ask for the minimum order quantity up front\"}")
[ "$code" = 200 ] || [ "$code" = 201 ] && ok "feedback" || bad "feedback ($code)"
n=$(curl -s -X POST "$BASE/api/orgs/$ORG/retro" -H "authorization: Bearer $TOKEN" | python3 -c 'import sys,json;print(json.load(sys.stdin).get("created",0))')
[ "$n" -ge 1 ] && ok "retro proposed $n change(s)" || bad "retro proposed 0 (threshold still 2? set RULE_AFTER_DOWNS=1)"
exit $FAILED
