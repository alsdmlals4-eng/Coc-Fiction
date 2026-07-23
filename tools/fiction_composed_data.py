#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _compose(manifest_path: Path, *, baseline_key: str = "baseline") -> dict[str, Any]:
    manifest = _load(manifest_path)
    if "chapters" in manifest:
        return manifest
    base_path = manifest_path.parent / manifest[baseline_key]
    base = _load(base_path)
    by_chapter = {int(item["chapter"]): item for item in base.get("chapters", [])}
    seen_override_chapters: set[int] = set()
    for rel in manifest.get("overrides", []):
        override = _load(manifest_path.parent / rel)
        for item in override.get("chapters", []):
            number = int(item["chapter"])
            if number in seen_override_chapters:
                raise ValueError(f"duplicate chapter across overrides: {number}")
            seen_override_chapters.add(number)
            by_chapter[number] = item
    result = dict(base)
    result["schema_version"] = manifest.get("schema_version", result.get("schema_version", 1))
    result["generated_at"] = manifest.get("generated_at", result.get("generated_at"))
    result["status"] = manifest.get("status", result.get("status"))
    result["chapters"] = [by_chapter[n] for n in sorted(by_chapter)]
    result["composition"] = {
        "manifest": manifest_path.as_posix(),
        "baseline": manifest[baseline_key],
        "overrides": manifest.get("overrides", []),
    }
    return result


def load_manuscript_index(fiction_root: Path) -> dict[str, Any]:
    return _compose(fiction_root / "MANUSCRIPT_INDEX.json")


def load_reverse_outline(fiction_root: Path) -> dict[str, Any]:
    return _compose(fiction_root / "analysis" / "REVERSE_OUTLINE_001_225.json")
