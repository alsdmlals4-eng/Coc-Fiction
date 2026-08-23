#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import re
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = [ROOT / "tools" / f"_payload_031_035.part{i:02d}.txt" for i in range(1, 10)]
TARGET = ROOT / "fiction" / "manuscript" / "part-1" / "031-035.md"
EXPECTED_FILE_SHA = "e6701ad7f05623c90c854785fa2a53a3733c811c051a7b7b27a54a565d8a60e0"
EXPECTED_BODIES = {
    31: (10305, "c24a4c8b236e12b54825c44c810a96588e4b1360b02f8e8a9f4df5d26fd20353"),
    32: (6291, "e55613d4b68fd0d6222a680d3eba1d0416033504322fc9aaae6cf09a9cdc6bce"),
    33: (5933, "a6042d9b3c6dc9b82e603c2088a45d9a2f09b974ff224d0a3de618eb5c1d4cec"),
    34: (5935, "ffbe4a8459f972bcdae6f9fa27416c63a64efb900c19006348d7718c9c20286d"),
    35: (6194, "c4b02af3eb326dfd18ec0331c762c92655cb97525b8b3223d407e69ce912d5f2"),
}
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)


def main() -> None:
    sizes = [path.stat().st_size for path in PARTS]
    expected_sizes = [4000] * 8 + [1760]
    if sizes != expected_sizes:
        raise SystemExit(f"payload sizes mismatch: {sizes}")
    encoded = "".join(path.read_text(encoding="utf-8") for path in PARTS)
    if len(encoded) != 33760:
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
