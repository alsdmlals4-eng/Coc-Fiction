#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "check_fiction_scene_passes.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise SystemExit(f"scene-pass validator patch target missing: {label}")
    return text.replace(old, new, 1)


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")

    text = replace_once(
        text,
        'passes = registry.get("completed_bundle_passes", [])\nby_bundle = {item.get("bundle"): item for item in passes}\n',
        'passes = registry.get("completed_bundle_passes", [])\nby_bundle = {item.get("bundle"): item for item in passes}\ncurrent_frontier = registry.get("external_artifact_reconciliation", {}).get("reconciled_prefix_end", 0)\nif not isinstance(current_frontier, int):\n    current_frontier = 0\n',
        "frontier prelude",
    )

    text = replace_once(
        text,
        '    for raw_number, expected_sha in item.get("preserved_boundary_shas", {}).items():\n        number = int(raw_number)\n        body = parsed.get(number, "")\n        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()\n        if actual != expected_sha:\n            errors.append(f"boundary chapter {number} SHA changed")\n',
        '    for raw_number, expected_sha in item.get("preserved_boundary_shas", {}).items():\n        number = int(raw_number)\n        chapter_numbers = [int(x) for x in item.get("chapters", [])]\n        # A right boundary can later become production in a subsequent bounded pass.\n        # Once that happens its old legacy SHA is historical evidence, not an active immutability gate.\n        if chapter_numbers and number > max(chapter_numbers) and number <= current_frontier:\n            continue\n        body = parsed.get(number, "")\n        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()\n        if actual != expected_sha:\n            errors.append(f"boundary chapter {number} SHA changed")\n',
        "historical right-boundary SHA",
    )

    text = replace_once(
        text,
        '    35: "완전 소 생물씨.",\n    36: "사명은 끝났다",\n    37: "승자의 손",\n    38: "인질은 제가 되죠",\n    39: "군함이 왔다",\n    40: "아버지의 자리",\n    91:',
        '    35: "완전 소 생물씨.",\n    # Ch036-040 exact body identity is already locked by the promotion contract SHA checks.\n    # Do not use chapter titles as body-substring invariants; titles are metadata, not prose.\n    91:',
        "title-as-body invariants",
    )

    old_boundary = '''chapter35_outline = outline_entries.get(35, {})
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
'''
    new_boundary = '''boundary = reconciliation.get("boundary_after_chapter")
if isinstance(boundary, int):
    boundary_left = outline_entries.get(boundary, {})
    boundary_right = outline_entries.get(boundary + 1, {})
    if boundary_left.get("next_chapter") is not None:
        errors.append(f"chapter {boundary} reverse outline must stop at the current migration boundary")
    if "RECONCILIATION_MIGRATION_BOUNDARY" not in boundary_left.get("structural_flags", []):
        errors.append(f"chapter {boundary} reverse outline missing migration-boundary flag")
    expected_pressure = f"제{boundary + 1}화 이후는 아직 legacy tail"
    if expected_pressure not in boundary_left.get("evidence", {}).get("next_pressure", ""):
        errors.append(f"chapter {boundary} reverse outline missing boundary pressure")
    if boundary_right.get("previous_chapter") is not None:
        errors.append(
            f"legacy chapter {boundary + 1} must not claim current chapter {boundary} as previous continuity"
        )
    if "LEGACY_TAIL_BOUNDARY" not in boundary_right.get("structural_flags", []):
        errors.append(f"chapter {boundary + 1} reverse outline missing legacy-tail boundary flag")
else:
    errors.append("current migration boundary must be an integer")
'''
    text = replace_once(text, old_boundary, new_boundary, "dynamic migration boundary")

    text = replace_once(
        text,
        'if registry.get("next_bundle_passes") != ["fiction/manuscript/part-1/036-040.md"]:\n    errors.append("next bundle pass order mismatch")\n',
        'next_bundles = registry.get("next_bundle_passes")\nif not isinstance(next_bundles, list) or len(next_bundles) != 1 or not isinstance(boundary, int):\n    errors.append("next bundle pass order mismatch")\nelse:\n    match = re.search(r"/(\\d{3})-(\\d{3})\\.md$", str(next_bundles[0]))\n    if (\n        not match\n        or int(match.group(1)) != boundary + 1\n        or int(match.group(2)) != boundary + 5\n    ):\n        errors.append("next bundle pass order mismatch")\n',
        "dynamic next bundle",
    )

    text = replace_once(
        text,
        'print(\n    "Fiction scene-pass validation PASSED "\n    "(001-035 pending promotion prefix; migration boundary 35→36; "\n    "036-040 next; 091-095 source-matched)"\n)\n',
        'next_label = registry.get("next_bundle_passes", ["UNKNOWN"])[0]\nprint(\n    "Fiction scene-pass validation PASSED "\n    f"(001-{current_frontier:03d} candidate prefix; migration boundary "\n    f"{current_frontier}→{current_frontier + 1}; next={next_label}; 091-095 source-matched)"\n)\n',
        "dynamic success summary",
    )

    TARGET.write_text(text, encoding="utf-8")
    print("frontier-aware scene-pass validation installed")


if __name__ == "__main__":
    main()
