#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
ANALYSIS = FICTION / "analysis"
OUTLINE = ANALYSIS / "REVERSE_OUTLINE_001_225.json"
REPORT = ANALYSIS / "REVERSE_OUTLINE_REPORT.md"
GATES = ANALYSIS / "REPRESENTATIVE_CHAPTER_GATES.md"
errors: list[str] = []

for path in (OUTLINE, REPORT, GATES):
    if not path.is_file():
        errors.append(f"missing {path.relative_to(ROOT)}")

try:
    index = json.loads((FICTION / "MANUSCRIPT_INDEX.json").read_text(encoding="utf-8"))
    index_entries = {int(item["chapter"]): item for item in index.get("chapters", [])}
except Exception as exc:
    index_entries = {}
    errors.append(f"invalid MANUSCRIPT_INDEX.json: {exc}")

try:
    outline = json.loads(OUTLINE.read_text(encoding="utf-8"))
    chapters = outline.get("chapters", [])
except Exception as exc:
    outline = {}
    chapters = []
    errors.append(f"invalid reverse outline JSON: {exc}")

if outline.get("status") != "ACTIVE_ANALYSIS / EXTRACTIVE_BASELINE / MANUAL_REVIEW_REQUIRED":
    errors.append("reverse outline status must preserve manual-review requirement")
if "No manuscript body" not in outline.get("protected_content", ""):
    errors.append("reverse outline must state that manuscript bodies are protected")

numbers = [item.get("chapter") for item in chapters]
if numbers != list(range(1, 226)):
    errors.append("reverse outline must contain chapters 1-225 in order exactly once")

gates = outline.get("representative_gate_chapters", [])
if len(gates) != 12 or len(set(gates)) != 12:
    errors.append("representative gate list must contain exactly 12 unique chapters")
if sorted(item.get("chapter") for item in chapters if item.get("representative_gate")) != sorted(gates):
    errors.append("chapter gate markers differ from representative_gate_chapters")

required_evidence = (
    "starting_state",
    "immediate_goal_or_focus",
    "opposition_and_cost",
    "turn_or_discovery",
    "decision_or_choice",
    "ending_state",
    "next_pressure",
)
for item in chapters:
    number = item.get("chapter")
    entry = index_entries.get(number)
    if not entry:
        errors.append(f"chapter {number}: missing index entry")
        continue
    source = item.get("source", {})
    for key in ("title", "pov"):
        if item.get(key) != entry.get(key):
            errors.append(f"chapter {number}: {key} mismatch with manuscript index")
    for key in ("bundle", "body_sha256", "body_chars"):
        if source.get(key) != entry.get(key):
            errors.append(f"chapter {number}: source {key} mismatch with manuscript index")
    evidence = item.get("evidence", {})
    for key in required_evidence:
        value = evidence.get(key)
        if not isinstance(value, str) or len(value.strip()) < 8:
            errors.append(f"chapter {number}: empty/short evidence field {key}")
    if item.get("review_status") != "AUTO_BASELINE_REVIEW_REQUIRED":
        errors.append(f"chapter {number}: false or missing review status")
    if not item.get("chapter_function") or not item.get("state_change_axes"):
        errors.append(f"chapter {number}: missing function or state-change axes")

report_text = REPORT.read_text(encoding="utf-8") if REPORT.is_file() else ""
gate_text = GATES.read_text(encoding="utf-8") if GATES.is_file() else ""
for number in gates:
    if f"제{number}화" not in gate_text:
        errors.append(f"representative gate report missing chapter {number}")
for heading in (
    "## 4. 부·외전별 정량 기준선",
    "## 5. 전체 구조 지도",
    "## 6. Finding-first 판정",
    "## 8. 다음 정확한 작업",
):
    if heading not in report_text:
        errors.append(f"reverse outline report missing heading: {heading}")

for stale in (
    "archive/",
    "SUPERSEDED",
    "총 140화",
    "현재 사건 배치 원고",
    "5화 단위 확장 뒤",
    "확장 미착수",
    "제1화~제5화 확장부터",
    "1Q753033aiMhYBMOE8NodXaRKcpH9S2NdBMg31CKC2HI",
    "1NktYrRuhcoGXRuaHdCz-p4FeQQjbT5iWZWrN3Zg1-i4",
    "14sPx4rmIaUXlRJvCIj_FKp9osm5fOElZwUzIpGBx198",
    "쵸르브라트",
    "미하일 카쉬프",
    "피엘렛토",
    "붉은 늑대",
):
    for path in (OUTLINE, REPORT, GATES):
        if path.is_file() and stale in path.read_text(encoding="utf-8"):
            errors.append(f"stale reference in {path.relative_to(ROOT)}: {stale}")

if re.search(r"(?:전체|최종).{0,12}(?:퇴고|검수|교정).{0,8}(?:완료|통과)", report_text + gate_text):
    errors.append("analysis documents may not claim full/final revision completion")

if errors:
    print("Fiction reverse-outline validation FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

print(
    "Fiction reverse-outline validation PASSED "
    f"({len(chapters)} chapters, {len(gates)} representative gates)"
)
