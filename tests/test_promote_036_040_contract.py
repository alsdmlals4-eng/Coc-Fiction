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
    36: {"title":"사명은 끝났다","pov":"엘리스 → 주안 → 엘리스 → 이안 → 주안","chars":6242,"sha":"a73ee6d8d4f99ab24e7604ae891b58da420ce5549777395c262da69ea340b358"},
    37: {"title":"승자의 손","pov":"엘리스 → 이안 → 엘리스","chars":5872,"sha":"53604e0ca6bcddd2beebb996aeb102ff7417a645c31e3340880bc451da8dc3e8"},
    38: {"title":"인질은 제가 되죠","pov":"엘리스 → 이안 → 엘리스 → 이안","chars":5821,"sha":"c8a9f4a4c867009b73e11257af21bf6050e5b146e4d9c2dc3ffed34d541186d5"},
    39: {"title":"군함이 왔다","pov":"주안 → 엘리스 → 이안","chars":6163,"sha":"8ad77ac006e209745a56b4cbba6d3ba26f7a5a55fa75ff00a8dd2efe39955472"},
    40: {"title":"아버지의 자리","pov":"엘리스 → 이안 → 엘리스","chars":6237,"sha":"1de35b4f4ecb19706f05bac827ed916484f59a2e167a0d4277012696cd1d9f19"},
}

class Promote036040ContractTests(unittest.TestCase):
    def test_exact_user_designated_source_bodies_are_installed(self):
        path = FICTION / "manuscript" / "part-1" / "036-040.md"
        text = path.read_text(encoding="utf-8")
        parsed = {
            int(m.group(1)): {"title":m.group(2).strip(),"pov":m.group(3).strip(),"body":m.group(4).strip()}
            for m in CHAPTER_RE.finditer(text)
        }
        self.assertEqual(sorted(parsed), list(EXPECTED))
        for number, expected in EXPECTED.items():
            actual = parsed[number]
            self.assertEqual(actual["title"], expected["title"])
            self.assertEqual(actual["pov"], expected["pov"])
            self.assertEqual(len(actual["body"]), expected["chars"])
            self.assertEqual(hashlib.sha256(actual["body"].encode("utf-8")).hexdigest(), expected["sha"])
        for forbidden in ("앨리스","복종인자","히템","블랙킹","조작된 감정"):
            self.assertNotIn(forbidden, text)

    def test_frontier_advances_only_to_40(self):
        registry = json.loads((FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))
        rec = registry["external_artifact_reconciliation"]
        self.assertEqual(rec["reconciled_prefix_end"], 40)
        self.assertEqual(rec["legacy_tail_starts_at"], 41)
        self.assertEqual(rec["boundary_after_chapter"], 40)
        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")
        self.assertEqual(registry["next_bundle_passes"], ["fiction/manuscript/part-1/041-045.md"])
        passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
        item = passes["fiction/manuscript/part-1/036-040.md"]
        self.assertEqual(item["chapters"], [36,37,38,39,40])
        self.assertEqual(item["boundary_chapters"], [35,41])
        self.assertEqual(item["preserved_boundary_shas"]["35"], "c4b02af3eb326dfd18ec0331c762c92655cb97525b8b3223d407e69ce912d5f2")

    def test_required_bundle_consumers_exist(self):
        for rel in (
            "analysis/MANUSCRIPT_INDEX_OVERRIDE_036_040.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_036_040.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_041_MIGRATION_BOUNDARY.json",
            "analysis/SCENE_CARDS_036_040.md",
            "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_036_040.md",
        ):
            self.assertTrue((FICTION / rel).is_file(), rel)

    def test_reverse_outline_moves_fail_closed_boundary_to_40_41(self):
        from tools.fiction_composed_data import load_reverse_outline
        outline = load_reverse_outline(FICTION)
        by_chapter = {int(item["chapter"]): item for item in outline["chapters"]}
        self.assertEqual(by_chapter[35]["next_chapter"]["chapter"], 36)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[35]["structural_flags"])
        self.assertEqual(by_chapter[36]["previous_chapter"]["chapter"], 35)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by_chapter[36]["structural_flags"])
        self.assertIsNone(by_chapter[40]["next_chapter"])
        self.assertIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[40]["structural_flags"])
        self.assertIsNone(by_chapter[41]["previous_chapter"])
        self.assertIn("LEGACY_TAIL_BOUNDARY", by_chapter[41]["structural_flags"])

    def test_canon_protections_hold(self):
        canon = json.loads((FICTION / "CANON_REGISTRY.json").read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in canon["canon"]}
        self.assertEqual(by_id["alice.mental-ability"]["status"], "CANON")
        self.assertEqual(by_id["part1.talon-core-antagonist"]["status"], "CANON")
        self.assertIn("인간", by_id["alice.mental-ability"]["summary"])

if __name__ == "__main__":
    unittest.main()
