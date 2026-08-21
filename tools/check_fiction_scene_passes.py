#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from fiction_composed_data import load_manuscript_index, load_reverse_outline

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)
errors: list[str] = []

index = load_manuscript_index(FICTION)
index_entries = {int(item["chapter"]): item for item in index["chapters"]}
outline = load_reverse_outline(FICTION)
outline_entries = {int(item["chapter"]): item for item in outline["chapters"]}
registry = json.loads((FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))

parsed: dict[int, str] = {}
for path in sorted((FICTION / "manuscript").rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    for match in CHAPTER_RE.finditer(text):
        parsed[int(match.group(1))] = match.group(4).strip()

expected_passes = {
    "fiction/manuscript/part-1/001-005.md": {
        "chapters": [1, 2, 3, 4, 5],
        "boundaries": [6],
        "card_boundaries": ["제1→2화", "제2→3화", "제3→4화", "제4→5화", "제5→6화"],
    },
    "fiction/manuscript/part-1/006-010.md": {
        "chapters": [6, 7, 8, 9, 10],
        "boundaries": [5, 11],
        "card_boundaries": ["제5→6화", "제6→7화", "제7→8화", "제8→9화", "제9→10화", "제10→11화"],
    },
    "fiction/manuscript/part-1/011-015.md": {
        "chapters": [11, 12, 13, 14, 15],
        "boundaries": [10, 16],
        "card_boundaries": ["제10→11화", "제11→12화", "제12→13화", "제13→14화", "제14→15화", "제15→16화"],
    },
    "fiction/manuscript/part-1/016-020.md": {
        "chapters": [16, 17, 18, 19, 20],
        "boundaries": [15, 21],
        "card_boundaries": ["제15→16화", "제16→17화", "제17→18화", "제18→19화", "제19→20화", "제20→21화"],
    },
    "fiction/manuscript/part-1/021-025.md": {
        "chapters": [21, 22, 23, 24, 25],
        "boundaries": [20, 26],
        "card_boundaries": ["제20→21화", "제21→22화", "제22→23화", "제23→24화", "제24→25화", "제25→26화"],
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
    1: "위대한 심연의 군주.",
    2: "제가 골랐거든요.",
    3: "머나먼 카르코사에서 온 나의 동지들에게.",
    4: "내가 시켜서 말고.",
    5: "신호기 잃어버리지 마세요",
    6: "울릴 때까지 살아남는 것.",
    7: "서로 편이면 충분할 것 같습니다.",
    8: "잡히면 설명해줄게!",
    9: "친구가 진짜라는 사실과.",
    10: "직접 물어봐. 왜 그랬는지.",
    11: "그건 또 별개고.",
    12: "같은 얼굴을 가진, 전혀 다른 사람.",
    13: "누구도 부모의 죄를 딸의 선택으로 바꿔 쓸 수는 없다.",
    14: "이번 방향은 처음으로 자신이 정했다.",
    15: "안 믿으면 계약이죠.",
    16: "살아서 해.",
    17: "자기 몸을 다시 자기 것으로 만드는 일이 먼저였다.",
    18: "읽을지는 당신이 정해.",
    19: "하템. 밀리와 별개 인물. 같은 얼굴은 동일인의 증거가 아니다.",
    20: "마음에 드는 규칙만 적으면 규칙이 아니라 희망사항이니까요.",
    21: "뛰어들지 않는 선택을 계속하는 일이었다.",
    22: "다음에는 숨 냄새부터 지워라.",
    23: "과거의 원인이 무엇인지도 모른다. 그래도 선택한 순간의 감각은 기억할 수 있었다.",
    24: "그 다음 한 박자를 제가 만들겠습니다.",
    25: "갈 겁니까?",
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

for bundle_name in ("006-010.md", "011-015.md", "016-020.md", "021-025.md"):
    current_bundle = (FICTION / "manuscript" / "part-1" / bundle_name).read_text(encoding="utf-8")
    for excluded in ("복종인자", "히템", "앨리스", "쵸르브라트", "미하일 카쉬프", "피엘렛토", "붉은 늑대", "컨소시엄"):
        if excluded in current_bundle:
            errors.append(f"excluded/superseded term restored in current {bundle_name[:-3]}: {excluded}")

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

reconciliation = registry.get("external_artifact_reconciliation", {})
if reconciliation.get("artifact") != "폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx":
    errors.append("external reconciliation artifact mismatch")
if reconciliation.get("artifact_sha256") != "248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9":
    errors.append("external reconciliation artifact SHA mismatch")
if reconciliation.get("target_chapters") != [1, 161]:
    errors.append("external reconciliation target range mismatch")
if reconciliation.get("reconciled_prefix_end") != 25:
    errors.append("reconciled prefix must be chapter 25 after current 021-025 propagation")
if reconciliation.get("legacy_tail_starts_at") != 26:
    errors.append("legacy tail must begin at chapter 26 after current 021-025 propagation")
if reconciliation.get("boundary_after_chapter") != 25:
    errors.append("migration boundary must be after chapter 25")
if reconciliation.get("whole_manuscript_continuity") != "NOT_YET_CLAIMED":
    errors.append("whole-manuscript continuity must remain unclaimed during mixed migration")

chapter10_outline = outline_entries.get(10, {})
chapter10_next = chapter10_outline.get("next_chapter")
if not isinstance(chapter10_next, dict) or chapter10_next.get("chapter") != 11:
    errors.append("current chapter 10 reverse outline must connect to current chapter 11")
if "RECONCILIATION_MIGRATION_BOUNDARY" in chapter10_outline.get("structural_flags", []):
    errors.append("chapter 10 must no longer carry the migration-boundary flag")

chapter15_outline = outline_entries.get(15, {})
chapter15_next = chapter15_outline.get("next_chapter")
if not isinstance(chapter15_next, dict) or chapter15_next.get("chapter") != 16:
    errors.append("current chapter 15 reverse outline must connect to current chapter 16")
if "RECONCILIATION_MIGRATION_BOUNDARY" in chapter15_outline.get("structural_flags", []):
    errors.append("chapter 15 must no longer carry the migration-boundary flag")

chapter16_outline = outline_entries.get(16, {})
chapter16_previous = chapter16_outline.get("previous_chapter")
if not isinstance(chapter16_previous, dict) or chapter16_previous.get("chapter") != 15:
    errors.append("current chapter 16 reverse outline must connect back to chapter 15")
if "LEGACY_TAIL_BOUNDARY" in chapter16_outline.get("structural_flags", []):
    errors.append("current chapter 16 must no longer carry the legacy-tail boundary flag")

chapter20_outline = outline_entries.get(20, {})
chapter20_next = chapter20_outline.get("next_chapter")
if not isinstance(chapter20_next, dict) or chapter20_next.get("chapter") != 21:
    errors.append("current chapter 20 reverse outline must connect to current chapter 21")
if "RECONCILIATION_MIGRATION_BOUNDARY" in chapter20_outline.get("structural_flags", []):
    errors.append("chapter 20 must no longer carry the migration-boundary flag")

chapter21_outline = outline_entries.get(21, {})
chapter21_previous = chapter21_outline.get("previous_chapter")
if not isinstance(chapter21_previous, dict) or chapter21_previous.get("chapter") != 20:
    errors.append("current chapter 21 reverse outline must connect back to chapter 20")
if "LEGACY_TAIL_BOUNDARY" in chapter21_outline.get("structural_flags", []):
    errors.append("current chapter 21 must no longer carry the legacy-tail boundary flag")

chapter25_outline = outline_entries.get(25, {})
if chapter25_outline.get("next_chapter") is not None:
    errors.append("chapter 25 reverse outline must stop at the current migration boundary")
if "RECONCILIATION_MIGRATION_BOUNDARY" not in chapter25_outline.get("structural_flags", []):
    errors.append("chapter 25 reverse outline missing migration-boundary flag")
if "제26화 이후는 아직 legacy tail" not in chapter25_outline.get("evidence", {}).get("next_pressure", ""):
    errors.append("chapter 25 reverse outline missing boundary pressure")

chapter26_outline = outline_entries.get(26, {})
if chapter26_outline.get("previous_chapter") is not None:
    errors.append("legacy chapter 26 reverse outline must not claim current chapter 25 as previous continuity")
if "LEGACY_TAIL_BOUNDARY" not in chapter26_outline.get("structural_flags", []):
    errors.append("chapter 26 reverse outline missing legacy-tail boundary flag")

if registry.get("next_pass_mode") != "EXTERNAL_ARTIFACT_CANON_RECONCILIATION":
    errors.append("next pass mode must be external artifact canon reconciliation")
if registry.get("next_bundle_passes") != ["fiction/manuscript/part-1/026-030.md"]:
    errors.append("next bundle pass order mismatch")
if registry.get("deferred_bundle_passes") != ["fiction/manuscript/part-2/176-180.md"]:
    errors.append("deferred source-pass order mismatch")

if errors:
    print("Fiction scene-pass validation FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(
    "Fiction scene-pass validation PASSED "
    "(001-025 current production prefix; migration boundary 25→26; "
    "026-030 next; 091-095 source-matched)"
)
