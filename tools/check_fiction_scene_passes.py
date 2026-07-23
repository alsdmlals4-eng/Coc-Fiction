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

expected_passes = {
    "fiction/manuscript/part-1/006-010.md": {
        "chapters": [6, 7, 8, 9, 10],
        "boundaries": [5, 11],
        "card_boundaries": ["제5→6화", "제6→7화", "제7→8화", "제8→9화", "제9→10화", "제10→11화"],
    },
    "fiction/manuscript/side-story-lake/091-095.md": {
        "chapters": [91, 92, 93, 94, 95],
        "boundaries": [90, 96],
        "card_boundaries": ["제90→91화", "제91→92화", "제92→93화", "제93→94화", "제94→95화", "제95→96화"],
    },
}
passes = registry.get("completed_bundle_passes", [])
by_bundle = {item.get("bundle"): item for item in passes}
if set(by_bundle) != set(expected_passes):
    errors.append(f"completed bundle set mismatch: {sorted(by_bundle)}")

for bundle, expected in expected_passes.items():
    item = by_bundle.get(bundle)
    if not item:
        continue
    if item.get("chapters") != expected["chapters"]:
        errors.append(f"{bundle} chapter list mismatch")
    if item.get("boundary_chapters") != expected["boundaries"]:
        errors.append(f"{bundle} boundary list mismatch")
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
    for raw_number, expected_sha in item.get("preserved_boundary_shas", {}).items():
        number = int(raw_number)
        body = parsed.get(number, "")
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if actual != expected_sha:
            errors.append(f"boundary chapter {number} SHA changed")
    card_path = ROOT / item.get("scene_cards", "")
    if card_path.is_file():
        cards = card_path.read_text(encoding="utf-8")
        for number in expected["chapters"]:
            if f"## 제{number}화" not in cards:
                errors.append(f"scene card missing chapter {number}")
        for boundary in expected["card_boundaries"]:
            if boundary not in cards:
                errors.append(f"scene card missing boundary {boundary}")

required_phrases = {
    6: "복도에서 첫 총성이 울리기 전",
    7: "자기 안의 차가운 보호 반응",
    9: "조금 전 서비스 통로에서 데커와 총을 주고받는 동안",
    91: "답을 찾았느냐",
    92: "세 사람이 함께 살기로 고른 집",
    93: "2018년 2월",
    94: "티베트 쪽이었습니다",
    95: "고기 먹으러",
}
for number, phrase in required_phrases.items():
    if phrase not in parsed.get(number, ""):
        errors.append(f"chapter {number} missing invariant: {phrase}")

forbidden_phrases = {
    7: ["다른 자신이 문을 세게 두드렸다"],
    9: ["지원선에서 갈고리를 타고 넘어오는 동안"],
    91: ["호수 아래에서 회수한 기록은 서로 모순됐다"],
    92: ["호출기가 울린 저녁"],
    93: ["아킴의 정기 방문 대상은 평범해 보였다"],
    94: ["작은 녹음기를 켰다"],
    95: ["서울 외곽의 작은 호수"],
}
for number, phrases in forbidden_phrases.items():
    for phrase in phrases:
        if phrase in parsed.get(number, ""):
            errors.append(f"chapter {number} stale scene remains: {phrase}")

lake_bundle = (FICTION / "manuscript" / "side-story-lake" / "091-095.md").read_text(encoding="utf-8")
for excluded in ("오션", "아프리카", "버실라", "Woff", "피엘렛토", "쵸르브라트"):
    if excluded in lake_bundle:
        errors.append(f"excluded adaptation term restored in 091-095: {excluded}")
for source_marker in (
    "COC 외전 - 호수가 보이는 마을(2).pdf pp.113-120",
    "COC 외전 - 호수가 보이는 마을(2).pdf pp.145-147",
):
    if source_marker not in lake_bundle:
        errors.append(f"missing primary source marker: {source_marker}")

if registry.get("next_bundle_passes") != ["fiction/manuscript/part-2/176-180.md"]:
    errors.append("next bundle pass order mismatch")

if errors:
    print("Fiction scene-pass validation FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("Fiction scene-pass validation PASSED (006-010 internal, 091-095 source-matched)")
