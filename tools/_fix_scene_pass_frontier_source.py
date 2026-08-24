#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "check_fiction_scene_passes.py"

OLD = '''reconciliation = registry.get("external_artifact_reconciliation", {})
if reconciliation.get("artifact") != "폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx":
    errors.append("external reconciliation artifact mismatch")
if reconciliation.get("artifact_sha256") != "89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10":
    errors.append("external reconciliation artifact SHA mismatch")
'''

NEW = '''reconciliation = registry.get("external_artifact_reconciliation", {})
# The active reconciliation source must follow the current sequential frontier instead of
# being pinned to one historical source bundle. Find the completed pass that owns the
# frontier chapter and verify the receipt against its user-designated source evidence.
frontier_pass = None
for candidate in passes:
    candidate_chapters = [int(x) for x in candidate.get("chapters", [])]
    if candidate_chapters and max(candidate_chapters) == current_frontier:
        frontier_pass = candidate
        break
if frontier_pass is None:
    errors.append(f"no completed scene pass owns current frontier {current_frontier}")
else:
    source_files = [x for x in frontier_pass.get("source_files", []) if isinstance(x, dict)]
    authoritative_sources = [
        x for x in source_files
        if isinstance(x.get("name"), str)
        and isinstance(x.get("sha256"), str)
        and "user-designated" in str(x.get("role", "")).lower()
    ]
    if not authoritative_sources:
        authoritative_sources = [
            x for x in source_files
            if isinstance(x.get("name"), str) and isinstance(x.get("sha256"), str)
        ]
    if not authoritative_sources:
        errors.append(f"frontier scene pass {frontier_pass.get('bundle')} lacks source receipt")
    else:
        expected_source = authoritative_sources[0]
        if reconciliation.get("artifact") != expected_source.get("name"):
            errors.append("external reconciliation artifact mismatch")
        if reconciliation.get("artifact_sha256") != expected_source.get("sha256"):
            errors.append("external reconciliation artifact SHA mismatch")
'''


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    if NEW in text:
        print("scene-pass frontier source validation already dynamic")
        return
    if OLD not in text:
        raise SystemExit("expected hard-coded reconciliation source block not found")
    text = text.replace(OLD, NEW, 1)
    text = text.replace(
        'errors.append("reconciled prefix must be chapter 45 after current 036-040 propagation")',
        'errors.append("reconciled prefix must match the current bounded frontier")',
    )
    text = text.replace(
        'errors.append("legacy tail must begin at chapter 46 after current 036-040 propagation")',
        'errors.append("legacy tail must begin immediately after the current bounded frontier")',
    )
    TARGET.write_text(text, encoding="utf-8")
    print("patched scene-pass validator to derive active source from frontier pass")


if __name__ == "__main__":
    main()
