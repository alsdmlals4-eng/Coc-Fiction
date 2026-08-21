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


EXPECTED = {
    21: {
        "title": "삼 분만 기다립니다",
        "pov": "이안 → 엘리스 → 이안 → 엘리스 → 이안",
        "chars": 6472,
        "sha": "feb8df2a30c678e174a8cafbbeb8e33ec4d64042339f514a8b771e3b5b61b389",
    },
    22: {
        "title": "다음에는 냄새부터 지워라",
        "pov": "주안 → 엘리스 → 주안 → 엘리스 → 주안 → 엘리스",
        "chars": 5916,
        "sha": "6ae4dba9533cad99139cfef11fdadfbddf5a381bf95091bc939296694c68e801",
    },
    23: {
        "title": "떨어지면 받겠습니다",
        "pov": "주안 → 엘리스 → 이안 → 엘리스 → 이안 → 주안",
        "chars": 6779,
        "sha": "cd506e7449f718dfdda9d67db3aba654619457991ffb0fe0cba2ef43f660c40b",
    },
    24: {
        "title": "한 박자 늦게",
        "pov": "주안 → 이안 → 엘리스 → 주안 → 이안 → 엘리스 → 주안 → 이안",
        "chars": 6961,
        "sha": "c111f79f73c034a6bc2f5dea8606e8b35c687b6a55842a6fd873adbda18b8549",
    },
    25: {
        "title": "승자를 만들지 않기로 했다",
        "pov": "이안 → 엘리스 → 주안 → 이안 → 주안",
        "chars": 5870,
        "sha": "09a945739b8438e30b3721c4c777a0f1c4736f5d6ac7a0684f02877e399869e8",
    },
}


class Promote021025ContractTests(unittest.TestCase):
    def test_exact_candidate_bodies_are_installed(self):
        path = FICTION / "manuscript" / "part-1" / "021-025.md"
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

    def test_frontier_advances_only_to_25(self):
        registry = json.loads(
            (FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8")
        )
        rec = registry["external_artifact_reconciliation"]
        self.assertEqual(rec["reconciled_prefix_end"], 25)
        self.assertEqual(rec["legacy_tail_starts_at"], 26)
        self.assertEqual(rec["boundary_after_chapter"], 25)
        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")
        self.assertEqual(registry["next_bundle_passes"], ["fiction/manuscript/part-1/026-030.md"])

        passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
        item = passes["fiction/manuscript/part-1/021-025.md"]
        self.assertEqual(item["chapters"], [21, 22, 23, 24, 25])
        self.assertEqual(item["boundary_chapters"], [20, 26])
        self.assertEqual(item["preserved_boundary_shas"]["20"], "dc78dd2f3ab00d853225ca4c98a85832d5fbb088df0b304258172e2ffd754523")
        self.assertEqual(item["preserved_boundary_shas"]["26"], "13e7273f2f7a685fc7548edfc28963da673c77936ad0575f2f31ac7830cf1d13")

    def test_required_bundle_consumers_exist(self):
        for rel in (
            "analysis/MANUSCRIPT_INDEX_OVERRIDE_021_025.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_021_025.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_026_MIGRATION_BOUNDARY.json",
            "analysis/SCENE_CARDS_021_025.md",
            "reports/REVISION_2026-08-21_CURRENT_RECONCILIATION_021_025.md",
        ):
            self.assertTrue((FICTION / rel).is_file(), rel)

    def test_reverse_outline_moves_fail_closed_boundary_to_25_26(self):
        from tools.fiction_composed_data import load_reverse_outline

        outline = load_reverse_outline(FICTION)
        by_chapter = {int(item["chapter"]): item for item in outline["chapters"]}

        self.assertEqual(by_chapter[20]["next_chapter"]["chapter"], 21)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[20]["structural_flags"])
        self.assertEqual(by_chapter[21]["previous_chapter"]["chapter"], 20)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by_chapter[21]["structural_flags"])
        self.assertIsNone(by_chapter[25]["next_chapter"])
        self.assertIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[25]["structural_flags"])
        self.assertIsNone(by_chapter[26]["previous_chapter"])
        self.assertIn("LEGACY_TAIL_BOUNDARY", by_chapter[26]["structural_flags"])


if __name__ == "__main__":
    unittest.main()
