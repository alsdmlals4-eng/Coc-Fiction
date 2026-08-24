#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
F = ROOT / "fiction"
SOURCE = "폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본(1).docx"
SOURCE_SHA = "9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad"
EXPECTED = {
    41: {"title":"잘 돌아왔다","pov":"엘리스 → 이안 → 주안","chars":4255,"sha":"3879d479bec2458e7da2afd78a9c6cc748c9a20e5c0be935d9de365ea05f942a"},
    42: {"title":"살아 돌아온 몸","pov":"엘리스 → 이안 → 주안 → 엘리스","chars":6012,"sha":"e48ad4266831cc8b74ececc7e7fb6f831012a0464005e61eb06fb369d0945a2f"},
    43: {"title":"확인하고 설명하겠습니다","pov":"주안 → 엘리스 → 주안 → 엘리스 → 이안 → 주안 → 엘리스","chars":7004,"sha":"7da555457ebd2debd70fafb41283f9973440d0e99ef098c3c4acc3ba200baaac"},
    44: {"title":"응답하지 않은 호출기","pov":"주안 → 엘리스 → 주안 → 이안 → 엘리스 → 주안 → 엘리스 → 이안","chars":6720,"sha":"6c885ee543a45f145e7d920f7fbb89b5ebb280bf1d4c891a2b671b3c428122dd"},
    45: {"title":"노란 옷은 안 입습니다","pov":"주안","chars":5876,"sha":"e73c81689638476f6736cd9361cdd22dc9e80a076822162856b7516e3a7c12a1"},
}
CH_RE = re.compile(r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)", re.M | re.S)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bodies() -> dict[int, str]:
    out = {}
    for path in sorted((F / "manuscript").rglob("*.md")):
        for m in CH_RE.finditer(path.read_text(encoding="utf-8")):
            out[int(m.group(1))] = m.group(4).strip()
    return out


def main() -> None:
    all_bodies = bodies()
    for n, exp in EXPECTED.items():
        body = all_bodies.get(n, "")
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if len(body) != exp["chars"] or actual != exp["sha"]:
            raise SystemExit(f"exact source not installed Ch{n}: chars={len(body)} sha={actual}")
    ch46_sha = hashlib.sha256(all_bodies[46].encode("utf-8")).hexdigest()
    expected46 = "33a9f6acb305e423e942789e62af90d7b446fd422cb81293f0ed87f084c5f0b2"
    if ch46_sha != expected46:
        raise SystemExit(f"legacy Ch46 boundary changed: {ch46_sha}")

    idx_override_rel = "analysis/MANUSCRIPT_INDEX_OVERRIDE_041_045.json"
    dump(F / idx_override_rel, {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / BUNDLE_041_045 / BRIDGE_CURRENT_RECONCILED_PENDING_PR57",
        "baseline": "analysis/baselines/MANUSCRIPT_INDEX_2026-07-23_PILOT.json",
        "chapters": [
            {"chapter": n, "title": EXPECTED[n]["title"], "pov": EXPECTED[n]["pov"], "body_chars": EXPECTED[n]["chars"], "body_sha256": EXPECTED[n]["sha"], "bundle": "fiction/manuscript/part-1/041-045.md"}
            for n in range(41, 46)
        ],
    })
    idx = load(F / "MANUSCRIPT_INDEX.json")
    if idx_override_rel not in idx["overrides"]:
        idx["overrides"].insert(idx["overrides"].index("analysis/MANUSCRIPT_INDEX_OVERRIDE_091_095.json"), idx_override_rel)
    idx["status"] = "ACTIVE / COMPOSED / 225_STORAGE_CHAPTERS / MIXED_MIGRATION / PENDING_CURRENT_PREFIX_001_045_PR57"
    dump(F / "MANUSCRIPT_INDEX.json", idx)

    registry_path = F / "analysis/SCENE_PASS_REGISTRY.json"
    registry = load(registry_path)
    rec = registry["external_artifact_reconciliation"]
    rec.update({
        "artifact": SOURCE,
        "artifact_sha256": SOURCE_SHA,
        "reconciled_prefix_end": 45,
        "legacy_tail_starts_at": 46,
        "boundary_after_chapter": 45,
        "whole_manuscript_continuity": "NOT_YET_CLAIMED",
        "rule": "Chapters 1-45 are the bounded reconciled candidate prefix on PR #57. Ch041-066 are Aftermath & 8-year Bridge; Part 2 begins Ch067+. Stored Ch46+ remain legacy until their own pass; 101-105 remains fail-closed.",
    })
    registry["completed_bundle_passes"] = [x for x in registry["completed_bundle_passes"] if x.get("bundle") != "fiction/manuscript/part-1/041-045.md"]
    registry["completed_bundle_passes"].append({
        "bundle": "fiction/manuscript/part-1/041-045.md",
        "chapters": [41,42,43,44,45],
        "boundary_chapters": [40,46],
        "scene_cards": "fiction/analysis/SCENE_CARDS_041_045.md",
        "revision_report": "fiction/reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_041_045.md",
        "source_files": [
            {"name": SOURCE, "sha256": SOURCE_SHA, "role": "user-designated Bridge source authority"},
            {"name": "fiction/CANON_REGISTRY.json", "role": "latest approved canon protection"},
        ],
        "chapter_shas": {str(n): EXPECTED[n]["sha"] for n in range(41,46)},
        "preserved_boundary_shas": {"40":"1de35b4f4ecb19706f05bac827ed916484f59a2e167a0d4277012696cd1d9f19", "46": expected46},
        "status": "COMPLETE_CURRENT_SOURCE_CANON_RECONCILIATION / BRIDGE_CANDIDATE_PREFIX / PENDING_PR57",
    })
    registry["next_bundle_passes"] = ["fiction/manuscript/part-1/046-050.md"]
    dump(registry_path, registry)

    receipt_path = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
    receipt = load(receipt_path)
    receipt["pending_frontier_change_pr"] = 57
    receipt["next_bounded_bundle"] = "fiction/manuscript/part-1/041-045.md"
    dump(receipt_path, receipt)

    with tempfile.TemporaryDirectory(prefix="bridge-outline-") as tmp:
        generated_path = Path(tmp) / "generated.json"
        subprocess.run([sys.executable, str(ROOT / "tools/build_fiction_reverse_outline.py"), "--materialize", str(generated_path)], cwd=ROOT, check=True)
        generated = load(generated_path)
    by = {int(x["chapter"]): x for x in generated["chapters"]}

    prev_path = F / "analysis/REVERSE_OUTLINE_OVERRIDE_036_040.json"
    prev = load(prev_path)
    prev["chapters"] = [by[int(x["chapter"])] if int(x["chapter"]) == 40 else x for x in prev["chapters"]]
    prev["status"] = "ACTIVE_OVERRIDE / BUNDLE_036_040 / CURRENT_RECONCILED"
    dump(prev_path, prev)

    dump(F / "analysis/REVERSE_OUTLINE_OVERRIDE_041_045.json", {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / BUNDLE_041_045 / BRIDGE_CURRENT_RECONCILED_PENDING_PR57",
        "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
        "chapters": [by[n] for n in range(41,46)],
    })
    dump(F / "analysis/REVERSE_OUTLINE_OVERRIDE_046_MIGRATION_BOUNDARY.json", {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / LEGACY_TAIL_BOUNDARY_046",
        "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
        "chapters": [by[46]],
    })
    outline_path = F / "analysis/REVERSE_OUTLINE_001_225.json"
    outline = load(outline_path)
    overrides = [x for x in outline["overrides"] if x != "REVERSE_OUTLINE_OVERRIDE_041_MIGRATION_BOUNDARY.json"]
    anchor = overrides.index("REVERSE_OUTLINE_OVERRIDE_091_095.json")
    for rel in ("REVERSE_OUTLINE_OVERRIDE_041_045.json", "REVERSE_OUTLINE_OVERRIDE_046_MIGRATION_BOUNDARY.json"):
        if rel not in overrides:
            overrides.insert(anchor, rel)
            anchor += 1
    outline["overrides"] = overrides
    dump(outline_path, outline)

    functions = {
        41: "Part 1 결전 직후 가족 재회와 살아 돌아온 관계의 비정상성을 Bridge의 출발점으로 재정렬한다.",
        42: "주안의 변화한 몸을 보상으로 단순화하지 않고 선택을 침식할 수 있는 후유상태로 검증한다.",
        43: "주안이 자기 감정의 기원을 확인하되 엘리스의 현재 감정을 대신 판정하지 않는 경계를 세운다.",
        44: "응답하지 않음을 영구 거절로 확정하지 않고 관계의 불확실성과 수신기 보존을 동시에 남긴다.",
        45: "황색과 거리를 둔 주안의 현재 선택을 고정하고 8년 Bridge의 다음 생활·훈련 축으로 넘긴다.",
    }
    cards = ["# SCENE CARDS · Bridge 041–045", "", f"> Source: `{SOURCE}` / `{SOURCE_SHA}`", "> Boundary: Part 1 001–040 → Bridge 041–066 → Part 2 067+", ""]
    for n in range(41,46):
        cards += [f"## 제{n}화 · {EXPECTED[n]['title']}", f"- POV: {EXPECTED[n]['pov']}", f"- 기능: {functions[n]}", f"- body SHA256: `{EXPECTED[n]['sha']}`", ""]
    for left,right in ((40,41),(41,42),(42,43),(43,44),(44,45),(45,46)):
        cards += [f"## 제{left}→{right}화", f"- 판정: {'DIRECT_CONTINUITY_PASS' if right <= 45 else 'FAIL_CLOSED_UNTIL_NEXT_PROMOTION'}", ""]
    (F / "analysis/SCENE_CARDS_041_045.md").write_text("\n".join(cards)+"\n", encoding="utf-8")
    (F / "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_041_045.md").write_text(
        f"# REVISION · Bridge 041–045 current reconciliation · 2026-08-24\n\n- source: `{SOURCE}`\n- source SHA256: `{SOURCE_SHA}`\n- exact-transfer chapters: 41–45\n- structure: Part 1 `001–040` → Aftermath & 8-year Bridge `041–066` → Part 2 `067+`\n- candidate boundary: `045→046`\n- whole manuscript continuity: `NOT_YET_CLAIMED`\n\n## Canon guards\n- 엘리스 D04 인간 포함 정신조작 가능 범위 유지.\n- Ch43 주안은 자기 감정 기원만 검증하며 엘리스의 현재 선택을 대신 판정하지 않음.\n- Ch44 미응답은 영구 이별/거절이 아니며 수신기를 버리지 않음.\n- 라르고 `[규율]` 실제 공개는 Rift Accord까지 금지.\n- `복종인자` / `조작된 감정` 프레임 재도입 금지.\n",
        encoding="utf-8",
    )

    checker = ROOT / "tools/check_fiction_scene_passes.py"
    s = checker.read_text(encoding="utf-8")
    if '"fiction/manuscript/part-1/041-045.md"' not in s:
        marker = '    "fiction/manuscript/side-story-lake/091-095.md": {'
        addition = '    "fiction/manuscript/part-1/041-045.md": {\n        "chapters": [41, 42, 43, 44, 45],\n        "boundaries": [40, 46],\n        "card_boundaries": ["제40→41화", "제41→42화", "제42→43화", "제43→44화", "제44→45화", "제45→46화"],\n    },\n'
        if marker not in s:
            raise SystemExit("scene-pass checker insertion marker missing")
        s = s.replace(marker, addition + marker, 1)
    s = s.replace('if reconciliation.get("reconciled_prefix_end") != 40:', 'if reconciliation.get("reconciled_prefix_end") != 45:')
    s = s.replace('reconciled prefix must be chapter 40', 'reconciled prefix must be chapter 45')
    s = s.replace('if reconciliation.get("legacy_tail_starts_at") != 41:', 'if reconciliation.get("legacy_tail_starts_at") != 46:')
    s = s.replace('legacy tail must begin at chapter 41', 'legacy tail must begin at chapter 46')
    s = s.replace('if reconciliation.get("boundary_after_chapter") != 40:', 'if reconciliation.get("boundary_after_chapter") != 45:')
    s = s.replace('migration boundary must be after chapter 40', 'migration boundary must be after chapter 45')
    s = s.replace('((10, 11), (15, 16), (20, 21), (25, 26), (30, 31), (35, 36))', '((10, 11), (15, 16), (20, 21), (25, 26), (30, 31), (35, 36), (40, 41))')
    s = s.replace('001-040 candidate prefix; migration boundary 40→41', '001-045 candidate prefix; migration boundary 45→46')
    checker.write_text(s, encoding="utf-8")

    review_path = ROOT / "docs/coordination/2026-08-24_COC_PROMOTION_041_045_ADVERSARIAL_REVIEW.md"
    review_path.write_text(
        "# COC Bridge Promotion 041–045 · 5× Adversarial Review — 2026-08-24\n\n"
        "1. **Part boundary / distortion** — 001–040 Part 1, 041–066 Bridge, 067+ Part 2를 분리하고 Part 2 상태를 Bridge에 선반영하지 않음. PASS.\n"
        "2. **Agency / relationship** — Ch43 주안의 불확실성은 자기 감정 기원에 한정; 엘리스의 현재 선택을 대신 부정하지 않음. Ch44 미응답은 영구 이별이 아니며 수신기 보존. PASS.\n"
        "3. **Power / reveal timing** — 엘리스 D04 인간 포함 범위 유지; 장면별 비사용을 능력 부재로 해석하지 않음. 라르고 `[규율]` 공개 없음. PASS.\n"
        "4. **Canon / omission / regression** — `복종인자`, `조작된 감정`, `히템`, `앨리스` 재도입 없음; 101–105 source gap 유지. PASS.\n"
        "5. **Provenance / boundary / maintenance** — 041–045 exact source SHA 고정, Ch40→41 current 연결, Ch45→46 fail-closed, Ch46 body 보존. 임시 자동화는 merge 전 제거 예정. PASS.\n\n"
        "`CLEAN_REVIEW_EXIT` is contingent on exact-head hosted CI Green, unresolved review threads 0, and latest-main freshness.\n",
        encoding="utf-8",
    )
    print("patched Bridge 041-045 consumers")


if __name__ == "__main__":
    main()
