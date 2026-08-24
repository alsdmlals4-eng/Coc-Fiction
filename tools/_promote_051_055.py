#!/usr/bin/env python3
from __future__ import annotations
import base64,gzip,hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; F=ROOT/"fiction"
SOURCE_FILE="폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx"; SOURCE_SHA="84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496"
parts=[ROOT/f"tools/_payload_051_055.part{i:02d}" for i in range(1,5)]; enc="".join(p.read_text(encoding="utf-8").strip() for p in parts)
SOURCE_MD=gzip.decompress(base64.b64decode(enc)).decode("utf-8"); SOURCE_MD_SHA="e4fe2a8f88feca6972a54eed6c395a27fd2f4753687878419d5f66411893b939"
if hashlib.sha256(SOURCE_MD.encode()).hexdigest()!=SOURCE_MD_SHA: raise SystemExit("Ch051-055 staged payload SHA mismatch")
EXPECTED={51:{"title":"잊어도 되는 기억","pov":"주안 → 이안 → 주안","chars":5568,"sha":"5c030e6bef2a802db670f600ad0bb5079bcba185b5bd134eae3ad44f3fe52880"},52:{"title":"잊으면 안 될 것","pov":"주안 → 이안 → 주안 → 이안","chars":4934,"sha":"5ad14e30c75d7ce3a82514ebcd016aab92bf2f9a384962d47e4d5c4f69c396ce"},53:{"title":"주교님의 외갑","pov":"주안 → 이안 → 주안 → 이안 → 주안 → 이안","chars":5244,"sha":"286f8768e7ccf046f9a51a500b59fd62ec95bbcc44354a3916075fd5b2a701e8"},54:{"title":"사슬을 끊는 법","pov":"주안 → 이안 → 주안 → 이안 → 주안","chars":5666,"sha":"dba02380a691b8b2d68fe1a8c95734350e9233b2589f8776156052e64e2a2550"},55:{"title":"세상을 봐야 합니다","pov":"주안 → 이안 → 주안 → 이안","chars":4981,"sha":"35b0cb9f53775945a9cafe2aa307e3ffe04a3355b38b3e1db831826db60d5fdc"}}
CH50_SHA="5b3bd9bcbb7b3d04deb38dfdb39db2c9fdc56fb50df18ea9425562c9b484880e"; CH56_SHA="f0f1d1e7ce95b4c484d7c26997343851e1b3381ccdfcf1c751d41224d2bf6be5"
CARDS='''# SCENE CARDS · Bridge 051–055

> Source: `폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx` / `84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496`
> Boundary: Part 1 001–040 → Bridge 041–066 → Part 2 067+

## 제51화 · 잊어도 되는 기억
- POV: 주안 → 이안 → 주안
- 기능: 기억수의 효과·비가역 위험을 검증하고 자발적 복용을 충분한 정보·안전과 동일시하지 않는다.
- body SHA256: `5c030e6bef2a802db670f600ad0bb5079bcba185b5bd134eae3ad44f3fe52880`

## 제52화 · 잊으면 안 될 것
- POV: 주안 → 이안 → 주안 → 이안
- 기능: 수신기·통증·기록을 단서로 감정의 순수성이 아니라 반복된 선택의 맥락을 회수한다.
- body SHA256: `5ad14e30c75d7ce3a82514ebcd016aab92bf2f9a384962d47e4d5c4f69c396ce`

## 제53화 · 주교님의 외갑
- POV: 주안 → 이안 → 주안 → 이안 → 주안 → 이안
- 기능: 쵸세이칸 본체와 외갑을 분리하고 보호 장치가 보호 대상의 현재 의사와 무관하게 폭주할 수 있음을 확인한다.
- body SHA256: `286f8768e7ccf046f9a51a500b59fd62ec95bbcc44354a3916075fd5b2a701e8`

## 제54화 · 사슬을 끊는 법
- POV: 주안 → 이안 → 주안 → 이안 → 주안
- 기능: 쵸세이칸의 동의·거리 선택을 먼저 확보하고 외갑–마도서 연결 사슬만 끊는다.
- body SHA256: `dba02380a691b8b2d68fe1a8c95734350e9233b2589f8776156052e64e2a2550`

## 제55화 · 세상을 봐야 합니다
- POV: 주안 → 이안 → 주안 → 이안
- 기능: 보호와 감금을 분리하고 쵸세이칸이 외부 세계를 직접 보고 다음 선택을 할 권리를 연다.
- body SHA256: `35b0cb9f53775945a9cafe2aa307e3ffe04a3355b38b3e1db831826db60d5fdc`

## 제50→51화
- 판정: DIRECT_CONTINUITY_PASS
## 제51→52화
- 판정: DIRECT_CONTINUITY_PASS
## 제52→53화
- 판정: DIRECT_CONTINUITY_PASS
## 제53→54화
- 판정: DIRECT_CONTINUITY_PASS
## 제54→55화
- 판정: DIRECT_CONTINUITY_PASS
## 제55→56화
- 판정: FAIL_CLOSED_UNTIL_NEXT_PROMOTION
'''
REPORT='''# REVISION · Current Reconciliation 051–055 · 2026-08-24

## Scope
- bounded bundle: `fiction/manuscript/part-1/051-055.md`
- source: `폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx`
- source SHA256: `84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496`
- main production before merge: `001–050`
- PR #61 candidate: `001–055`
- fail-closed boundary after candidate: `055→056`

## Reconciliation
- 사용자 지정 DOCX의 Ch51–55 사건 순서·POV marker·대사·행동·인과를 source authority로 사용했다.
- current Canon과 충돌하는 legacy Alice 한국어 표기만 `엘리스`로 정규화했다.
- 기억수의 자발적 복용을 충분한 정보·안전·가역성이 보장된 동의로 과장하지 않는다.
- Ch53–54는 보호 장치가 보호 대상의 선택을 앞지를 수 있다는 문제를 외갑 구조로 검증한다.
- Ch55는 세상을 직접 경험한 뒤 선택할 권리를 연다.
- 엘리스 D04 인간 포함 정신조작 가능 범위와 라르고 reveal timing을 변경하지 않는다.
- Ch56 본문은 변경하지 않는다. `101–105` source gap과 whole-manuscript `NOT_YET_CLAIMED`를 유지한다.

## Exact body receipts
- Ch51 `5c030e6bef2a802db670f600ad0bb5079bcba185b5bd134eae3ad44f3fe52880`
- Ch52 `5ad14e30c75d7ce3a82514ebcd016aab92bf2f9a384962d47e4d5c4f69c396ce`
- Ch53 `286f8768e7ccf046f9a51a500b59fd62ec95bbcc44354a3916075fd5b2a701e8`
- Ch54 `dba02380a691b8b2d68fe1a8c95734350e9233b2589f8776156052e64e2a2550`
- Ch55 `35b0cb9f53775945a9cafe2aa307e3ffe04a3355b38b3e1db831826db60d5fdc`
'''
NOTE='''
## PR #61 candidate · Bridge 051–055 readback
- Ch51 `잊어도 되는 기억`: 기억수의 효과·비가역 위험을 검증한다.
- Ch52 `잊으면 안 될 것`: 반복된 선택의 맥락을 회수한다.
- Ch53 `주교님의 외갑`: 쵸세이칸 본체와 외갑을 분리한다.
- Ch54 `사슬을 끊는 법`: 현재 의사를 먼저 확보하고 필요한 연결만 끊는다.
- Ch55 `세상을 봐야 합니다`: 보호와 감금을 분리하고 외부 세계를 직접 볼 권리를 연다.
- main production은 merge 전 `001–050`; PR #61 candidate만 `001–055 / 055→056`이다.
'''
def wt(p,s):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);s=s if s.endswith("\n") else s+"\n"
 if not p.exists() or p.read_text(encoding="utf-8")!=s:p.write_text(s,encoding="utf-8")
def wj(p,o):wt(p,json.dumps(o,ensure_ascii=False,indent=2)+"\n")
def sl(t,k,v):
 p=rf"(?m)^{re.escape(k)}:.*$";line=f"{k}: {v}";return re.sub(p,line,t,count=1) if re.search(p,t) else t
# Verify staged manuscript structure/body before writing.
cp=re.compile(r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",re.M|re.S)
parsed={int(m.group(1)):(m.group(2).strip(),m.group(3).strip(),m.group(4).strip()) for m in cp.finditer(SOURCE_MD)}
if sorted(parsed)!=list(EXPECTED):raise SystemExit("staged manuscript chapter set mismatch")
for n,e in EXPECTED.items():
 title,pov,body=parsed[n]
 if (title,pov,len(body),hashlib.sha256(body.encode()).hexdigest())!=(e["title"],e["pov"],e["chars"],e["sha"]):raise SystemExit(f"Ch{n} staged body receipt mismatch")
wt(F/"manuscript/part-1/051-055.md",SOURCE_MD)
idx={"schema_version":1,"updated_at":"2026-08-24","status":"ACTIVE_OVERRIDE / BUNDLE_051_055 / BRIDGE_CURRENT_RECONCILED","baseline":"analysis/baselines/MANUSCRIPT_INDEX_2026-07-23_PILOT.json","chapters":[{"chapter":n,"title":EXPECTED[n]["title"],"pov":EXPECTED[n]["pov"],"body_chars":EXPECTED[n]["chars"],"body_sha256":EXPECTED[n]["sha"],"bundle":"fiction/manuscript/part-1/051-055.md"} for n in range(51,56)]};wj(F/"analysis/MANUSCRIPT_INDEX_OVERRIDE_051_055.json",idx)
ip=F/"MANUSCRIPT_INDEX.json";im=json.loads(ip.read_text(encoding="utf-8"));rel="analysis/MANUSCRIPT_INDEX_OVERRIDE_051_055.json"
if rel not in im["overrides"]:im["overrides"].insert(im["overrides"].index("analysis/MANUSCRIPT_INDEX_OVERRIDE_091_095.json"),rel)
im["status"]="ACTIVE / COMPOSED / 225_STORAGE_CHAPTERS / MIXED_MIGRATION / CURRENT_PREFIX_001_055";wj(ip,im)
rp=ROOT/"docs/fiction-ops/CURRENT_STATE_RECEIPT.json";r=json.loads(rp.read_text(encoding="utf-8"));r.update({"frontier_observed_at_main":None,"last_frontier_change_pr":59,"pending_frontier_change_pr":61,"verified_prefix_end":55,"legacy_tail_starts_at":56,"boundary_after_chapter":55,"next_bounded_bundle":"fiction/manuscript/part-1/056-060.md","whole_manuscript_continuity":"NOT_YET_CLAIMED","candidate_sha256":SOURCE_SHA});wj(rp,r)
rgp=F/"analysis/SCENE_PASS_REGISTRY.json";rg=json.loads(rgp.read_text(encoding="utf-8"));rec=rg["external_artifact_reconciliation"];rec.update({"artifact":SOURCE_FILE,"artifact_sha256":SOURCE_SHA,"reconciled_prefix_end":55,"legacy_tail_starts_at":56,"boundary_after_chapter":55,"whole_manuscript_continuity":"NOT_YET_CLAIMED","rule":"Chapters 1-55 are the bounded reconciled candidate prefix in PR #61. Ch041-066 are Aftermath & 8-year Bridge; stored Ch56+ remain legacy until their own pass; 101-105 remains fail-closed."})
np={"bundle":"fiction/manuscript/part-1/051-055.md","chapters":[51,52,53,54,55],"boundary_chapters":[50,56],"scene_cards":"fiction/analysis/SCENE_CARDS_051_055.md","revision_report":"fiction/reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_051_055.md","source_files":[{"name":SOURCE_FILE,"sha256":SOURCE_SHA,"role":"user-designated Bridge source authority"},{"name":"fiction/CANON_REGISTRY.json","role":"latest approved canon protection"}],"chapter_shas":{str(n):EXPECTED[n]["sha"] for n in range(51,56)},"preserved_boundary_shas":{"50":CH50_SHA,"56":CH56_SHA},"status":"COMPLETE_CURRENT_SOURCE_CANON_RECONCILIATION / BRIDGE_CURRENT_PREFIX"}
rg["completed_bundle_passes"]=[np if x.get("bundle")==np["bundle"] else x for x in rg["completed_bundle_passes"]]
if not any(x.get("bundle")==np["bundle"] for x in rg["completed_bundle_passes"]):rg["completed_bundle_passes"].append(np)
rg["next_pass_mode"]="USER_SOURCE_CHUNK_CANON_RECONCILIATION";rg["next_bundle_passes"]=["fiction/manuscript/part-1/056-060.md"];wj(rgp,rg);wt(F/"analysis/SCENE_CARDS_051_055.md",CARDS);wt(F/"reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_051_055.md",REPORT)
from build_fiction_reverse_outline import build_current
gen=build_current(ROOT);by={int(x["chapter"]):x for x in gen["chapters"]}
wj(F/"analysis/REVERSE_OUTLINE_OVERRIDE_046_050.json",{"schema_version":1,"updated_at":"2026-08-24","status":"ACTIVE_OVERRIDE / BUNDLE_046_050 / BRIDGE_CURRENT_RECONCILED","baseline":"baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json","chapters":[by[n] for n in range(46,51)]});wj(F/"analysis/REVERSE_OUTLINE_OVERRIDE_051_055.json",{"schema_version":1,"updated_at":"2026-08-24","status":"ACTIVE_OVERRIDE / BUNDLE_051_055 / BRIDGE_CURRENT_RECONCILED","baseline":"baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json","chapters":[by[n] for n in range(51,56)]});wj(F/"analysis/REVERSE_OUTLINE_OVERRIDE_056_MIGRATION_BOUNDARY.json",{"schema_version":1,"updated_at":"2026-08-24","status":"ACTIVE_OVERRIDE / LEGACY_TAIL_BOUNDARY_056","baseline":"baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json","chapters":[by[56]]})
rop=F/"analysis/REVERSE_OUTLINE_001_225.json";ro=json.loads(rop.read_text(encoding="utf-8"));ovs=[x for x in ro["overrides"] if x!="REVERSE_OUTLINE_OVERRIDE_051_MIGRATION_BOUNDARY.json"]
for q in ("REVERSE_OUTLINE_OVERRIDE_051_055.json","REVERSE_OUTLINE_OVERRIDE_056_MIGRATION_BOUNDARY.json"):
 if q not in ovs:ovs.insert(ovs.index("REVERSE_OUTLINE_OVERRIDE_091_095.json"),q)
ro["overrides"]=ovs;wj(rop,ro)
scp=ROOT/"tools/check_fiction_scene_passes.py";s=scp.read_text(encoding="utf-8")
if '"fiction/manuscript/part-1/051-055.md"' not in s:
 marker='    "fiction/manuscript/side-story-lake/091-095.md": {';block='    "fiction/manuscript/part-1/051-055.md": {\n        "chapters": [51, 52, 53, 54, 55],\n        "boundaries": [50, 56],\n        "card_boundaries": ["제50→51화", "제51→52화", "제52→53화", "제53→54화", "제54→55화", "제55→56화"],\n    },\n'
 if marker not in s:raise SystemExit("scene-pass insertion marker missing")
 wt(scp,s.replace(marker,block+marker,1))
for p,fields in [(F/"ACTIVE_CONTEXT.md",{"frontier_observed_at_main":"null","last_frontier_change_pr":"59","pending_frontier_change_pr":"61","current_bundle_source":SOURCE_FILE,"current_bundle_source_sha256":SOURCE_SHA,"reconciled_prefix_end":"55","legacy_tail_starts_at":"56","boundary_after_chapter":"55","next_bounded_bundle":"fiction/manuscript/part-1/056-060.md","main_production_prefix_end":"50","candidate_prefix_end":"55"}),(F/"HANDOFF.md",{"frontier_observed_at_main":"null","last_frontier_change_pr":"59","pending_frontier_change_pr":"61","current_bundle_source":SOURCE_FILE,"current_bundle_source_sha256":SOURCE_SHA,"reconciled_prefix_end":"55","legacy_tail_starts_at":"56","boundary_after_chapter":"55","next_bounded_bundle":"fiction/manuscript/part-1/056-060.md","main_production_prefix_end":"50","candidate_prefix_end":"55"})]:
 t=p.read_text(encoding="utf-8")
 for k,v in fields.items():t=sl(t,k,v)
 wt(p,t)
sp=ROOT/"[소설]/00_운영체계/START_HERE.md";t=sp.read_text(encoding="utf-8")
for k,v in {"current_bundle_source":SOURCE_FILE,"current_bundle_source_sha256":SOURCE_SHA,"repository_reconciled_prefix":"001-050","legacy_tail_starts_at":"056","last_frontier_change_pr":"59","next_bundle":"fiction/manuscript/part-1/051-055.md","main_production_prefix":"001-050","repository_candidate_prefix":"001-055","pending_frontier_pr":"61","next_bundle_after_merge":"fiction/manuscript/part-1/056-060.md"}.items():t=sl(t,k,v)
wt(sp,t)
mp=F/"FICTION_MASTER.md";t=mp.read_text(encoding="utf-8")
for k,v in {"current_bundle_source":SOURCE_FILE,"current_bundle_source_sha256":SOURCE_SHA,"reconciled_prefix":"001-055","legacy_tail_starts_at":"056","boundary_after_chapter":"055","last_frontier_change_pr":"59","pending_frontier_change_pr":"61","next_reconciliation":"056-060"}.items():t=sl(t,k,v)
wt(mp,t)
for p in (F/"ACTIVE_CONTEXT.md",F/"FICTION_MASTER.md"):
 t=p.read_text(encoding="utf-8")
 if "## PR #61 candidate · Bridge 051–055 readback" not in t:wt(p,t+NOTE)
print("materialized Ch051-055 candidate + coupled consumers")
