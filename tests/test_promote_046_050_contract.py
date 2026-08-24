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
    46: {"title":"자아를 찾으러 떠났습니다","pov":"주안","chars":5861,"sha":"ae3928bb6234eb4086115c74614d43aee3b436aa52cc30d14641a5673878791d"},
    47: {"title":"호수가 보이는 마을","pov":"이안 → 주안 → 이안","chars":6228,"sha":"03e0e7c4fcbfedd4326f335bdc5f49b79fbaf3acc2c1ceaa8e56fa91c8bc6a83"},
    48: {"title":"돼지고기는 아니었습니다","pov":"주안 → 이안","chars":5800,"sha":"4cd101ebbb686f269ae2efe1e3e40eba11edd75420c3782aa8918f58df8bb41e"},
    49: {"title":"여덟 해 만입니다","pov":"이안 → 주안 → 이안 → 주안","chars":5793,"sha":"6408f1e4b70b7fdbe43912c5b43c0ce2394d1303a6cbc81f31ea4d0ff9f307be"},
    50: {"title":"낙원의 손님분들","pov":"이안 → 주안","chars":5296,"sha":"5b3bd9bcbb7b3d04deb38dfdb39db2c9fdc56fb50df18ea9425562c9b484880e"},
}


class Promote046050ContractTests(unittest.TestCase):
    def test_source_manifest_tracks_exact_bridge_source(self):
        manifest = json.loads((ROOT / "docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json").read_text(encoding="utf-8"))
        entries = {item["range"]: item for item in manifest["chunks"] if item.get("canonical", False)}
        source = entries["041-050"]
        self.assertEqual(source["filename"], SOURCE_FILE)
        self.assertEqual(source["sha256"], SOURCE_SHA256)
        self.assertEqual(source["authority"], "USER_DESIGNATED_SOURCE")
        self.assertEqual(manifest["coverage_gaps"], ["101-105"])

    def test_user_designated_bridge_bodies_are_canon_reconciled_and_installed(self):
        path = FICTION / "manuscript/part-1/046-050.md"
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

    def test_candidate_frontier_advances_only_to_50(self):
        registry = json.loads((FICTION / "analysis/SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))
        rec = registry["external_artifact_reconciliation"]
        self.assertEqual(rec["reconciled_prefix_end"], 50)
        self.assertEqual(rec["legacy_tail_starts_at"], 51)
        self.assertEqual(rec["boundary_after_chapter"], 50)
        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")
        self.assertEqual(registry["next_bundle_passes"], ["fiction/manuscript/part-1/051-055.md"])
        passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
        item = passes["fiction/manuscript/part-1/046-050.md"]
        self.assertEqual(item["chapters"], [46,47,48,49,50])
        self.assertEqual(item["boundary_chapters"], [45,51])
        self.assertEqual(item["preserved_boundary_shas"]["45"], "e73c81689638476f6736cd9361cdd22dc9e80a076822162856b7516e3a7c12a1")
        self.assertEqual(item["preserved_boundary_shas"]["51"], "f149a848ef8c2069d0e461a8b9fe1a73b657c77b9e5327196ce905cfafb60ac1")

    def test_required_bundle_consumers_exist(self):
        for rel in (
            "analysis/MANUSCRIPT_INDEX_OVERRIDE_046_050.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_046_050.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_051_MIGRATION_BOUNDARY.json",
            "analysis/SCENE_CARDS_046_050.md",
            "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_046_050.md",
        ):
            self.assertTrue((FICTION / rel).is_file(), rel)

    def test_reverse_outline_connects_bridge_and_moves_boundary(self):
        from tools.fiction_composed_data import load_reverse_outline
        outline = load_reverse_outline(FICTION)
        by = {int(item["chapter"]): item for item in outline["chapters"]}
        self.assertEqual(by[45]["next_chapter"]["chapter"], 46)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by[45]["structural_flags"])
        self.assertEqual(by[46]["previous_chapter"]["chapter"], 45)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by[46]["structural_flags"])
        self.assertIsNone(by[50]["next_chapter"])
        self.assertIn("RECONCILIATION_MIGRATION_BOUNDARY", by[50]["structural_flags"])
        self.assertIsNone(by[51]["previous_chapter"])
        self.assertIn("LEGACY_TAIL_BOUNDARY", by[51]["structural_flags"])

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
