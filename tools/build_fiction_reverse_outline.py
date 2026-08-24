#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

from fiction_composed_data import load_manuscript_index, load_reverse_outline
from reverse_outline_generator_base import build


def _load_registry(root: Path) -> dict:
    path = root / "fiction" / "analysis" / "SCENE_PASS_REGISTRY.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def apply_reconciliation_boundary(root: Path, generated: dict) -> dict:
    registry = _load_registry(root)
    reconciliation = registry.get("external_artifact_reconciliation", {})
    if reconciliation.get("whole_manuscript_continuity") != "NOT_YET_CLAIMED":
        return generated
    boundary = reconciliation.get("boundary_after_chapter")
    if not isinstance(boundary, int):
        return generated

    by_chapter = {int(item["chapter"]): item for item in generated.get("chapters", [])}
    left = by_chapter.get(boundary)
    right = by_chapter.get(boundary + 1)
    if left:
        left["next_chapter"] = None
        flags = list(left.get("structural_flags", []))
        if "RECONCILIATION_MIGRATION_BOUNDARY" not in flags:
            flags.append("RECONCILIATION_MIGRATION_BOUNDARY")
        left["structural_flags"] = flags
        left.setdefault("evidence", {})["next_pressure"] = (
            f"정본 마이그레이션 경계. 저장소 제{boundary + 1}화 이후는 아직 legacy tail이며 "
            f"현재 제{boundary}화와의 서사 연속성을 주장하지 않는다."
        )
    if right:
        right["previous_chapter"] = None
        flags = list(right.get("structural_flags", []))
        if "LEGACY_TAIL_BOUNDARY" not in flags:
            flags.append("LEGACY_TAIL_BOUNDARY")
        right["structural_flags"] = flags
    return generated


def build_current(root: Path) -> dict:
    with tempfile.TemporaryDirectory(prefix="fiction-outline-") as tmp:
        temp_root = Path(tmp)
        fiction = temp_root / "fiction"
        fiction.mkdir(parents=True)
        (fiction / "MANUSCRIPT_INDEX.json").write_text(
            json.dumps(load_manuscript_index(root / "fiction"), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        os.symlink(root / "fiction" / "manuscript", fiction / "manuscript", target_is_directory=True)
        generated = build(temp_root)
        return apply_reconciliation_boundary(root, generated)


def strict_reproducibility_chapters(root: Path) -> set[int]:
    """Return chapters whose analysis is current authority and must reproduce exactly.

    The storage manuscript intentionally contains a legacy tail during mixed migration. Requiring
    current-generator metadata to match every unreconciled legacy chapter makes that storage tail
    behave like production authority. Strict reproducibility therefore covers the sequential current
    frontier plus any separately completed source passes (for example the verified 091–095 pass).
    """
    registry = _load_registry(root)
    reconciliation = registry.get("external_artifact_reconciliation", {})
    frontier = reconciliation.get("reconciled_prefix_end")
    if not isinstance(frontier, int):
        return set(range(1, 226))

    strict = set(range(1, frontier + 1))
    for item in registry.get("completed_bundle_passes", []):
        for raw in item.get("chapters", []):
            try:
                strict.add(int(raw))
            except (TypeError, ValueError):
                continue
    return strict


def _report_diff(effective: dict, generated: dict, chapters: set[int]) -> None:
    by_e = {int(item["chapter"]): item for item in effective.get("chapters", [])}
    by_g = {int(item["chapter"]): item for item in generated.get("chapters", [])}
    changed: list[int] = []
    for number in sorted(chapters):
        e = by_e.get(number)
        g = by_g.get(number)
        if e == g:
            continue
        changed.append(number)
        e = e or {}
        g = g or {}
        keys = [key for key in sorted(set(e) | set(g)) if e.get(key) != g.get(key)]
        print(f"reverse-outline diff chapter {number}: {keys}")
        for key in keys[:6]:
            print(f"  effective[{key!r}]={e.get(key)!r}")
            print(f"  generated[{key!r}]={g.get(key)!r}")
    print(f"reverse-outline changed strict chapters: {changed}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--materialize")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    generated = build_current(root)
    if args.materialize:
        out = root / args.materialize
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(generated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote materialized reverse outline: {out}")
        return
    if not args.check:
        raise SystemExit("use --check or --materialize PATH; active data is maintained by baseline plus bundle overrides")

    effective = load_reverse_outline(root / "fiction")
    by_e = {int(item["chapter"]): item for item in effective.get("chapters", [])}
    by_g = {int(item["chapter"]): item for item in generated.get("chapters", [])}
    if set(by_e) != set(range(1, 226)) or set(by_g) != set(range(1, 226)):
        raise SystemExit("reverse outline must contain storage chapters 1-225 exactly once")

    strict = strict_reproducibility_chapters(root)
    changed = {number for number in strict if by_e.get(number) != by_g.get(number)}
    if changed:
        _report_diff(effective, generated, strict)
        raise SystemExit("reverse outline current-authority composition is stale; update the completed bundle override")
    print(
        f"Reverse outline reproducibility PASSED "
        f"(strict current-authority chapters={len(strict)}, storage chapters=225)"
    )


if __name__ == "__main__":
    main()
