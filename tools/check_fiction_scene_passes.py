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
    "fiction/manuscript/part-1/026-030.md": {
        "chapters": [26, 27, 28, 29, 30],
        "boundaries": [25, 31],
        "card_boundaries": ["제25→26화", "제26→27화", "제27→28화", "제28→29화", "제29→30화", "제30→31화"],
    },
    "fiction/manuscript/part-1/031-035.md": {
        "chapters": [31, 32, 33, 34, 35],
        "boundaries": [30, 36],
        "card_boundaries": ["제30→31화", "제31→32화", "제32→33화", "제33→34화", "제34→35화", "제35→36화"],
    },
    "fiction/manuscript/part-1/036-040.md": {
        "chapters": [36, 37, 38, 39, 40],
        "boundaries": [35, 41],
        "card_boundaries": ["제35→36화", "제36→37화", "제37→38화", "제38→39화", "제39→40화", "제40→41화"],
    },
    "fiction/manuscript/part-1/041-045.md": {
        "chapters": [41, 42, 43, 44, 45],
        "boundaries": [40, 46],
        "card_boundaries": ["제40→41화", "제41→42화", "제42→43화", "제43→44화", "제44→45화", "제45→46화"],
    },
    "fiction/manuscript/side-story-lake/091-095.md": {
        "chapters": [91, 92, 93, 94, 95],
        "boundaries": [90, 96],
        "card_boundaries": ["제90→91화", "제91→92화", "제92→93화", "제93→94화", "제94→95화", "제95→96화"],
    },
}

passes = registry.get("completed_bundle_passes", [])
by_bundle = {item.get("bundle"): item for item in passes}
current_frontier = registry.get("external_artifact_reconciliation", {}).get("reconciled_prefix_end", 0)
if not isinstance(current_frontier, int):
    current_frontier = 0
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
        chapter_numbers = [int(x) for x in item.get("chapters", [])]
        # A right boundary can later become production in a subsequent bounded pass.
        # Once that happens its old legacy SHA is historical evidence, not an active immutability gate.
        if chapter_numbers and number > max(chapter_numbers) and number <= current_frontier:
            continue
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
    26: "괴물이 자기 책임을 다시 고르게 만들어서 열렸다.",
    27: "하템은 죽었다.",
    28: "환각.",
    30: "폭풍을 걷는 자.",
    31: "내가 네 주인은 아니야.",
    32: "그 질문이 틀렸을 가능성이 큽니다.",
    33: "지금보다 괴물이 되어야 합니다.",
    34: "핵은 보이지 않았다.",
    35: "완전 소 생물씨.",
    # Ch036-040 exact body identity is already locked by the promotion contract SHA checks.
    # Do not use chapter titles as body-substring invariants; titles are metadata, not prose.
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

for bundle_name in ("006-010.md", "011-015.md", "016-020.md", "021-025.md", "026-030.md", "031-035.md", "036-040.md"):
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
if reconciliation.get("artifact") != "폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx":
    errors.append("external reconciliation artifact mismatch")
if reconciliation.get("artifact_sha256") != "89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10":
    errors.append("external reconciliation artifact SHA mismatch")
if reconciliation.get("source_manifest") != "docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json":
    errors.append("user source manifest mismatch")
if reconciliation.get("source_authority") != "USER_DESIGNATED_SOURCE_CHUNK_SET":
    errors.append("source authority mode mismatch")
if reconciliation.get("target_chapters") != [1, 161]:
    errors.append("external reconciliation target range mismatch")
if reconciliation.get("reconciled_prefix_end") != 45:
    errors.append("reconciled prefix must be chapter 45 after current 036-040 propagation")
if reconciliation.get("legacy_tail_starts_at") != 46:
    errors.append("legacy tail must begin at chapter 46 after current 036-040 propagation")
if reconciliation.get("boundary_after_chapter") != 45:
    errors.append("migration boundary must be after chapter 45")
if reconciliation.get("whole_manuscript_continuity") != "NOT_YET_CLAIMED":
    errors.append("whole-manuscript continuity must remain unclaimed during mixed migration")

for left_number, right_number in ((10, 11), (15, 16), (20, 21), (25, 26), (30, 31), (35, 36), (40, 41)):
    left = outline_entries.get(left_number, {})
    right = outline_entries.get(right_number, {})
    left_next = left.get("next_chapter")
    right_previous = right.get("previous_chapter")
    if not isinstance(left_next, dict) or left_next.get("chapter") != right_number:
        errors.append(f"current chapter {left_number} must connect to chapter {right_number}")
    if not isinstance(right_previous, dict) or right_previous.get("chapter") != left_number:
        errors.append(f"current chapter {right_number} must connect back to chapter {left_number}")
    if "RECONCILIATION_MIGRATION_BOUNDARY" in left.get("structural_flags", []):
        errors.append(f"chapter {left_number} must not carry migration-boundary flag")
    if "LEGACY_TAIL_BOUNDARY" in right.get("structural_flags", []):
        errors.append(f"chapter {right_number} must not carry legacy-tail boundary flag")

boundary = reconciliation.get("boundary_after_chapter")
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

if registry.get("next_pass_mode") != "USER_SOURCE_CHUNK_CANON_RECONCILIATION":
    errors.append("next pass mode must be user source chunk canon reconciliation")
next_bundles = registry.get("next_bundle_passes")
if not isinstance(next_bundles, list) or len(next_bundles) != 1 or not isinstance(boundary, int):
    errors.append("next bundle pass order mismatch")
else:
    match = re.search(r"/(\d{3})-(\d{3})\.md$", str(next_bundles[0]))
    if (
        not match
        or int(match.group(1)) != boundary + 1
        or int(match.group(2)) != boundary + 5
    ):
        errors.append("next bundle pass order mismatch")
if registry.get("deferred_bundle_passes") != ["fiction/manuscript/part-2/176-180.md"]:
    errors.append("deferred source-pass order mismatch")

if errors:
    print("Fiction scene-pass validation FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

next_label = registry.get("next_bundle_passes", ["UNKNOWN"])[0]
print(
    "Fiction scene-pass validation PASSED "
    f"(001-{current_frontier:03d} candidate prefix; migration boundary "
    f"{current_frontier}→{current_frontier + 1}; next={next_label}; 091-095 source-matched)"
)
