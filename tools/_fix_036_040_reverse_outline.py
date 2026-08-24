#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from build_fiction_reverse_outline import build_current

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
ANALYSIS = FICTION / "analysis"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    generated = build_current(ROOT)
    by_chapter = {int(item["chapter"]): item for item in generated["chapters"]}

    prior_path = ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_031_035.json"
    prior = load(prior_path)
    prior["chapters"] = [
        by_chapter[35] if int(item["chapter"]) == 35 else item
        for item in prior["chapters"]
    ]
    prior["status"] = "ACTIVE_OVERRIDE / BUNDLE_031_035 / CURRENT_RECONCILED"
    dump(prior_path, prior)

    dump(
        ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_036_040.json",
        {
            "schema_version": 1,
            "updated_at": "2026-08-24",
            "status": "ACTIVE_OVERRIDE / BUNDLE_036_040 / CURRENT_RECONCILED_PENDING_PR55",
            "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
            "chapters": [by_chapter[n] for n in range(36, 41)],
        },
    )
    dump(
        ANALYSIS / "REVERSE_OUTLINE_OVERRIDE_041_MIGRATION_BOUNDARY.json",
        {
            "schema_version": 1,
            "updated_at": "2026-08-24",
            "status": "ACTIVE_OVERRIDE / LEGACY_TAIL_BOUNDARY_041",
            "baseline": "baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
            "chapters": [by_chapter[41]],
        },
    )
    print("regenerated Ch35-41 reverse-outline overrides from current manuscript/index")


if __name__ == "__main__":
    main()
