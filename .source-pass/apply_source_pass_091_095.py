#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, shutil, subprocess, tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT / ".source-pass"
TARGET = ROOT / "fiction/manuscript/side-story-lake/091-095.md"
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

shutil.rmtree(TEMP)
print("source pass 091-095 applied")
