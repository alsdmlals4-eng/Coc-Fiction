#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import re
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = [ROOT / "tools" / f"_payload_046_050.part{i:02d}.txt" for i in range(1, 4)]
TARGET = ROOT / "fiction" / "manuscript" / "part-1" / "046-050.md"
EXPECTED_FILE_SHA = "a8e9b44f86b4a8d599aa6ca05f191e82aee9daf9d9c1583fbdc6d6c869e3c7d7"
EXPECTED_ENCODED_LENGTH = 29940
EXPECTED_BODIES = {
    46: (5861, "ae3928bb6234eb4086115c74614d43aee3b436aa52cc30d14641a5673878791d"),
    47: (6229, "ed332a61c44bdac0ca394b5f8f6f24ab75c4d388bc289677768aeaee015c9e6a"),
    48: (5800, "4cd101ebbb686f269ae2efe1e3e40eba11edd75420c3782aa8918f58df8bb41e"),
    49: (5793, "6408f1e4b70b7fdbe43912c5b43c0ce2394d1303a6cbc81f31ea4d0ff9f307be"),
    50: (5296, "5b3bd9bcbb7b3d04deb38dfdb39db2c9fdc56fb50df18ea9425562c9b484880e"),
}
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)


def main() -> None:
    encoded = "".join(path.read_text(encoding="utf-8").strip() for path in PARTS)
    if len(encoded) != EXPECTED_ENCODED_LENGTH:
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
