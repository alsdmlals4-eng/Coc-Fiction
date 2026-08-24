#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
F = ROOT / "fiction"
SOURCE = "폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx"
SOURCE_SHA = "89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10"
EXPECTED = {
    36: {"title":"사명은 끝났다","pov":"엘리스 → 주안 → 엘리스 → 이안 → 주안","chars":6242,"sha":"a73ee6d8d4f99ab24e7604ae891b58da420ce5549777395c262da69ea340b358"},
    37: {"title":"승자의 손","pov":"엘리스 → 이안 → 엘리스","chars":5872,"sha":"53604e0ca6bcddd2beebb996aeb102ff7417a645c31e3340880bc451da8dc3e8"},
    38: {"title":"인질은 제가 되죠","pov":"엘리스 → 이안 → 엘리스 → 이안","chars":5821,"sha":"c8a9f4a4c867009b73e11257af21bf6050e5b146e4d9c2dc3ffed34d541186d5"},
    39: {"title":"군함이 왔다","pov":"주안 → 엘리스 → 이안","chars":6163,"sha":"8ad77ac006e209745a56b4cbba6d3ba26f7a5a55fa75ff00a8dd2efe39955472"},
    40: {"title":"아버지의 자리","pov":"엘리스 → 이안 → 엘리스","chars":6237,"sha":"1de35b4f4ecb19706f05bac827ed916484f59a2e167a0d4277012696cd1d9f19"},
}
CH_RE = re.compile(r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)", re.M | re.S)

def load(path): return json.loads(path.read_text(encoding="utf-8"))
def dump(path, data): path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def all_bodies():
    out = {}
    for path in sorted((F / "manuscript").rglob("*.md")):
        for m in CH_RE.finditer(path.read_text(encoding="utf-8")):
            out[int(m.group(1))] = m.group(4).strip()
    return out

def compose(path):
    manifest = load(path)
    base = load(path.parent / manifest["baseline"])
    by = {int(item["chapter"]): item for item in base["chapters"]}
    for rel in manifest.get("overrides", []):
        for item in load(path.parent / rel).get("chapters", []):
            by[int(item["chapter"])] = item
    return by

def main():
    bodies = all_bodies()
    for number, exp in EXPECTED.items():
        body = bodies[number]
        if len(body) != exp["chars"] or hashlib.sha256(body.encode()).hexdigest() != exp["sha"]:
            raise SystemExit(f"exact manuscript not installed for Ch{number}")
    old41_sha = hashlib.sha256(bodies[41].encode()).hexdigest()

    index_override = {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / BUNDLE_036_040 / CURRENT_RECONCILED_PENDING_PR55",
        "baseline": "analysis/baselines/MANUSCRIPT_INDEX_2026-07-23_PILOT.json",
        "chapters": [
            {"chapter": n, "title": EXPECTED[n]["title"], "pov": EXPECTED[n]["pov"], "body_chars": EXPECTED[n]["chars"], "body_sha256": EXPECTED[n]["sha"], "bundle": "fiction/manuscript/part-1/036-040.md"}
            for n in range(36, 41)
        ],
    }
    dump(F / "analysis/MANUSCRIPT_INDEX_OVERRIDE_036_040.json", index_override)
    index = load(F / "MANUSCRIPT_INDEX.json")
    rel = "analysis/MANUSCRIPT_INDEX_OVERRIDE_036_040.json"
    if rel not in index["overrides"]:
        index["overrides"].insert(index["overrides"].index("analysis/MANUSCRIPT_INDEX_OVERRIDE_091_095.json"), rel)
    index["status"] = "ACTIVE / COMPOSED / 225_STORAGE_CHAPTERS / MIXED_MIGRATION / PENDING_CURRENT_PREFIX_001_040_PR55"
    dump(F / "MANUSCRIPT_INDEX.json", index)

    outline_manifest_path = F / "analysis/REVERSE_OUTLINE_001_225.json"
    composed = compose(outline_manifest_path)
    prior = load(F / "analysis/REVERSE_OUTLINE_OVERRIDE_031_035.json")
    ch35 = next(item for item in prior["chapters"] if int(item["chapter"]) == 35)
    ch35["next_chapter"] = {"chapter": 36, "title": EXPECTED[36]["title"], "pov": EXPECTED[36]["pov"]}
    ch35["structural_flags"] = [flag for flag in ch35.get("structural_flags", []) if flag != "RECONCILIATION_MIGRATION_BOUNDARY"]
    prior["status"] = "ACTIVE_OVERRIDE / BUNDLE_031_035 / CURRENT_RECONCILED"
    dump(F / "analysis/REVERSE_OUTLINE_OVERRIDE_031_035.json", prior)

    entries = []
    for n in range(36, 41):
        item = dict(composed[n])
        item["chapter"] = n
        item["section"] = {"key": "part-1", "label": "1부 《폭풍의 눈》"}
        item["title"] = EXPECTED[n]["title"]
        item["pov"] = EXPECTED[n]["pov"]
        item["source"] = {"bundle": "fiction/manuscript/part-1/036-040.md", "body_sha256": EXPECTED[n]["sha"], "body_chars": EXPECTED[n]["chars"]}
        flags = [flag for flag in item.get("structural_flags", []) if flag not in ("LEGACY_TAIL_BOUNDARY", "RECONCILIATION_MIGRATION_BOUNDARY")]
        if n == 40: flags.append("RECONCILIATION_MIGRATION_BOUNDARY")
        item["structural_flags"] = list(dict.fromkeys(flags))
        item["previous_chapter"] = {"chapter": n - 1, "title": EXPECTED[n - 1]["title"], "pov": EXPECTED[n - 1]["pov"]} if n > 36 else {"chapter": 35, "title": "완전 소 생물", "pov": "이안 → 주안 → 엘리스 → 이안 → 주안 → 엘리스"}
        item["next_chapter"] = {"chapter": n + 1, "title": EXPECTED[n + 1]["title"], "pov": EXPECTED[n + 1]["pov"]} if n < 40 else None
        entries.append(item)
    dump(F / "analysis/REVERSE_OUTLINE_OVERRIDE_036_040.json", {"schema_version": 1, "updated_at": "2026-08-24", "status": "ACTIVE_OVERRIDE / BUNDLE_036_040 / CURRENT_RECONCILED_PENDING_PR55", "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json", "chapters": entries})
    ch41 = dict(composed[41])
    ch41["previous_chapter"] = None
    flags = [flag for flag in ch41.get("structural_flags", []) if flag != "RECONCILIATION_MIGRATION_BOUNDARY"]
    if "LEGACY_TAIL_BOUNDARY" not in flags: flags.append("LEGACY_TAIL_BOUNDARY")
    ch41["structural_flags"] = flags
    dump(F / "analysis/REVERSE_OUTLINE_OVERRIDE_041_MIGRATION_BOUNDARY.json", {"schema_version": 1, "updated_at": "2026-08-24", "status": "ACTIVE_OVERRIDE / LEGACY_TAIL_BOUNDARY_041", "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json", "chapters": [ch41]})
    outline_manifest = load(outline_manifest_path)
    overrides = [rel for rel in outline_manifest["overrides"] if rel != "REVERSE_OUTLINE_OVERRIDE_036_MIGRATION_BOUNDARY.json"]
    for rel in ("REVERSE_OUTLINE_OVERRIDE_036_040.json", "REVERSE_OUTLINE_OVERRIDE_041_MIGRATION_BOUNDARY.json"):
        if rel not in overrides: overrides.insert(overrides.index("REVERSE_OUTLINE_OVERRIDE_091_095.json"), rel)
    outline_manifest["overrides"] = overrides
    dump(outline_manifest_path, outline_manifest)

    functions = {36:"세실리아 회수 직후 탈론의 사명과 결말을 닫고 자기 이유를 확인하는 주안을 대비한다.",37:"승자의 소유 프레임을 거부하고 행동 중지·협상으로 전환한다.",38:"엘리스가 자발적 인질 제안을 협상 도구로 선택해 정치 전환을 주도한다.",39:"델타그린 군함 도착으로 전장 권력축을 재배치한다.",40:"윌리엄의 사랑과 죄를 동시에 인정하면서 그의 방식이 아닌 자기 방식의 책임을 선택해 Part 1을 닫는다."}
    cards = ["# SCENE CARDS · 036–040", "", f"> Source: `{SOURCE}` / `{SOURCE_SHA}`", ""]
    for n in range(36, 41): cards += [f"## 제{n}화 · {EXPECTED[n]['title']}", f"- POV: {EXPECTED[n]['pov']}", f"- 기능: {functions[n]}", f"- body SHA256: `{EXPECTED[n]['sha']}`", ""]
    for left, right in ((35,36),(36,37),(37,38),(38,39),(39,40),(40,41)): cards += [f"## 제{left}→{right}화", f"- 판정: {'DIRECT_CONTINUITY_PASS' if right <= 40 else 'FAIL_CLOSED_UNTIL_NEXT_PROMOTION'}", ""]
    (F / "analysis/SCENE_CARDS_036_040.md").write_text("\n".join(cards) + "\n", encoding="utf-8")
    (F / "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_036_040.md").write_text(f"# REVISION · 036–040 current reconciliation · 2026-08-24\n\n- source: `{SOURCE}`\n- source SHA256: `{SOURCE_SHA}`\n- exact-transfer chapters: 36–40\n- candidate boundary: 040→041\n- whole manuscript continuity: `NOT_YET_CLAIMED`\n\n## Canon guards\n- 엘리스 인간 포함 정신조작 가능 범위 유지; 선택 보존은 윤리·자기규율.\n- 탈론 Ch36 source-supported 결말과 Part 1 core-antagonist 위상 보존.\n- 세실리아 생존 상태와 미확정 원인·귀속 보존.\n- 황색 지휘부 손실을 조직 전체 소멸로 평탄화하지 않음.\n- 라르고 `[규율]` Part 1 공개 금지.\n- 라자크 explicit death evidence 없으면 UNKNOWN.\n", encoding="utf-8")

    registry_path = F / "analysis/SCENE_PASS_REGISTRY.json"
    registry = load(registry_path)
    rec = registry["external_artifact_reconciliation"]
    rec.update({"artifact": SOURCE, "artifact_sha256": SOURCE_SHA, "reconciled_prefix_end": 40, "legacy_tail_starts_at": 41, "boundary_after_chapter": 40, "whole_manuscript_continuity": "NOT_YET_CLAIMED", "rule": "Chapters 1-40 are the bounded reconciled candidate prefix on PR #55. Stored Ch41+ remain legacy tail until their own pass; 101-105 remains fail-closed."})
    registry["completed_bundle_passes"] = [item for item in registry["completed_bundle_passes"] if item.get("bundle") != "fiction/manuscript/part-1/036-040.md"]
    registry["completed_bundle_passes"].append({"bundle":"fiction/manuscript/part-1/036-040.md","chapters":[36,37,38,39,40],"boundary_chapters":[35,41],"scene_cards":"fiction/analysis/SCENE_CARDS_036_040.md","revision_report":"fiction/reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_036_040.md","source_files":[{"name":SOURCE,"sha256":SOURCE_SHA,"role":"user-designated source authority"},{"name":"fiction/CANON_REGISTRY.json","role":"latest approved canon protection"}],"chapter_shas":{str(n):EXPECTED[n]["sha"] for n in range(36,41)},"preserved_boundary_shas":{"35":"c4b02af3eb326dfd18ec0331c762c92655cb97525b8b3223d407e69ce912d5f2","41":old41_sha},"status":"COMPLETE_CURRENT_SOURCE_CANON_RECONCILIATION / CANDIDATE_PREFIX / PENDING_PR55"})
    registry["next_bundle_passes"] = ["fiction/manuscript/part-1/041-045.md"]
    dump(registry_path, registry)

    receipt_path = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
    receipt = load(receipt_path)
    receipt["pending_frontier_change_pr"] = 55
    receipt["next_bounded_bundle"] = "fiction/manuscript/part-1/036-040.md"
    dump(receipt_path, receipt)

    review = "# COC Promotion 036–040 · 5× Adversarial Review — 2026-08-24\n\n1. Identity/life-state: Cecilia alive entering Ch36; Milly/Hatem separate; Lhazak UNKNOWN without proof. PASS.\n2. Power/reveal timing: Elise D04 human-inclusive; Largo `[규율]` not revealed in Part 1. PASS.\n3. Faction flattening: Yellow leadership loss != organization extinction; Garon negotiation != permanent faction conversion. PASS.\n4. Agency/theme: Jooan self-check and Elise negotiation remain choices; William love does not erase wrongdoing. PASS.\n5. Boundary/provenance: Ch35→36 candidate-current; Ch40→41 fail-closed; 101–105 gap and whole continuity unresolved. PASS.\n\n`CLEAN_REVIEW_EXIT` contingent on exact-head hosted validation Green.\n"
    (ROOT / "docs/coordination/2026-08-24_COC_PROMOTION_036_040_ADVERSARIAL_REVIEW.md").write_text(review, encoding="utf-8")

    checker = ROOT / "tools/check_fiction_scene_passes.py"
    s = checker.read_text(encoding="utf-8")
    marker = '    "fiction/manuscript/side-story-lake/091-095.md": {'
    addition = '    "fiction/manuscript/part-1/036-040.md": {\n        "chapters": [36, 37, 38, 39, 40],\n        "boundaries": [35, 41],\n        "card_boundaries": ["제35→36화", "제36→37화", "제37→38화", "제38→39화", "제39→40화", "제40→41화"],\n    },\n'
    if '"fiction/manuscript/part-1/036-040.md": {' not in s: s = s.replace(marker, addition + marker)
    s = s.replace('    35: "완전 소 생물씨.",\n    91:', '    35: "완전 소 생물씨.",\n    36: "사명은 끝났다",\n    37: "승자의 손",\n    38: "인질은 제가 되죠",\n    39: "군함이 왔다",\n    40: "아버지의 자리",\n    91:')
    s = s.replace('("006-010.md", "011-015.md", "016-020.md", "021-025.md", "026-030.md", "031-035.md")', '("006-010.md", "011-015.md", "016-020.md", "021-025.md", "026-030.md", "031-035.md", "036-040.md")')
    s = s.replace('reconciliation.get("reconciled_prefix_end") != 35', 'reconciliation.get("reconciled_prefix_end") != 40').replace('reconciled prefix must be chapter 35 after current 031-035 propagation', 'reconciled prefix must be chapter 40 after current 036-040 propagation').replace('reconciliation.get("legacy_tail_starts_at") != 36', 'reconciliation.get("legacy_tail_starts_at") != 41').replace('legacy tail must begin at chapter 36 after current 031-035 propagation', 'legacy tail must begin at chapter 41 after current 036-040 propagation').replace('reconciliation.get("boundary_after_chapter") != 35', 'reconciliation.get("boundary_after_chapter") != 40').replace('migration boundary must be after chapter 35', 'migration boundary must be after chapter 40').replace('((10, 11), (15, 16), (20, 21), (25, 26), (30, 31))', '((10, 11), (15, 16), (20, 21), (25, 26), (30, 31), (35, 36))')
    checker.write_text(s, encoding="utf-8")
    print(f"patched 036-040 consumers; preserved Ch41 body SHA {old41_sha}")

if __name__ == "__main__":
    main()
