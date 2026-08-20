# Coc-Fiction 소설 작업 시작 지점

## 최초 읽기

```text
docs/coordination/CONCURRENT_WORK.md
→ [소설]/00_운영체계/OPERATING_MODEL.md
→ [소설]/00_운영체계/DOCUMENTATION_MAP.md
→ fiction/FICTION_MASTER.md
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json
→ docs/fiction-ops/2026-08-20_WORKING_001_161_CANDIDATE_QA.md
→ 현재 묶음 Scene Card·Revision Report
→ fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md
→ fiction/analysis/REVERSE_OUTLINE_REPORT.md
→ fiction/MANUSCRIPT_INDEX.json
→ fiction/STYLE_GUIDE.md
→ 현재 원고 묶음
```

색인과 역개요의 대형 데이터는 manifest+override로 합성한다. baseline은 직접 작업 입력으로 읽거나 수정하지 않는다.

## 현재 단계

```yaml
work_mode: IMPLEMENT / REVIEW
manuscript_stage: REVISE / PROMOTE_BOUNDED
current_candidate: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_candidate_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
candidate_coverage: 001-161
candidate_qa: QA_GREEN
repository_reconciled_prefix: 001-015
legacy_tail_starts_at: 016
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bundle: fiction/manuscript/part-1/016-020.md
```

## 전체 lifecycle vocabulary

운영체계 라우팅 이름은 축약하지 않는다.

- Work Mode: `PLAN → BUILD → REVIEW`
- Manuscript Stage: `DISCOVER → OUTLINE → DRAFT → REVISE → POLISH`
- 현재는 `BUILD/REVIEW` 안의 bounded promotion과 `REVISE` 단계다.

GitHub의 225화/45묶음 경로는 migration container다. current narrative 최종 numbering은 001–161이며, 저장 225화 토폴로지를 최신 서사 편성으로 재해석하지 않는다.

## 프로젝트 Skill

- `fiction-project-operations`: 범위·계약·체크포인트·인수인계·병합
- `fiction-story-development`: 코어·인과·인물·장면 카드·stress-test
- `fiction-drafting`: 승인된 POV·대화·묘사·리듬 수정
- `fiction-canon-and-research`: 원본 로그·Canon·연표·출처·구형 참조 감사
- `fiction-revision-and-validation`: 구조·묶음 퇴고·연속성·적대적 검토·회귀·PR 검수

Base의 공용 serial-fiction 작법은 재사용하되 작품 Canon과 current candidate authority는 Coc-Fiction 내부 정본이 책임진다.

## 절대 우선순위

최신 사용자 지시 → 작품 코어·Canon Registry → 접근 가능한 원본 사건 기록 → 부별 바이블·연속성 → QA_GREEN current candidate → current GitHub production prefix → 수동 장면 카드·Revision Report → 역개요·진단 → 외부 참고.

## 현재 보호 규칙

- `엘리스`가 Alice Carter의 한국어 정본 표기다.
- 주안: `반응 → 멈춤 → 이유 → 선택`.
- 엘리스 정신 능력: 지배가 아니라 선택 보존.
- 이안: 기록·검증, unknown을 사실로 승격하지 않음.
- D01: bounded external acquisition network; 상위 client/hierarchy 미확정.
- D02: +2h 사진은 fixed future가 아니라 authentic non-current cross-loop evidence.
- D03: 다른 회차 세 시신은 명시적 사건이 바꾸기 전까지 물리적 경찰 증거.
- Elliott sword: 귀속 미정·공동봉인; Jumin 반응/메스 변형은 후계 인증 아님.
- POV: Scene-Locked Hybrid; scene break 없는 head hopping 금지.
- current Ch10 Milly disappearance는 객관적 사망 확정이 아니다.
- current Ch12 Hatem/Milly same-face evidence는 동일인 확정이 아니라 별도 인물 + 얼굴 기원 미스터리다.
- current Ch13–14 Elise arc는 부모의 죄·보호 자아가 엘리스의 선택권을 대신하지 못한다는 규칙을 보호한다.

## current prefix / migration boundary

- `001–015`: current production prefix.
- `005→006`: current continuity `PASS`.
- `010→011`: current continuity `PASS / PARALLEL_FRONT`.
- `015→016`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.
- Ch15 reverse outline: `next_chapter=null`.
- legacy Ch16 reverse outline: `previous_chapter=null`.

current candidate 전체가 Green이어도 GitHub production authority는 5화 단위 검증 없이 자동 확장하지 않는다.

## 다음 시작 묶음

`fiction/manuscript/part-1/016-020.md`

```text
current candidate 016-020 exact extraction
→ Ch15 current 종료 상태와 앞 경계 검증
→ 원본·Canon·사용자 Decision 대조
→ KEEP / APPLY / REWORK / REJECT
→ manuscript/index/reverse-outline/Scene Pass/routers 원자 갱신
→ exact-head Fiction operating-system CI
→ review thread 0 / main freshness 확인
→ squash merge + post-merge readback
→ frontier 20으로 이동
```

기존 deferred source-pass는 `SCENE_PASS_REGISTRY.json`에서 보존하며 bounded migration 순서를 건너뛰지 않는다.

## 금지

- 구 압축본·구 저장 편성을 current source authority로 다시 올리지 않는다.
- 파일명의 `최종`만으로 자동 승격하지 않는다.
- current migration boundary를 정상 next chapter로 가정하지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
- 과거 CI Green을 현재 exact head의 Green으로 재사용하지 않는다.
