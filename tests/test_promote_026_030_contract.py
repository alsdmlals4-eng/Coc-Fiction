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

SOURCE_FILE = "폭풍의눈_2차퇴고_제021-030화_상실광기_강적위상_가독성강화본(1).docx"
SOURCE_SHA256 = "e15c8fb4ed4ab1b6980c2c57f3979986bdbfa02f77aafef3cc84d3652cb70547"

EXPECTED = {
    26: {
        "title": "네 책임은 지금",
        "pov": "엘리스 → 주안 → 이안 → 엘리스 → 주안",
        "chars": 5852,
        "sha": "9af7d74668a8deeab176923f704514f1dc8fd9ba2996efef2bd4c1869db64539",
    },
    27: {
        "title": "친구가 적진에 있었다",
        "pov": "이안 → 이안 → 이안 → 이안",
        "chars": 7317,
        "sha": "341f3d7d86018f7c02a2fe9f396e9e5e0a30b985b9185d50dfa3791a343dc9b8",
    },
    28: {
        "title": "편해져도 된다는 말",
        "pov": "이안 → 엘리스 → 엘리스 → 이안",
        "chars": 6334,
        "sha": "a809db4608f35c625d421288b62176e85480bf1b74ac8a61f63627547f0022f6",
    },
    29: {
        "title": "친구를 막는 법",
        "pov": "이안 → 엘리스 → 이안 → 주안",
        "chars": 6545,
        "sha": "cb8095dff21ba84a94433460df1b50e0b2b5a6e0930a8b846e3248f93db33891",
    },
    30: {
        "title": "폭풍을 걷는 자",
        "pov": "이안 → 엘리스 → 이안 → 엘리스 → 이안 → 주안",
        "chars": 6499,
        "sha": "5ca93e6979b8beaa0d6ffe07809c664c0b7b907387b47b1732b431be364baac1",
    },
}


class Promote026030ContractTests(unittest.TestCase):
    def test_source_manifest_tracks_user_designated_chunk(self):
        manifest = json.loads(
            (ROOT / "docs" / "fiction-ops" / "2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json").read_text(encoding="utf-8")
        )
        entries = {item["range"]: item for item in manifest["chunks"] if item.get("canonical", False)}
        source = entries["021-030"]
        self.assertEqual(source["filename"], SOURCE_FILE)
        self.assertEqual(source["sha256"], SOURCE_SHA256)
        self.assertEqual(source["authority"], "USER_DESIGNATED_SOURCE")
        self.assertEqual(manifest["coverage_gaps"], ["101-105"])

    def test_exact_user_designated_source_bodies_are_installed(self):
        path = FICTION / "manuscript" / "part-1" / "026-030.md"
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
            "히템",
        ):
            self.assertNotIn(forbidden, text)

    def test_historical_026_030_promotion_receipt_is_preserved(self):
        registry = json.loads(
            (FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8")
        )
        rec = registry["external_artifact_reconciliation"]
        self.assertGreaterEqual(rec["reconciled_prefix_end"], 30)
        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")

        passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
        item = passes["fiction/manuscript/part-1/026-030.md"]
        self.assertEqual(item["chapters"], [26, 27, 28, 29, 30])
        self.assertEqual(item["boundary_chapters"], [25, 31])
        self.assertEqual(
            item["preserved_boundary_shas"]["25"],
            "09a945739b8438e30b3721c4c777a0f1c4736f5d6ac7a0684f02877e399869e8",
        )
        self.assertEqual(
            item["historical_boundary_shas"]["31"],
            "ddf006beaf4a34b1855cc138677e2bcdb139056aeed6624a2295411cc20ec9c3",
        )

    def test_required_bundle_consumers_exist(self):
        for rel in (
            "analysis/MANUSCRIPT_INDEX_OVERRIDE_026_030.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_026_030.json",
            "analysis/SCENE_CARDS_026_030.md",
            "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_026_030.md",
        ):
            self.assertTrue((FICTION / rel).is_file(), rel)

    def test_reverse_outline_keeps_promoted_026_030_connected_after_later_promotions(self):
        from tools.fiction_composed_data import load_reverse_outline

        outline = load_reverse_outline(FICTION)
        by_chapter = {int(item["chapter"]): item for item in outline["chapters"]}

        self.assertEqual(by_chapter[25]["next_chapter"]["chapter"], 26)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[25]["structural_flags"])
        self.assertEqual(by_chapter[26]["previous_chapter"]["chapter"], 25)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by_chapter[26]["structural_flags"])
        self.assertEqual(by_chapter[30]["next_chapter"]["chapter"], 31)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by_chapter[30]["structural_flags"])
        self.assertEqual(by_chapter[31]["previous_chapter"]["chapter"], 30)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by_chapter[31]["structural_flags"])

    def test_new_character_canon_is_preserved(self):
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
