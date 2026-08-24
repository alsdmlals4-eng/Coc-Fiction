#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "fiction" / "analysis" / "REVERSE_OUTLINE_OVERRIDE_006_010.json"

data = json.loads(PATH.read_text(encoding="utf-8"))
found = False
for item in data.get("chapters", []):
    if int(item.get("chapter", 0)) == 8:
        flags = list(item.get("structural_flags", []))
        item["structural_flags"] = [flag for flag in flags if flag != "ONE_OFF_POV"]
        found = True
        break
if not found:
    raise SystemExit("Ch8 reverse-outline override missing")
PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("normalized current-authority Ch8 reverse-outline metadata")
