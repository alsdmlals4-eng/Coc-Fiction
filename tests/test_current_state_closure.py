import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md"
RECEIPT = ROOT / "docs/fiction-ops/CURRENT_STATE_RECEIPT.json"


class CurrentStateClosureTests(unittest.TestCase):
    def test_root_agents_routes_to_live_fiction_authority(self):
        agents = ROOT / "AGENTS.md"
        self.assertTrue(agents.exists(), "root AGENTS.md must exist")
        text = agents.read_text(encoding="utf-8")
        for required in (
            "[소설]/00_운영체계/START_HERE.md",
            "docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md",
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
        self.assertIn(
            "docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md",
            start,
        )

    def test_start_here_state_matches_current_receipt(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        start = (ROOT / "[소설]/00_운영체계/START_HERE.md").read_text(encoding="utf-8")
        prefix = receipt["verified_prefix_end"]
        tail = receipt["legacy_tail_starts_at"]
        pending = receipt.get("pending_frontier_change_pr")
        if pending is None:
            self.assertIn(f"repository_reconciled_prefix: 001-{prefix:03d}", start)
            self.assertIn(f"next_bundle: {receipt['next_bounded_bundle']}", start)
        else:
            self.assertIn(f"repository_candidate_prefix: 001-{prefix:03d}", start)
            self.assertIn(f"pending_frontier_pr: {pending}", start)
            self.assertIn(f"next_bundle_after_merge: {receipt['next_bounded_bundle']}", start)
        self.assertIn(f"legacy_tail_starts_at: {tail:03d}", start)

    def test_current_state_receipt_matches_scene_pass_frontier(self):
        self.assertTrue(RECEIPT.exists(), "current-state receipt must exist")
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
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
        self.assertEqual(receipt["next_bounded_bundle"], scene["next_bundle_passes"][0])

        pending = receipt.get("pending_frontier_change_pr")
        if pending is None:
            observed = receipt.get("frontier_observed_at_main")
            self.assertIsInstance(observed, str)
            self.assertRegex(observed, r"^[0-9a-f]{40}$")
            self.assertIsInstance(receipt.get("last_frontier_change_pr"), int)
        else:
            self.assertIsInstance(pending, int)
            self.assertGreater(pending, 0)
            self.assertIsNone(receipt.get("frontier_observed_at_main"))
            last = receipt.get("last_frontier_change_pr")
            self.assertIsInstance(last, int)
            self.assertGreater(last, 0)
            self.assertNotEqual(last, pending)

    def test_active_routers_match_current_frontier_and_pending_or_closed_receipt(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
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

    def test_pr61_receipt_is_closed_without_advancing_the_frontier(self):
        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        self.assertEqual(receipt["last_frontier_change_pr"], 61)
        self.assertIsNone(receipt["pending_frontier_change_pr"])
        self.assertEqual(
            receipt["frontier_observed_at_main"],
            "1de8beef60612ecc8113b4d7b8146ba7733d96d6",
        )
        self.assertEqual(receipt["verified_prefix_end"], 55)
        self.assertEqual(receipt["legacy_tail_starts_at"], 56)
        self.assertEqual(receipt["manuscript_promotion_state"], "PAUSED_UNTIL_EXPLICIT_RESUME")

    def test_repository_policy_removes_notion_from_current_completion(self):
        self.assertTrue(POLICY.is_file())
        policy = POLICY.read_text(encoding="utf-8")
        for token in (
            "HISTORICAL_MIGRATION_REFERENCE_ONLY",
            "SUPERSEDED_HISTORICAL_COMPATIBILITY",
            "routine current work에서 Notion을 읽거나 쓰거나 동기화하거나 destination readback 완료 조건으로 사용하지 않는다",
            "Notion readback은 completion gate가 아니다",
        ):
            self.assertIn(token, policy)

        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("단일 활성 owner", agents)
        self.assertIn("Notion", agents)
        self.assertIn("완료 조건으로 사용하지 않는다", agents)

        for relative in (
            "[소설]/00_운영체계/START_HERE.md",
            "fiction/ACTIVE_CONTEXT.md",
            "fiction/HANDOFF.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("REPOSITORY_ONLY_CURRENT", text, relative)
            self.assertIn("Notion", text, relative)
            self.assertTrue(
                "완료 조건이 아니다" in text
                or "Gate가 아니다" in text
                or "completion target이 아니다" in text,
                relative,
            )

    def test_research_feasibility_autonomy_and_visual_candidate_contract(self):
        policy = POLICY.read_text(encoding="utf-8")
        for token in (
            "ADOPT / ADAPT / REJECT",
            "FEASIBLE | PARTIAL | BLOCKED_UNVERIFIED",
            "SPEC_ONLY_IS_NOT_PRODUCTION_PROOF",
            "GENERATED_CANDIDATE != USER_APPROVED != CANON_REGISTERED != DISTRIBUTION_READY",
            "모델의 임의 영구 기억이 아니라 repository에 남는 재사용 가능한 운영 evidence",
        ):
            self.assertIn(token, policy)

        receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        self.assertEqual(receipt["manuscript_promotion_state"], "PAUSED_UNTIL_EXPLICIT_RESUME")

    def test_stale_pending_and_050_frontier_are_not_live_router_state(self):
        for relative in (
            "[소설]/00_운영체계/START_HERE.md",
            "fiction/ACTIVE_CONTEXT.md",
            "fiction/HANDOFF.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("pending_frontier_change_pr: 61", text, relative)
            self.assertNotIn("production prefix: `001–050`", text, relative)
            self.assertNotIn("fail-closed boundary: `50→51`", text, relative)


if __name__ == "__main__":
    unittest.main()
