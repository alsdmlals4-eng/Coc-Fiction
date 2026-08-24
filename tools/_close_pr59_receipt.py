#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MERGE_SHA = "431acae9b6e62dfd3a26fe177724314dfe4004e7"
SOURCE = "폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본(1).docx"
SOURCE_SHA = "9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old in text:
        return text.replace(old, new, 1)
    if new in text:
        return text
    raise SystemExit(f"closure marker missing: {label}")


def close_receipt() -> None:
    p = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
    data = load(p)
    data.update({
        "frontier_observed_at_main": MERGE_SHA,
        "last_frontier_change_pr": 59,
        "pending_frontier_change_pr": None,
        "verified_prefix_end": 50,
        "legacy_tail_starts_at": 51,
        "boundary_after_chapter": 50,
        "next_bounded_bundle": "fiction/manuscript/part-1/051-055.md",
        "whole_manuscript_continuity": "NOT_YET_CLAIMED",
        "candidate_sha256": SOURCE_SHA,
    })
    dump(p, data)


def patch_active() -> None:
    p = ROOT / "fiction/ACTIVE_CONTEXT.md"
    t = p.read_text(encoding="utf-8")
    for old,new,label in (
        ("frontier_observed_at_main: null", f"frontier_observed_at_main: {MERGE_SHA}", "active sha"),
        ("last_frontier_change_pr: 57", "last_frontier_change_pr: 59", "active last pr"),
        ("pending_frontier_change_pr: 59", "pending_frontier_change_pr: null", "active pending"),
        ("main_production_prefix_end: 45\ncandidate_prefix_end: 50\n", "main_production_prefix_end: 50\n", "active candidate keys"),
        ("## Current main production 001–045 / PR #59 candidate 001–050 contract", "## Current production prefix 001–050 contract", "active title"),
        ("Main production은 PR #57 기준 `001–045 / 045→046`이다. PR #59 candidate는 exact-source 검증을 거쳐 `001–050 / 050→051`로 이동 중이며 merge 전까지 production으로 간주하지 않는다.", "PR #59 병합으로 Ch45→46은 current continuity가 되었고 현재 main fail-closed 경계는 `050→051`이다.", "active boundary prose"),
        ("- **PR #57: Bridge Ch041–045 user-source bounded promotion merged; production frontier is 001–045.**", "- **PR #57: Bridge Ch041–045 user-source bounded promotion merged.**\n- **PR #59: Bridge Ch046–050 user-source bounded promotion merged; production frontier is 001–050.**", "active milestone"),
    ):
        t = replace_once(t, old, new, label)
    p.write_text(t, encoding="utf-8")


def patch_handoff() -> None:
    p = ROOT / "fiction/HANDOFF.md"
    t = p.read_text(encoding="utf-8")
    for old,new,label in (
        ("frontier_observed_at_main: null", f"frontier_observed_at_main: {MERGE_SHA}", "handoff sha"),
        ("last_frontier_change_pr: 57", "last_frontier_change_pr: 59", "handoff last pr"),
        ("pending_frontier_change_pr: 59", "pending_frontier_change_pr: null", "handoff pending"),
        ("main_production_prefix_end: 45\ncandidate_prefix_end: 50\n", "main_production_prefix_end: 50\n", "handoff candidate keys"),
        ("- **PR #57: Bridge Ch041–045 user-source bounded promotion merged.**", "- **PR #57: Bridge Ch041–045 user-source bounded promotion merged.**\n- **PR #59: Bridge Ch046–050 user-source bounded promotion merged.**", "handoff milestone"),
        ("- main production prefix: `001–045`.\n- PR #59 candidate prefix: `001–050`.\n- candidate fail-closed boundary: `50→51`.\n- next bundle after merge: `051–055`.", "- production prefix: `001–050`.\n- fail-closed boundary: `50→51`.\n- next bundle: `051–055`.", "handoff current status"),
        ("Main production은 `001–045 / 045→046`이며 PR #59 candidate는 `001–050 / 050→051`로 이동 중이다. merge 전에는 candidate를 production으로 간주하지 않는다.", "PR #59 병합으로 Ch45→46은 current continuity가 되었고 main의 새 fail-closed 경계는 Ch50→51이다.", "handoff boundary prose"),
        ("`fiction/manuscript/part-1/046-050.md`를 `폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본(1).docx` / SHA256 `9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad` 기준으로 bounded promotion한다.", "다음 bounded unit은 `fiction/manuscript/part-1/051-055.md`다. 재개 시 source manifest와 Library에서 해당 구간 사용자 지정 원본을 다시 확인한 뒤 작업한다.", "handoff next work"),
    ):
        t = replace_once(t, old, new, label)
    p.write_text(t, encoding="utf-8")


def patch_start_here() -> None:
    p = ROOT / "[소설]/00_운영체계/START_HERE.md"
    t = p.read_text(encoding="utf-8")
    for old,new,label in (
        ("repository_reconciled_prefix: 001-045", "repository_reconciled_prefix: 001-050", "start prefix"),
        ("last_frontier_change_pr: 57", "last_frontier_change_pr: 59", "start last pr"),
        ("next_bundle: fiction/manuscript/part-1/046-050.md", "next_bundle: fiction/manuscript/part-1/051-055.md", "start next"),
        ("main_production_prefix: 001-045\nrepository_candidate_prefix: 001-050\npending_frontier_pr: 59\nnext_bundle_after_merge: fiction/manuscript/part-1/051-055.md\n", "main_production_prefix: 001-050\n", "start candidate keys"),
        ("- GitHub `main` production: `001–045` (PR #57).", "- GitHub `main` production: `001–050` (PR #59).", "start production"),
        ("- main `045→046`은 아직 production 경계다.\n- PR #59 candidate `050→051`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "- `045→046`은 current continuity PASS.\n- `050→051`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "start boundary"),
        ("`fiction/manuscript/part-1/046-050.md`", "`fiction/manuscript/part-1/051-055.md`", "start work bundle"),
        ("Ch50→51 boundary verification\n→ exact source Ch46-50 receipt verification", "Ch50→51 boundary verification\n→ source manifest / Library exact source lookup for Ch51-55", "start steps"),
    ):
        t = replace_once(t, old, new, label)
    p.write_text(t, encoding="utf-8")


def patch_master() -> None:
    p = ROOT / "fiction/FICTION_MASTER.md"
    t = p.read_text(encoding="utf-8")
    for old,new,label in (
        ("reconciled_prefix: 001-045", "reconciled_prefix: 001-050", "master prefix"),
        ("legacy_tail_starts_at: 046", "legacy_tail_starts_at: 051", "master tail"),
        ("boundary_after_chapter: 045", "boundary_after_chapter: 050", "master boundary"),
        ("last_frontier_change_pr: 57", "last_frontier_change_pr: 59", "master last pr"),
        ("next_reconciliation: 046-050", "next_reconciliation: 051-055", "master next"),
        ("## 6. current production prefix 001–045 readback", "## 6. current production prefix 001–050 readback", "master title"),
        ("left_current: 45\nright_legacy: 46", "left_current: 50\nright_legacy: 51", "master boundary block"),
        ("PR #57 병합으로 Ch40→41은 current continuity가 되었고 새 main fail-closed 경계는 Ch45→46이다.", "PR #59 병합으로 Ch45→46은 current continuity가 되었고 새 main fail-closed 경계는 Ch50→51이다.", "master boundary prose"),
        ("마지막 main production frontier 변경은 PR #57 병합이다.", "마지막 main production frontier 변경은 PR #59 병합이다.", "master execution"),
        ("의 `046–050`다.", "의 `051–055`다.", "master next phrase"),
    ):
        t = replace_once(t, old, new, label)
    if "- 046 `자아를 찾으러 떠났습니다`" not in t:
        marker = "- 045 `노란 옷은 안 입습니다`: 황색과 거리를 둔 주안의 현재 선택을 고정하고 다음 Bridge 생활·훈련 축으로 넘긴다."
        block = marker + "\n" + "\n".join([
            "- 046 `자아를 찾으러 떠났습니다`: 황색 내부의 소속을 계약 가능한 손님 관계로 제한하고 임무 뒤 귀환도 주안 자신의 선택으로 남긴다.",
            "- 047 `호수가 보이는 마을`: 8년 뒤 독립 성장한 이안과 주안의 동선을 실종·기억 혼란 사건과 재회 압력으로 모은다. 폐기된 연락축 표기 1건은 current Canon에 따라 일반 외부 연락책으로 최소 치환했다.",
            "- 048 `돼지고기는 아니었습니다`: 수상한 식당과 실종 흔적을 검증하고 묶인 아킴의 구조를 재회보다 먼저 선택한다.",
            "- 049 `여덟 해 만입니다`: 이안·주안·아킴 재회를 성립시키되 각자의 8년 성장과 가론의 반복되는 폭력 패턴을 동시에 보존한다.",
            "- 050 `낙원의 손님분들`: 문과 대화를 먼저 시도해 낙원에 환자 위장으로 진입하고, 루바의 기억 관련 물을 다음 Ch51 압력으로 넘긴다.",
        ])
        t = replace_once(t, marker, block, "master 046-050 readback")
    p.write_text(t, encoding="utf-8")


def patch_status() -> None:
    p = ROOT / "fiction/MANUSCRIPT_INDEX.json"
    data = load(p)
    data["status"] = str(data.get("status", "")).replace("PENDING_CURRENT_PREFIX_001_050_PR59", "CURRENT_PREFIX_001_050")
    dump(p, data)

    for rel in (
        "fiction/analysis/MANUSCRIPT_INDEX_OVERRIDE_046_050.json",
        "fiction/analysis/REVERSE_OUTLINE_OVERRIDE_046_050.json",
    ):
        p = ROOT / rel
        data = load(p)
        data["status"] = str(data.get("status", "")).replace("BRIDGE_CURRENT_RECONCILED_PENDING_PR59", "BRIDGE_CURRENT_RECONCILED")
        dump(p, data)

    p = ROOT / "fiction/analysis/SCENE_PASS_REGISTRY.json"
    data = load(p)
    rec = data["external_artifact_reconciliation"]
    rec["rule"] = "Chapters 1-50 are the bounded reconciled production prefix on main after PR #59. Ch041-066 are Aftermath & 8-year Bridge; stored Ch51+ remain legacy until their own pass; 101-105 remains fail-closed."
    for item in data.get("completed_bundle_passes", []):
        if item.get("bundle") == "fiction/manuscript/part-1/046-050.md":
            item["status"] = "COMPLETE_CURRENT_SOURCE_CANON_RECONCILIATION / BRIDGE_CURRENT_PREFIX"
    dump(p, data)


def main() -> None:
    close_receipt()
    patch_active()
    patch_handoff()
    patch_start_here()
    patch_master()
    patch_status()
    print("closed PR59 frontier receipt semantics at production 001-050")


if __name__ == "__main__":
    main()
