#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
REGISTRY = FICTION / "analysis" / "SCENE_PASS_REGISTRY.json"
TEST = ROOT / "tests" / "test_promote_026_030_contract.py"
OLD_CH31_SHA = "ddf006beaf4a34b1855cc138677e2bcdb139056aeed6624a2295411cc20ec9c3"


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
    item = passes["fiction/manuscript/part-1/026-030.md"]
    preserved = item.setdefault("preserved_boundary_shas", {})
    historical = item.setdefault("historical_boundary_shas", {})
    old = preserved.pop("31", historical.get("31"))
    if old != OLD_CH31_SHA:
        raise SystemExit(f"unexpected historical Ch31 SHA: {old}")
    historical["31"] = OLD_CH31_SHA
    item["status"] = (
        "COMPLETE_USER_SOURCE_CANON_RECONCILIATION / CURRENT_PREFIX / "
        "HISTORICAL_BOUNDARY_030_031_RESOLVED"
    )
    REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    text = TEST.read_text(encoding="utf-8")
    text = text.replace(
        "    def test_frontier_advances_only_to_30(self):",
        "    def test_historical_026_030_promotion_receipt_is_preserved(self):",
    )
    old_frontier = '''        self.assertEqual(rec["reconciled_prefix_end"], 30)\n        self.assertEqual(rec["legacy_tail_starts_at"], 31)\n        self.assertEqual(rec["boundary_after_chapter"], 30)\n        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")\n        self.assertEqual(registry["next_bundle_passes"], ["fiction/manuscript/part-1/031-035.md"])\n'''
    new_frontier = '''        self.assertGreaterEqual(rec["reconciled_prefix_end"], 30)\n        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")\n'''
    if old_frontier not in text:
        raise SystemExit("old frontier assertion block not found")
    text = text.replace(old_frontier, new_frontier, 1)
    text = text.replace(
        '            item["preserved_boundary_shas"]["31"],',
        '            item["historical_boundary_shas"]["31"],',
        1,
    )
    text = text.replace(
        '            "analysis/REVERSE_OUTLINE_OVERRIDE_031_MIGRATION_BOUNDARY.json",\n',
        "",
        1,
    )

    pattern = re.compile(
        r"    def test_reverse_outline_moves_fail_closed_boundary_to_30_31\(self\):\n.*?"
        r"\n    def test_new_character_canon_is_preserved\(self\):",
        re.S,
    )
    replacement = '''    def test_reverse_outline_keeps_promoted_026_030_connected_after_later_promotions(self):\n        from tools.fiction_composed_data import load_reverse_outline\n\n        outline = load_reverse_outline(FICTION)\n        by_chapter = {int(item["chapter"]): item for item in outline["chapters"]}\n\n        self.assertEqual(by_chapter[25]["next_chapter"]["chapter"], 26)\n        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[25]["structural_flags"])\n        self.assertEqual(by_chapter[26]["previous_chapter"]["chapter"], 25)\n        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by_chapter[26]["structural_flags"])\n        self.assertEqual(by_chapter[30]["next_chapter"]["chapter"], 31)\n        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[30]["structural_flags"])\n        self.assertEqual(by_chapter[31]["previous_chapter"]["chapter"], 30)\n        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by_chapter[31]["structural_flags"])\n\n    def test_new_character_canon_is_preserved(self):'''
    text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise SystemExit(f"reverse-outline historical test block replacement count={count}")
    TEST.write_text(text, encoding="utf-8")

    Path(__file__).unlink()


if __name__ == "__main__":
    main()
