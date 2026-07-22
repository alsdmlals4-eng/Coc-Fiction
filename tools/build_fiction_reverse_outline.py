#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

from fiction_composed_data import load_manuscript_index, load_reverse_outline
from reverse_outline_generator_base import build


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
        return build(temp_root)


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
    if effective.get("chapters") != generated.get("chapters"):
        raise SystemExit("reverse outline composition is stale; update the bundle override")
    print("Reverse outline reproducibility PASSED (225 composed chapters)")


if __name__ == "__main__":
    main()
