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
SOURCE_FILE = "폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본(1).docx"
SOURCE_SHA256 = "9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad"
EXPECTED = {
    41: {"title":"잘 돌아왔다","pov":"엘리스 → 이안 → 주안","chars":4255,"sha":"3879d479bec2458e7da2afd78a9c6cc748c9a20e5c0be935d9de365ea05f942a"},
    42: {"title":"살아 돌아온 몸","pov":"엘리스 → 이안 → 주안 → 엘리스","chars":6012,"sha":"e48ad4266831cc8b74ececc7e7fb6f831012a0464005e61eb06fb369d0945a2f"},
    43: {"title":"확인하고 설명하겠습니다","pov":"주안 → 엘리스 → 주안 → 엘리스 → 이안 → 주안 → 엘리스","chars":7004,"sha":"7da555457ebd2debd70fafb41283f9973440d0e99ef098c3c4acc3ba200baaac"},
    44: {"title":"응답하지 않은 호출기","pov":"주안 → 엘리스 → 주안 → 이안 → 엘리스 → 주안 → 엘리스 → 이안","chars":6720,"sha":"6c885ee543a45f145e7d920f7fbb89b5ebb280bf1d4c891a2b671b3c428122dd"},
    45: {"title":"노란 옷은 안 입습니다","pov":"주안","chars":5876,"sha":"e73c81689638476f6736cd9361cdd22dc9e80a076822162856b7516e3a7c12a1"},
}


class Promote041045ContractTests(unittest.TestCase):
    def test_source_manifest_tracks_exact_bridge_source(self):
        manifest = json.loads((ROOT / "docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json").read_text(encoding="utf-8"))
        entries = {item["range"]: item for item in manifest["chunks"] if item.get("canonical", False)}
        source = entries["041-050"]
        self.assertEqual(source["filename"], SOURCE_FILE)
        self.assertEqual(source["sha256"], SOURCE_SHA256)
        self.assertEqual(source["authority"], "USER_DESIGNATED_SOURCE")
        self.assertEqual(manifest["coverage_gaps"], ["101-105"])

    def test_exact_user_designated_bridge_bodies_are_installed(self):
        path = FICTION / "manuscript/part-1/041-045.md"
        text = path.read_text(encoding="utf-8")
        parsed = {
            int(m.group(1)): {"title":m.group(2).strip(), "pov":m.group(3).strip(), "body":m.group(4).strip()}
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
        self.assertNotIn("[규율]", text)

    def test_historical_041_045_promotion_receipt_is_preserved(self):
        registry = json.loads((FICTION / "analysis/SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))
        rec = registry["external_artifact_reconciliation"]
        self.assertGreaterEqual(rec["reconciled_prefix_end"], 45)
        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")
        passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
        item = passes["fiction/manuscript/part-1/041-045.md"]
        self.assertEqual(item["chapters"], [41,42,43,44,45])
        self.assertEqual(item["boundary_chapters"], [40,46])
        self.assertEqual(item["preserved_boundary_shas"]["40"], "1de35b4f4ecb19706f05bac827ed916484f59a2e167a0d4277012696cd1d9f19")
        self.assertEqual(item["chapter_shas"], {str(n): EXPECTED[n]["sha"] for n in range(41,46)})
        sources = [x for x in item.get("source_files", []) if isinstance(x, dict)]
        self.assertTrue(any(x.get("name") == SOURCE_FILE and x.get("sha256") == SOURCE_SHA256 for x in sources))

    def test_required_bundle_consumers_exist(self):
        for rel in (
            "analysis/MANUSCRIPT_INDEX_OVERRIDE_041_045.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_041_045.json",
            "analysis/SCENE_CARDS_041_045.md",
            "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_041_045.md",
        ):
            self.assertTrue((FICTION / rel).is_file(), rel)

    def test_reverse_outline_keeps_promoted_041_045_connected_after_later_promotions(self):
        from tools.fiction_composed_data import load_reverse_outline
        outline = load_reverse_outline(FICTION)
        by = {int(item["chapter"]): item for item in outline["chapters"]}
        self.assertEqual(by[40]["next_chapter"]["chapter"], 41)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by[40]["structural_flags"])
        self.assertEqual(by[41]["previous_chapter"]["chapter"], 40)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by[41]["structural_flags"])
        registry = json.loads((FICTION / "analysis/SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))
        frontier = registry["external_artifact_reconciliation"]["reconciled_prefix_end"]
        if frontier > 45:
            self.assertEqual(by[45]["next_chapter"]["chapter"], 46)
            self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by[45]["structural_flags"])
            self.assertEqual(by[46]["previous_chapter"]["chapter"], 45)
            self.assertNotIn("LEGACY_TAIL_BOUNDARY", by[46]["structural_flags"])
        else:
            self.assertIsNone(by[45]["next_chapter"])
            self.assertIn("RECONCILIATION_MIGRATION_BOUNDARY", by[45]["structural_flags"])
            self.assertIsNone(by[46]["previous_chapter"])
            self.assertIn("LEGACY_TAIL_BOUNDARY", by[46]["structural_flags"])

    def test_bridge_scope_and_canon_guards_hold(self):
        active = (FICTION / "ACTIVE_CONTEXT.md").read_text(encoding="utf-8")
        master = (FICTION / "FICTION_MASTER.md").read_text(encoding="utf-8")
        canon = json.loads((FICTION / "CANON_REGISTRY.json").read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in canon["canon"]}
        self.assertIn("041–066", active)
        self.assertIn("067+", active)
        self.assertIn("041–066", master)
        self.assertEqual(by_id["alice.mental-ability"]["status"], "CANON")
        self.assertEqual(by_id["largo.reveal-sequence"]["status"], "CANON")


if __name__ == "__main__":
    unittest.main()
