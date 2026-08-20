#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
errors: list[str] = []

registry = json.loads((FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))
reconciliation = registry.get("external_artifact_reconciliation", {})

expected_frontier = {
    "reconciled_prefix_end": 20,
    "legacy_tail_starts_at": 21,
    "boundary_after_chapter": 20,
}
for key, expected in expected_frontier.items():
    if reconciliation.get(key) != expected:
        errors.append(f"{key}: expected {expected}, got {reconciliation.get(key)}")

expected_next = ["fiction/manuscript/part-1/021-025.md"]
if registry.get("next_bundle_passes") != expected_next:
    errors.append(f"next_bundle_passes: expected {expected_next}, got {registry.get('next_bundle_passes')}")

completed = {item.get("bundle") for item in registry.get("completed_bundle_passes", [])}
expected_bundle = "fiction/manuscript/part-1/016-020.md"
if expected_bundle not in completed:
    errors.append("016-020 completed bundle pass is absent")

text = (FICTION / "manuscript" / "part-1" / "016-020.md").read_text(encoding="utf-8")
found = {
    int(number): title.strip()
    for number, title in re.findall(r"^## 제(\d+)화 · (.+)$", text, re.MULTILINE)
    if 16 <= int(number) <= 20
}
expected_titles = {
    16: "마시면 돌아갈 수 있다면",
    17: "주안 씨, 정신 차려요",
    18: "지금은 주안이 중요하니까",
    19: "스승이 남긴 질문",
    20: "지도 한 장을 훔치는 시간",
}
if found != expected_titles:
    errors.append(f"current Ch16-20 titles absent: {found}")

if not errors:
    raise SystemExit("RED contract unexpectedly passed before Ch016-020 propagation")

print("Ch016-020 RED contract FAILED as expected before propagation")
for error in errors:
    print(f"- {error}")
raise SystemExit(1)
