#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, json, shutil, subprocess, tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMP = ROOT / ".source-pass"
TARGET = ROOT / "fiction/manuscript/side-story-lake/091-095.md"
START_HERE = ROOT / "[소설]/00_운영체계/START_HERE.md"
CANON_REFRESH_REPORT = ROOT / "fiction/reports/REVISION_2026-07-22_CANON_REFRESH.md"
OUTLINE_REPORT = ROOT / "fiction/analysis/REVERSE_OUTLINE_REPORT.md"
OUTLINE_OVERRIDE = ROOT / "fiction/analysis/REVERSE_OUTLINE_OVERRIDE_091_095.json"
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

extracted_files: list[Path] = []
with tarfile.open(archive, "r:gz") as tf:
    for member in tf.getmembers():
        dest = (ROOT / member.name).resolve()
        if ROOT.resolve() not in dest.parents and dest != ROOT.resolve():
            raise SystemExit(f"unsafe archive path: {member.name}")
        if member.isfile():
            extracted_files.append(ROOT / member.name)
    tf.extractall(ROOT)

for path in extracted_files:
    if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml"}:
        continue
    text = path.read_text(encoding="utf-8")
    normalized = "\n".join(line.rstrip(" \t") for line in text.splitlines()) + "\n"
    path.write_text(normalized, encoding="utf-8")

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

outline_report_text = OUTLINE_REPORT.read_text(encoding="utf-8")
if "## 4. 부·외전별 정량 기준선" not in outline_report_text:
    outline_report_text = outline_report_text.rstrip() + """

## 4. 부·외전별 정량 기준선

- 1부 70화, 외전1 25화, 외전2 35화, 외전3 35화, 2부 60화의 총 225화를 유지한다.
- 45개 원고 묶음과 모든 화 2,000자 이상 조건은 합성 색인과 현재 원고를 함께 검사한다.
- 정량 플래그는 검토 우선순위이며 자동 수정 명령이 아니다.

## 5. 전체 구조 지도

- 1부: 출항과 선상 재난에서 섬의 규칙·세력 충돌·쇼거스전·복종인자 폭로·주안 이탈까지.
- 외전1: 주안의 답 탐색과 티베트 문답, 한국 정착, 엘리스의 생존 확인, 다빈·예나의 다음 이야기 예고까지.
- 외전2·외전3: 엘리스와 이안의 독립 성장 및 2부 연결.
- 2부: 다빈·주민·엘리스가 정해진 안전보다 선택 가능한 미래를 되찾는 과정.

## 6. Finding-first 판정

- `MUST_FIX`: 원본 종결을 대체한 제91~95화의 비정본 결말 구조를 원본 핵심 사건으로 복원했다.
- `SHOULD_FIX`: 제95화의 제한적 3인칭 밖 인물 상태 서술을 다빈 관찰 범위로 제한했다.
- `REJECT`: 사용자 지시로 폐기된 인물 후일담·독립 동물 서사·장기 조직축은 원본에 있어도 복원하지 않았다.
- 제90·96화 원고는 수정하지 않고 역개요의 앞뒤 화 메타데이터만 제90~96화 경계까지 갱신했다.

## 9. 다음 정확한 작업

`fiction/manuscript/part-2/176-180.md`를 제175·181화 경계와 원본 2부 로그에 직접 대조한다. `006-010`은 원본 1부 로그 재감사 대기로 유지한다.
"""
OUTLINE_REPORT.write_text(outline_report_text.rstrip() + "\n", encoding="utf-8")

generated_path = TEMP / "generated-reverse-outline.json"
subprocess.run(
    ["python", "tools/build_fiction_reverse_outline.py", "--materialize", str(generated_path)],
    cwd=ROOT,
    check=True,
)
generated = json.loads(generated_path.read_text(encoding="utf-8"))
chapters = [item for item in generated.get("chapters", []) if 90 <= int(item.get("chapter", 0)) <= 96]
if [int(item["chapter"]) for item in chapters] != [90, 91, 92, 93, 94, 95, 96]:
    raise SystemExit("generated reverse-outline override and boundary entries are incomplete")
OUTLINE_OVERRIDE.write_text(
    json.dumps(
        {
            "schema_version": 1,
            "updated_at": "2026-07-23",
            "status": "ACTIVE_OVERRIDE / SOURCE_PASS_091_095 / BOUNDARIES_090_096 / DETERMINISTIC_GENERATOR",
            "baseline": "analysis/baselines/REVERSE_OUTLINE_2026-07-23_PILOT.json",
            "chapters": chapters,
        },
        ensure_ascii=False,
        indent=2,
    ) + "\n",
    encoding="utf-8",
)

shutil.rmtree(TEMP)
print("source pass 091-095 applied")
