#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MERGE_SHA = "2a7d6d1267708b63797ccb429e111252068ad22e"
SOURCE = "폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본(1).docx"
SOURCE_SHA = "9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"closure marker missing: {label}")
    return text.replace(old, new, 1)


def patch_receipt() -> None:
    p = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
    data = load(p)
    data.update({
        "frontier_observed_at_main": MERGE_SHA,
        "last_frontier_change_pr": 57,
        "pending_frontier_change_pr": None,
        "verified_prefix_end": 45,
        "legacy_tail_starts_at": 46,
        "boundary_after_chapter": 45,
        "next_bounded_bundle": "fiction/manuscript/part-1/046-050.md",
        "whole_manuscript_continuity": "NOT_YET_CLAIMED",
        "candidate_sha256": SOURCE_SHA,
    })
    dump(p, data)


def patch_active() -> None:
    p = ROOT / "fiction/ACTIVE_CONTEXT.md"
    t = p.read_text(encoding="utf-8")
    for old,new,label in (
        ("frontier_observed_at_main: null", f"frontier_observed_at_main: {MERGE_SHA}", "active main sha"),
        ("last_frontier_change_pr: 55", "last_frontier_change_pr: 57", "active last pr"),
        ("pending_frontier_change_pr: 57", "pending_frontier_change_pr: null", "active pending"),
        ("main_production_prefix_end: 40\ncandidate_prefix_end: 45\n", "main_production_prefix_end: 45\n", "active candidate keys"),
        ("- **PR #55: Ch036–040 user-source bounded promotion merged; production frontier is 001–040.**", "- **PR #55: Ch036–040 user-source bounded promotion merged.**\n- **PR #57: Bridge Ch041–045 user-source bounded promotion merged; production frontier is 001–045.**", "active milestone"),
        ("## Current production prefix 001–040 contract", "## Current production prefix 001–045 contract", "active section title"),
        ("PR #55 병합 기준 main production은 `001–040` / `040→041`이다. 현재 PR #57 candidate는 exact-source 검증을 거쳐 `001–045` / `045→046`으로 이동 중이며, merge 전까지 production으로 간주하지 않는다.", "PR #57 병합으로 Ch40→41은 current continuity가 되었고 현재 main fail-closed 경계는 `045→046`이다.", "active candidate paragraph"),
        ("left_current: 40\nright_legacy: 41\nleft_next_chapter: null\nright_previous_chapter: null", "left_current: 45\nright_legacy: 46\nleft_next_chapter: null\nright_previous_chapter: null", "active boundary"),
        ("`fiction/manuscript/part-1/041-045.md`", "`fiction/manuscript/part-1/046-050.md`", "active next bundle"),
        ("**Ch40→41 migration boundary**에서 사용자 지정", "**Ch45→46 migration boundary**에서 같은 사용자 지정", "active next boundary"),
    ):
        t = replace_once(t, old, new, label)
    insertion = (
        "- Ch40: 윌리엄의 사랑과 잘못을 동시에 인정하고 엘리스가 아버지의 방식이 아닌 자기 방식의 책임을 선택하며 Part 1 본편을 닫는다.\n"
        "- Ch41 `잘 돌아왔다`: Part 1 결전 이후 가족 재회와 살아 돌아온 관계의 비정상성을 Bridge의 출발점으로 정리한다.\n"
        "- Ch42 `살아 돌아온 몸`: 주안의 변화한 몸을 보상이 아니라 선택을 침식할 수 있는 후유 상태로 검증한다.\n"
        "- Ch43 `확인하고 설명하겠습니다`: 주안은 자기 감정의 기원을 확인하지만 엘리스의 현재 선택을 대신 판정하지 않는다.\n"
        "- Ch44 `응답하지 않은 호출기`: 미응답을 영구 이별로 확정하지 않고 관계의 불확실성과 수신기 보존을 함께 남긴다.\n"
        "- Ch45 `노란 옷은 안 입습니다`: 황색과 거리를 둔 주안의 현재 선택을 고정하고 다음 8년 Bridge 생활·훈련 축으로 넘긴다."
    )
    t = replace_once(t, "- Ch40: 윌리엄의 사랑과 잘못을 동시에 인정하고 엘리스가 아버지의 방식이 아닌 자기 방식의 책임을 선택하며 Part 1 본편을 닫는다.", insertion, "active bridge readback")
    p.write_text(t, encoding="utf-8")


def patch_handoff() -> None:
    p = ROOT / "fiction/HANDOFF.md"
    t = p.read_text(encoding="utf-8")
    replacements = (
        ("frontier_observed_at_main: null", f"frontier_observed_at_main: {MERGE_SHA}"),
        ("last_frontier_change_pr: 55", "last_frontier_change_pr: 57"),
        ("pending_frontier_change_pr: 57", "pending_frontier_change_pr: null"),
        ("main_production_prefix_end: 40\ncandidate_prefix_end: 45\n", "main_production_prefix_end: 45\n"),
        ("- **PR #57: Bridge Ch041–045 user-source bounded promotion candidate; merge 전 production 아님.**", "- **PR #57: Bridge Ch041–045 user-source bounded promotion merged.**"),
        ("- main production prefix: `001–040`.\n- PR #57 candidate prefix: `001–045`.\n- candidate fail-closed boundary: `45→46`.\n- next bundle after merge: `046–050` from the same user-designated 041–050 source.", "- production prefix: `001–045`.\n- fail-closed boundary: `45→46`.\n- next bundle: `046–050` from the same user-designated 041–050 source."),
    )
    for old,new in replacements:
        t = replace_once(t, old, new, f"handoff {old[:24]}")
    p.write_text(t, encoding="utf-8")


def patch_start_here() -> None:
    p = ROOT / "[소설]/00_운영체계/START_HERE.md"
    t = p.read_text(encoding="utf-8")
    for old,new,label in (
        ("repository_reconciled_prefix: 001-040", "repository_reconciled_prefix: 001-045", "start prefix"),
        ("main_production_prefix: 001-040\nrepository_candidate_prefix: 001-045\npending_frontier_pr: 57\nnext_bundle_after_merge: fiction/manuscript/part-1/046-050.md\n", "", "start candidate keys"),
        ("last_frontier_change_pr: 55", "last_frontier_change_pr: 57", "start last pr"),
        ("next_bundle: fiction/manuscript/part-1/041-045.md", "next_bundle: fiction/manuscript/part-1/046-050.md", "start next"),
        ("- GitHub `main` production: `001–040` (PR #55).", "- GitHub `main` production: `001–045` (PR #57).", "start production"),
        ("- `040→041`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "- `040→041`은 current continuity PASS.\n- `045→046`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "start boundary prose"),
        ("`fiction/manuscript/part-1/041-045.md`", "`fiction/manuscript/part-1/046-050.md`", "start work bundle"),
        ("Ch40→41 boundary verification\n→ exact source Ch41-45 extraction", "Ch45→46 boundary verification\n→ exact source Ch46-50 extraction", "start work steps"),
    ):
        t = replace_once(t, old, new, label)
    p.write_text(t, encoding="utf-8")


def patch_master() -> None:
    p = ROOT / "fiction/FICTION_MASTER.md"
    t = p.read_text(encoding="utf-8")
    for old,new,label in (
        ("current_bundle_source: 폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx", f"current_bundle_source: {SOURCE}", "master source"),
        ("current_bundle_source_sha256: 89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10", f"current_bundle_source_sha256: {SOURCE_SHA}", "master source sha"),
        ("reconciled_prefix: 001-040", "reconciled_prefix: 001-045", "master prefix"),
        ("legacy_tail_starts_at: 041", "legacy_tail_starts_at: 046", "master tail"),
        ("boundary_after_chapter: 040", "boundary_after_chapter: 045", "master boundary"),
        ("last_frontier_change_pr: 55", "last_frontier_change_pr: 57", "master last pr"),
        ("next_reconciliation: 041-045", "next_reconciliation: 046-050", "master next"),
        ("## 6. current production prefix 001–040 readback", "## 6. current production prefix 001–045 readback", "master section title"),
        ("left_current: 40\nright_legacy: 41", "left_current: 45\nright_legacy: 46", "master boundary block"),
        ("PR #55 병합으로 Ch35→36은 current continuity가 되었고 새 main fail-closed 경계는 Ch40→41이다.", "PR #57 병합으로 Ch40→41은 current continuity가 되었고 새 main fail-closed 경계는 Ch45→46이다.", "master boundary paragraph"),
        ("마지막 main production frontier 변경은 PR #55 병합이다.", "마지막 main production frontier 변경은 PR #57 병합이다.", "master execution"),
        ("의 `041–045`다.", "의 `046–050`다.", "master next phrase"),
    ):
        t = replace_once(t, old, new, label)
    bridge = (
        "- 040 `아버지의 자리`: 윌리엄의 사랑과 잘못을 동시에 인정하고 엘리스가 자기 방식의 책임을 선택하며 Part 1 본편을 닫는다.\n"
        "- 041 `잘 돌아왔다`: 가족 재회와 살아 돌아온 관계를 Aftermath & 8-year Bridge의 출발점으로 재정렬한다.\n"
        "- 042 `살아 돌아온 몸`: 주안의 변화한 몸을 보상으로 단순화하지 않고 선택 침식 가능성이 있는 후유 상태로 검증한다.\n"
        "- 043 `확인하고 설명하겠습니다`: 주안은 자기 감정의 기원을 검증하되 엘리스의 현재 선택을 대신 판정하지 않는다.\n"
        "- 044 `응답하지 않은 호출기`: 미응답을 영구 이별로 확정하지 않고 수신기를 보존한다.\n"
        "- 045 `노란 옷은 안 입습니다`: 황색과 거리를 둔 주안의 현재 선택을 고정하고 다음 Bridge 생활·훈련 축으로 넘긴다."
    )
    t = replace_once(t, "- 040 `아버지의 자리`: 윌리엄의 사랑과 잘못을 동시에 인정하고 엘리스가 자기 방식의 책임을 선택하며 Part 1 본편을 닫는다.", bridge, "master bridge readback")
    p.write_text(t, encoding="utf-8")


def patch_status_files() -> None:
    p = ROOT / "fiction/MANUSCRIPT_INDEX.json"
    data = load(p)
    data["status"] = str(data.get("status", "")).replace("PENDING_CURRENT_PREFIX_001_045_PR57", "CURRENT_PREFIX_001_045")
    dump(p, data)

    for rel in (
        "fiction/analysis/MANUSCRIPT_INDEX_OVERRIDE_041_045.json",
        "fiction/analysis/REVERSE_OUTLINE_OVERRIDE_041_045.json",
    ):
        p = ROOT / rel
        data = load(p)
        data["status"] = str(data.get("status", "")).replace("BRIDGE_CURRENT_RECONCILED_PENDING_PR57", "BRIDGE_CURRENT_RECONCILED")
        dump(p, data)

    p = ROOT / "fiction/analysis/SCENE_PASS_REGISTRY.json"
    data = load(p)
    rec = data["external_artifact_reconciliation"]
    rec["rule"] = "Chapters 1-45 are the bounded reconciled production prefix on main after PR #57. Ch041-066 are Aftermath & 8-year Bridge; stored Ch46+ remain legacy until their own pass; 101-105 remains fail-closed."
    for item in data.get("completed_bundle_passes", []):
        if item.get("bundle") == "fiction/manuscript/part-1/041-045.md":
            item["status"] = "COMPLETE_CURRENT_SOURCE_CANON_RECONCILIATION / BRIDGE_CURRENT_PREFIX"
    dump(p, data)


def main() -> None:
    patch_receipt()
    patch_active()
    patch_handoff()
    patch_start_here()
    patch_master()
    patch_status_files()
    print("closed PR57 frontier receipt semantics at production 001-045")


if __name__ == "__main__":
    main()
