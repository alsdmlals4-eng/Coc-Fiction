#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "fiction" / "HANDOFF.md"
LINE = "- **PR #59: Bridge Ch046–050 user-source bounded promotion merged.**"
text = PATH.read_text(encoding="utf-8")
while f"{LINE}\n{LINE}" in text:
    text = text.replace(f"{LINE}\n{LINE}", LINE, 1)
PATH.write_text(text, encoding="utf-8")
print("normalized PR59 HANDOFF milestone")
