#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, re, zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = [ROOT / "tools" / f"_payload_036_040.part{i:02d}.txt" for i in range(1, 5)]
TARGET = ROOT / "fiction" / "manuscript" / "part-1" / "036-040.md"
EXPECTED_FILE_SHA = "dbbe2faaa6c03373b2251bb7c0ad85c4595febe39253cfa4f6efd8c03d869398"
EXPECTED_BODIES = {
    36: (6242, "a73ee6d8d4f99ab24e7604ae891b58da420ce5549777395c262da69ea340b358"),
    37: (5872, "53604e0ca6bcddd2beebb996aeb102ff7417a645c31e3340880bc451da8dc3e8"),
    38: (5821, "c8a9f4a4c867009b73e11257af21bf6050e5b146e4d9c2dc3ffed34d541186d5"),
    39: (6163, "8ad77ac006e209745a56b4cbba6d3ba26f7a5a55fa75ff00a8dd2efe39955472"),
    40: (6237, "1de35b4f4ecb19706f05bac827ed916484f59a2e167a0d4277012696cd1d9f19"),
}
CHAPTER_RE = re.compile(r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)", re.M | re.S)

def main() -> None:
    encoded = "".join(path.read_text(encoding="utf-8") for path in PARTS)
    data = zlib.decompress(base64.b64decode(encoded))
    actual_file_sha = hashlib.sha256(data).hexdigest()
    if actual_file_sha != EXPECTED_FILE_SHA:
        raise SystemExit(f"materialized file SHA mismatch: {actual_file_sha}")
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
    print(f"materialized {TARGET.relative_to(ROOT)} bytes={len(data)} sha256={actual_file_sha}")

if __name__ == "__main__":
    main()
