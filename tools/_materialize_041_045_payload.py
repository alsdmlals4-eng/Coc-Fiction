#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import re
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = [ROOT / "tools" / f"_payload_041_045.part{i:02d}.txt" for i in range(1, 9)]
TARGET = ROOT / "fiction" / "manuscript" / "part-1" / "041-045.md"
EXPECTED_ENCODED_LEN = 30536
EXPECTED_FILE_SHA = "cfec9e5149e067413b793e87ab3ccd02a77f2cf725e9b82f6f4f2fb30fd6ecb9"
EXPECTED_BODIES = {
    41: (4255, "3879d479bec2458e7da2afd78a9c6cc748c9a20e5c0be935d9de365ea05f942a"),
    42: (6012, "e48ad4266831cc8b74ececc7e7fb6f831012a0464005e61eb06fb369d0945a2f"),
    43: (7004, "7da555457ebd2debd70fafb41283f9973440d0e99ef098c3c4acc3ba200baaac"),
    44: (6720, "6c885ee543a45f145e7d920f7fbb89b5ebb280bf1d4c891a2b671b3c428122dd"),
    45: (5876, "e73c81689638476f6736cd9361cdd22dc9e80a076822162856b7516e3a7c12a1"),
}
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)


def main() -> None:
    missing = [str(p) for p in PARTS if not p.is_file()]
    if missing:
        raise SystemExit(f"missing payload parts: {missing}")
    encoded = "".join(p.read_text(encoding="utf-8").strip() for p in PARTS)
    if len(encoded) != EXPECTED_ENCODED_LEN:
        raise SystemExit(f"payload length mismatch: {len(encoded)}")
    data = zlib.decompress(base64.b64decode(encoded))
    file_sha = hashlib.sha256(data).hexdigest()
    if file_sha != EXPECTED_FILE_SHA:
        raise SystemExit(f"materialized file SHA mismatch: {file_sha}")
    text = data.decode("utf-8")
    parsed = {int(m.group(1)): m.group(4).strip() for m in CHAPTER_RE.finditer(text)}
    if sorted(parsed) != list(EXPECTED_BODIES):
        raise SystemExit(f"chapter set mismatch: {sorted(parsed)}")
    for number, (chars, sha) in EXPECTED_BODIES.items():
        body = parsed[number]
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if len(body) != chars or actual != sha:
            raise SystemExit(f"chapter {number} mismatch chars={len(body)} sha={actual}")
    TARGET.write_bytes(data)
    print(f"materialized {TARGET.relative_to(ROOT)} bytes={len(data)} sha256={file_sha}")


if __name__ == "__main__":
    main()
