import json
import re
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

    def test_root_agents_changes_trigger_fiction_validation(self):
        workflow = (ROOT / ".github/workflows/fiction-ops-validation.yml").read_text(
            encoding="utf-8"
        )
        trigger_line = '      - "AGENTS.md"'
        self.assertGreaterEqual(
            workflow.count(trigger_line),
            2,
            "root AGENTS.md must trigger both pull_request and main push validation",
        )

    def test_internal_start_here_routes_through_current_state_receipt(self):
        start = (ROOT / "[소설]/00_운영체계/START_HERE.md").read_text(encoding="utf-8")
        self.assertIn("docs/fiction-ops/CURRENT_STATE_RECEIPT.json", start)

    def test_current_state_receipt_matches_scene_pass_frontier(self):
        receipt_path = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"
        self.assertTrue(receipt_path.exists(), "current-state receipt must exist")
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        scene = json.loads(
            (ROOT / "fiction/analysis/SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8")
        )
        frontier = scene["external_artifact_reconciliation"]

        self.assertEqual(receipt["schema_version"], 1)
        self.assertNotIn("last_integrated_pr", receipt)
        self.assertEqual(receipt["verified_prefix_end"], frontier["reconciled_prefix_end"])
        self.assertEqual(receipt["legacy_tail_starts_at"], frontier["legacy_tail_starts_at"])
        self.assertEqual(receipt["boundary_after_chapter"], frontier["boundary_after_chapter"])
        self.assertEqual(receipt["candidate_sha256"], frontier["artifact_sha256"])
        self.assertEqual(receipt["whole_manuscript_continuity"], frontier["whole_manuscript_continuity"])
        self.assertEqual(
            receipt["next_bounded_bundle"],
            scene["next_bundle_passes"][0],
        )

        pending = receipt.get("pending_frontier_change_pr")
        if pending is None:
            observed = receipt.get("frontier_observed_at_main")
            self.assertIsInstance(observed, str)
            self.assertRegex(observed, r"^[0-9a-f]{40}$")
            self.assertIsInstance(receipt.get("last_frontier_change_pr"), int)
        else:
            self.assertEqual(pending, 42)
            self.assertIsNone(receipt.get("frontier_observed_at_main"))
            self.assertEqual(receipt.get("last_frontier_change_pr"), 39)

    def test_active_routers_match_current_frontier_and_pending_or_closed_receipt(self):
        receipt = json.loads(
            (ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json").read_text(encoding="utf-8")
        )
        active = (ROOT / "fiction/ACTIVE_CONTEXT.md").read_text(encoding="utf-8")
        handoff = (ROOT / "fiction/HANDOFF.md").read_text(encoding="utf-8")
        prefix = receipt["verified_prefix_end"]
        tail = receipt["legacy_tail_starts_at"]
        next_bundle = Path(receipt["next_bounded_bundle"]).stem

        for text, name in ((active, "ACTIVE_CONTEXT"), (handoff, "HANDOFF")):
            self.assertIn(f"reconciled_prefix_end: {prefix}", text, name)
            self.assertIn(f"legacy_tail_starts_at: {tail}", text, name)
            self.assertIn(f"boundary_after_chapter: {prefix}", text, name)
            self.assertIn(next_bundle, text, name)
            pending = receipt.get("pending_frontier_change_pr")
            if pending is not None:
                self.assertIn(f"pending_frontier_change_pr: {pending}", text, name)
            else:
                self.assertIn(
                    f"last_frontier_change_pr: {receipt['last_frontier_change_pr']}",
                    text,
                    name,
                )


if __name__ == "__main__":
    unittest.main()
