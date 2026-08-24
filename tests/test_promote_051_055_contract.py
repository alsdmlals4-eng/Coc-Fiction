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
SOURCE_FILE = "폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx"
SOURCE_SHA256 = "84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496"
LEGACY_ALICE_KO = "앨" + "리스"
EXPECTED = {
    51: {"title":"잊어도 되는 기억","pov":"주안 → 이안 → 주안","chars":5568,"sha":"5c030e6bef2a802db670f600ad0bb5079bcba185b5bd134eae3ad44f3fe52880"},
    52: {"title":"잊으면 안 될 것","pov":"주안 → 이안 → 주안 → 이안","chars":4934,"sha":"5ad14e30c75d7ce3a82514ebcd016aab92bf2f9a384962d47e4d5c4f69c396ce"},
    53: {"title":"주교님의 외갑","pov":"주안 → 이안 → 주안 → 이안 → 주안 → 이안","chars":5244,"sha":"286f8768e7ccf046f9a51a500b59fd62ec95bbcc44354a3916075fd5b2a701e8"},
    54: {"title":"사슬을 끊는 법","pov":"주안 → 이안 → 주안 → 이안 → 주안","chars":5666,"sha":"dba02380a691b8b2d68fe1a8c95734350e9233b2589f8776156052e64e2a2550"},
    55: {"title":"세상을 봐야 합니다","pov":"주안 → 이안 → 주안 → 이안","chars":4981,"sha":"35b0cb9f53775945a9cafe2aa307e3ffe04a3355b38b3e1db831826db60d5fdc"},
}


def parsed_bodies(path: Path):
    text = path.read_text(encoding="utf-8")
    return {
        int(m.group(1)): {"title": m.group(2).strip(), "pov": m.group(3).strip(), "body": m.group(4).strip()}
        for m in CHAPTER_RE.finditer(text)
    }


class Promote051055ContractTests(unittest.TestCase):
    def test_source_manifest_tracks_exact_bridge_source(self):
        manifest = json.loads((ROOT / "docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json").read_text(encoding="utf-8"))
        entries = {item["range"]: item for item in manifest["chunks"] if item.get("canonical", False)}
        source = entries["051-060"]
        self.assertEqual(source["filename"], SOURCE_FILE)
        self.assertEqual(source["sha256"], SOURCE_SHA256)
        self.assertEqual(source["authority"], "USER_DESIGNATED_SOURCE")
        self.assertEqual(manifest["coverage_gaps"], ["101-105"])

    def test_source_derived_bodies_are_canon_reconciled_and_installed(self):
        path = FICTION / "manuscript/part-1/051-055.md"
        text = path.read_text(encoding="utf-8")
        parsed = parsed_bodies(path)
        self.assertEqual(sorted(parsed), list(EXPECTED))
        for number, expected in EXPECTED.items():
            actual = parsed[number]
            self.assertEqual(actual["title"], expected["title"])
            self.assertEqual(actual["pov"], expected["pov"])
            self.assertEqual(len(actual["body"]), expected["chars"])
            self.assertEqual(hashlib.sha256(actual["body"].encode("utf-8")).hexdigest(), expected["sha"])
        for forbidden in (LEGACY_ALICE_KO,"복종인자","히템","블랙킹","조작된 감정","쵸르브라트","미하일 카쉬프","피엘렛토","붉은 늑대","컨소시엄","협상 책임자","오션"):
            self.assertNotIn(forbidden, text)
        self.assertNotIn("[규율]", text)

    def test_candidate_frontier_advances_only_to_55(self):
        registry = json.loads((FICTION / "analysis/SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))
        rec = registry["external_artifact_reconciliation"]
        self.assertEqual(rec["reconciled_prefix_end"], 55)
        self.assertEqual(rec["legacy_tail_starts_at"], 56)
        self.assertEqual(rec["boundary_after_chapter"], 55)
        self.assertEqual(rec["whole_manuscript_continuity"], "NOT_YET_CLAIMED")
        self.assertEqual(registry["next_bundle_passes"], ["fiction/manuscript/part-1/056-060.md"])
        passes = {item["bundle"]: item for item in registry["completed_bundle_passes"]}
        item = passes["fiction/manuscript/part-1/051-055.md"]
        self.assertEqual(item["chapters"], [51,52,53,54,55])
        self.assertEqual(item["boundary_chapters"], [50,56])
        self.assertEqual(item["preserved_boundary_shas"]["50"], "5b3bd9bcbb7b3d04deb38dfdb39db2c9fdc56fb50df18ea9425562c9b484880e")
        legacy = parsed_bodies(FICTION / "manuscript/part-1/056-060.md")
        self.assertIn(56, legacy)
        current_legacy_sha = hashlib.sha256(legacy[56]["body"].encode("utf-8")).hexdigest()
        self.assertEqual(item["preserved_boundary_shas"]["56"], current_legacy_sha)

    def test_required_bundle_consumers_exist(self):
        for rel in (
            "analysis/MANUSCRIPT_INDEX_OVERRIDE_051_055.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_051_055.json",
            "analysis/REVERSE_OUTLINE_OVERRIDE_056_MIGRATION_BOUNDARY.json",
            "analysis/SCENE_CARDS_051_055.md",
            "reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_051_055.md",
        ):
            self.assertTrue((FICTION / rel).is_file(), rel)

    def test_reverse_outline_connects_bridge_and_moves_boundary(self):
        from tools.fiction_composed_data import load_reverse_outline
        outline = load_reverse_outline(FICTION)
        by = {int(item["chapter"]): item for item in outline["chapters"]}
        self.assertIsNotNone(by[50]["next_chapter"])
        if by[50]["next_chapter"] is not None:
            self.assertEqual(by[50]["next_chapter"]["chapter"], 51)
        self.assertNotIn("RECONCILIATION_MIGRATION_BOUNDARY", by[50]["structural_flags"])
        self.assertIsNotNone(by[51]["previous_chapter"])
        if by[51]["previous_chapter"] is not None:
            self.assertEqual(by[51]["previous_chapter"]["chapter"], 50)
        self.assertNotIn("LEGACY_TAIL_BOUNDARY", by[51]["structural_flags"])
        self.assertIsNone(by[55]["next_chapter"])
        self.assertIn("RECONCILIATION_MIGRATION_BOUNDARY", by[55]["structural_flags"])
        self.assertIsNone(by[56]["previous_chapter"])
        self.assertIn("LEGACY_TAIL_BOUNDARY", by[56]["structural_flags"])

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
