#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, shutil, subprocess, tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT / ".source-pass"
TARGET = ROOT / "fiction/manuscript/side-story-lake/091-095.md"
START_HERE = ROOT / "[소설]/00_운영체계/START_HERE.md"
CANON_REFRESH_REPORT = ROOT / "fiction/reports/REVISION_2026-07-22_CANON_REFRESH.md"
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

report_text = CANON_REFRESH_REPORT.read_text(encoding="utf-8")
report_text = report_text.replace(
    "# 2026-07-22 최신 정본 복구·개선 보고\n",
    "# 2026-07-22 정본 복구 체크포인트 보고\n\n> 상태: HISTORICAL CHECKPOINT / 현재 작업 상태는 `fiction/ACTIVE_CONTEXT.md`를 따른다.\n",
    1,
)
report_text = report_text.replace(
    "초기 감사에서 별도 `225화 압축 초안`을 현재 원고로 간주했으나, 최신 통합 문서에는 그보다 확장·수정된 225화 전체 원고가 존재했다. 별도 압축 초안을 바탕으로 만든 임시 산출물은 게시 전에 폐기하고 최신 통합 문서에서 전부 재생성했다.",
    "초기 감사에서 당시 별도 구형 압축 원고를 현재 원고로 간주했으나, 최신 통합 문서에는 그보다 확장·수정된 225화 전체 원고가 존재했다. 구형 압축 원고를 바탕으로 만든 임시 산출물은 게시 전에 폐기하고 최신 통합 문서에서 전부 재생성했다.",
    1,
)
report_text = report_text.replace(
    "## 남은 작업\n\n- 제1화~제225화 구조 역개요\n- 원본 PDF/로그 전체 장면 단위 재대조\n- 대표 화 품질 게이트와 POV별 문체 baseline\n- 부 단위 Developmental·Structural·Continuity 패스\n- 전체 Line edit·Copyedit·Proofread\n- 독자 이해·몰입·속도 표본 테스트",
    "## 당시 남은 작업과 현재 상태\n\n- 제1화~제225화 구조 역개요: 완료\n- 대표 화 품질 게이트와 POV별 문체 기준선: 완료\n- 원본 PDF/로그 전체 장면 단위 재대조: 진행 중; `091-095` 원본 직접 대조 완료, `006-010` 재감사와 `176-180` 대조 대기\n- 부 단위 Developmental·Structural·Continuity 패스: 진행 중\n- 전체 Line edit·Copyedit·Proofread: 미완료\n- 독자 이해·몰입·속도 표본 테스트: 미완료",
    1,
)
CANON_REFRESH_REPORT.write_text(report_text.rstrip() + "\n", encoding="utf-8")

shutil.rmtree(TEMP)
print("source pass 091-095 applied")
