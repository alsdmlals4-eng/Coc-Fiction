import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CurrentStateClosureTests(unittest.TestCase):
    def test_root_agents_routes_to_live_fiction_authority(self):
        agents = ROOT / "AGENTS.md"
        self.assertTrue(agents.exists(), "root AGENTS.md must exist")
        text = agents.read_text(encoding="utf-8")
        for required in (
            "[소설]/00_운영체계/START_HERE.md",
            "fiction/ACTIVE_CONTEXT.md",
            "fiction/CANON_REGISTRY.json",
            "fiction/analysis/SCENE_PASS_REGISTRY.json",
            "docs/fiction-ops/CURRENT_STATE_RECEIPT.json",
        ):
            self.assertIn(required, text)

    def test_current_state_receipt_matches_scene_pass_frontier(self):
        receipt_path = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
        self.assertTrue(receipt_path.exists(), "current-state receipt must exist")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        scene = json.loads(
            (ROOT / "fiction/analysis/SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8")
        )
        frontier = scene["external_artifact_reconciliation"]

        self.assertEqual(receipt["schema_version"], 1)
        self.assertEqual(
            receipt["frontier_observed_at_main"],
            "395f0af0120f5ab6949c86772d3b77b5b3eb9f3a",
        )
        self.assertEqual(receipt["last_frontier_change_pr"], 39)
        self.assertNotIn("last_integrated_pr", receipt)
        self.assertEqual(receipt["verified_prefix_end"], 20)
        self.assertEqual(receipt["legacy_tail_starts_at"], 21)
        self.assertEqual(receipt["boundary_after_chapter"], 20)
        self.assertEqual(
            receipt["next_bounded_bundle"],
            "fiction/manuscript/part-1/021-025.md",
        )
        self.assertEqual(receipt["whole_manuscript_continuity"], "NOT_YET_CLAIMED")
        self.assertEqual(receipt["verified_prefix_end"], frontier["reconciled_prefix_end"])
        self.assertEqual(receipt["legacy_tail_starts_at"], frontier["legacy_tail_starts_at"])
        self.assertEqual(receipt["boundary_after_chapter"], frontier["boundary_after_chapter"])
        self.assertEqual(
            receipt["candidate_sha256"], frontier["artifact_sha256"]
        )

    def test_active_routers_describe_pr39_as_frontier_change_not_latest_repo_pr(self):
        active = (ROOT / "fiction/ACTIVE_CONTEXT.md").read_text(encoding="utf-8")
        handoff = (ROOT / "fiction/HANDOFF.md").read_text(encoding="utf-8")

        for text, name in ((active, "ACTIVE_CONTEXT"), (handoff, "HANDOFF")):
            self.assertIn("PR #39", text, f"{name} must identify the frontier-changing PR")
            self.assertIn("last_frontier_change_pr: 39", text)
            self.assertIn("001–020", text, f"{name} must state the current prefix")
            self.assertIn("021-025", text, f"{name} must state the next bounded bundle")
            self.assertNotIn("last_integrated_pr: 39", text)

        self.assertNotIn(
            "current pass: Ch016–020 exact source/index/reverse-outline/scene-pass Green candidate",
            active,
        )
        self.assertNotIn(
            "current branch: Ch016–020 exact source + composed index + generator-derived reverse outline + scene-pass contract",
            handoff,
        )


if __name__ == "__main__":
    unittest.main()
