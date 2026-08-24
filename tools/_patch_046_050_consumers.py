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
PENDING_PR = 59
MAIN_PREFIX = 45
CANDIDATE_PREFIX = 50
TAIL = 51
NEXT_BUNDLE = "fiction/manuscript/part-1/051-055.md"
EXPECTED = {
    46: {"title":"자아를 찾으러 떠났습니다","pov":"주안","chars":5861,"sha":"ae3928bb6234eb4086115c74614d43aee3b436aa52cc30d14641a5673878791d"},
    47: {"title":"호수가 보이는 마을","pov":"이안 → 주안 → 이안","chars":6228,"sha":"03e0e7c4fcbfedd4326f335bdc5f49b79fbaf3acc2c1ceaa8e56fa91c8bc6a83"},
    48: {"title":"돼지고기는 아니었습니다","pov":"주안 → 이안","chars":5800,"sha":"4cd101ebbb686f269ae2efe1e3e40eba11edd75420c3782aa8918f58df8bb41e"},
    49: {"title":"여덟 해 만입니다","pov":"이안 → 주안 → 이안 → 주안","chars":5793,"sha":"6408f1e4b70b7fdbe43912c5b43c0ce2394d1303a6cbc81f31ea4d0ff9f307be"},
    50: {"title":"낙원의 손님분들","pov":"이안 → 주안","chars":5296,"sha":"5b3bd9bcbb7b3d04deb38dfdb39db2c9fdc56fb50df18ea9425562c9b484880e"},
}
CH_RE = re.compile(r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)", re.M | re.S)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parsed_bodies() -> dict[int, str]:
    out = {}
    for path in sorted((F / "manuscript").rglob("*.md")):
        for m in CH_RE.finditer(path.read_text(encoding="utf-8")):
            out[int(m.group(1))] = m.group(4).strip()
    return out


def patch_yaml(path: Path, replacements: dict[str, str], additions: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.find("```yaml\n")
    end = text.find("\n```", start + 8)
    if start < 0 or end < 0:
        raise SystemExit(f"yaml block missing: {path}")
    body_start = start + len("```yaml\n")
    lines = text[body_start:end].splitlines()
    seen = set()
    out = []
    for line in lines:
        key = line.split(":", 1)[0].strip() if ":" in line else ""
        if key in replacements:
            out.append(f"{key}: {replacements[key]}")
            seen.add(key)
        elif key in {item.split(":", 1)[0].strip() for item in additions}:
            continue
        else:
            out.append(line)
    missing = set(replacements) - seen
    if missing:
        raise SystemExit(f"yaml keys missing in {path}: {sorted(missing)}")
    out.extend(additions)
    path.write_text(text[:body_start] + "\n".join(out) + text[end:], encoding="utf-8")


def patch_scene_checker() -> None:
    path = ROOT / "tools/check_fiction_scene_passes.py"
    text = path.read_text(encoding="utf-8")
    if '"fiction/manuscript/part-1/046-050.md"' not in text:
        marker = '    "fiction/manuscript/side-story-lake/091-095.md": {'
        addition = '''    "fiction/manuscript/part-1/046-050.md": {
        "chapters": [46, 47, 48, 49, 50],
        "boundaries": [45, 51],
        "card_boundaries": ["제45→46화", "제46→47화", "제47→48화", "제48→49화", "제49→50화", "제50→51화"],
    },
'''
        if marker not in text:
            raise SystemExit("scene-pass expected-pass marker missing")
        text = text.replace(marker, addition + marker, 1)

    old = '''if reconciliation.get("reconciled_prefix_end") != 45:
    errors.append("reconciled prefix must match the current bounded frontier")
if reconciliation.get("legacy_tail_starts_at") != 46:
    errors.append("legacy tail must begin immediately after the current bounded frontier")
if reconciliation.get("boundary_after_chapter") != 45:
    errors.append("migration boundary must be after chapter 45")
'''
    new = '''part1_completed = []
for item in passes:
    bundle = str(item.get("bundle", ""))
    chapters = sorted(int(x) for x in item.get("chapters", []))
    if bundle.startswith("fiction/manuscript/part-1/") and chapters:
        part1_completed.append((chapters[0], chapters[-1], item))
part1_completed.sort(key=lambda row: row[0])
expected_frontier = 0
for start, end, _item in part1_completed:
    if start == expected_frontier + 1 and list(range(start, end + 1)) == list(range(start, end + 1)):
        expected_frontier = end
    elif start > expected_frontier + 1:
        break
if reconciliation.get("reconciled_prefix_end") != expected_frontier:
    errors.append(f"reconciled prefix must match completed sequential frontier {expected_frontier}")
if reconciliation.get("legacy_tail_starts_at") != expected_frontier + 1:
    errors.append("legacy tail must begin immediately after the completed sequential frontier")
if reconciliation.get("boundary_after_chapter") != expected_frontier:
    errors.append(f"migration boundary must be after chapter {expected_frontier}")
'''
    if old in text:
        text = text.replace(old, new, 1)

    old_loop = 'for left_number, right_number in ((10, 11), (15, 16), (20, 21), (25, 26), (30, 31), (35, 36), (40, 41)):'
    new_loop = '''sequential_boundaries = []
for previous, current in zip(part1_completed, part1_completed[1:]):
    left_number = previous[1]
    right_number = current[0]
    if left_number + 1 == right_number and right_number <= current_frontier:
        sequential_boundaries.append((left_number, right_number))
for left_number, right_number in sequential_boundaries:'''
    if old_loop in text:
        text = text.replace(old_loop, new_loop, 1)

    old_bundles = 'for bundle_name in ("006-010.md", "011-015.md", "016-020.md", "021-025.md", "026-030.md", "031-035.md", "036-040.md"):\n    current_bundle = (FICTION / "manuscript" / "part-1" / bundle_name).read_text(encoding="utf-8")'
    new_bundles = '''current_part1_bundles = sorted(
    Path(str(item.get("bundle"))).name
    for item in passes
    if str(item.get("bundle", "")).startswith("fiction/manuscript/part-1/")
    and item.get("chapters")
    and max(int(x) for x in item.get("chapters", [])) <= current_frontier
)
for bundle_name in current_part1_bundles:
    current_bundle = (FICTION / "manuscript" / "part-1" / bundle_name).read_text(encoding="utf-8")'''
    if old_bundles in text:
        text = text.replace(old_bundles, new_bundles, 1)

    path.write_text(text, encoding="utf-8")


def main() -> None:
    bodies = parsed_bodies()
    for number, expected in EXPECTED.items():
        body = bodies.get(number, "")
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if len(body) != expected["chars"] or actual != expected["sha"]:
            raise SystemExit(f"exact manuscript not installed Ch{number}: chars={len(body)} sha={actual}")
    ch51_sha = hashlib.sha256(bodies[51].encode("utf-8")).hexdigest()
    expected51 = "f149a848ef8c2069d0e461a8b9fe1a73b657c77b9e5327196ce905cfafb60ac1"
    if ch51_sha != expected51:
        raise SystemExit(f"legacy Ch51 boundary changed: {ch51_sha}")

    index_rel = "analysis/MANUSCRIPT_INDEX_OVERRIDE_046_050.json"
    dump(F / index_rel, {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / BUNDLE_046_050 / BRIDGE_CURRENT_RECONCILED_PENDING_PR59",
        "baseline": "analysis/baselines/MANUSCRIPT_INDEX_2026-07-23_PILOT.json",
        "chapters": [
            {"chapter": n, "title": EXPECTED[n]["title"], "pov": EXPECTED[n]["pov"], "body_chars": EXPECTED[n]["chars"], "body_sha256": EXPECTED[n]["sha"], "bundle": "fiction/manuscript/part-1/046-050.md"}
            for n in range(46, 51)
        ],
    })
    index_path = F / "MANUSCRIPT_INDEX.json"
    index = load(index_path)
    if index_rel not in index["overrides"]:
        index["overrides"].insert(index["overrides"].index("analysis/MANUSCRIPT_INDEX_OVERRIDE_091_095.json"), index_rel)
    index["status"] = "ACTIVE / COMPOSED / 225_STORAGE_CHAPTERS / MIXED_MIGRATION / PENDING_CURRENT_PREFIX_001_050_PR59"
    dump(index_path, index)

    registry_path = F / "analysis/SCENE_PASS_REGISTRY.json"
    registry = load(registry_path)
    rec = registry["external_artifact_reconciliation"]
    rec.update({
        "artifact": SOURCE,
        "artifact_sha256": SOURCE_SHA,
        "reconciled_prefix_end": CANDIDATE_PREFIX,
        "legacy_tail_starts_at": TAIL,
        "boundary_after_chapter": CANDIDATE_PREFIX,
        "whole_manuscript_continuity": "NOT_YET_CLAIMED",
        "rule": "Chapters 1-50 are the bounded reconciled candidate prefix on PR #59. Ch041-066 are Aftermath & 8-year Bridge; Part 2 begins Ch067+. Stored Ch51+ remain legacy until their own pass; 101-105 remains fail-closed.",
    })
    registry["completed_bundle_passes"] = [x for x in registry["completed_bundle_passes"] if x.get("bundle") != "fiction/manuscript/part-1/046-050.md"]
    registry["completed_bundle_passes"].append({
        "bundle": "fiction/manuscript/part-1/046-050.md",
        "chapters": [46,47,48,49,50],
        "boundary_chapters": [45,51],
        "scene_cards": "fiction/analysis/SCENE_CARDS_046_050.md",
        "revision_report": "fiction/reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_046_050.md",
        "source_files": [
            {"name": SOURCE, "sha256": SOURCE_SHA, "role": "user-designated Bridge source authority"},
            {"name": "fiction/CANON_REGISTRY.json", "role": "latest approved canon protection"},
        ],
        "chapter_shas": {str(n): EXPECTED[n]["sha"] for n in range(46,51)},
        "preserved_boundary_shas": {"45":"e73c81689638476f6736cd9361cdd22dc9e80a076822162856b7516e3a7c12a1", "51": expected51},
        "status": "COMPLETE_CURRENT_SOURCE_CANON_RECONCILIATION / BRIDGE_CANDIDATE_PREFIX / PENDING_PR59",
    })
    registry["next_bundle_passes"] = [NEXT_BUNDLE]
    dump(registry_path, registry)

    receipt_path = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
    receipt = load(receipt_path)
    receipt.update({
        "frontier_observed_at_main": None,
        "last_frontier_change_pr": 57,
        "pending_frontier_change_pr": PENDING_PR,
        "verified_prefix_end": CANDIDATE_PREFIX,
        "legacy_tail_starts_at": TAIL,
        "boundary_after_chapter": CANDIDATE_PREFIX,
        "next_bounded_bundle": NEXT_BUNDLE,
        "candidate_sha256": SOURCE_SHA,
        "whole_manuscript_continuity": "NOT_YET_CLAIMED",
    })
    dump(receipt_path, receipt)

    with tempfile.TemporaryDirectory(prefix="bridge-046-outline-") as tmp:
        generated_path = Path(tmp) / "generated.json"
        subprocess.run([sys.executable, str(ROOT / "tools/build_fiction_reverse_outline.py"), "--materialize", str(generated_path)], cwd=ROOT, check=True)
        generated = load(generated_path)
    by = {int(item["chapter"]): item for item in generated["chapters"]}

    prior_path = F / "analysis/REVERSE_OUTLINE_OVERRIDE_041_045.json"
    prior = load(prior_path)
    prior["chapters"] = [by[45] if int(item["chapter"]) == 45 else item for item in prior["chapters"]]
    prior["status"] = "ACTIVE_OVERRIDE / BUNDLE_041_045 / BRIDGE_CURRENT_RECONCILED"
    dump(prior_path, prior)

    dump(F / "analysis/REVERSE_OUTLINE_OVERRIDE_046_050.json", {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / BUNDLE_046_050 / BRIDGE_CURRENT_RECONCILED_PENDING_PR59",
        "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
        "chapters": [by[n] for n in range(46,51)],
    })
    dump(F / "analysis/REVERSE_OUTLINE_OVERRIDE_051_MIGRATION_BOUNDARY.json", {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / LEGACY_TAIL_BOUNDARY_051",
        "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
        "chapters": [by[51]],
    })
    outline_path = F / "analysis/REVERSE_OUTLINE_001_225.json"
    outline = load(outline_path)
    overrides = [x for x in outline["overrides"] if x != "REVERSE_OUTLINE_OVERRIDE_046_MIGRATION_BOUNDARY.json"]
    anchor = overrides.index("REVERSE_OUTLINE_OVERRIDE_091_095.json")
    for rel in ("REVERSE_OUTLINE_OVERRIDE_046_050.json", "REVERSE_OUTLINE_OVERRIDE_051_MIGRATION_BOUNDARY.json"):
        if rel not in overrides:
            overrides.insert(anchor, rel)
            anchor += 1
    outline["overrides"] = overrides
    dump(outline_path, outline)

    functions = {
        46: "주안이 황색에서의 장기 체류를 소속·복종이 아니라 계약 가능한 손님 관계로 규정하고, 임무 뒤 귀환 여부도 자기 선택으로 남긴다.",
        47: "8년 뒤 이안과 주안의 독립 성장선을 병치하고 호수가 보이는 마을의 실종·기억 혼란 사건과 재회를 같은 방향으로 모은다.",
        48: "식당의 수상한 고기와 실종 흔적을 검증하며, 이안이 묶인 아킴을 확인해 재회보다 생존 구조를 먼저 선택한다.",
        49: "8년 만의 이안·주안·아킴 재회를 성립시키면서 가론의 오래된 폭력 패턴을 다시 제어하고 낙원 치료시설로 목적선을 합친다.",
        50: "절단기·총보다 문과 대화를 먼저 시도하고 낙원 내부에 환자 위장으로 진입해 루바와 기억에 작용하는 물의 다음 압력을 연다.",
    }
    cards = ["# SCENE CARDS · Bridge 046–050", "", f"> Source: `{SOURCE}` / `{SOURCE_SHA}`", "> Boundary: Part 1 001–040 → Bridge 041–066 → Part 2 067+", ""]
    for n in range(46,51):
        cards += [f"## 제{n}화 · {EXPECTED[n]['title']}", f"- POV: {EXPECTED[n]['pov']}", f"- 기능: {functions[n]}", f"- body SHA256: `{EXPECTED[n]['sha']}`", ""]
    for left,right in ((45,46),(46,47),(47,48),(48,49),(49,50),(50,51)):
        cards += [f"## 제{left}→{right}화", f"- 판정: {'DIRECT_CONTINUITY_PASS' if right <= 50 else 'FAIL_CLOSED_UNTIL_NEXT_PROMOTION'}", ""]
    (F / "analysis/SCENE_CARDS_046_050.md").write_text("\n".join(cards)+"\n", encoding="utf-8")
    (F / "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_046_050.md").write_text(
        f"# REVISION · Bridge 046–050 current reconciliation · 2026-08-24\n\n- source: `{SOURCE}`\n- source SHA256: `{SOURCE_SHA}`\n- source-derived chapters: 46–50\n- Ch47 canon-directed reconciliation: source body `ed332a61c44bdac0ca394b5f8f6f24ab75c4d388bc289677768aeaee015c9e6a` → production body `03e0e7c4fcbfedd4326f335bdc5f49b79fbaf3acc2c1ceaa8e56fa91c8bc6a83`; deprecated contact-axis label replaced by generic old external contact wording; event/information function unchanged.\n- structure: Part 1 `001–040` → Aftermath & 8-year Bridge `041–066` → Part 2 `067+`\n- candidate boundary: `050→051`\n- whole manuscript continuity: `NOT_YET_CLAIMED`\n\n## Canon guards\n- 주안의 황색 체류·이탈은 계약과 자기선택으로 읽고 복종 프레임으로 되돌리지 않음.\n- Ch49 재회는 8년의 독립 성장을 지우지 않음.\n- Ch50의 대화 우선과 환자 위장은 루바를 단순 악역으로 확정하지 않으며, 자발성만으로 충분한 설명·동의를 자동 확정하지 않음.\n- 엘리스 D04와 라르고 reveal timing은 기존 Canon을 그대로 유지.\n",
        encoding="utf-8",
    )

    patch_scene_checker()

    common = {
        "frontier_observed_at_main": "null",
        "last_frontier_change_pr": "57",
        "pending_frontier_change_pr": str(PENDING_PR),
        "reconciled_prefix_end": str(CANDIDATE_PREFIX),
        "legacy_tail_starts_at": str(TAIL),
        "boundary_after_chapter": str(CANDIDATE_PREFIX),
        "next_bounded_bundle": NEXT_BUNDLE,
    }
    patch_yaml(F / "ACTIVE_CONTEXT.md", common, [f"main_production_prefix_end: {MAIN_PREFIX}", f"candidate_prefix_end: {CANDIDATE_PREFIX}"])
    patch_yaml(F / "HANDOFF.md", common, [f"main_production_prefix_end: {MAIN_PREFIX}", f"candidate_prefix_end: {CANDIDATE_PREFIX}"])
    patch_yaml(ROOT / "[소설]/00_운영체계/START_HERE.md", {
        "legacy_tail_starts_at": f"{TAIL:03d}",
        "last_frontier_change_pr": "57",
        "next_bundle": "fiction/manuscript/part-1/046-050.md",
    }, [
        f"main_production_prefix: 001-{MAIN_PREFIX:03d}",
        f"repository_candidate_prefix: 001-{CANDIDATE_PREFIX:03d}",
        f"pending_frontier_pr: {PENDING_PR}",
        f"next_bundle_after_merge: {NEXT_BUNDLE}",
    ])

    active_path = F / "ACTIVE_CONTEXT.md"
    active = active_path.read_text(encoding="utf-8")
    active = active.replace("## Current production prefix 001–045 contract", "## Current main production 001–045 / PR #59 candidate 001–050 contract")
    active = active.replace("left_current: 45\nright_legacy: 46", "left_current: 50\nright_legacy: 51")
    active = active.replace("PR #57 병합으로 Ch40→41은 current continuity가 되었고 현재 main fail-closed 경계는 `045→046`이다.", "Main production은 PR #57 기준 `001–045 / 045→046`이다. PR #59 candidate는 exact-source 검증을 거쳐 `001–050 / 050→051`로 이동 중이며 merge 전까지 production으로 간주하지 않는다.")
    if "- Ch46 `자아를 찾으러 떠났습니다`" not in active:
        marker = "- Ch45 `노란 옷은 안 입습니다`: 황색과 거리를 둔 주안의 현재 선택을 고정하고 다음 8년 Bridge 생활·훈련 축으로 넘긴다."
        block = marker + "\n" + "\n".join([
            "- Ch46 `자아를 찾으러 떠났습니다`: 황색 내부의 호칭·전력 분류를 계약으로 제한하고 귀환 의무 없는 손님 지위를 자기선택으로 유지한다.",
            "- Ch47 `호수가 보이는 마을`: 8년 뒤 독립 성장한 이안과 주안의 동선을 사건·재회 압력으로 모은다.",
            "- Ch48 `돼지고기는 아니었습니다`: 수상한 식당과 실종 흔적을 검증하고 묶인 아킴의 생존 구조를 재회보다 먼저 선택한다.",
            "- Ch49 `여덟 해 만입니다`: 이안·주안·아킴 재회를 성립시키고 가론의 오래된 폭력 패턴을 말과 중단 규칙으로 제어한다.",
            "- Ch50 `낙원의 손님분들`: 낙원에 대화·환자 위장으로 진입하고 루바의 기억 관련 물을 Ch51 압력으로 넘긴다.",
        ])
        active = active.replace(marker, block, 1)
    active_path.write_text(active, encoding="utf-8")

    handoff_path = F / "HANDOFF.md"
    handoff = handoff_path.read_text(encoding="utf-8")
    handoff = handoff.replace("- production prefix: `001–045`.\n- fail-closed boundary: `45→46`.\n- next bundle: `046–050` from the same user-designated 041–050 source.", "- main production prefix: `001–045`.\n- PR #59 candidate prefix: `001–050`.\n- candidate fail-closed boundary: `50→51`.\n- next bundle after merge: `051–055`.")
    handoff = handoff.replace("left_current: 40\nright_legacy: 41", "left_current: 50\nright_legacy: 51")
    handoff = handoff.replace("PR #55 병합으로 Ch35→36은 current continuity가 되었고 main의 새 fail-closed 경계는 Ch40→41이다.", "Main production은 `001–045 / 045→046`이며 PR #59 candidate는 `001–050 / 050→051`로 이동 중이다. merge 전에는 candidate를 production으로 간주하지 않는다.")
    handoff = handoff.replace("`fiction/manuscript/part-1/041-045.md`를", "`fiction/manuscript/part-1/046-050.md`를")
    handoff_path.write_text(handoff, encoding="utf-8")

    start_path = ROOT / "[소설]/00_운영체계/START_HERE.md"
    start = start_path.read_text(encoding="utf-8")
    start = start.replace("- `045→046`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "- main `045→046`은 아직 production 경계다.\n- PR #59 candidate `050→051`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.")
    start = start.replace("Ch45→46 boundary verification\n→ exact source Ch46-50 extraction", "Ch50→51 boundary verification\n→ exact source Ch46-50 receipt verification")
    start_path.write_text(start, encoding="utf-8")

    print("patched Bridge 046-050 candidate consumers")


if __name__ == "__main__":
    main()
