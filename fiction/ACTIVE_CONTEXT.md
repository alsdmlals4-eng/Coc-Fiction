# ACTIVE CONTEXT

갱신: 2026-08-21

## Resume-first

이 문서는 live router다. 저장된 SHA를 절대 최신값으로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
work_mode: IMPLEMENT / REVIEW
frontier_observed_at_main: null
last_frontier_change_pr: 39
pending_frontier_change_pr: 42
current_state_receipt: docs/fiction-ops/CURRENT_STATE_RECEIPT.json
current_candidate: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_candidate_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
delivery_state: QA_VERIFIED
candidate_state: QA_GREEN
repository_promotion_state: PARTIAL
reconciled_prefix_end: 25
legacy_tail_starts_at: 26
boundary_after_chapter: 25
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/026-030.md
```

`frontier_observed_at_main`과 `last_frontier_change_pr`은 **현재 production frontier의 마지막 merged 증거**다. 저장소의 영구적인 최신 SHA/PR을 의미하지 않으며, 재개 시 GitHub에서 최신 `main`과 open PR을 다시 조회한다.

새 세션 첫 행동:

`latest main → open PR → AGENTS → CURRENT_STATE_RECEIPT → ACTIVE_CONTEXT → CANON_REGISTRY → SCENE_PASS_REGISTRY → candidate manifest/QA → next bundle`

## Artifact-promotion gate

```yaml
states:
  delivery_state: DRAFT | QA_VERIFIED | DELIVERED
  repository_promotion_state: NOT_REQUIRED | PENDING | PARTIAL | PROMOTED
rule: delivery_state와 repository_promotion_state를 서로 자동 승격하지 않는다.
```

QA_GREEN current candidate 전체가 있어도 GitHub production authority는 bounded Green pass를 통과한 범위까지만 확장한다.

## Completed implementation milestones

- PR #29: Canon reconciliation.
- PR #30: exact 17-file candidate manifest.
- PR #31: QA_GREEN integrated candidate evidence.
- PR #32: Ch006–010 bounded production promotion.
- PR #36: Ch011–015 bounded production promotion.
- **PR #39: Ch016–020 bounded production promotion merged; current repository prefix is 001–020.**

## Current prefix 001–025 contract

- Ch5→6, Ch10→11, Ch15→16: current continuity.
- Ch16: 위험한 해결책도 당사자 선택 없이 강행하지 않는다.
- Ch17: 주안의 반응성과 신체 회복은 복종·소유의 증거가 아니다.
- Ch18: 정보·힘 제공과 결정 대행을 분리한다.
- Ch19: 하템과 밀리는 별도 인물이며 같은 얼굴만으로 동일인 결론을 내리지 않는다.
- Ch19 Ian: `관찰 → 가설 → 검증 → 기록`; unknown은 unknown으로 남긴다.
- Ch20: 지도 확보 성공과 잠입 실패를 동시에 기록한다.
- Ch21: 모르는 마법·기억은 `확인`으로 남기고, 뛰어들지 않는 선택을 지킨다.
- Ch22: 정찰/추적 회피에서 주안의 제동을 자기 선택으로 유지한다.
- Ch23: 구출 행동과 설명되지 않은 신체 반응을 구별하고 접촉 전 기다린다.
- Ch24: `반응 → 멈춤 → 이유 → 선택`을 팀 전술로 실행한다.
- Ch25: 실제 위험만 막고 엘리스에게 `갈 겁니까?`라고 선택을 묻는다.

## Current migration boundary

```yaml
left_current: 25
right_legacy: 26
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

Ch20→21 current continuity는 PASS다. 저장 화수가 인접하다는 이유만으로 current Ch25→legacy Ch26 연속성을 주장하지 않는다.

## Canon protection

- central question: 보호·사랑·선의가 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 정신 능력은 지배가 아니라 선택 보존.
- Ian: observation → hypothesis → verification → record.
- Dabin: 자신의 몸과 미래를 선택할 권리.
- Jumin: 최적화보다 당사자 동의 우선.
- Elliott: 타인의 미래를 대신 고정하려는 비극적 반례.
- D01: bounded external acquisition network; 최상위 client/hierarchy unresolved.
- D02: +2h 사진은 fixed future가 아닌 authentic non-current cross-loop evidence.
- D03: 다른 회차 세 시신은 명시적 사건 전까지 물리적 경찰 증거.
- Elliott sword: 귀속 미정 / joint seal; 반응·형상변화는 후계 인증이 아니다.
- Alice Carter 한국어 정본: `엘리스`.
- POV: Scene-Locked Hybrid; scene break 없는 head-hopping 금지.

## Promotion gate

각 5화 묶음마다:
1. locked QA_GREEN candidate에서 exact 추출
2. 앞 경계 검증
3. manuscript + index + reverse outline + scene cards + registry + routers + validators 동시 갱신
4. exact-head Fiction operating-system CI Green
5. unresolved review thread 0
6. main freshness 확인
7. squash merge
8. post-merge main readback + Notion sync

## Next exact work

`fiction/manuscript/part-1/026-030.md`

다음 pass는 **Ch25→26 migration boundary**에서 시작한다. `176-180` deferred source audit은 bounded migration 순서를 건너뛰는 근거가 아니다.

## Base / shared governance

- Base adoption pin은 별도 감사 없이 자동 상승시키지 않는다.
- 다른 workstream의 open/draft/ready PR은 수정하지 않는다.
