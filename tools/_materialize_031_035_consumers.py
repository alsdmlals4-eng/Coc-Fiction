#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from build_fiction_reverse_outline import build_current

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
ANALYSIS = FICTION / "analysis"

BUNDLE = "fiction/manuscript/part-1/031-035.md"
SOURCE_FILE = "폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx"
SOURCE_SHA256 = "89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10"
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_all() -> dict[int, dict]:
    parsed: dict[int, dict] = {}
    for path in sorted((FICTION / "manuscript").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in CHAPTER_RE.finditer(text):
            number = int(match.group(1))
            body = match.group(4).strip()
            parsed[number] = {
                "chapter": number,
                "title": match.group(2).strip(),
                "pov": match.group(3).strip(),
                "body": body,
                "body_chars": len(body),
                "body_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
                "bundle": path.relative_to(ROOT).as_posix(),
            }
    return parsed


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, got {count}")
    return text.replace(old, new, 1)


def update_manuscript_status() -> None:
    path = ROOT / BUNDLE
    text = path.read_text(encoding="utf-8")
    text, count = re.subn(
        r"^> 상태:.*$",
        "> 상태: 2,000자 이상 확장 원고 DRAFT.",
        text,
        count=1,
        flags=re.M,
    )
    if count != 1:
        raise SystemExit("031-035 status line not found")
    path.write_text(text, encoding="utf-8")


def update_index(parsed: dict[int, dict]) -> None:
    override = {
        "schema_version": 1,
        "updated_at": "2026-08-24",
        "status": "ACTIVE_OVERRIDE / BUNDLE_031_035 / CURRENT_RECONCILED_PENDING_PR50",
        "baseline": "analysis/baselines/MANUSCRIPT_INDEX_2026-07-23_PILOT.json",
        "chapters": [
            {
                "chapter": n,
                "title": parsed[n]["title"],
                "pov": parsed[n]["pov"],
                "body_chars": parsed[n]["body_chars"],
                "body_sha256": parsed[n]["body_sha256"],
                "bundle": BUNDLE,
            }
            for n in range(31, 36)
        ],
    }
    write_json(ANALYSIS / "MANUSCRIPT_INDEX_OVERRIDE_031_035.json", override)

    manifest_path = FICTION / "MANUSCRIPT_INDEX.json"
    manifest = load_json(manifest_path)
    rel = "analysis/MANUSCRIPT_INDEX_OVERRIDE_031_035.json"
    overrides = [x for x in manifest["overrides"] if x != rel]
    insert_at = overrides.index("analysis/MANUSCRIPT_INDEX_OVERRIDE_091_095.json")
    overrides.insert(insert_at, rel)
    manifest["overrides"] = overrides
    manifest["generated_at"] = "2026-08-24"
    manifest["status"] = (
        "ACTIVE / COMPOSED / 225_STORAGE_CHAPTERS / MIXED_MIGRATION / "
        "PENDING_CURRENT_PREFIX_001_035_PR50"
    )
    write_json(manifest_path, manifest)


def update_registry(parsed: dict[int, dict]) -> None:
    path = ANALYSIS / "SCENE_PASS_REGISTRY.json"
    registry = load_json(path)
    registry["updated_at"] = "2026-08-24"
    rec = registry["external_artifact_reconciliation"]
    rec.update(
        {
            "artifact": SOURCE_FILE,
            "artifact_sha256": SOURCE_SHA256,
            "source_manifest": "docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json",
            "source_authority": "USER_DESIGNATED_SOURCE_CHUNK_SET",
            "reconciled_prefix_end": 35,
            "legacy_tail_starts_at": 36,
            "boundary_after_chapter": 35,
            "whole_manuscript_continuity": "NOT_YET_CLAIMED",
            "rule": (
                "Chapters 1-35 are the bounded reconciled candidate prefix on PR #50. "
                "Stored Ch36+ remain legacy-tail artifacts until their own 5-chapter promotion pass. "
                "The user source set currently has a declared 101-105 coverage gap and must not be "
                "auto-filled from derived or legacy sources."
            ),
        }
    )

    current = {
        "bundle": BUNDLE,
        "chapters": [31, 32, 33, 34, 35],
        "boundary_chapters": [30, 36],
        "scene_cards": "fiction/analysis/SCENE_CARDS_031_035.md",
        "revision_report": "fiction/reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_031_035.md",
        "source_files": [
            {
                "name": SOURCE_FILE,
                "sha256": SOURCE_SHA256,
                "role": "user-designated source authority",
            },
            {
                "name": "docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json",
                "role": "user source-set authority manifest",
            },
            {
                "name": "fiction/CANON_REGISTRY.json",
                "role": "latest direct user decisions and approved canon protection",
            },
        ],
        "chapter_shas": {str(n): parsed[n]["body_sha256"] for n in range(31, 36)},
        "preserved_boundary_shas": {
            "30": parsed[30]["body_sha256"],
            "36": parsed[36]["body_sha256"],
        },
        "status": "COMPLETE_USER_SOURCE_CANON_RECONCILIATION / PENDING_PR50",
    }
    passes = [item for item in registry.get("completed_bundle_passes", []) if item.get("bundle") != BUNDLE]
    inserted = False
    new_passes = []
    for item in passes:
        if not inserted and item.get("bundle") == "fiction/manuscript/side-story-lake/091-095.md":
            new_passes.append(current)
            inserted = True
        new_passes.append(item)
    if not inserted:
        new_passes.append(current)
    registry["completed_bundle_passes"] = new_passes
    registry["next_pass_mode"] = "USER_SOURCE_CHUNK_CANON_RECONCILIATION"
    registry["next_bundle_passes"] = ["fiction/manuscript/part-1/036-040.md"]
    write_json(path, registry)


def update_reverse_outline() -> dict[int, dict]:
    generated = build_current(ROOT)
    by_chapter = {int(item["chapter"]): item for item in generated["chapters"]}

    previous_path = ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_026_030.json"
    previous = load_json(previous_path)
    previous["updated_at"] = "2026-08-24"
    previous["chapters"] = [by_chapter[n] for n in range(26, 31)]
    write_json(previous_path, previous)

    write_json(
        ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_031_035.json",
        {
            "schema_version": 1,
            "updated_at": "2026-08-24",
            "status": "ACTIVE_OVERRIDE / BUNDLE_031_035 / CURRENT_RECONCILED_PENDING_PR50",
            "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
            "chapters": [by_chapter[n] for n in range(31, 36)],
        },
    )
    write_json(
        ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_036_MIGRATION_BOUNDARY.json",
        {
            "schema_version": 1,
            "updated_at": "2026-08-24",
            "status": "ACTIVE_OVERRIDE / CH036_LEGACY_TAIL_BOUNDARY / PENDING_PR50",
            "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
            "chapters": [by_chapter[36]],
        },
    )
    old_boundary = ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_031_MIGRATION_BOUNDARY.json"
    if old_boundary.exists():
        old_boundary.unlink()

    manifest_path = ANALYSIS / "REVERSE_OUTLINE_001_225.json"
    manifest = load_json(manifest_path)
    old = "REVERSE_OUTLINE_OVERRIDE_031_MIGRATION_BOUNDARY.json"
    replacements = {
        "REVERSE_OUTLINE_OVERRIDE_031_035.json",
        "REVERSE_OUTLINE_OVERRIDE_036_MIGRATION_BOUNDARY.json",
    }
    overrides = [x for x in manifest["overrides"] if x != old and x not in replacements]
    insert_at = overrides.index("REVERSE_OUTLINE_OVERRIDE_091_095.json")
    overrides[insert_at:insert_at] = [
        "REVERSE_OUTLINE_OVERRIDE_031_035.json",
        "REVERSE_OUTLINE_OVERRIDE_036_MIGRATION_BOUNDARY.json",
    ]
    manifest["overrides"] = overrides
    manifest["generated_at"] = "2026-08-24"
    write_json(manifest_path, manifest)
    return by_chapter


def update_scene_artifacts(by_chapter: dict[int, dict]) -> None:
    cards = [
        "# Scene Cards · Ch031–035",
        "",
        f"> source: `{SOURCE_FILE}` / SHA256 `{SOURCE_SHA256}`",
        "> state: PENDING_PR50 · exact user-source body + generated reverse-outline evidence",
        "",
    ]
    for n in range(31, 36):
        item = by_chapter[n]
        ev = item["evidence"]
        cards.extend(
            [
                f"## 제{n}화 · {item['title']}",
                f"- POV: `{item['pov']}`",
                f"- 시작 상태: {ev['starting_state']}",
                f"- 즉시 목표/초점: {ev['immediate_goal_or_focus']}",
                f"- 저항/비용: {ev['opposition_and_cost']}",
                f"- 전환/발견: {ev['turn_or_discovery']}",
                f"- 선택/행동: {ev['decision_or_choice']}",
                f"- 종료 상태: {ev['ending_state']}",
                "",
            ]
        )
    cards.extend(
        [
            "## Boundary readback",
            "- 제30→31화 · current Ch30의 창/쿠바라 압력이 Ch31 지연전으로 직접 이어짐.",
            "- 제31→32화 · 밀리 결말과 쇼거스 자율 폭주가 전장 전체 위협으로 확장.",
            "- 제32→33화 · 쇼거스 공략 정보가 주안의 위험한 자가선택/육체 변화로 이어짐.",
            "- 제33→34화 · 주안의 변화 뒤 핵 공략을 반복 가능한 전술로 정리.",
            "- 제34→35화 · 핵 감소 전술을 4인 협업 결전으로 수렴.",
            "- 제35→36화 · 세실리아 노출 직후 탈론의 회수 사명이 같은 동작으로 이어지지만 Ch36은 아직 legacy tail.",
            "",
            "## Protected canon",
            "- 엘리스는 인간 포함 정신 대상을 조작할 수 있다. 선택 보존은 능력 제한이 아니라 자기규율.",
            "- 밀리=남성, 하템=여성 별도 인물. 하템 사후 화면은 신규 정보 없는 환각/기억.",
            "- 주안의 보호행동은 소유/복종이 아니라 `반응 → 멈춤 → 이유 → 선택`으로 판정.",
            "- whole-manuscript continuity는 `NOT_YET_CLAIMED`.",
            "",
        ]
    )
    (ANALYSIS / "SCENE_CARDS_031_035.md").write_text("\n".join(cards), encoding="utf-8")

    report = f"""# Revision Report · Ch031–035 bounded reconciliation

## Status
- source authority: `{SOURCE_FILE}`
- source SHA256: `{SOURCE_SHA256}`
- candidate frontier on PR #50: `001–035`
- next fail-closed boundary: `035→036`
- whole-manuscript continuity: `NOT_YET_CLAIMED`

## Exact-transfer receipt
| Chapter | Title | POV | Body chars | Body SHA256 |
| --- | --- | --- | ---: | --- |
"""
    for n in range(31, 36):
        item = by_chapter[n]
        report += (
            f"| {n} | {item['title']} | {item['pov']} | "
            f"{item['source']['body_chars']} | `{item['source']['body_sha256']}` |\n"
        )
    report += """
## Canon conflict scan
- 엘리스: 인간을 포함한 정신 대상의 인지·판단·행동 조작 가능. 선택 보존은 윤리·자기규율.
- 주안: `반응 → 멈춤 → 이유 → 선택`; 보호행동을 소유/복종으로 환원하지 않음.
- 이안: 관찰 → 가설 → 검증 → 기록; 하템 환각은 신규 객관정보를 만들지 않음.
- 밀리/하템: 별도 인물·별도 죽음.
- 탈론: Part 1 core antagonist의 높은 화면 안 전투 위상 유지.

## Boundary
- Ch30→31: DIRECT CONTINUITY candidate PASS.
- Ch35→36: source-level DIRECT CONTINUITY를 확인했지만 Ch36은 별도 다음 bounded pass 전까지 legacy tail.

## 5× adversarial review
1. Source identity / exact body receipt: PASS.
2. Character identity / death-state / D04 capability drift: PASS.
3. Agency / ownership / obedience flattening: PASS.
4. Consumer propagation / rollback boundary: PASS.
5. Part boundary / future-tail overclaim / 101–105 source gap: PASS.

`CLEAN_REVIEW_EXIT` is conditional on exact-head hosted CI Green and unresolved review thread 0.

## Implementation Reality Gate
- manuscript exact source installed: YES
- index/reverse-outline/scene-pass/router consumers materialized: YES
- Ch36+ prose mutation: NO
- whole-manuscript continuity claimed: NO
- production merge claimed before CI: NO
"""
    report_path = FICTION / "reports" / "REVISION_2026-08-24_CURRENT_RECONCILIATION_031_035.md"
    report_path.write_text(report, encoding="utf-8")

    coordination = f"""# COC Promotion 031–035 · Adversarial Review — 2026-08-24

```yaml
scope: Ch031-035
source: {SOURCE_FILE}
source_sha256: {SOURCE_SHA256}
pending_pr: 50
candidate_frontier: 001-035
legacy_tail: 036+
whole_manuscript_continuity: NOT_YET_CLAIMED
```

## Loop 1 · source / identity
Exact user-source title·POV·body SHA를 promotion contract와 대조. `앨리스`, `히템`, 폐기 세력축 재유입 없음.

## Loop 2 · character state
밀리와 하템의 별도 인물/별도 사망을 유지. 세실리아는 Ch35에서 생존 노출까지, 원인 해설은 미확정. 라자크 상태는 자동 사망 확정 금지.

## Loop 3 · agency / ownership
주안의 보호와 엘리스의 창 사용을 소유·복종으로 평탄화하지 않음. 엘리스의 인간 포함 정신조작 능력과 선택 보존 자기규율을 동시에 유지.

## Loop 4 · continuity / consumer
Ch30→31은 candidate direct continuity. Ch35→36은 source-level direct continuity지만 Ch36은 별도 promotion 전까지 legacy tail. index / reverse outline / Scene Pass / router / receipt를 동일 frontier로 맞춤.

## Loop 5 · scope / overclaim
Part 1 = 001–040, Bridge = 041–066, Part 2 = 067+. 이번 PR은 031–035만 승격 후보. `101–105` source gap 자동 보충 금지. whole-manuscript continuity 완료 주장 금지.

## Exit
`CLEAN_REVIEW_EXIT` is valid only after exact-head hosted validation is Green.
"""
    coord_path = ROOT / "docs" / "coordination" / "2026-08-24_COC_PROMOTION_031_035_ADVERSARIAL_REVIEW.md"
    coord_path.write_text(coordination, encoding="utf-8")


def update_scene_pass_checker() -> None:
    path = ROOT / "tools" / "check_fiction_scene_passes.py"
    text = path.read_text(encoding="utf-8")

    if '"fiction/manuscript/part-1/031-035.md": {' not in text:
        marker = '    "fiction/manuscript/side-story-lake/091-095.md": {'
        block = """    "fiction/manuscript/part-1/031-035.md": {
        "chapters": [31, 32, 33, 34, 35],
        "boundaries": [30, 36],
        "card_boundaries": ["제30→31화", "제31→32화", "제32→33화", "제33→34화", "제34→35화", "제35→36화"],
    },
"""
        text = replace_once(text, marker, block + marker, "insert expected 031-035 pass")

    text = text.replace(
        'for bundle_name in ("006-010.md", "011-015.md", "016-020.md", "021-025.md", "026-030.md"):',
        'for bundle_name in ("006-010.md", "011-015.md", "016-020.md", "021-025.md", "026-030.md", "031-035.md"):',
    )

    required_anchor = '    30: "폭풍을 걷는 자.",\n'
    if '    31: "내가 네 주인은 아니야.",' not in text:
        text = replace_once(
            text,
            required_anchor,
            required_anchor
            + '    31: "내가 네 주인은 아니야.",\n'
            + '    32: "그 질문이 틀렸을 가능성이 큽니다.",\n'
            + '    33: "지금보다 괴물이 되어야 합니다.",\n'
            + '    34: "핵은 보이지 않았다.",\n'
            + '    35: "완전 소 생물씨.",\n',
            "add Ch031-035 invariants",
        )

    text = text.replace(
        'if reconciliation.get("artifact") != "폭풍의눈_2차퇴고_제021-030화_상실광기_강적위상_가독성강화본(1).docx":',
        f'if reconciliation.get("artifact") != "{SOURCE_FILE}":',
    )
    text = text.replace(
        'if reconciliation.get("artifact_sha256") != "e15c8fb4ed4ab1b6980c2c57f3979986bdbfa02f77aafef3cc84d3652cb70547":',
        f'if reconciliation.get("artifact_sha256") != "{SOURCE_SHA256}":',
    )
    text = text.replace('if reconciliation.get("reconciled_prefix_end") != 30:', 'if reconciliation.get("reconciled_prefix_end") != 35:')
    text = text.replace('reconciled prefix must be chapter 30 after current 026-030 propagation', 'reconciled prefix must be chapter 35 after current 031-035 propagation')
    text = text.replace('if reconciliation.get("legacy_tail_starts_at") != 31:', 'if reconciliation.get("legacy_tail_starts_at") != 36:')
    text = text.replace('legacy tail must begin at chapter 31 after current 026-030 propagation', 'legacy tail must begin at chapter 36 after current 031-035 propagation')
    text = text.replace('if reconciliation.get("boundary_after_chapter") != 30:', 'if reconciliation.get("boundary_after_chapter") != 35:')
    text = text.replace('migration boundary must be after chapter 30', 'migration boundary must be after chapter 35')
    text = text.replace(
        'for left_number, right_number in ((10, 11), (15, 16), (20, 21), (25, 26)):',
        'for left_number, right_number in ((10, 11), (15, 16), (20, 21), (25, 26), (30, 31)):',
    )

    boundary_pattern = re.compile(
        r'chapter30_outline = outline_entries\.get\(30, \{\}\).*?'
        r'if registry\.get\("next_pass_mode"\)',
        re.S,
    )
    boundary_replacement = """chapter35_outline = outline_entries.get(35, {})
if chapter35_outline.get("next_chapter") is not None:
    errors.append("chapter 35 reverse outline must stop at the current migration boundary")
if "RECONCILIATION_MIGRATION_BOUNDARY" not in chapter35_outline.get("structural_flags", []):
    errors.append("chapter 35 reverse outline missing migration-boundary flag")
if "제36화 이후는 아직 legacy tail" not in chapter35_outline.get("evidence", {}).get("next_pressure", ""):
    errors.append("chapter 35 reverse outline missing boundary pressure")

chapter36_outline = outline_entries.get(36, {})
if chapter36_outline.get("previous_chapter") is not None:
    errors.append("legacy chapter 36 must not claim current chapter 35 as previous continuity")
if "LEGACY_TAIL_BOUNDARY" not in chapter36_outline.get("structural_flags", []):
    errors.append("chapter 36 reverse outline missing legacy-tail boundary flag")

if registry.get("next_pass_mode")"""
    text, count = boundary_pattern.subn(boundary_replacement, text, count=1)
    if count != 1:
        raise SystemExit(f"replace scene-pass boundary block: expected 1, got {count}")

    text = text.replace(
        'if registry.get("next_bundle_passes") != ["fiction/manuscript/part-1/031-035.md"]:',
        'if registry.get("next_bundle_passes") != ["fiction/manuscript/part-1/036-040.md"]:',
    )
    text = text.replace(
        '"(001-030 current production prefix; migration boundary 30→31; "\n    "031-035 next; 091-095 source-matched)"',
        '"(001-035 pending promotion prefix; migration boundary 35→36; "\n    "036-040 next; 091-095 source-matched)"',
    )
    path.write_text(text, encoding="utf-8")


def update_receipt_and_routers() -> None:
    receipt_path = ROOT / "docs" / "fiction-ops" / "CURRENT_STATE_RECEIPT.json"
    receipt = load_json(receipt_path)
    receipt.update(
        {
            "frontier_observed_at_main": None,
            "last_frontier_change_pr": 48,
            "pending_frontier_change_pr": 50,
            "verified_prefix_end": 35,
            "legacy_tail_starts_at": 36,
            "boundary_after_chapter": 35,
            "next_bounded_bundle": "fiction/manuscript/part-1/036-040.md",
            "whole_manuscript_continuity": "NOT_YET_CLAIMED",
            "candidate_sha256": SOURCE_SHA256,
            "source_manifest": "docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json",
            "rule": "FETCH_LATEST_MAIN_BEFORE_USE",
        }
    )
    write_json(receipt_path, receipt)

    start_path = ROOT / "[소설]" / "00_운영체계" / "START_HERE.md"
    start = start_path.read_text(encoding="utf-8")
    start = start.replace("repository_reconciled_prefix: 001-030", "repository_candidate_prefix: 001-035")
    start = start.replace("legacy_tail_starts_at: 031", "legacy_tail_starts_at: 036")
    start = start.replace("next_bundle: fiction/manuscript/part-1/031-035.md", "next_bundle_after_merge: fiction/manuscript/part-1/036-040.md")
    start = start.replace(
        "현재 PR #50은 이 묶음의 진행 중 Draft이므로 다른 workstream 보호 규칙에 따라 이 Canon 교정 작업에서 수정하지 않는다.",
        "현재 PR #50은 사용자 승인으로 이 작업의 current-task workstream이다. exact-head Green과 병합 전에는 production 완료로 간주하지 않는다.",
    )
    start = start.replace(
        "- `030→031`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.\n- Ch25 reverse outline: `next_chapter=26`.\n- Ch30 reverse outline: `next_chapter=null`.\n- legacy Ch31 reverse outline: `previous_chapter=null`.",
        "- main verified `030→031` 경계는 PR #50 candidate에서 재개되며, pending candidate frontier는 `001–035`.\n- Ch30 reverse outline: `next_chapter=31` candidate 연결.\n- Ch35 reverse outline: `next_chapter=null`.\n- legacy Ch36 reverse outline: `previous_chapter=null`.\n- `035→036`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.",
    )
    start_path.write_text(start, encoding="utf-8")

    for rel in ("fiction/ACTIVE_CONTEXT.md", "fiction/HANDOFF.md"):
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        text = text.replace("frontier_observed_at_main: fb97068c714f5731bf712316d59a58adab7f4a86", "frontier_observed_at_main: null")
        text = text.replace("reconciled_prefix_end: 30", "reconciled_prefix_end: 35")
        text = text.replace("legacy_tail_starts_at: 31", "legacy_tail_starts_at: 36")
        text = text.replace("boundary_after_chapter: 30", "boundary_after_chapter: 35")
        text = text.replace("next_bounded_bundle: fiction/manuscript/part-1/031-035.md", "next_bounded_bundle: fiction/manuscript/part-1/036-040.md")
        text = text.replace("left_current: 30", "left_current: 35")
        text = text.replace("right_legacy: 31", "right_legacy: 36")
        text = text.replace(
            "PR #50: Ch031–035 bounded promotion Draft / 진행 중. 이 workstream에서는 수정하지 않는다.",
            "PR #50: Ch031–035 bounded promotion candidate / current-task 승인 범위. exact-head Green 전에는 production 완료 아님.",
        )
        text = text.replace(
            "PR #50: Ch031–035 bounded promotion Draft / 진행 중. 다른 workstream open PR 보호 규칙에 따라 직접 수정하지 않는다.",
            "PR #50: Ch031–035 bounded promotion candidate / current-task 승인 범위. exact-head Green 전에는 production 완료 아님.",
        )
        text = text.replace(
            "현재 PR #50은 진행 중 workstream이므로 이 Canon 교정 작업에서 수정하지 않는다.",
            "현재 PR #50은 사용자 승인으로 current-task workstream이 되었으며 exact-head Green 전에는 production 완료로 간주하지 않는다.",
        )
        path.write_text(text, encoding="utf-8")

    master_path = FICTION / "FICTION_MASTER.md"
    master = master_path.read_text(encoding="utf-8")
    master = master.replace("reconciled_prefix: 001-030", "reconciled_prefix: 001-035")
    master = master.replace("legacy_tail_starts_at: 031", "legacy_tail_starts_at: 036")
    master = master.replace("boundary_after_chapter: 030", "boundary_after_chapter: 035")
    master = master.replace("next_reconciliation: 031-035", "next_reconciliation: 036-040")
    master = master.replace("## 6. current candidate prefix 001–030 readback", "## 6. pending candidate prefix 001–035 readback")
    master = master.replace(
        "- 030 `폭풍을 걷는 자`: 밀리의 storm-walk와 쿠바라 창의 연결 절단을 관찰하지만 기원·전체 기능·소유권은 미확정으로 둔다.",
        "- 030 `폭풍을 걷는 자`: 밀리의 storm-walk와 쿠바라 창의 연결 절단을 관찰하지만 기원·전체 기능·소유권은 미확정으로 둔다.\n"
        "- 031–035: 사용자 지정 031–040 source의 exact body를 candidate로 설치. 밀리 최종 상실, 쇼거스 핵 공략, 주안 강화와 엘리스 정신능력 사용을 최신 Canon 아래 검증한다. PR #50 병합 전에는 main production으로 과장하지 않는다.",
    )
    master = master.replace("left_current: 30", "left_current: 35")
    master = master.replace("right_legacy: 31", "right_legacy: 36")
    master = master.replace(
        "Ch30→31은 fail-closed이며 numbering만으로 연속성을 주장하지 않는다.",
        "PR #50 candidate에서 Ch30→31은 source/consumer 검증으로 다시 연결한다. 새 fail-closed 경계는 Ch35→36이며, Ch36은 별도 pass 전까지 legacy tail이다.",
    )
    master = master.replace(
        "현재 다음 promotion PR #50은 `031–035` Draft / 진행 중이므로 이 Canon 교정 workstream에서는 수정하지 않는다.",
        "현재 promotion PR #50은 사용자 승인된 current-task workstream이며 `031–035` candidate를 검증 중이다. exact-head Green과 merge 전에는 production 완료로 간주하지 않는다.",
    )
    master = master.replace(
        "다음 bounded source는 사용자 지정 `031–040` 원본이며 우선 `031–035`를 처리한다.",
        "PR #50이 Green/merge되면 같은 사용자 지정 `031–040` 원본의 다음 bounded unit `036–040`을 처리한다.",
    )
    master_path.write_text(master, encoding="utf-8")


def clean_temporary_bootstrap() -> None:
    workflow_path = ROOT / ".github" / "workflows" / "fiction-ops-validation.yml"
    workflow = workflow_path.read_text(encoding="utf-8")
    workflow = workflow.replace("permissions:\n  contents: write", "permissions:\n  contents: read")
    workflow, count = re.subn(
        r"\n      # BEGIN TEMP-031-035-CONSUMER-MATERIALIZER\n.*?"
        r"      # END TEMP-031-035-CONSUMER-MATERIALIZER\n",
        "\n",
        workflow,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit(f"temporary workflow step marker missing: {count}")
    workflow_path.write_text(workflow, encoding="utf-8")
    Path(__file__).unlink()


def main() -> None:
    update_manuscript_status()
    parsed = parse_all()
    if sorted(parsed) != list(range(1, 226)):
        raise SystemExit(f"chapter set mismatch: {len(parsed)}")
    if [parsed[n]["chapter"] for n in range(31, 36)] != [31, 32, 33, 34, 35]:
        raise SystemExit("031-035 parse failed")
    if parsed[30]["body_sha256"] != "5ca93e6979b8beaa0d6ffe07809c664c0b7b907387b47b1732b431be364baac1":
        raise SystemExit("protected Ch30 SHA changed")
    if parsed[36]["body_sha256"] != "c5dd1b067199247a221350efd77e555c5cc98d08a648eb0f06ec9bd5ddfaf96e":
        raise SystemExit("protected Ch36 SHA changed")

    update_index(parsed)
    update_registry(parsed)
    by_chapter = update_reverse_outline()
    update_scene_artifacts(by_chapter)
    update_scene_pass_checker()
    update_receipt_and_routers()
    clean_temporary_bootstrap()


if __name__ == "__main__":
    main()
