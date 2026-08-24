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
EXPECTED_SOURCE_FILE_SHA = "a8e9b44f86b4a8d599aa6ca05f191e82aee9daf9d9c1583fbdc6d6c869e3c7d7"
EXPECTED_PRODUCTION_FILE_SHA = "51a11403634bcf9e5f68868c0441f9573ace9b79bc09b0365660781c6124ac32"
EXPECTED_ENCODED_LENGTH = 29940
EXPECTED_PART_LENGTHS = [10000, 10000, 9940]
SOURCE_BODIES = {
    46: (5861, "ae3928bb6234eb4086115c74614d43aee3b436aa52cc30d14641a5673878791d"),
    47: (6229, "ed332a61c44bdac0ca394b5f8f6f24ab75c4d388bc289677768aeaee015c9e6a"),
    48: (5800, "4cd101ebbb686f269ae2efe1e3e40eba11edd75420c3782aa8918f58df8bb41e"),
    49: (5793, "6408f1e4b70b7fdbe43912c5b43c0ce2394d1303a6cbc81f31ea4d0ff9f307be"),
    50: (5296, "5b3bd9bcbb7b3d04deb38dfdb39db2c9fdc56fb50df18ea9425562c9b484880e"),
}
PRODUCTION_BODIES = dict(SOURCE_BODIES)
PRODUCTION_BODIES[47] = (6228, "03e0e7c4fcbfedd4326f335bdc5f49b79fbaf3acc2c1ceaa8e56fa91c8bc6a83")
CANON_OLD = "쵸르브라트 쪽 연락책"
CANON_NEW = "오래된 외부 연락책"
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)


def parse(text: str) -> dict[int, str]:
    return {int(m.group(1)): m.group(4).strip() for m in CHAPTER_RE.finditer(text)}


def verify_bodies(text: str, expected: dict[int, tuple[int, str]], label: str) -> None:
    parsed = parse(text)
    if sorted(parsed) != list(expected):
        raise SystemExit(f"{label} chapter set mismatch: {sorted(parsed)}")
    for number, (chars, sha) in expected.items():
        body = parsed[number]
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if len(body) != chars or actual != sha:
            raise SystemExit(f"{label} chapter {number} mismatch chars={len(body)} sha={actual}")


def main() -> None:
    chunks = [path.read_text(encoding="utf-8").strip() for path in PARTS]
    raw_lengths = [len(chunk) for chunk in chunks]
    if raw_lengths == [10003, 10000, 9940] and chunks[0].endswith("w=="):
        chunks[0] = chunks[0][:-3]
    lengths = [len(chunk) for chunk in chunks]
    print(f"payload part lengths raw={raw_lengths} normalized={lengths}; expected={EXPECTED_PART_LENGTHS}")
    if lengths != EXPECTED_PART_LENGTHS:
        raise SystemExit(f"payload part length mismatch after normalization: {lengths}")
    encoded = "".join(chunks)
    if len(encoded) != EXPECTED_ENCODED_LENGTH:
        raise SystemExit(f"payload length mismatch: {len(encoded)}")

    source_data = zlib.decompress(base64.b64decode(encoded))
    source_file_sha = hashlib.sha256(source_data).hexdigest()
    if source_file_sha != EXPECTED_SOURCE_FILE_SHA:
        raise SystemExit(f"source materialized file SHA mismatch: {source_file_sha}")
    source_text = source_data.decode("utf-8")
    verify_bodies(source_text, SOURCE_BODIES, "source")

    if source_text.count(CANON_OLD) != 1:
        raise SystemExit(f"expected exactly one canon-reconciliation target, got {source_text.count(CANON_OLD)}")
    production_text = source_text.replace(CANON_OLD, CANON_NEW, 1)
    if CANON_OLD in production_text:
        raise SystemExit("superseded contact-axis label remains after reconciliation")
    production_data = production_text.encode("utf-8")
    production_file_sha = hashlib.sha256(production_data).hexdigest()
    if production_file_sha != EXPECTED_PRODUCTION_FILE_SHA:
        raise SystemExit(f"production reconciled file SHA mismatch: {production_file_sha}")
    verify_bodies(production_text, PRODUCTION_BODIES, "production")

    TARGET.write_bytes(production_data)
    print(
        f"materialized {TARGET.relative_to(ROOT)} source_sha={source_file_sha} "
        f"production_sha={production_file_sha} canon_reconciliation=1"
    )


if __name__ == "__main__":
    main()
