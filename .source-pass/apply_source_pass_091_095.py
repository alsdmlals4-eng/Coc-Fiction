#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, shutil, subprocess, tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT / ".source-pass"
TARGET = ROOT / "fiction/manuscript/side-story-lake/091-095.md"
START_HERE = ROOT / "[소설]/00_운영체계/START_HERE.md"
EXPECTED_GIT_BLOB = "d3fbb8f0906d36b0016266139cd636fb31f7cfed"

actual_blob = subprocess.check_output(["git", "hash-object", str(TARGET)], cwd=ROOT, text=True).strip()
if actual_blob != EXPECTED_GIT_BLOB:
    raise SystemExit(f"precondition failed for 091-095.md: {actual_blob}")

chunks = sorted(TEMP.glob("part-*"))
if not chunks:
    raise SystemExit("source-pass chunks missing")
payload = "".join(p.read_text(encoding="ascii") for p in chunks)
archive = TEMP / "patch.tar.gz"
raw = base64.b64decode(payload)
expected_archive_sha = "1a497b199dca717ecbbbbbaf5f6f51dd939c6e6b15b035b3aa5dd065ca958632"
actual_archive_sha = hashlib.sha256(raw).hexdigest()
if actual_archive_sha != expected_archive_sha:
    raise SystemExit(f"archive SHA mismatch: {actual_archive_sha}")
archive.write_bytes(raw)

with tarfile.open(archive, "r:gz") as tf:
    for member in tf.getmembers():
        dest = (ROOT / member.name).resolve()
        if ROOT.resolve() not in dest.parents and dest != ROOT.resolve():
            raise SystemExit(f"unsafe archive path: {member.name}")
    tf.extractall(ROOT)

start_text = START_HERE.read_text(encoding="utf-8")
if "## 작업 단계 지도" not in start_text:
    start_text = start_text.rstrip() + """

## 작업 단계 지도

- Work Mode: `PLAN → BUILD → REVIEW`
- Manuscript Stage: `DISCOVER → OUTLINE → DRAFT → REVISE → POLISH`
- 현재 단계는 `REVIEW / REVISE`이며, 다음 묶음도 계획·원본 대조·승인된 수정·회귀 검증 순서를 생략하지 않는다.
"""
    START_HERE.write_text(start_text.rstrip() + "\n", encoding="utf-8")

shutil.rmtree(TEMP)
print("source pass 091-095 applied")
