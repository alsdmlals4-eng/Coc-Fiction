#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MERGE_SHA = "e4d904101635fad36b7d470251b48b370143f369"
NEXT_SOURCE = "폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본(1).docx"
NEXT_SOURCE_SHA = "9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise SystemExit(f"closure patch target missing: {label}")
    return text.replace(old, new)


def close_receipt() -> None:
    path = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
    data = load(path)
    data.update(
        {
            "frontier_observed_at_main": MERGE_SHA,
            "last_frontier_change_pr": 55,
            "pending_frontier_change_pr": None,
            "verified_prefix_end": 40,
            "legacy_tail_starts_at": 41,
            "boundary_after_chapter": 40,
            "next_bounded_bundle": "fiction/manuscript/part-1/041-045.md",
            "whole_manuscript_continuity": "NOT_YET_CLAIMED",
        }
    )
    dump(path, data)


def close_active() -> None:
    path = ROOT / "fiction/ACTIVE_CONTEXT.md"
    text = path.read_text(encoding="utf-8")
    replacements = (
        ("frontier_observed_at_main: null", f"frontier_observed_at_main: {MERGE_SHA}", "active observed"),
        ("last_frontier_change_pr: 50", "last_frontier_change_pr: 55", "active last PR"),
        ("pending_frontier_change_pr: 55", "pending_frontier_change_pr: null", "active pending"),
        ("- **PR #50: Ch031–035 user-source bounded promotion merged; main production frontier is 001–035.**\n- **PR #55: Ch036–040 user-source bounded promotion pending candidate; candidate frontier 001–040, not main production until merge.**", "- **PR #50: Ch031–035 user-source bounded promotion merged.**\n- **PR #55: Ch036–040 user-source bounded promotion merged; production frontier is 001–040.**", "active milestones"),
        ("## Pending PR #55 candidate prefix 001–040 contract\n\n> GitHub `main` production은 PR #55 병합 전까지 `001–035`다. 아래 `001–040`은 exact-head 검증 중인 **pending candidate**이며 production 완료 주장이 아니다.", "## Current production prefix 001–040 contract", "active heading"),
        ("- Ch35: 주안·엘리스·이안·아킴의 협업으로 쇼거스 핵을 소진한다. 세실리아는 생존 상태로 노출되며 원인은 아직 미확정이다. 탈론의 세실리아 회수 행동은 Ch36으로 이어지지만 Ch36은 아직 legacy tail이다.", "- Ch35: 주안·엘리스·이안·아킴의 협업으로 쇼거스 핵을 소진한다. 세실리아는 생존 상태로 노출되며 원인은 아직 미확정이다. 탈론의 세실리아 회수 행동은 Ch36으로 이어진다.\n- Ch36: 세실리아 회수 직후 탈론의 사명과 결말을 닫되 그의 핵심 적대 위상을 약화하지 않는다. 황색 지휘부 손실을 조직 전체 소멸로 확대하지 않는다.\n- Ch37: 승리와 소유를 분리하고 전투 중지·협상으로 다음 갈등 방식을 전환한다.\n- Ch38: 엘리스가 자발적 인질 제안을 협상 수단으로 선택하며 결정권을 직접 행사한다.\n- Ch39: 델타그린 군함 도착으로 전장 권력축이 재배치되지만 기존 세력의 의미를 자동 소거하지 않는다.\n- Ch40: 윌리엄의 사랑과 잘못을 동시에 인정하고 엘리스가 아버지의 방식이 아닌 자기 방식의 책임을 선택하며 Part 1 본편을 닫는다.", "active 036-040 readback"),
        ("PR #55 candidate에서는 Ch35→36 연결을 검증했고 현재 fail-closed 경계는 Ch40→41이다. 다만 GitHub `main` production frontier는 PR #55 병합 전까지 001–035로 유지한다.", "PR #55 병합으로 Ch35→36이 current continuity가 되었고 현재 main fail-closed 경계는 Ch40→41이다.", "active boundary prose"),
        ("## Next exact work after PR #55 merge\n\n`fiction/manuscript/part-1/041-045.md`\n\nPR #55가 exact-head Green·review thread 0·main freshness를 통과해 병합된 뒤 **Ch40→41 migration boundary**에서 다음 사용자 지정 `041–050` source로 진행한다.", f"## Next exact work\n\n`fiction/manuscript/part-1/041-045.md`\n\n**Ch40→41 migration boundary**에서 사용자 지정 `{NEXT_SOURCE}` / SHA256 `{NEXT_SOURCE_SHA}`를 기준으로 진행한다. 041–066은 Aftermath & 8년 Bridge이며 Part 2(067+)와 섞지 않는다.", "active next"),
    )
    for old, new, label in replacements:
        text = replace(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def close_handoff() -> None:
    path = ROOT / "fiction/HANDOFF.md"
    text = path.read_text(encoding="utf-8")
    replacements = (
        ("frontier_observed_at_main: null", f"frontier_observed_at_main: {MERGE_SHA}", "handoff observed"),
        ("last_frontier_change_pr: 50", "last_frontier_change_pr: 55", "handoff last PR"),
        ("pending_frontier_change_pr: 55", "pending_frontier_change_pr: null", "handoff pending"),
        ("`frontier_observed_at_main: null`은 PR #55가 아직 pending candidate임을 뜻한다. 마지막 실제 main frontier 변경은 PR #50의 `001–035`이며, PR #55 병합 전 `001–040`을 main production으로 부르지 않는다.", f"`frontier_observed_at_main`은 PR #55가 production frontier를 `001–040`으로 이동시킨 실제 merge `{MERGE_SHA}`를 기록한다. 저장소 최신 SHA 포인터로 재사용하지 않고 재개 시 최신 main을 다시 조회한다.", "handoff observed prose"),
        ("- **PR #50: Ch031–035 user-source bounded promotion merged.**\n- **PR #55: Ch036–040 user-source bounded promotion pending candidate.**\n- main production prefix: `001–035`; pending candidate prefix: `001–040`.\n- candidate fail-closed boundary: `40→41`.\n- next bundle after PR #55 merge: `041–045` from the user-designated 041–050 source.", "- **PR #50: Ch031–035 user-source bounded promotion merged.**\n- **PR #55: Ch036–040 user-source bounded promotion merged.**\n- production prefix: `001–040`.\n- fail-closed boundary: `40→41`.\n- next bundle: `041–045` from the user-designated 041–050 source.", "handoff state"),
        ("## Ch026–035 보호 readback", "## Ch026–040 보호 readback", "handoff readback heading"),
        ("- Ch35: 4인 협업으로 쇼거스 핵을 소진하고 세실리아를 생존 상태로 노출한다. 세실리아가 쇼거스 안에 있었던 원인은 아직 미확정이다.", "- Ch35: 4인 협업으로 쇼거스 핵을 소진하고 세실리아를 생존 상태로 노출한다. 세실리아가 쇼거스 안에 있었던 원인은 아직 미확정이다.\n- Ch36: 탈론의 사명과 결말을 source-supported 범위에서 닫고, 핵심 적대 위상과 황색 조직의 비소멸을 함께 보존한다.\n- Ch37–38: 승리=소유 프레임을 거부하고 엘리스가 협상·자발적 인질 선택으로 정치 전환을 주도한다.\n- Ch39: 델타그린 군함 도착으로 권력축이 재배치된다.\n- Ch40: 윌리엄의 사랑과 잘못을 동시에 보존한 채 엘리스가 자기 방식의 책임을 선택하고 Part 1 본편을 닫는다.", "handoff 036-040 readback"),
        ("PR #55 candidate에서 Ch35→36은 exact source와 consumer 검증으로 연결되며, 새 fail-closed candidate 경계는 Ch40→41이다. main은 PR #55 병합 전까지 001–035 production이다.", "PR #55 병합으로 Ch35→36은 current continuity가 되었고 main의 새 fail-closed 경계는 Ch40→41이다.", "handoff boundary"),
        ("현재: PR #55 exact-head validation → review thread 0 → main freshness → squash merge.\n\n병합 뒤: `fiction/manuscript/part-1/041-045.md`를 사용자 지정 `041–050` 원본으로 bounded promotion한다.", f"`fiction/manuscript/part-1/041-045.md`를 `{NEXT_SOURCE}` / SHA256 `{NEXT_SOURCE_SHA}` 기준으로 bounded promotion한다. 041–066은 Aftermath & 8년 Bridge이고 Part 2 진입은 067+다.", "handoff next"),
    )
    for old, new, label in replacements:
        text = replace(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def close_start() -> None:
    path = ROOT / "[소설]/00_운영체계/START_HERE.md"
    text = path.read_text(encoding="utf-8")
    replacements = (
        ("repository_candidate_prefix: 001-040", "repository_reconciled_prefix: 001-040", "start prefix"),
        ("last_frontier_change_pr: 50\npending_frontier_pr: 55\nnext_bundle_after_merge: fiction/manuscript/part-1/041-045.md", "last_frontier_change_pr: 55\nnext_bundle: fiction/manuscript/part-1/041-045.md", "start PR metadata"),
        ("- GitHub `main` production: `001–035` (PR #50).\n- PR #55 pending candidate: `001–040`; 아직 main production 완료가 아니다.\n- candidate continuity는 `035→036`까지 연결 검증됨.", "- GitHub `main` production: `001–040` (PR #55).\n- `035→036`은 current continuity PASS.", "start boundary state"),
        ("현재 PR #55 후보 묶음:\n`fiction/manuscript/part-1/036-040.md`\n\n병합 후 다음 묶음:\n`fiction/manuscript/part-1/041-045.md` · 사용자 지정 `041–050` source를 사용한다.", f"다음 시작 묶음:\n`fiction/manuscript/part-1/041-045.md`\n\n사용자 지정 `{NEXT_SOURCE}` / SHA256 `{NEXT_SOURCE_SHA}`를 사용한다. 041–066은 Aftermath & 8년 Bridge이며 Part 2는 067+다.", "start next work"),
        ("Ch35→36 boundary verification\n→ exact source Ch36-40 extraction", "Ch40→41 boundary verification\n→ exact source Ch41-45 extraction", "start lifecycle"),
    )
    for old, new, label in replacements:
        text = replace(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def close_master() -> None:
    path = ROOT / "fiction/FICTION_MASTER.md"
    text = path.read_text(encoding="utf-8")
    replacements = (
        ("last_frontier_change_pr: 50\npending_frontier_change_pr: 55\nmain_frontier_before_pending: 001-035\nnext_reconciliation_after_merge: 041-045", "last_frontier_change_pr: 55\npending_frontier_change_pr: null\nnext_reconciliation: 041-045", "master yaml"),
        ("## 6. pending PR #55 candidate prefix 001–040 readback\n\n> `001–040`은 PR #55 branch candidate다. GitHub `main` production은 병합 전까지 `001–035`로 유지한다.", "## 6. current production prefix 001–040 readback", "master heading"),
        ("- 035 `완전 소 생물`: 주안·엘리스·이안·아킴의 협업으로 쇼거스 핵을 소진한다. 세실리아는 생존 상태로 노출되며, 왜 쇼거스 안에 있었는지는 아직 미확정이다.", "- 035 `완전 소 생물`: 주안·엘리스·이안·아킴의 협업으로 쇼거스 핵을 소진한다. 세실리아는 생존 상태로 노출되며, 왜 쇼거스 안에 있었는지는 아직 미확정이다.\n- 036 `사명은 끝났다`: 탈론의 사명과 결말을 source-supported 범위에서 닫고 핵심 적대 위상·황색 조직의 비소멸을 보존한다.\n- 037 `승자의 손`: 승리와 소유를 분리하고 전투에서 협상으로 갈등 방식을 전환한다.\n- 038 `인질은 제가 되죠`: 엘리스가 자발적 인질 제안을 협상 수단으로 선택해 결정권을 행사한다.\n- 039 `군함이 왔다`: 델타그린 군함 도착으로 전장 권력축이 재배치된다.\n- 040 `아버지의 자리`: 윌리엄의 사랑과 잘못을 동시에 인정하고 엘리스가 자기 방식의 책임을 선택하며 Part 1 본편을 닫는다.", "master 036-040 readback"),
        ("PR #55 candidate에서는 Ch35→36 연결을 검증했고 새 fail-closed 경계는 Ch40→41이다. main production은 PR #55 병합 전까지 001–035다.", "PR #55 병합으로 Ch35→36은 current continuity가 되었고 새 main fail-closed 경계는 Ch40→41이다.", "master boundary"),
        ("마지막 main production frontier 변경은 PR #50 병합이다. PR #55는 036–040 pending candidate이며 병합 전 production 완료로 부르지 않는다.", "마지막 main production frontier 변경은 PR #55 병합이다.", "master execution"),
        ("PR #55 병합 뒤 다음 bounded unit은 사용자 지정 `041–050` 원본의 `041–045`다.", f"다음 bounded unit은 `{NEXT_SOURCE}` / SHA256 `{NEXT_SOURCE_SHA}`의 `041–045`다. 041–066은 Aftermath & 8년 Bridge이고 Part 2는 067+다.", "master next"),
    )
    for old, new, label in replacements:
        text = replace(text, old, new, label)
    path.write_text(text, encoding="utf-8")


def close_registry_and_statuses() -> None:
    path = ROOT / "fiction/analysis/SCENE_PASS_REGISTRY.json"
    data = load(path)
    rec = data["external_artifact_reconciliation"]
    rec["rule"] = "Chapters 1-40 are the bounded reconciled production prefix on main after PR #55. Stored Ch41+ remain legacy tail until their own pass; 101-105 remains fail-closed."
    for item in data.get("completed_bundle_passes", []):
        if item.get("bundle") == "fiction/manuscript/part-1/036-040.md":
            item["status"] = "COMPLETE_CURRENT_SOURCE_CANON_RECONCILIATION / CURRENT_PREFIX"
    dump(path, data)

    index_path = ROOT / "fiction/MANUSCRIPT_INDEX.json"
    index = load(index_path)
    index["status"] = "ACTIVE / COMPOSED / 225_STORAGE_CHAPTERS / MIXED_MIGRATION / CURRENT_PREFIX_001_040"
    dump(index_path, index)

    for rel in (
        "fiction/analysis/MANUSCRIPT_INDEX_OVERRIDE_036_040.json",
        "fiction/analysis/REVERSE_OUTLINE_OVERRIDE_036_040.json",
    ):
        target = ROOT / rel
        obj = load(target)
        obj["status"] = obj.get("status", "").replace(" / CURRENT_RECONCILED_PENDING_PR55", " / CURRENT_RECONCILED")
        dump(target, obj)


def main() -> None:
    close_receipt()
    close_active()
    close_handoff()
    close_start()
    close_master()
    close_registry_and_statuses()
    print("closed PR55 frontier receipt at main 001-040; next 041-045")


if __name__ == "__main__":
    main()
