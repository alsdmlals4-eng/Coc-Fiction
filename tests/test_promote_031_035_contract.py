import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)

SOURCE_FILE = "폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx"
SOURCE_SHA256 = "89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10"

EXPECTED = {
    31: {
        "title": "창을 잡는 사람",
        "pov": "주안 → 엘리스 → 주안 → 엘리스 → 주안 → 엘리스 → 이안",
        "chars": 10305,
        "sha": "c24a4c8b236e12b54825c44c810a96588e4b1360b02f8e8a9f4df5d26fd20353",
    },
    32: {
        "title": "전장 전체가 몸이었다",
        "pov": "이안 → 주안 → 엘리스 → 이안 → 주안",
        "chars": 6291,
        "sha": "e55613d4b68fd0d6222a680d3eba1d0416033504322fc9aaae6cf09a9cdc6bce",
    },
    33: {
        "title": "괴물이 되어야 합니다",
        "pov": "주안 → 엘리스 → 주안 → 엘리스 → 주안",
        "chars": 5933,
        "sha": "a6042d9b3c6dc9b82e603c2088a45d9a2f09b974ff224d0a3de618eb5c1d4cec",
    },
    34: {
        "title": "핵은 붉었다",
        "pov": "주안 → 엘리스 → 이안 → 주안 → 엘리스",
        "chars": 5935,
        "sha": "ffbe4a8459f972bcdae6f9fa27416c63a64efb900c19006348d7718c9c20286d",
    },
    35: {
        "title": "완전 소 생물",
        "pov": "이안 → 주안 → 엘리스 → 이안 → 주안 → 엘리스",
        "chars": 6194,
        "sha": "c4b02af3eb326dfd18ec0331c762c92655cb97525b8b3223d407e69ce912d5f2",
    },
}


class Promote031035ContractTests(unittest.TestCase):
    def test_source_manifest_tracks_user_designated_chunk(self):
        manifest = json.loads(
            (ROOT / "docs" / "fiction-ops" / "2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json").read_text(encoding="utf-8")
        )
        entries = {item["range"]: item for item in manifest["chunks"] if item.get("canonical", False)}
        source = entries["031-040"]
        self.assertEqual(source["filename"], SOURCE_FILE)
        self.assertEqual(source["sha256"], SOURCE_SHA256)
        self.assertEqual(source["authority"], "USER_DESIGNATED_SOURCE")
        self.assertEqual(manifest["coverage_gaps"], ["101-105"])

    def test_exact_user_designated_source_bodies_are_installed(self):
        path = FICTION / "manuscript" / "part-1" / "031-035.md"
        text = path.read_text(encoding="utf-8")
        parsed = {
            int(match.group(1)): {
                "title": match.group(2).strip(),
                "pov": match.group(3).strip(),
                "body": match.group(4).strip(),
            }
            for match in CHAPTER_RE.finditer(text)
        }
        self.assertEqual(sorted(parsed), list(EXPECTED))
        for number, expected in EXPECTED.items():
            actual = parsed[number]
            self.assertEqual(actual["title"], expected["title"])
            self.assertEqual(actual["pov"], expected["pov"])
            self.assertEqual(len(actual["body"]), expected["chars"])
            self.assertEqual(
                hashlib.sha256(actual["body"].encode("utf-8")).hexdigest(),
                expected["sha"],
            )

        for forbidden in (
            "앨리스",
            "복종인자",
            "히템",
            "블랙킹",
            "오션",
            "쵸르브라트",
            "미하일 카쉬프",
            "피엘렛토",
            "붉은 늑대",
            "컨소시엄",
            "조작된 감정",
        ):
            self.assertNotIn(forbidden, text)

    def test_frontier_advances_only_to_35(self):
        registry = json.loads(
            (FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8")
        )
        rec = registry["external_artifact_reconciliation"]
        self.assertEqual(rec["reconciled_prefix_end"], 35)
        self.assertEqual(rec["legacy_tail_starts_at"], 36)
        self.assertEqual(rec["boundary_after_chapter"], 35)
        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")
        self.assertEqual(registry["next_bundle_passes"], ["fiction/manuscript/part-1/036-040.md"])

        passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
        item = passes["fiction/manuscript/part-1/031-035.md"]
        self.assertEqual(item["chapters"], [31, 32, 33, 34, 35])
        self.assertEqual(item["boundary_chapters"], [30, 36])
        self.assertEqual(
            item["preserved_boundary_shas"]["30"],
            "5ca93e6979b8beaa0d6ffe07809c664c0b7b907387b47b1732b431be364baac1",
        )
        self.assertEqual(
            item["preserved_boundary_shas"]["36"],
            "c5dd1b067199247a221350efd77e555c5cc98d08a648eb0f06ec9bd5ddfaf96e",
        )

    def test_required_bundle_consumers_exist(self):
        for rel in (
            "analysis/MANUSCRIPT_INDEX_OVERRIDE_031_035.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_031_035.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_036_MIGRATION_BOUNDARY.json",
            "analysis/SCENE_CARDS_031_035.md",
            "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_031_035.md",
        ):
            self.assertTrue((FICTION / rel).is_file(), rel)

    def test_reverse_outline_moves_fail_closed_boundary_to_35_36(self):
        from tools.fiction_composed_data import load_reverse_outline

        outline = load_reverse_outline(FICTION)
        by_chapter = {int(item["chapter"]): item for item in outline["chapters"]}

        self.assertEqual(by_chapter[30]["next_chapter"]["chapter"], 31)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[30]["structural_flags"])
        self.assertEqual(by_chapter[31]["previous_chapter"]["chapter"], 30)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by_chapter[31]["structural_flags"])
        self.assertIsNone(by_chapter[35]["next_chapter"])
        self.assertIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[35]["structural_flags"])
        self.assertIsNone(by_chapter[36]["previous_chapter"])
        self.assertIn("LEGACY_TAIL_BOUNDARY", by_chapter[36]["structural_flags"])

    def test_character_canon_protections_still_hold(self):
        canon = json.loads((FICTION / "CANON_REGISTRY.json").read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in canon["canon"]}
        for canon_id in (
            "part1.talon-core-antagonist",
            "part1.milly-sex-and-miskatonic-disguise",
            "part1.hatem-sex-and-default-mask",
        ):
            self.assertEqual(by_id[canon_id]["status"], "CANON")


if __name__ == "__main__":
    unittest.main()
