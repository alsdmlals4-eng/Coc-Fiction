# Coc-Fiction 소설 작업 시작 지점

## 최초 읽기

```text
docs/coordination/CONCURRENT_WORK.md
→ [소설]/00_운영체계/OPERATING_MODEL.md
→ fiction/FICTION_MASTER.md
→ docs/fiction-ops/CURRENT_STATE_RECEIPT.json
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json
→ docs/fiction-ops/2026-08-20_WORKING_001_161_CANDIDATE_QA.md
→ 현재 묶음 Scene Card·Revision Report
→ fiction/analysis/REVERSE_OUTLINE_REPORT.md
→ fiction/MANUSCRIPT_INDEX.json
→ fiction/STYLE_GUIDE.md
→ 현재 원고 묶음
```

`CURRENT_STATE_RECEIPT.json`의 SHA/PR은 production frontier가 마지막으로 바뀐 증거다. 저장소 최신값을 고정하는 포인터가 아니므로 실제 작업 전 최신 `main`과 open PR을 다시 조회한다.

색인과 역개요는 immutable baseline + 승인 bundle override를 합성한다. baseline을 직접 수정하지 않는다.

## 현재 단계

```yaml
work_mode: IMPLEMENT / REVIEW
manuscript_stage: REVISE / PROMOTE_BOUNDED
current_candidate: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_candidate_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
candidate_coverage: 001-161
candidate_qa: QA_GREEN
repository_reconciled_prefix: 001-020
legacy_tail_starts_at: 021
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bundle: fiction/manuscript/part-1/021-025.md
```

## lifecycle vocabulary

- Work Mode: `PLAN → BUILD → REVIEW`
- Manuscript Stage: `DISCOVER → OUTLINE → DRAFT → REVISE → POLISH`
- 현재는 BUILD/REVIEW 안의 bounded promotion + REVISE 단계다.

GitHub 225화/45묶음 경로는 migration container이며 current narrative 최종 numbering은 001–161이다.

## 현재 보호 규칙

- Alice Carter 한국어 정본은 `엘리스`.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise 정신 능력: 지배가 아니라 선택 보존.
- Ian: 기록·검증, unknown을 사실로 승격하지 않음.
- D01: bounded external acquisition network.
- D02: +2h 사진은 fixed future가 아닌 authentic non-current cross-loop evidence.
- D03: 다른 회차 세 시신은 명시적 사건이 바꾸기 전까지 물리적 경찰 증거.
- Elliott sword: 귀속 미정·공동봉인; 반응/형상변화는 후계 인증 아님.
- POV: Scene-Locked Hybrid; scene break 없는 head hopping 금지.

## current prefix / migration boundary

- `001–020`: current production prefix.
- `005→006`, `010→011`, `015→016`: current continuity PASS.
- `020→021`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.
- Ch20 reverse outline: `next_chapter=null`.
- legacy Ch21 reverse outline: `previous_chapter=null`.

current candidate 전체가 Green이어도 GitHub production authority는 5화 단위 Green 없이 자동 확장하지 않는다.

## 다음 시작 묶음

`fiction/manuscript/part-1/021-025.md`

```text
current candidate Ch21-25 exact extraction
→ Ch20 current 종료 상태와 앞 경계 검증
→ 원본·Canon·사용자 Decision 대조
→ KEEP / APPLY / REWORK / REJECT
→ manuscript/index/reverse-outline/Scene Pass/routers 원자 갱신
→ exact-head Fiction operating-system CI
→ review thread 0 / main freshness
→ squash merge + post-merge readback
```

## 금지

- 구 저장 편성을 current source authority로 되돌리지 않는다.
- 파일명의 `최종`만으로 자동 승격하지 않는다.
- migration boundary를 정상 next chapter로 가정하지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
- 과거 CI Green을 current exact head Green으로 재사용하지 않는다.
