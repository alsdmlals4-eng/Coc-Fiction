#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본(1).docx"
SOURCE_SHA = "9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad"
PENDING_PR = 57
MAIN_PREFIX = 40
CANDIDATE_PREFIX = 45
TAIL = 46
NEXT_BUNDLE = "fiction/manuscript/part-1/046-050.md"


def replace_yaml_block(path: Path, replacements: dict[str, str], additions: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    start = text.find("```yaml\n")
    if start < 0:
        raise SystemExit(f"yaml block missing: {path}")
    body_start = start + len("```yaml\n")
    end = text.find("\n```", body_start)
    if end < 0:
        raise SystemExit(f"yaml block close missing: {path}")
    block = text[body_start:end]
    lines = block.splitlines()
    seen = set()
    out = []
    for line in lines:
        if ":" not in line:
            out.append(line)
            continue
        key = line.split(":", 1)[0].strip()
        if key in replacements:
            out.append(f"{key}: {replacements[key]}")
            seen.add(key)
        else:
            out.append(line)
    for item in additions:
        key = item.split(":", 1)[0].strip()
        if key not in {line.split(":", 1)[0].strip() for line in out if ":" in line}:
            out.append(item)
    missing = set(replacements) - seen
    if missing:
        raise SystemExit(f"yaml keys missing in {path}: {sorted(missing)}")
    text = text[:body_start] + "\n".join(out) + text[end:]
    path.write_text(text, encoding="utf-8")


def patch_receipt() -> None:
    path = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update(
        {
            "frontier_observed_at_main": None,
            "last_frontier_change_pr": 55,
            "pending_frontier_change_pr": PENDING_PR,
            "verified_prefix_end": CANDIDATE_PREFIX,
            "legacy_tail_starts_at": TAIL,
            "boundary_after_chapter": CANDIDATE_PREFIX,
            "next_bounded_bundle": NEXT_BUNDLE,
            "whole_manuscript_continuity": "NOT_YET_CLAIMED",
            "candidate_sha256": SOURCE_SHA,
        }
    )
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def patch_active() -> None:
    path = ROOT / "fiction/ACTIVE_CONTEXT.md"
    replace_yaml_block(
        path,
        {
            "frontier_observed_at_main": "null",
            "last_frontier_change_pr": "55",
            "pending_frontier_change_pr": str(PENDING_PR),
            "current_bundle_source": SOURCE,
            "current_bundle_source_sha256": SOURCE_SHA,
            "reconciled_prefix_end": str(CANDIDATE_PREFIX),
            "legacy_tail_starts_at": str(TAIL),
            "boundary_after_chapter": str(CANDIDATE_PREFIX),
            "next_bounded_bundle": NEXT_BUNDLE,
        },
        [
            f"main_production_prefix_end: {MAIN_PREFIX}",
            f"candidate_prefix_end: {CANDIDATE_PREFIX}",
        ],
    )
    text = path.read_text(encoding="utf-8")
    old = "PR #55 병합으로 Ch35→36이 current continuity가 되었고 현재 main fail-closed 경계는 Ch40→41이다."
    new = (
        "PR #55 병합 기준 main production은 `001–040` / `040→041`이다. "
        "현재 PR #57 candidate는 exact-source 검증을 거쳐 `001–045` / `045→046`으로 이동 중이며, "
        "merge 전까지 production으로 간주하지 않는다."
    )
    text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def patch_handoff() -> None:
    path = ROOT / "fiction/HANDOFF.md"
    replace_yaml_block(
        path,
        {
            "frontier_observed_at_main": "null",
            "last_frontier_change_pr": "55",
            "pending_frontier_change_pr": str(PENDING_PR),
            "current_bundle_source": SOURCE,
            "current_bundle_source_sha256": SOURCE_SHA,
            "reconciled_prefix_end": str(CANDIDATE_PREFIX),
            "legacy_tail_starts_at": str(TAIL),
            "boundary_after_chapter": str(CANDIDATE_PREFIX),
            "next_bounded_bundle": NEXT_BUNDLE,
        },
        [
            f"main_production_prefix_end: {MAIN_PREFIX}",
            f"candidate_prefix_end: {CANDIDATE_PREFIX}",
        ],
    )
    text = path.read_text(encoding="utf-8")
    marker = "- **PR #55: Ch036–040 user-source bounded promotion merged.**\n"
    if "PR #57" not in text:
        text = text.replace(
            marker,
            marker + "- **PR #57: Bridge Ch041–045 user-source bounded promotion candidate; merge 전 production 아님.**\n",
            1,
        )
    text = text.replace(
        "- production prefix: `001–040`.\n- fail-closed boundary: `40→41`.\n- next bundle: `041–045` from the user-designated 041–050 source.",
        "- main production prefix: `001–040`.\n- PR #57 candidate prefix: `001–045`.\n- candidate fail-closed boundary: `45→46`.\n- next bundle after merge: `046–050` from the same user-designated 041–050 source.",
    )
    path.write_text(text, encoding="utf-8")


def patch_start_here() -> None:
    path = ROOT / "[소설]/00_운영체계/START_HERE.md"
    replace_yaml_block(
        path,
        {
            "current_bundle_source": SOURCE,
            "current_bundle_source_sha256": SOURCE_SHA,
            "repository_reconciled_prefix": "001-040",
            "legacy_tail_starts_at": f"{TAIL:03d}",
            "last_frontier_change_pr": "55",
            "next_bundle": "fiction/manuscript/part-1/041-045.md",
        },
        [
            f"main_production_prefix: 001-{MAIN_PREFIX:03d}",
            f"repository_candidate_prefix: 001-{CANDIDATE_PREFIX:03d}",
            f"pending_frontier_pr: {PENDING_PR}",
            f"next_bundle_after_merge: {NEXT_BUNDLE}",
        ],
    )
    text = path.read_text(encoding="utf-8")
    text = text.replace("legacy_tail_starts_at: 041", f"legacy_tail_starts_at: {TAIL:03d}", 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    patch_receipt()
    patch_active()
    patch_handoff()
    patch_start_here()
    print("patched PR57 candidate receipt and live routers")


if __name__ == "__main__":
    main()
