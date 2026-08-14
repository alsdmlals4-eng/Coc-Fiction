from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOOP = ROOT / "docs/operations/loop"
SOURCE = "ad3a9cd24fb40b4f9f43dce779d2a2ed6f0f5d05"
PROJECT = "COC_FICTION"
PACKAGE = "COC_LOOP_NARRATIVE_PILOT_001"
REQUIREMENT = "COC_LOOP_CANON_PRESERVATION_001"
AUTHORITY = (
    "fiction/CANON_REGISTRY.json",
    "fiction/FICTION_MASTER.md",
    "fiction/STYLE_GUIDE.md",
    "fiction/ACTIVE_CONTEXT.md",
)


def load(name: str):
    path = LOOP / name
    if not path.is_file():
        raise AssertionError(f"missing Universal Loop contract: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


class UniversalLoopNarrativePilotTests(unittest.TestCase):
    def test_authority_sources_exist_and_are_not_pilot_outputs(self) -> None:
        planning = load("PLANNING_LOCK.json")
        self.assertEqual(planning["status"], "PLANNING_LOCKED")
        self.assertEqual(planning["project_id"], PROJECT)
        self.assertEqual(planning["source_commit"], SOURCE)
        paths = {item["path"] for item in planning["authority_sources"]}
        self.assertEqual(paths, set(AUTHORITY))
        for item in planning["authority_sources"]:
            self.assertEqual(item["source_commit"], SOURCE)
            self.assertTrue((ROOT / item["path"]).is_file())
        protected = "\n".join(planning["protected_meanings"] + planning["excluded_scope"])
        for token in ("CANON", "CHARACTER", "TIMELINE", "STYLE", "MANUSCRIPT", "UNAPPROVED"):
            self.assertIn(token, protected.upper())

    def test_capsule_is_a2_isolated_and_cross_project_imports_are_forbidden(self) -> None:
        capsule = load("PROJECT_EXECUTION_CAPSULE.json")
        self.assertEqual(capsule["contract_role"], "LOOP_PROJECT_EXECUTION_CAPSULE")
        self.assertEqual(capsule["project_id"], PROJECT)
        self.assertEqual(capsule["source_main_sha"], SOURCE)
        self.assertEqual(capsule["autonomy"], "A2_EXECUTE_ISOLATED")
        self.assertEqual(capsule["a3_auto_merge_allowlist"], [])
        self.assertEqual(capsule["scheduler_runtime_provider"], "NOT_CONFIGURED")
        self.assertTrue(all(value == "FORBIDDEN" for value in capsule["context_isolation"].values()))

    def test_pilot_package_changes_only_operations_contract_and_validation_paths(self) -> None:
        package = load("IMPLEMENTATION_PACKAGE.json")
        visual = load("VISUAL_LOCK.json")
        coverage = load("REQUIREMENT_COVERAGE_LEDGER.json")
        self.assertEqual(package["package_id"], PACKAGE)
        self.assertEqual(package["requirement_ids"], [REQUIREMENT])
        self.assertEqual(package["visual_impact"], "NONE")
        self.assertEqual(package["visual_lock_requirement"], "VISUAL_NOT_APPLICABLE")
        self.assertEqual(visual["status"], "VISUAL_NOT_APPLICABLE")
        self.assertEqual(visual["provider"], "NONE")
        allowed = set(package["allowed_paths"])
        self.assertEqual(
            allowed,
            {path for item in coverage["requirements"] for path in item["outputs"]},
        )
        for path in allowed:
            self.assertTrue(
                path.startswith("docs/operations/loop/")
                or path == "tests/test_universal_loop_narrative_pilot.py"
                or path == ".github/workflows/validate-universal-loop-narrative-pilot.yml"
            )
        forbidden = set(package["forbidden_paths"])
        self.assertTrue({"fiction/", "skills/", "tools/", "templates/"}.issubset(forbidden))

    def test_active_run_is_null_and_immutable_pilot_is_shadow_only(self) -> None:
        active = load("ACTIVE_LOOP_RUN.json")
        immutable = load("runs/COC_NARRATIVE_SHADOW_001.json")
        self.assertIsNone(active["active_run"])
        self.assertEqual(immutable["project_id"], PROJECT)
        self.assertEqual(immutable["package_id"], PACKAGE)
        self.assertEqual(immutable["state"], "CREATED")
        self.assertEqual(immutable["design_drift_status"], "NOT_CHECKED")

    def test_runtime_adapter_is_read_only_validation_oriented(self) -> None:
        adapter = load("RUNTIME_ADAPTER.json")
        self.assertEqual(adapter["project_id"], PROJECT)
        self.assertEqual(adapter["status"], "PROJECT_ADAPTER_VALIDATED")
        self.assertEqual(adapter["engine"], {"name": "FictionOps", "version": "1"})
        self.assertTrue({"fiction/", "skills/", "tools/"}.issubset(set(adapter["protected_paths"])))
        self.assertEqual(adapter["test_commands"][0]["network"], "DENIED")

    def test_authority_hash_snapshot_is_stable_for_the_test_process(self) -> None:
        first = {
            path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUTHORITY
        }
        second = {
            path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            for path in AUTHORITY
        }
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
