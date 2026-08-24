#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
ACTIVE = ROOT / "fiction/ACTIVE_CONTEXT.md"
HANDOFF = ROOT / "fiction/HANDOFF.md"
START = ROOT / "[소설]/00_운영체계/START_HERE.md"
MASTER = ROOT / "fiction/FICTION_MASTER.md"


def replace(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise SystemExit(f"pending-state patch target missing: {label}")
    return text.replace(old, new)


def update_receipt() -> None:
    data = json.loads(RECEIPT.read_text(encoding="utf-8"))
    data.update(
        {
            "frontier_observed_at_main": None,
            "last_frontier_change_pr": 50,
            "pending_frontier_change_pr": 55,
            "verified_prefix_end": 40,
            "legacy_tail_starts_at": 41,
            "boundary_after_chapter": 40,
            "next_bounded_bundle": "fiction/manuscript/part-1/041-045.md",
            "whole_manuscript_continuity": "NOT_YET_CLAIMED",
        }
    )
    RECEIPT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_active() -> None:
    text = ACTIVE.read_text(encoding="utf-8")
    for old, new, label in (
        ("frontier_observed_at_main: 7bc710f693bd4dec8c6929a6282653c288b252d9", "frontier_observed_at_main: null", "active observed main"),
        ("pending_frontier_change_pr: null", "pending_frontier_change_pr: 55", "active pending PR"),
        ("reconciled_prefix_end: 35", "reconciled_prefix_end: 40", "active prefix"),
        ("legacy_tail_starts_at: 36", "legacy_tail_starts_at: 41", "active tail"),
        ("boundary_after_chapter: 35", "boundary_after_chapter: 40", "active boundary"),
        ("next_bounded_bundle: fiction/manuscript/part-1/036-040.md", "next_bounded_bundle: fiction/manuscript/part-1/041-045.md", "active next"),
        ("## Current production prefix 001–035 contract", "## Pending PR #55 candidate prefix 001–040 contract\n\n> GitHub `main` production은 PR #55 병합 전까지 `001–035`다. 아래 `001–040`은 exact-head 검증 중인 **pending candidate**이며 production 완료 주장이 아니다.", "active contract heading"),
        ("- **PR #50: Ch031–035 user-source bounded promotion merged; production frontier is 001–035.**", "- **PR #50: Ch031–035 user-source bounded promotion merged; main production frontier is 001–035.**\n- **PR #55: Ch036–040 user-source bounded promotion pending candidate; candidate frontier 001–040, not main production until merge.**", "active milestones"),
        ("left_current: 35\nright_legacy: 36", "left_current: 40\nright_legacy: 41", "active boundary block"),
        ("Ch30→31 current continuity는 PASS다. 저장 화수가 인접하다는 이유만으로 current Ch35→legacy Ch36 연속성을 production으로 주장하지 않는다.", "PR #55 candidate에서는 Ch35→36 연결을 검증했고 현재 fail-closed 경계는 Ch40→41이다. 다만 GitHub `main` production frontier는 PR #55 병합 전까지 001–035로 유지한다.", "active boundary prose"),
        ("## Next exact work\n\n`fiction/manuscript/part-1/036-040.md`\n\n다음 pass는 **Ch35→36 migration boundary**에서 같은 사용자 지정 `031–040` source를 기준으로 시작한다.", "## Next exact work after PR #55 merge\n\n`fiction/manuscript/part-1/041-045.md`\n\nPR #55가 exact-head Green·review thread 0·main freshness를 통과해 병합된 뒤 **Ch40→41 migration boundary**에서 다음 사용자 지정 `041–050` source로 진행한다.", "active next prose"),
    ):
        text = replace(text, old, new, label)
    ACTIVE.write_text(text, encoding="utf-8")


def update_handoff() -> None:
    text = HANDOFF.read_text(encoding="utf-8")
    for old, new, label in (
        ("frontier_observed_at_main: 7bc710f693bd4dec8c6929a6282653c288b252d9", "frontier_observed_at_main: null", "handoff observed main"),
        ("pending_frontier_change_pr: null", "pending_frontier_change_pr: 55", "handoff pending"),
        ("reconciled_prefix_end: 35", "reconciled_prefix_end: 40", "handoff prefix"),
        ("legacy_tail_starts_at: 36", "legacy_tail_starts_at: 41", "handoff tail"),
        ("boundary_after_chapter: 35", "boundary_after_chapter: 40", "handoff boundary"),
        ("next_bounded_bundle: fiction/manuscript/part-1/036-040.md", "next_bounded_bundle: fiction/manuscript/part-1/041-045.md", "handoff next"),
        ("`frontier_observed_at_main`은 PR #50이 production frontier를 `001–035`로 이동시킨 실제 merge 증거다. 최신 저장소 SHA는 작업 시작 때 다시 조회한다.", "`frontier_observed_at_main: null`은 PR #55가 아직 pending candidate임을 뜻한다. 마지막 실제 main frontier 변경은 PR #50의 `001–035`이며, PR #55 병합 전 `001–040`을 main production으로 부르지 않는다.", "handoff observed prose"),
        ("- **PR #50: Ch031–035 user-source bounded promotion merged.**\n- production prefix: `001–035`.\n- fail-closed boundary: `35→36`.\n- next source bundle: `036–040` from the same user-designated 031–040 DOCX.", "- **PR #50: Ch031–035 user-source bounded promotion merged.**\n- **PR #55: Ch036–040 user-source bounded promotion pending candidate.**\n- main production prefix: `001–035`; pending candidate prefix: `001–040`.\n- candidate fail-closed boundary: `40→41`.\n- next bundle after PR #55 merge: `041–045` from the user-designated 041–050 source.", "handoff current state"),
        ("left_current: 35\nright_legacy: 36", "left_current: 40\nright_legacy: 41", "handoff boundary block"),
        ("Ch30→31은 current continuity다. 인접 번호만으로 Ch35→36을 current continuity로 올리지 않는다.", "PR #55 candidate에서 Ch35→36은 exact source와 consumer 검증으로 연결되며, 새 fail-closed candidate 경계는 Ch40→41이다. main은 PR #55 병합 전까지 001–035 production이다.", "handoff boundary prose"),
        ("## 다음 정확한 작업\n\n`fiction/manuscript/part-1/036-040.md`\n\n같은 사용자 지정 `031–040` 원본을 기준으로 Ch35→36 경계를 다시 열고, exact body → index → reverse outline → Scene Pass → router → regression contract 순으로 동일한 bounded promotion을 진행한다.", "## 다음 정확한 작업\n\n현재: PR #55 exact-head validation → review thread 0 → main freshness → squash merge.\n\n병합 뒤: `fiction/manuscript/part-1/041-045.md`를 사용자 지정 `041–050` 원본으로 bounded promotion한다.", "handoff next prose"),
    ):
        text = replace(text, old, new, label)
    HANDOFF.write_text(text, encoding="utf-8")


def update_start() -> None:
    text = START.read_text(encoding="utf-8")
    for old, new, label in (
        ("repository_reconciled_prefix: 001-035", "repository_candidate_prefix: 001-040", "start candidate prefix"),
        ("legacy_tail_starts_at: 036", "legacy_tail_starts_at: 041", "start tail"),
        ("last_frontier_change_pr: 50\nnext_bundle: fiction/manuscript/part-1/036-040.md", "last_frontier_change_pr: 50\npending_frontier_pr: 55\nnext_bundle_after_merge: fiction/manuscript/part-1/041-045.md", "start pending metadata"),
        ("- `001–035`: PR #50까지 production으로 승격 완료.\n- `005→006`, `010→011`, `015→016`, `020→021`, `025→026`, `030→031`: current continuity PASS.\n- Ch35 reverse outline: `next_chapter=null`.\n- legacy Ch36 reverse outline: `previous_chapter=null`.\n- `035→036`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "- GitHub `main` production: `001–035` (PR #50).\n- PR #55 pending candidate: `001–040`; 아직 main production 완료가 아니다.\n- candidate continuity는 `035→036`까지 연결 검증됨.\n- Ch40 reverse outline: `next_chapter=null`.\n- legacy Ch41 reverse outline: `previous_chapter=null`.\n- `040→041`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.", "start boundary section"),
        ("다음 시작 묶음:\n`fiction/manuscript/part-1/036-040.md`\n\n같은 사용자 지정 `031–040` source를 사용한다.", "현재 PR #55 후보 묶음:\n`fiction/manuscript/part-1/036-040.md`\n\n병합 후 다음 묶음:\n`fiction/manuscript/part-1/041-045.md` · 사용자 지정 `041–050` source를 사용한다.", "start current work"),
    ):
        text = replace(text, old, new, label)
    START.write_text(text, encoding="utf-8")


def update_master() -> None:
    text = MASTER.read_text(encoding="utf-8")
    for old, new, label in (
        ("reconciled_prefix: 001-035\nlegacy_tail_starts_at: 036\nboundary_after_chapter: 035\nwhole_manuscript_continuity: NOT_YET_CLAIMED\nlast_frontier_change_pr: 50\nnext_reconciliation: 036-040", "reconciled_prefix: 001-040\nlegacy_tail_starts_at: 041\nboundary_after_chapter: 040\nwhole_manuscript_continuity: NOT_YET_CLAIMED\nlast_frontier_change_pr: 50\npending_frontier_change_pr: 55\nmain_frontier_before_pending: 001-035\nnext_reconciliation_after_merge: 041-045", "master yaml"),
        ("## 6. current production prefix 001–035 readback", "## 6. pending PR #55 candidate prefix 001–040 readback\n\n> `001–040`은 PR #55 branch candidate다. GitHub `main` production은 병합 전까지 `001–035`로 유지한다.", "master section"),
        ("left_current: 35\nright_legacy: 36", "left_current: 40\nright_legacy: 41", "master boundary block"),
        ("Ch30→31 current continuity는 PASS다. 새 fail-closed 경계는 Ch35→36이며 Ch36은 별도 pass 전까지 legacy tail이다.", "PR #55 candidate에서는 Ch35→36 연결을 검증했고 새 fail-closed 경계는 Ch40→41이다. main production은 PR #55 병합 전까지 001–035다.", "master boundary prose"),
        ("마지막 production frontier 변경은 PR #50 병합이다.", "마지막 main production frontier 변경은 PR #50 병합이다. PR #55는 036–040 pending candidate이며 병합 전 production 완료로 부르지 않는다.", "master execution"),
        ("다음 bounded unit은 같은 사용자 지정 `031–040` 원본의 `036–040`이다.", "PR #55 병합 뒤 다음 bounded unit은 사용자 지정 `041–050` 원본의 `041–045`다.", "master next"),
    ):
        text = replace(text, old, new, label)
    MASTER.write_text(text, encoding="utf-8")


def main() -> None:
    update_receipt()
    update_active()
    update_handoff()
    update_start()
    update_master()
    print("synchronized PR55 pending candidate receipt and live routers")


if __name__ == "__main__":
    main()
