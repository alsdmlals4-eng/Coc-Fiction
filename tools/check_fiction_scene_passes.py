#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from fiction_composed_data import load_manuscript_index

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)
errors: list[str] = []

index = load_manuscript_index(FICTION)
index_entries = {int(item["chapter"]): item for item in index["chapters"]}
registry = json.loads((FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))

parsed: dict[int, str] = {}
for path in sorted((FICTION / "manuscript").rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    for match in CHAPTER_RE.finditer(text):
        parsed[int(match.group(1))] = match.group(4).strip()

passes = registry.get("completed_bundle_passes", [])
if len(passes) != 1:
    errors.append(f"expected one completed bundle pass, got {len(passes)}")
else:
    item = passes[0]
    if item.get("bundle") != "fiction/manuscript/part-1/006-010.md":
        errors.append("unexpected completed bundle")
    if item.get("chapters") != [6, 7, 8, 9, 10]:
        errors.append("006-010 chapter list mismatch")
    if item.get("boundary_chapters") != [5, 11]:
        errors.append("006-010 boundary list mismatch")
    for key in ("scene_cards", "revision_report"):
        rel = item.get(key)
        if not rel or not (ROOT / rel).is_file():
            errors.append(f"missing scene pass artifact: {rel}")
    for raw_number, expected_sha in item.get("chapter_shas", {}).items():
        number = int(raw_number)
        body = parsed.get(number, "")
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if actual != expected_sha:
            errors.append(f"scene pass chapter {number} registry SHA mismatch")
        if index_entries.get(number, {}).get("body_sha256") != actual:
            errors.append(f"scene pass chapter {number} index SHA mismatch")

required = {
    6: "복도에서 첫 총성이 울리기 전",
    7: "자기 안의 차가운 보호 반응",
    9: "조금 전 서비스 통로에서 데커와 총을 주고받는 동안",
}
for number, phrase in required.items():
    if phrase not in parsed.get(number, ""):
        errors.append(f"chapter {number} missing scene-pass invariant: {phrase}")

forbidden = {
    7: "다른 자신이 문을 세게 두드렸다",
    9: "지원선에서 갈고리를 타고 넘어오는 동안",
}
for number, phrase in forbidden.items():
    if phrase in parsed.get(number, ""):
        errors.append(f"chapter {number} stale continuity text remains: {phrase}")

expected_next = [
    "fiction/manuscript/side-story-lake/091-095.md",
    "fiction/manuscript/part-2/176-180.md",
]
if registry.get("next_bundle_passes") != expected_next:
    errors.append("next bundle pass order mismatch")

cards = (FICTION / "analysis" / "SCENE_CARDS_006_010.md").read_text(encoding="utf-8")
for number in range(6, 11):
    if f"## 제{number}화" not in cards:
        errors.append(f"scene card missing chapter {number}")
for boundary in ("제5→6화", "제6→7화", "제7→8화", "제8→9화", "제9→10화", "제10→11화"):
    if boundary not in cards:
        errors.append(f"scene card missing boundary {boundary}")

if errors:
    print("Fiction scene-pass validation FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("Fiction scene-pass validation PASSED (bundle 006-010)")
