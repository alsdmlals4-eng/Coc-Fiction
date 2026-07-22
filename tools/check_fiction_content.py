#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import sys

from fiction_composed_data import load_manuscript_index

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
errors: list[str] = []

REQUIRED = [
    "FICTION_MASTER.md",
    "ACTIVE_CONTEXT.md",
    "HANDOFF.md",
    "CANON_REGISTRY.json",
    "MANUSCRIPT_INDEX.json",
    "STYLE_GUIDE.md",
    "SOURCE_MANIFEST.md",
    "archive/SUPERSEDED_GOOGLE_DOCS.md",
    "archive/SUPERSEDED_140_EPISODE_PLAN.md",
    "bible/01_PROJECT_CORE.md",
    "bible/02_CANON_AND_CONTINUITY.md",
    "bible/03_PART1_STORY_BIBLE.md",
    "bible/04_PART2_STORY_BIBLE.md",
]
for rel in REQUIRED:
    if not (FICTION / rel).is_file():
        errors.append(f"missing {rel}")

try:
    registry = json.loads((FICTION / "CANON_REGISTRY.json").read_text(encoding="utf-8"))
    if registry.get("core_status") != "CORE_CONFIRMED":
        errors.append("canon registry core status is not CORE_CONFIRMED")
    forbidden_terms = list(registry.get("validation", {}).get("forbidden_in_active_manuscript", []))
    if not forbidden_terms:
        errors.append("canon registry forbidden term list is empty")
except Exception as exc:
    registry = {}
    forbidden_terms = []
    errors.append(f"invalid canon registry: {exc}")

try:
    index = load_manuscript_index(FICTION)
    index_entries = {int(item["chapter"]): item for item in index.get("chapters", [])}
except Exception as exc:
    index_entries = {}
    errors.append(f"invalid manuscript index: {exc}")

bundles = sorted((FICTION / "manuscript").rglob("*.md"))
if len(bundles) != 45:
    errors.append(f"expected 45 manuscript bundles, got {len(bundles)}")

chapter_pattern = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)
seen: dict[int, tuple[str, str, str, Path]] = {}
for path in bundles:
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^> 상태: 2,000자 이상 확장 원고 DRAFT\.", text, re.M):
        errors.append(f"missing expanded DRAFT status: {path.relative_to(ROOT)}")
    if re.search(r"^> 상태:.*(?:전체 퇴고 완료|최종 원고|교정 완료)", text, re.M):
        errors.append(f"false completion label: {path.relative_to(ROOT)}")
    for match in chapter_pattern.finditer(text):
        number = int(match.group(1))
        if number in seen:
            errors.append(f"duplicate chapter {number}")
            continue
        seen[number] = (match.group(2).strip(), match.group(3).strip(), match.group(4).strip(), path)

if sorted(seen) != list(range(1, 226)):
    errors.append("chapter numbers are missing or duplicated")
if sorted(index_entries) != list(range(1, 226)):
    errors.append("manuscript index must contain chapters 1-225 exactly once")

for number, (title, pov, body, path) in seen.items():
    if len(body) < 2000:
        errors.append(f"chapter {number} below 2,000 chars: {len(body)}")
    entry = index_entries.get(number)
    if not entry:
        continue
    expected_path = path.relative_to(ROOT).as_posix()
    if entry.get("bundle") != expected_path:
        errors.append(f"chapter {number} bundle mismatch")
    if entry.get("title") != title or entry.get("pov") != pov:
        errors.append(f"chapter {number} title/POV index mismatch")
    if entry.get("body_chars") != len(body):
        errors.append(f"chapter {number} length index mismatch")
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    if entry.get("body_sha256") != digest:
        errors.append(f"chapter {number} body SHA mismatch")

for path in bundles:
    text = path.read_text(encoding="utf-8")
    for term in forbidden_terms:
        if term in text:
            errors.append(f"superseded term {term} in active manuscript {path.relative_to(ROOT)}")

superseded_allowlist = {
    FICTION / "CANON_REGISTRY.json",
    FICTION / "FICTION_MASTER.md",
}
active_roots = (
    FICTION,
    ROOT / "[소설]" / "00_운영체계",
    ROOT / "docs" / "coordination",
)
active_files: set[Path] = set()
for active_root in active_roots:
    if not active_root.exists():
        continue
    for path in active_root.rglob("*"):
        if path.is_file() and "archive" not in path.parts and path.suffix in {".md", ".json"}:
            active_files.add(path)
for path in sorted(active_files):
    if path in superseded_allowlist:
        continue
    text = path.read_text(encoding="utf-8")
    for term in forbidden_terms:
        if term in text:
            errors.append(f"superseded term {term} in active file {path.relative_to(ROOT)}")

archive_google = FICTION / "archive/SUPERSEDED_GOOGLE_DOCS.md"
archive_text = archive_google.read_text(encoding="utf-8") if archive_google.is_file() else ""
old_ids = re.findall(r"`([A-Za-z0-9_-]{20,})`", archive_text)
if len(old_ids) < 3:
    errors.append("superseded Google Doc IDs missing from archive inventory")
for path in sorted(active_files):
    text = path.read_text(encoding="utf-8")
    for old_id in old_ids:
        if old_id in text:
            errors.append(f"old Google Doc id in active file {path.relative_to(ROOT)}")

source_manifest = (FICTION / "SOURCE_MANIFEST.md").read_text(encoding="utf-8")
for active_id in (
    "1b7LL-q6p4UTV6DCYDj3CcLgemw3gyLcU_3WSaaSV6zE",
    "1gP0yTgT0eLgMcb-21FW1qwgWQVSKxfjiAvIVLyqlJ2E",
):
    if active_id not in source_manifest:
        errors.append(f"active Google Doc id missing from SOURCE_MANIFEST: {active_id}")

legacy_patterns = ("총 140화", "2부: 제91화~제140화", "제138화~제140화")
for path in sorted(active_files):
    text = path.read_text(encoding="utf-8")
    for pattern in legacy_patterns:
        if pattern in text:
            errors.append(f"active legacy 140-plan content in {path.relative_to(ROOT)}: {pattern}")

stale_stage_phrases = (
    "현재 사건 배치 원고",
    "5화 단위 확장 뒤",
    "확장 미착수",
    "제1화~제5화 확장부터",
)
for path in sorted(active_files):
    text = path.read_text(encoding="utf-8")
    for phrase in stale_stage_phrases:
        if phrase in text:
            errors.append(f"stale workflow phrase in {path.relative_to(ROOT)}: {phrase}")

if errors:
    print("Fiction content validation FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

lengths = [len(item[2]) for item in seen.values()]
print(
    "Fiction content validation PASSED "
    f"({len(bundles)} bundles, 225 chapters, min={min(lengths)}, max={max(lengths)})"
)
