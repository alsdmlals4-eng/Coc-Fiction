#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_CHARS = '47: {"title":"호수가 보이는 마을","pov":"이안 → 주안 → 이안","chars":6229,"sha":"ed332a61c44bdac0ca394b5f8f6f24ab75c4d388bc289677768aeaee015c9e6a"}'
NEW_CHARS = '47: {"title":"호수가 보이는 마을","pov":"이안 → 주안 → 이안","chars":6228,"sha":"03e0e7c4fcbfedd4326f335bdc5f49b79fbaf3acc2c1ceaa8e56fa91c8bc6a83"}'

for rel in ("tools/_patch_046_050_consumers.py", "tests/test_promote_046_050_contract.py"):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    if NEW_CHARS not in text:
        if OLD_CHARS not in text:
            raise SystemExit(f"expected Ch47 receipt marker missing: {rel}")
        text = text.replace(OLD_CHARS, NEW_CHARS, 1)
    if rel.startswith("tests/"):
        text = text.replace(
            "def test_exact_user_designated_bridge_bodies_are_installed(self):",
            "def test_user_designated_bridge_bodies_are_canon_reconciled_and_installed(self):",
            1,
        )
    else:
        text = text.replace(
            "- exact-transfer chapters: 46–50\\n",
            "- source-derived chapters: 46–50\\n- Ch47 canon-directed reconciliation: source body `ed332a61c44bdac0ca394b5f8f6f24ab75c4d388bc289677768aeaee015c9e6a` → production body `03e0e7c4fcbfedd4326f335bdc5f49b79fbaf3acc2c1ceaa8e56fa91c8bc6a83`; deprecated contact-axis label replaced by generic old external contact wording; event/information function unchanged.\\n",
            1,
        )
    path.write_text(text, encoding="utf-8")

print("updated Ch047 canon-reconciled production receipts")
