#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from tools.build_fiction_reverse_outline import build_current
from tools.fiction_composed_data import load_reverse_outline

ROOT = Path(__file__).resolve().parents[1]
effective = load_reverse_outline(ROOT / "fiction")
generated = build_current(ROOT)
by_e = {int(x["chapter"]): x for x in effective.get("chapters", [])}
by_g = {int(x["chapter"]): x for x in generated.get("chapters", [])}
changed = []
for n in sorted(set(by_e) | set(by_g)):
    if by_e.get(n) != by_g.get(n):
        changed.append(n)
        e = by_e.get(n, {})
        g = by_g.get(n, {})
        keys = sorted(set(e) | set(g))
        diffs = [k for k in keys if e.get(k) != g.get(k)]
        print(f"CH{n} DIFF KEYS: {diffs}")
        for key in diffs[:8]:
            print(f"  {key}: EFFECTIVE={e.get(key)!r}")
            print(f"  {key}: GENERATED={g.get(key)!r}")
print(f"CHANGED_CHAPTERS={changed}")
raise SystemExit(1 if changed else 0)
