#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "tools" / "check_fiction_content.py"
text = TARGET.read_text(encoding="utf-8")
old = '''seen: dict[int, tuple[str, str, str, Path]] = {}
for path in bundles:
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^> 상태: 2,000자 이상 확장 원고 DRAFT\\.", text, re.M):
        errors.append(f"missing expanded DRAFT status: {path.relative_to(ROOT)}")
'''
new = '''seen: dict[int, tuple[str, str, str, Path]] = {}
try:
    scene_pass_registry = json.loads(
        (FICTION / "analysis/SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8")
    )
    completed_bundle_paths = {
        str(item.get("bundle"))
        for item in scene_pass_registry.get("completed_bundle_passes", [])
        if isinstance(item, dict) and item.get("bundle")
    }
except Exception as exc:
    completed_bundle_paths = set()
    errors.append(f"invalid scene-pass registry for manuscript status validation: {exc}")

for path in bundles:
    text = path.read_text(encoding="utf-8")
    relative_path = path.relative_to(ROOT).as_posix()
    if relative_path not in completed_bundle_paths and not re.search(
        r"^> 상태: 2,000자 이상 확장 원고 DRAFT\\.", text, re.M
    ):
        errors.append(f"missing expanded DRAFT status: {path.relative_to(ROOT)}")
'''
if old not in text:
    if "completed_bundle_paths" in text:
        print("frontier-aware manuscript status validation already installed")
        raise SystemExit(0)
    raise SystemExit("target status-validation block not found")
TARGET.write_text(text.replace(old, new), encoding="utf-8")
print("patched check_fiction_content.py to use completed scene-pass ownership")
