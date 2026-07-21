#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "[소설]/00_운영체계/SKILL_REGISTRY.json"

REQUIRED_FILES = [
    "docs/coordination/CONCURRENT_WORK.md",
    "[소설]/00_운영체계/START_HERE.md",
    "[소설]/00_운영체계/OPERATING_MODEL.md",
    "[소설]/00_운영체계/DOCUMENTATION_MAP.md",
    "[소설]/00_운영체계/SKILL_REGISTRY.json",
    "docs/fiction-ops/BASE_ADOPTION_AUDIT.md",
    "docs/fiction-ops/CRAFT_RESEARCH.md",
    "docs/fiction-ops/REFERENCE_CARD_TEMPLATE.md",
    "skills/fiction-project-operations/SKILL.md",
    "skills/fiction-story-development/SKILL.md",
    "skills/fiction-drafting/SKILL.md",
    "skills/fiction-canon-and-research/SKILL.md",
    "skills/fiction-revision-and-validation/SKILL.md",
    "skills/FICTION_SKILL_LEARNING_LOG.md",
    "templates/fiction-ops/ACTIVE_CONTEXT.template.md",
    "templates/fiction-ops/CANON_REGISTRY.template.json",
    "templates/fiction-ops/SCENE_CARD.template.md",
    "templates/fiction-ops/STYLE_GUIDE.template.md",
    "templates/fiction-ops/REVISION_REPORT.template.md",
]

EXPECTED_SKILLS = {
    "fiction-project-operations",
    "fiction-story-development",
    "fiction-drafting",
    "fiction-canon-and-research",
    "fiction-revision-and-validation",
}

EXPECTED_BASE_CAPABILITIES = {
    "managing-project-intake-and-work-contract",
    "managing-game-project-operating-system",
    "managing-design-documents",
    "evolving-project-discipline-skills",
    "pruning-stale-and-nonfunctional-material",
    "simplifying-skill-bodies",
    "refactoring-with-contract-preservation",
    "synchronizing-local-and-github-state",
    "maintaining-long-running-task-continuity",
    "governing-game-user-research-coverage",
    "creating-user-learning-notes",
    "building-project-visual-dashboards",
    "diagnosing-game-engine-runtime-failures",
    "maintaining-project-context-and-handoff",
    "analyzing-and-refining-game-concepts",
    "identifying-project-core",
    "establishing-project-core",
    "running-adversarial-review-and-refinement",
    "designing-vertical-slices",
    "orchestrating-deepseek-worktrees",
    "reviewing-and-validating-project-changes",
    "auditing-canonical-reference-freshness",
    "designing-art-prompts-and-technique-cards",
    "auditing-and-refining-ui-art",
    "managing-base-change-proposals",
}

REQUIRED_RESEARCH_URLS = [
    "https://owl.purdue.edu/",
    "https://www.advancedfictionwriting.com/articles/snowflake-method/",
    "https://www.advancedfictionwriting.com/articles/writing-the-perfect-scene/",
    "https://writing.wisc.edu/handbook/reverseoutlines/",
    "https://writingcenter.unc.edu/tips-and-tools/revising-drafts/",
    "https://writingcenter.unc.edu/tips-and-tools/editing-and-proofreading/",
    "https://korean.go.kr/kornorms/main/main.do",
]

ACTIVE_DOCS = [
    "[소설]/00_운영체계/START_HERE.md",
    "[소설]/00_운영체계/OPERATING_MODEL.md",
    "skills/fiction-project-operations/SKILL.md",
    "skills/fiction-story-development/SKILL.md",
    "skills/fiction-drafting/SKILL.md",
    "skills/fiction-canon-and-research/SKILL.md",
    "skills/fiction-revision-and-validation/SKILL.md",
]

GAME_ONLY_TERMS = [
    "Godot",
    "Unity",
    "frame time",
    "GPU",
    "터치 UI",
    "게임 엔진",
    "플레이어 행동",
    "Vertical Slice",
]


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: JSON root must be an object")
    return value


def front_matter_name(text: str) -> str | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    name = re.search(r"^name:\s*(.+?)\s*$", match.group(1), re.MULTILINE)
    return name.group(1) if name else None


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    try:
        registry = load_json(REGISTRY)
    except Exception as exc:
        print(f"Fiction operating system FAILED: {exc}")
        return 1

    policy = registry.get("routing_policy", {})
    if policy.get("load_all_skills") is not False:
        errors.append("registry must keep load_all_skills=false")
    if policy.get("default_selection") != "automatic-trigger-match":
        errors.append("registry must use automatic-trigger-match")
    if policy.get("work_modes") != ["PLAN", "BUILD", "REVIEW"]:
        errors.append("registry work_modes mismatch")

    skills = registry.get("skills", [])
    ids = [item.get("skill_id") for item in skills]
    if set(ids) != EXPECTED_SKILLS or len(ids) != len(EXPECTED_SKILLS):
        errors.append(f"expected exactly five fiction skills, got {ids}")

    for item in skills:
        skill_id = item.get("skill_id")
        if item.get("status") != "ACTIVE":
            errors.append(f"{skill_id}: status must be ACTIVE")
        if item.get("load_by_default") is not False:
            errors.append(f"{skill_id}: load_by_default must be false")
        for field in ("trigger_tags", "skill_modes", "use_when", "do_not_use_when"):
            if not item.get(field):
                errors.append(f"{skill_id}: missing {field}")
        path = ROOT / str(item.get("path", ""))
        if not path.is_file():
            errors.append(f"{skill_id}: missing skill path {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if front_matter_name(text) != skill_id:
            errors.append(f"{skill_id}: front matter name mismatch")
        for mode in item.get("skill_modes", []):
            if mode not in text:
                errors.append(f"{skill_id}: mode absent from SKILL.md: {mode}")

    research = (ROOT / "docs/fiction-ops/CRAFT_RESEARCH.md").read_text(encoding="utf-8")
    for url in REQUIRED_RESEARCH_URLS:
        if url not in research:
            errors.append(f"craft research missing source: {url}")

    for relative in ACTIVE_DOCS:
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for term in GAME_ONLY_TERMS:
            if term in text:
                errors.append(f"{relative}: game-only active term remains: {term}")

    start = (ROOT / "[소설]/00_운영체계/START_HERE.md").read_text(encoding="utf-8")
    for token in ("PLAN", "BUILD", "REVIEW", "DISCOVER", "OUTLINE", "DRAFT", "REVISE", "POLISH"):
        if token not in start:
            errors.append(f"START_HERE missing routing token: {token}")

    operating = (ROOT / "[소설]/00_운영체계/OPERATING_MODEL.md").read_text(encoding="utf-8")
    for token in ("Developmental", "Structural", "Continuity", "Line", "Copyedit", "Proofread", "MUST_FIX"):
        if token not in operating:
            errors.append(f"OPERATING_MODEL missing revision contract: {token}")

    audit = (ROOT / "docs/fiction-ops/BASE_ADOPTION_AUDIT.md").read_text(encoding="utf-8")
    mapped_base_ids = set(re.findall(r"^\| `([^`]+)` \|", audit, re.MULTILINE))
    if mapped_base_ids != EXPECTED_BASE_CAPABILITIES:
        missing = sorted(EXPECTED_BASE_CAPABILITIES - mapped_base_ids)
        extra = sorted(mapped_base_ids - EXPECTED_BASE_CAPABILITIES)
        errors.append(f"Base capability mapping mismatch; missing={missing}, extra={extra}")

    for json_path in ROOT.rglob("*.json"):
        if ".git" in json_path.parts:
            continue
        try:
            json.loads(json_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"invalid JSON: {json_path.relative_to(ROOT)}: {exc}")

    if errors:
        print("Fiction operating system FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Fiction operating system PASSED ({len(REQUIRED_FILES)} files, {len(skills)} skills)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
