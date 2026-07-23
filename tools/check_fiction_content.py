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
    "FICTION_MASTER.md", "ACTIVE_CONTEXT.md", "HANDOFF.md", "CANON_REGISTRY.json",
    "MANUSCRIPT_INDEX.json", "STYLE_GUIDE.md", "SOURCE_MANIFEST.md",
    "sources/PRIMARY_SOURCE_INVENTORY.md", "analysis/SCENE_PASS_REGISTRY.json",
    "archive/SUPERSEDED_GOOGLE_DOCS.md", "archive/SUPERSEDED_140_EPISODE_PLAN.md",
    "bible/01_PROJECT_CORE.md", "bible/02_CANON_AND_CONTINUITY.md",
    "bible/03_PART1_STORY_BIBLE.md", "bible/04_PART2_STORY_BIBLE.md",
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

active_roots = (FICTION, ROOT / "[소설]" / "00_운영체계", ROOT / "docs" / "coordination")
active_files: set[Path] = set()
for active_root in active_roots:
    if active_root.exists():
        for path in active_root.rglob("*"):
            if path.is_file() and "archive" not in path.parts and path.suffix in {".md", ".json"}:
                active_files.add(path)

# Canon/evidence documents may name rejected terms only to record the exclusion.
superseded_evidence_allowlist = {
    FICTION / "CANON_REGISTRY.json", FICTION / "FICTION_MASTER.md", FICTION / "HANDOFF.md",
    FICTION / "SOURCE_MANIFEST.md", FICTION / "sources/PRIMARY_SOURCE_INVENTORY.md",
    FICTION / "analysis/SCENE_CARDS_091_095.md",
    FICTION / "reports/REVISION_2026-07-23_SOURCE_PASS_091_095.md",
}
for path in sorted(active_files):
    if path in superseded_evidence_allowlist:
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

legacy_patterns = (
    "총 140화", "2부: 제91화~제140화", "제138화~제140화",
    "225화 압축 초안", "Coc 폭풍의 눈(주안편) — 통합 문서",
)
legacy_allowlist = {FICTION / "FICTION_MASTER.md", FICTION / "SOURCE_MANIFEST.md"}
for path in sorted(active_files):
    if path in legacy_allowlist:
        continue
    text = path.read_text(encoding="utf-8")
    for pattern in legacy_patterns:
        if pattern in text:
            errors.append(f"active legacy reference in {path.relative_to(ROOT)}: {pattern}")

stale_stage_phrases = (
    "현재 사건 배치 원고", "5화 단위 확장 뒤", "확장 미착수", "제1화~제5화 확장부터",
    "원본 Drive 폴더는 현재 연결 계정에서", "실제 본체는 확인되지 않았다",
    "원본 본체에 접근하기 전까지", "다음 단계는 `091-095`",
)
for path in sorted(active_files):
    text = path.read_text(encoding="utf-8")
    for phrase in stale_stage_phrases:
        if phrase in text:
            errors.append(f"stale workflow/source phrase in {path.relative_to(ROOT)}: {phrase}")

# Active documents must not direct workers to archive paths.
archive_policy_allowlist = {FICTION / "CANON_REGISTRY.json"}
for path in sorted(active_files):
    if path in archive_policy_allowlist:
        continue
    text = path.read_text(encoding="utf-8")
    if "`archive/" in text or "](archive/" in text:
        errors.append(f"active file directly references archive input: {path.relative_to(ROOT)}")

source_inventory = (FICTION / "sources/PRIMARY_SOURCE_INVENTORY.md").read_text(encoding="utf-8")
for required_source in (
    "COC 외전 - 호수가 보이는 마을(2).pdf",
    "c0576e6f5e293077a0a37646e56671415ba7a04b5e6a5da87f6ebdae8a78b36a",
    "COC 중편 - 네가 없는 마을 7일차 완결.pdf",
):
    if required_source not in source_inventory:
        errors.append(f"primary source inventory missing: {required_source}")

if errors:
    print("Fiction content validation FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)

lengths = [len(item[2]) for item in seen.values()]
print(f"Fiction content validation PASSED ({len(bundles)} bundles, 225 chapters, min={min(lengths)}, max={max(lengths)})")
