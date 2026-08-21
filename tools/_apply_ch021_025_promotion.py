#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
ANALYSIS = FICTION / "analysis"
REPORTS = FICTION / "reports"
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)
CANDIDATE = "폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx"
CANDIDATE_SHA = "248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9"
BUNDLE = "fiction/manuscript/part-1/021-025.md"
EXPECTED = {
    21: ("삼 분만 기다립니다", "이안 → 엘리스 → 이안 → 엘리스 → 이안", 6472, "feb8df2a30c678e174a8cafbbeb8e33ec4d64042339f514a8b771e3b5b61b389"),
    22: ("다음에는 냄새부터 지워라", "주안 → 엘리스 → 주안 → 엘리스 → 주안 → 엘리스", 5916, "6ae4dba9533cad99139cfef11fdadfbddf5a381bf95091bc939296694c68e801"),
    23: ("떨어지면 받겠습니다", "주안 → 엘리스 → 이안 → 엘리스 → 이안 → 주안", 6779, "cd506e7449f718dfdda9d67db3aba654619457991ffb0fe0cba2ef43f660c40b"),
    24: ("한 박자 늦게", "주안 → 이안 → 엘리스 → 주안 → 이안 → 엘리스 → 주안 → 이안", 6961, "c111f79f73c034a6bc2f5dea8606e8b35c687b6a55842a6fd873adbda18b8549"),
    25: ("승자를 만들지 않기로 했다", "이안 → 엘리스 → 주안 → 이안 → 주안", 5870, "09a945739b8438e30b3721c4c777a0f1c4736f5d6ac7a0684f02877e399869e8"),
}
CH20_SHA = "dc78dd2f3ab00d853225ca4c98a85832d5fbb088df0b304258172e2ffd754523"
CH26_SHA = "13e7273f2f7a685fc7548edfc28963da673c77936ad0575f2f31ac7830cf1d13"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, got {count}: {old!r}")
    return text.replace(old, new, 1)


def parsed_manuscript() -> dict[int, dict]:
    parsed: dict[int, dict] = {}
    for path in sorted((FICTION / "manuscript").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in CHAPTER_RE.finditer(text):
            body = match.group(4).strip()
            parsed[int(match.group(1))] = {
                "title": match.group(2).strip(),
                "pov": match.group(3).strip(),
                "body": body,
                "chars": len(body),
                "sha": hashlib.sha256(body.encode("utf-8")).hexdigest(),
                "bundle": path.relative_to(ROOT).as_posix(),
            }
    return parsed


def verify_source(parsed: dict[int, dict]) -> None:
    for number, (title, pov, chars, digest) in EXPECTED.items():
        item = parsed[number]
        assert item["title"] == title, (number, item["title"], title)
        assert item["pov"] == pov, (number, item["pov"], pov)
        assert item["chars"] == chars, (number, item["chars"], chars)
        assert item["sha"] == digest, (number, item["sha"], digest)
        assert item["bundle"] == BUNDLE
    assert parsed[20]["sha"] == CH20_SHA
    assert parsed[26]["sha"] == CH26_SHA
    text = (ROOT / BUNDLE).read_text(encoding="utf-8")
    for forbidden in (
        "앨리스", "복종인자", "블랙킹", "오션", "쵸르브라트", "미하일 카쉬프",
        "피엘렛토", "붉은 늑대", "컨소시엄", "조작된 감정",
    ):
        assert forbidden not in text, forbidden


def update_index(parsed: dict[int, dict]) -> None:
    override = {
        "schema_version": 1,
        "updated_at": "2026-08-21",
        "status": "ACTIVE_OVERRIDE / BUNDLE_021_025 / CURRENT_RECONCILED",
        "baseline": "analysis/baselines/MANUSCRIPT_INDEX_2026-07-23_PILOT.json",
        "chapters": [
            {
                "chapter": number,
                "title": parsed[number]["title"],
                "pov": parsed[number]["pov"],
                "body_chars": parsed[number]["chars"],
                "body_sha256": parsed[number]["sha"],
                "bundle": BUNDLE,
            }
            for number in range(21, 26)
        ],
    }
    write_json(ANALYSIS / "MANUSCRIPT_INDEX_OVERRIDE_021_025.json", override)

    manifest_path = FICTION / "MANUSCRIPT_INDEX.json"
    manifest = load_json(manifest_path)
    manifest["generated_at"] = "2026-08-21"
    manifest["status"] = "ACTIVE / COMPOSED / 225_STORAGE_CHAPTERS / MIXED_MIGRATION / CURRENT_PREFIX_001_025"
    new_override = "analysis/MANUSCRIPT_INDEX_OVERRIDE_021_025.json"
    overrides = [item for item in manifest["overrides"] if item != new_override]
    insert_at = overrides.index("analysis/MANUSCRIPT_INDEX_OVERRIDE_091_095.json")
    overrides.insert(insert_at, new_override)
    manifest["overrides"] = overrides
    write_json(manifest_path, manifest)


def update_registry(parsed: dict[int, dict]) -> None:
    path = ANALYSIS / "SCENE_PASS_REGISTRY.json"
    registry = load_json(path)
    registry["updated_at"] = "2026-08-21"
    rec = registry["external_artifact_reconciliation"]
    rec["reconciled_prefix_end"] = 25
    rec["legacy_tail_starts_at"] = 26
    rec["boundary_after_chapter"] = 25
    rec["whole_manuscript_continuity"] = "NOT_YET_CLAIMED"
    rec["rule"] = (
        "The QA_GREEN external candidate is the current revision input, not automatic GitHub production authority. "
        "Chapters 1-25 are the bounded reconciled production prefix on this promotion branch; stored chapters 26+ "
        "remain legacy-tail artifacts until their own 5-chapter promotion pass."
    )

    passes = [item for item in registry["completed_bundle_passes"] if item.get("bundle") != BUNDLE]
    for item in passes:
        if item.get("bundle") == "fiction/manuscript/part-1/016-020.md":
            historical = dict(item.get("historical_boundary_shas", {}))
            if item.get("preserved_boundary_shas", {}).get("21"):
                historical["21"] = item["preserved_boundary_shas"]["21"]
            item["historical_boundary_shas"] = historical
            item["preserved_boundary_shas"] = {"15": item["preserved_boundary_shas"]["15"]}
            item["status"] = "COMPLETE_CURRENT_CANDIDATE_CANON_RECONCILIATION / CURRENT_PREFIX / HISTORICAL_BOUNDARY_020_021_RESOLVED"

    new_pass = {
        "bundle": BUNDLE,
        "chapters": [21, 22, 23, 24, 25],
        "boundary_chapters": [20, 26],
        "scene_cards": "fiction/analysis/SCENE_CARDS_021_025.md",
        "revision_report": "fiction/reports/REVISION_2026-08-21_CURRENT_RECONCILIATION_021_025.md",
        "source_files": [
            {"name": CANDIDATE, "sha256": CANDIDATE_SHA, "role": "current QA_GREEN revision input"},
            {"name": "docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json", "role": "locked external source-artifact authority manifest"},
            {"name": "fiction/CANON_REGISTRY.json", "role": "current approved adaptation canon"},
        ],
        "chapter_shas": {str(number): parsed[number]["sha"] for number in range(21, 26)},
        "preserved_boundary_shas": {"20": CH20_SHA, "26": CH26_SHA},
        "status": "COMPLETE_CURRENT_CANDIDATE_CANON_RECONCILIATION / CURRENT_PREFIX / MIGRATION_BOUNDARY_AFTER_025",
    }
    insert_at = next(i for i, item in enumerate(passes) if item.get("bundle") == "fiction/manuscript/side-story-lake/091-095.md")
    passes.insert(insert_at, new_pass)
    registry["completed_bundle_passes"] = passes
    registry["next_pass_mode"] = "EXTERNAL_ARTIFACT_CANON_RECONCILIATION"
    registry["next_bundle_passes"] = ["fiction/manuscript/part-1/026-030.md"]
    registry["deferred_bundle_passes"] = ["fiction/manuscript/part-2/176-180.md"]
    write_json(path, registry)


def update_reverse_outline() -> None:
    sys.path.insert(0, str(ROOT / "tools"))
    from build_fiction_reverse_outline import build_current

    generated = build_current(ROOT)
    by_number = {int(item["chapter"]): item for item in generated["chapters"]}

    existing_path = ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_016_020.json"
    existing = load_json(existing_path)
    existing["updated_at"] = "2026-08-21"
    existing["status"] = "ACTIVE_OVERRIDE / BUNDLE_016_020 / CURRENT_RECONCILED / BOUNDARY_020_021_RESOLVED"
    existing["chapters"] = [by_number[number] for number in range(16, 21)]
    write_json(existing_path, existing)

    current = {
        "schema_version": 1,
        "updated_at": "2026-08-21",
        "status": "ACTIVE_OVERRIDE / BUNDLE_021_025 / CURRENT_RECONCILED",
        "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
        "chapters": [by_number[number] for number in range(21, 26)],
    }
    write_json(ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_021_025.json", current)

    boundary = {
        "schema_version": 1,
        "updated_at": "2026-08-21",
        "status": "ACTIVE_OVERRIDE / CH26_LEGACY_TAIL_BOUNDARY",
        "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
        "chapters": [by_number[26]],
    }
    write_json(ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_026_MIGRATION_BOUNDARY.json", boundary)

    old_boundary = ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_021_MIGRATION_BOUNDARY.json"
    if old_boundary.exists():
        old_boundary.unlink()

    manifest_path = ANALYSIS / "REVERSE_OUTLINE_001_225.json"
    manifest = load_json(manifest_path)
    manifest["generated_at"] = "2026-08-21"
    overrides = [
        item for item in manifest["overrides"]
        if item not in {
            "REVERSE_OUTLINE_OVERRIDE_021_MIGRATION_BOUNDARY.json",
            "REVERSE_OUTLINE_OVERRIDE_021_025.json",
            "REVERSE_OUTLINE_OVERRIDE_026_MIGRATION_BOUNDARY.json",
        }
    ]
    insert_at = overrides.index("REVERSE_OUTLINE_OVERRIDE_091_095.json")
    overrides[insert_at:insert_at] = [
        "REVERSE_OUTLINE_OVERRIDE_021_025.json",
        "REVERSE_OUTLINE_OVERRIDE_026_MIGRATION_BOUNDARY.json",
    ]
    manifest["overrides"] = overrides
    write_json(manifest_path, manifest)


def write_scene_cards() -> None:
    text = """# 제21–25화 Current Scene Cards\n\n상태: **CURRENT / QA_GREEN CANDIDATE RECONCILED / MANUAL READBACK**  \n갱신: 2026-08-21\n\n## 제21화 · 삼 분만 기다립니다\n- **POV:** 이안 → 엘리스 → 이안 → 엘리스 → 이안\n- **핵심 기능:** 제20화 배수로 도주를 즉시 이어받고, 이안이 마법·기억을 사실로 승격하지 않는 자기 규율을 지킨다.\n- **선택권 보호:** 엘리스는 명령으로 문제를 덮지 않고 선택 가능한 정보를 돌려준다.\n- **보호 문장:** `뛰어들지 않는 선택을 계속하는 일이었다.`\n\n## 제22화 · 다음에는 냄새부터 지워라\n- **POV:** 주안 → 엘리스 → 주안 → 엘리스 → 주안 → 엘리스\n- **핵심 기능:** 정찰과 추적 회피를 정보 문제로 유지한다.\n- **선택권 보호:** 주안의 제동은 자기 선택이며 엘리스의 접촉을 자동 명령·복종 증거로 만들지 않는다.\n- **보호 문장:** `다음에는 숨 냄새부터 지워라.`\n\n## 제23화 · 떨어지면 받겠습니다\n- **POV:** 주안 → 엘리스 → 이안 → 엘리스 → 이안 → 주안\n- **핵심 기능:** 주안이 데이비드를 놓고 엘리스를 받는 행동을 스스로 선택한 것으로 구별한다.\n- **선택권 보호:** 몸의 선행 반응과 사후 선택을 같은 것으로 취급하지 않는다.\n- **보호 문장:** `과거의 원인이 무엇인지도 모른다. 그래도 선택한 순간의 감각은 기억할 수 있었다.`\n\n## 제24화 · 한 박자 늦게\n- **POV:** 주안 → 이안 → 엘리스 → 주안 → 이안 → 엘리스 → 주안 → 이안\n- **핵심 기능:** `반응 → 멈춤 → 이유 → 선택`을 팀 전술 속 실제 행동으로 반복한다.\n- **선택권 보호:** 엘리스의 목소리를 치료나 지배의 만능키로 사용하지 않고, 혼자 해결하지 않는 구조를 택한다.\n- **보호 문장:** `그 다음 한 박자를 제가 만들겠습니다.`\n\n## 제25화 · 승자를 만들지 않기로 했다\n- **POV:** 이안 → 엘리스 → 주안 → 이안 → 주안\n- **핵심 기능:** 쇼거스 위협 앞에서 정보·보호·선택을 분리한 채 다음 전면 충돌 직전까지 압력을 올린다.\n- **선택권 보호:** 주안은 한 박자 멈춰 이유를 확인하고 실제 위험만 막으며 엘리스의 결정을 대신 고정하지 않는다.\n- **보호 문장:** `갈 겁니까?`\n\n## 경계 검수\n- **제20→21화:** PASS · 훔친 지도와 배수로 탈출 상태가 current Ch21의 같은 도주선으로 직접 이어진다.\n- **제21→22화:** PASS · 배수로 이탈 뒤 추적 회피/정찰 압력이 자연스럽게 전환된다.\n- **제22→23화:** PASS · 정찰 결과와 인물 위치가 절벽/구출 선택으로 연결된다.\n- **제23→24화:** PASS · 구출 뒤 선행 반응 문제를 한 박자 선택 규칙으로 구체화한다.\n- **제24→25화:** PASS · 팀 전술과 선택권 규칙이 쇼거스 전면 위협으로 증폭된다.\n- **제25→26화:** `MIGRATION_BOUNDARY / NOT_YET_CLAIMED` · stored Ch26은 legacy이며 인접 번호만으로 current 연속성을 주장하지 않는다.\n\n## 판정\n- `021–025`: current candidate exact body + Canon reconciliation PASS.\n- 새 Canon 결정 없음.\n- whole-manuscript continuity는 계속 `NOT_YET_CLAIMED`.\n"""
    (ANALYSIS / "SCENE_CARDS_021_025.md").write_text(text, encoding="utf-8")


def write_revision_report(parsed: dict[int, dict]) -> None:
    rows = "\n".join(
        f"| {n} | {parsed[n]['title']} | {parsed[n]['chars']} | `{parsed[n]['sha']}` |"
        for n in range(21, 26)
    )
    text = f"""# 2026-08-21 Current Reconciliation · Ch021–025\n\nStatus: `CURRENT_CANDIDATE_EXACT / CANON_RECONCILED / BOUNDED_PROMOTION_PENDING_PR42`\n\n## Source authority\n- artifact: `{CANDIDATE}`\n- SHA256: `{CANDIDATE_SHA}`\n- extraction: DOCX chapter-heading boundaries → exact paragraph join, independently reproduced against already-promoted Ch16–20 hashes before this pass.\n\n## Exact body receipt\n| Ch | Title | Body chars | SHA256 |\n|---:|---|---:|---|\n{rows}\n\n## Boundary evidence\n- Ch20 preserved SHA: `{CH20_SHA}`.\n- Ch20 end: stolen map + drain escape + left-branch choice.\n- current Ch21 start: same drain / Ian+Akim escape line. `20→21` direct continuity PASS.\n- stored Ch26 preserved SHA: `{CH26_SHA}`.\n- Ch26 remains legacy and is not rewritten or claimed as current. `25→26` is fail-closed migration boundary.\n\n## Canon / reader-value review\n- Ch21: Ian writes unknown as unknown; Elise returns choice instead of forcing a solution.\n- Ch22: Jooan's restraint remains self-chosen; Elise contact is not automatic command evidence.\n- Ch23: Jooan distinguishes chosen rescue from unexplained body impulse and waits before contact.\n- Ch24: `반응 → 멈춤 → 이유 → 선택` becomes explicit team behavior; no one-person domination solution.\n- Ch25: Jooan pauses, checks reason, blocks only the actual hazard, and asks Elise's choice before the next threat.\n\nForbidden/superseded terms checked in Ch21–25: `앨리스`, `복종인자`, `블랙킹`, `오션`, `쵸르브라트`, `미하일 카쉬프`, `피엘렛토`, `붉은 늑대`, `컨소시엄`, `조작된 감정` → 0 hits.\n\n## Scope ceiling\n- production frontier proposed: `001–025`.\n- legacy tail: `026+`.\n- next bounded bundle: `026–030`.\n- whole-manuscript continuity: `NOT_YET_CLAIMED`.\n- no new Canon decision, no Ch26+ manuscript mutation, no publication-layout claim.\n"""
    (REPORTS / "REVISION_2026-08-21_CURRENT_RECONCILIATION_021_025.md").write_text(text, encoding="utf-8")


def update_receipt() -> None:
    receipt = {
        "schema_version": 1,
        "frontier_observed_at_main": None,
        "last_frontier_change_pr": 39,
        "pending_frontier_change_pr": 42,
        "verified_prefix_end": 25,
        "legacy_tail_starts_at": 26,
        "boundary_after_chapter": 25,
        "next_bounded_bundle": "fiction/manuscript/part-1/026-030.md",
        "whole_manuscript_continuity": "NOT_YET_CLAIMED",
        "candidate_sha256": CANDIDATE_SHA,
        "rule": "FETCH_LATEST_MAIN_BEFORE_USE",
    }
    write_json(ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json", receipt)


def update_active_docs() -> None:
    replacements = {
        "fiction/ACTIVE_CONTEXT.md": [
            ("frontier_observed_at_main: 395f0af0120f5ab6949c86772d3b77b5b3eb9f3a\nlast_frontier_change_pr: 39", "frontier_observed_at_main: null\nlast_frontier_change_pr: 39\npending_frontier_change_pr: 42"),
            ("reconciled_prefix_end: 20", "reconciled_prefix_end: 25"),
            ("legacy_tail_starts_at: 21", "legacy_tail_starts_at: 26"),
            ("boundary_after_chapter: 20", "boundary_after_chapter: 25"),
            ("next_bounded_bundle: fiction/manuscript/part-1/021-025.md", "next_bounded_bundle: fiction/manuscript/part-1/026-030.md"),
            ("현재 production frontier가 마지막으로 바뀐 증거", "현재 production frontier의 마지막 merged 증거"),
            ("## Current prefix 001–020 contract", "## Current prefix 001–025 contract"),
            ("- Ch20: 지도 확보 성공과 잠입 실패를 동시에 기록한다.", "- Ch20: 지도 확보 성공과 잠입 실패를 동시에 기록한다.\n- Ch21: 모르는 마법·기억은 `확인`으로 남기고, 뛰어들지 않는 선택을 지킨다.\n- Ch22: 정찰/추적 회피에서 주안의 제동을 자기 선택으로 유지한다.\n- Ch23: 구출 행동과 설명되지 않은 신체 반응을 구별하고 접촉 전 기다린다.\n- Ch24: `반응 → 멈춤 → 이유 → 선택`을 팀 전술로 실행한다.\n- Ch25: 실제 위험만 막고 엘리스에게 `갈 겁니까?`라고 선택을 묻는다."),
            ("left_current: 20\nright_legacy: 21", "left_current: 25\nright_legacy: 26"),
            ("저장 화수가 인접하다는 이유만으로 current Ch20→legacy Ch21 연속성을 주장하지 않는다.", "Ch20→21 current continuity는 PASS다. 저장 화수가 인접하다는 이유만으로 current Ch25→legacy Ch26 연속성을 주장하지 않는다."),
            ("`fiction/manuscript/part-1/021-025.md`", "`fiction/manuscript/part-1/026-030.md`"),
            ("다음 pass는 **Ch20→21 migration boundary**에서 시작한다.", "다음 pass는 **Ch25→26 migration boundary**에서 시작한다."),
        ],
        "fiction/HANDOFF.md": [
            ("frontier_observed_at_main: 395f0af0120f5ab6949c86772d3b77b5b3eb9f3a\nlast_frontier_change_pr: 39", "frontier_observed_at_main: null\nlast_frontier_change_pr: 39\npending_frontier_change_pr: 42"),
            ("reconciled_prefix_end: 20", "reconciled_prefix_end: 25"),
            ("legacy_tail_starts_at: 21", "legacy_tail_starts_at: 26"),
            ("boundary_after_chapter: 20", "boundary_after_chapter: 25"),
            ("next_bounded_bundle: fiction/manuscript/part-1/021-025.md", "next_bounded_bundle: fiction/manuscript/part-1/026-030.md"),
            ("- current repository prefix: **001–020**.\n- next bounded promotion: **021–025**.", "- **PR #42: Ch021–025 bounded promotion pending exact-head merge/readback.**\n- branch-verified repository prefix: **001–025**.\n- next bounded promotion after merge: **026–030**."),
            ("repository_verified_prefix: [1, 20]\nlegacy_tail: [21, 225]", "repository_verified_prefix: [1, 25]\nlegacy_tail: [26, 225]"),
            ("left_current: 20\nright_legacy: 21", "left_current: 25\nright_legacy: 26"),
            ("Ch20→21은 fail-closed boundary다. 인접 번호를 근거로 현재 연속성을 추정하지 않는다.", "Ch20→21 current continuity는 PASS다. Ch25→26은 fail-closed boundary이며 인접 번호만으로 현재 연속성을 추정하지 않는다."),
            ("`fiction/manuscript/part-1/021-025.md`", "`fiction/manuscript/part-1/026-030.md`"),
            ("2. locked QA_GREEN candidate에서 Ch21–25 exact 추출.\n3. Ch20 종료 상태와 앞 경계 검증.", "2. locked QA_GREEN candidate에서 Ch26–30 exact 추출.\n3. Ch25 종료 상태와 앞 경계 검증."),
        ],
    }
    for rel, items in replacements.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for old, new in items:
            text = replace_once(text, old, new, rel)
        path.write_text(text, encoding="utf-8")

    start_path = ROOT / "[소설]/00_운영체계/START_HERE.md"
    start = start_path.read_text(encoding="utf-8")
    for old, new in (
        ("repository_reconciled_prefix: 001-020", "repository_reconciled_prefix: 001-025"),
        ("legacy_tail_starts_at: 021", "legacy_tail_starts_at: 026"),
        ("- `001–020`: current production prefix.", "- `001–025`: branch-verified current production prefix; PR #42 merge/readback pending."),
        ("- `020→021`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "- `020→021`: current continuity PASS.\n- `025→026`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`."),
        ("- Ch20 reverse outline: `next_chapter=null`.\n- legacy Ch21 reverse outline: `previous_chapter=null`.", "- Ch20 reverse outline: `next_chapter=21`.\n- Ch25 reverse outline: `next_chapter=null`.\n- legacy Ch26 reverse outline: `previous_chapter=null`."),
        ("`fiction/manuscript/part-1/021-025.md`", "`fiction/manuscript/part-1/026-030.md`"),
        ("current candidate Ch21-25 exact extraction\n→ Ch20 current 종료 상태와 앞 경계 검증", "current candidate Ch26-30 exact extraction\n→ Ch25 current 종료 상태와 앞 경계 검증"),
    ):
        start = replace_once(start, old, new, "START_HERE")
    start_path.write_text(start, encoding="utf-8")

    master_path = FICTION / "FICTION_MASTER.md"
    master = master_path.read_text(encoding="utf-8")
    for old, new in (
        ("reconciled_prefix: 001-020", "reconciled_prefix: 001-025"),
        ("legacy_tail_starts_at: 021", "legacy_tail_starts_at: 026"),
        ("boundary_after_chapter: 020", "boundary_after_chapter: 025"),
        ("next_reconciliation: 021-025", "next_reconciliation: 026-030"),
        ("## 6. current prefix 001–020 readback", "## 6. current prefix 001–025 readback"),
        ("- 020 `지도 한 장을 훔치는 시간`: 지도 획득 성공과 잠입 실패를 동시에 기록한다.", "- 020 `지도 한 장을 훔치는 시간`: 지도 획득 성공과 잠입 실패를 동시에 기록한다.\n- 021–025: 배수로 탈출→정찰→구출→한 박자 선택 규칙→쇼거스 전면 압력으로 current continuity를 잇고, 각 장면에서 정보·보호·선택을 분리한다."),
        ("left_current: 20\nright_legacy: 21", "left_current: 25\nright_legacy: 26"),
        ("Ch20→21은 fail-closed다. 인접 numbering으로 연속성을 자동 주장하지 않는다.", "Ch20→21 current continuity는 PASS다. Ch25→26은 fail-closed이며 인접 numbering으로 연속성을 자동 주장하지 않는다."),
        ("현재 다음 작업은 `fiction/manuscript/part-1/021-025.md`다.", "현재 다음 작업은 PR #42 merge/readback 뒤 `fiction/manuscript/part-1/026-030.md`다."),
        ("`candidate exact extraction → Ch20 boundary 검증", "`candidate exact extraction → Ch25 boundary 검증"),
    ):
        master = replace_once(master, old, new, "FICTION_MASTER")
    master_path.write_text(master, encoding="utf-8")


def update_reverse_report() -> None:
    path = ANALYSIS / "REVERSE_OUTLINE_REPORT.md"
    text = path.read_text(encoding="utf-8")
    for old, new in (
        ("- `016–020`: QA_GREEN current candidate 적용 + **Ch20 migration boundary**\n- `021`: legacy-tail boundary override", "- `016–020`: QA_GREEN current candidate 적용 + Ch20→21 current continuity 복구\n- `021–025`: QA_GREEN current candidate 적용 + **Ch25 migration boundary**\n- `026`: legacy-tail boundary override"),
        ("`001–020`은 current candidate와 대조된 production prefix이지만, 제21화 이후", "`001–025`는 current candidate와 대조된 branch-verified production prefix이지만, 제26화 이후"),
        ("reconciled_prefix_end: 20\nlegacy_tail_starts_at: 21\nboundary_after_chapter: 20", "reconciled_prefix_end: 25\nlegacy_tail_starts_at: 26\nboundary_after_chapter: 25"),
        ("- Ch5→6, Ch10→11, Ch15→16은 current continuity로 정상 연결한다.", "- Ch5→6, Ch10→11, Ch15→16, Ch20→21은 current continuity로 정상 연결한다."),
        ("- Ch20은 `RECONCILIATION_MIGRATION_BOUNDARY`; 합성 역개요에서 `next_chapter=null`이다.\n- stored Ch21은 `LEGACY_TAIL_BOUNDARY`; current Ch20을 자신의 정상 previous chapter로 자동 주장하지 않는다.\n- repository generator가 frontier 20 상태에서 Ch15–21을 재생성했고, Ch16–20 override는 해당 출력과 current body/index에 맞춰 저장했다.\n- `091–095` source-pass 및 과거 저장 편성 검증은 역사적 증거로 보존한다.\n- Ch21+는 자신의 bounded reconciliation 전까지 current narrative 연속성을 주장하지 않는다.", "- Ch20은 current Ch21로 정상 연결한다.\n- Ch25는 `RECONCILIATION_MIGRATION_BOUNDARY`; 합성 역개요에서 `next_chapter=null`이다.\n- stored Ch26은 `LEGACY_TAIL_BOUNDARY`; current Ch25를 자신의 정상 previous chapter로 자동 주장하지 않는다.\n- repository generator가 frontier 25 상태에서 Ch20–26을 재생성했고, Ch20/Ch21–25/Ch26 override는 current body/index 및 fail-closed boundary와 맞춘다.\n- `091–095` source-pass 및 과거 저장 편성 검증은 역사적 증거로 보존한다.\n- Ch26+는 자신의 bounded reconciliation 전까지 current narrative 연속성을 주장하지 않는다."),
        ("- 과거 15→16 boundary는 Ch16–20 current promotion으로 제거됐다.", "- 과거 15→16 boundary는 Ch16–20 current promotion으로 제거됐다.\n- 과거 20→21 boundary는 Ch21–25 current promotion으로 제거됐다."),
        ("- 새 fail-closed 경계는 **20→21**이다.\n- QA_GREEN 001–161 artifact 존재만으로 Ch21+ production authority를 자동 승격하지 않는다.", "- 새 fail-closed 경계는 **25→26**이다.\n- QA_GREEN 001–161 artifact 존재만으로 Ch26+ production authority를 자동 승격하지 않는다."),
        ("- current boundary `20→21`\n- next bounded bundle `021–025`", "- current boundary `25→26`\n- next bounded bundle `026–030`"),
        ("1. 제1–20화 production prefix와 제20→21 migration boundary를 exact-head CI로 검증한다.\n2. Green/merge/readback 뒤 다음 묶음 `fiction/manuscript/part-1/021-025.md`를 QA_GREEN current candidate와 대조한다.\n3. Ch20 종료 상태와 current Ch21의 배수로 도주 연결을 먼저 확인한다.", "1. 제1–25화 branch-verified prefix와 제25→26 migration boundary를 exact-head CI로 검증한다.\n2. PR #42 Green/merge/readback 뒤 다음 묶음 `fiction/manuscript/part-1/026-030.md`를 QA_GREEN current candidate와 대조한다.\n3. Ch25 종료 상태와 current candidate Ch26의 앞 경계를 먼저 확인하되 stored Ch26을 자동 current로 간주하지 않는다."),
    ):
        text = replace_once(text, old, new, "REVERSE_OUTLINE_REPORT")
    path.write_text(text, encoding="utf-8")


def update_scene_pass_validator() -> None:
    path = ROOT / "tools/check_fiction_scene_passes.py"
    text = path.read_text(encoding="utf-8")
    anchor = '''    "fiction/manuscript/side-story-lake/091-095.md": {\n'''
    block = '''    "fiction/manuscript/part-1/021-025.md": {\n        "chapters": [21, 22, 23, 24, 25],\n        "boundaries": [20, 26],\n        "card_boundaries": ["제20→21화", "제21→22화", "제22→23화", "제23→24화", "제24→25화", "제25→26화"],\n    },\n'''
    text = replace_once(text, anchor, block + anchor, "scene validator pass set")
    text = replace_once(
        text,
        '    20: "마음에 드는 규칙만 적으면 규칙이 아니라 희망사항이니까요.",\n    91:',
        '    20: "마음에 드는 규칙만 적으면 규칙이 아니라 희망사항이니까요.",\n    21: "뛰어들지 않는 선택을 계속하는 일이었다.",\n    22: "다음에는 숨 냄새부터 지워라.",\n    23: "과거의 원인이 무엇인지도 모른다. 그래도 선택한 순간의 감각은 기억할 수 있었다.",\n    24: "그 다음 한 박자를 제가 만들겠습니다.",\n    25: "갈 겁니까?",\n    91:',
        "scene validator phrases",
    )
    text = replace_once(
        text,
        'for bundle_name in ("006-010.md", "011-015.md", "016-020.md"):',
        'for bundle_name in ("006-010.md", "011-015.md", "016-020.md", "021-025.md"):',
        "scene validator current bundles",
    )
    for old, new in (
        ('if reconciliation.get("reconciled_prefix_end") != 20:\n    errors.append("reconciled prefix must be chapter 20 after current 016-020 propagation")', 'if reconciliation.get("reconciled_prefix_end") != 25:\n    errors.append("reconciled prefix must be chapter 25 after current 021-025 propagation")'),
        ('if reconciliation.get("legacy_tail_starts_at") != 21:\n    errors.append("legacy tail must begin at chapter 21 after current 016-020 propagation")', 'if reconciliation.get("legacy_tail_starts_at") != 26:\n    errors.append("legacy tail must begin at chapter 26 after current 021-025 propagation")'),
        ('if reconciliation.get("boundary_after_chapter") != 20:\n    errors.append("migration boundary must be after chapter 20")', 'if reconciliation.get("boundary_after_chapter") != 25:\n    errors.append("migration boundary must be after chapter 25")'),
        ('if registry.get("next_bundle_passes") != ["fiction/manuscript/part-1/021-025.md"]:\n    errors.append("next bundle pass order mismatch")', 'if registry.get("next_bundle_passes") != ["fiction/manuscript/part-1/026-030.md"]:\n    errors.append("next bundle pass order mismatch")'),
        ('"(001-020 current production prefix; migration boundary 20→21; "\n    "021-025 next; 091-095 source-matched)"', '"(001-025 current production prefix; migration boundary 25→26; "\n    "026-030 next; 091-095 source-matched)"'),
    ):
        text = replace_once(text, old, new, "scene validator frontier")

    old_outline = '''chapter20_outline = outline_entries.get(20, {})\nif chapter20_outline.get("next_chapter") is not None:\n    errors.append("chapter 20 reverse outline must stop at the current migration boundary")\nif "RECONCILIATION_MIGRATION_BOUNDARY" not in chapter20_outline.get("structural_flags", []):\n    errors.append("chapter 20 reverse outline missing migration-boundary flag")\nif "제21화 이후는 아직 legacy tail" not in chapter20_outline.get("evidence", {}).get("next_pressure", ""):\n    errors.append("chapter 20 reverse outline missing boundary pressure")\n\nchapter21_outline = outline_entries.get(21, {})\nif chapter21_outline.get("previous_chapter") is not None:\n    errors.append("legacy chapter 21 reverse outline must not claim current chapter 20 as previous continuity")\nif "LEGACY_TAIL_BOUNDARY" not in chapter21_outline.get("structural_flags", []):\n    errors.append("chapter 21 reverse outline missing legacy-tail boundary flag")\n'''
    new_outline = '''chapter20_outline = outline_entries.get(20, {})\nchapter20_next = chapter20_outline.get("next_chapter")\nif not isinstance(chapter20_next, dict) or chapter20_next.get("chapter") != 21:\n    errors.append("current chapter 20 reverse outline must connect to current chapter 21")\nif "RECONCILIATION_MIGRATION_BOUNDARY" in chapter20_outline.get("structural_flags", []):\n    errors.append("chapter 20 must no longer carry the migration-boundary flag")\n\nchapter21_outline = outline_entries.get(21, {})\nchapter21_previous = chapter21_outline.get("previous_chapter")\nif not isinstance(chapter21_previous, dict) or chapter21_previous.get("chapter") != 20:\n    errors.append("current chapter 21 reverse outline must connect back to chapter 20")\nif "LEGACY_TAIL_BOUNDARY" in chapter21_outline.get("structural_flags", []):\n    errors.append("current chapter 21 must no longer carry the legacy-tail boundary flag")\n\nchapter25_outline = outline_entries.get(25, {})\nif chapter25_outline.get("next_chapter") is not None:\n    errors.append("chapter 25 reverse outline must stop at the current migration boundary")\nif "RECONCILIATION_MIGRATION_BOUNDARY" not in chapter25_outline.get("structural_flags", []):\n    errors.append("chapter 25 reverse outline missing migration-boundary flag")\nif "제26화 이후는 아직 legacy tail" not in chapter25_outline.get("evidence", {}).get("next_pressure", ""):\n    errors.append("chapter 25 reverse outline missing boundary pressure")\n\nchapter26_outline = outline_entries.get(26, {})\nif chapter26_outline.get("previous_chapter") is not None:\n    errors.append("legacy chapter 26 reverse outline must not claim current chapter 25 as previous continuity")\nif "LEGACY_TAIL_BOUNDARY" not in chapter26_outline.get("structural_flags", []):\n    errors.append("chapter 26 reverse outline missing legacy-tail boundary flag")\n'''
    text = replace_once(text, old_outline, new_outline, "scene validator outline boundary")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    parsed = parsed_manuscript()
    verify_source(parsed)
    update_index(parsed)
    update_registry(parsed)
    update_reverse_outline()
    write_scene_cards()
    write_revision_report(parsed)
    update_receipt()
    update_active_docs()
    update_reverse_report()
    update_scene_pass_validator()
    print("Ch021-025 deterministic promotion apply PASS")


if __name__ == "__main__":
    main()
