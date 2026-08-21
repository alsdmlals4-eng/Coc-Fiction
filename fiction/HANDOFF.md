# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-22

## Resume-first

이 문서는 재개용 live router다. 저장된 SHA를 절대 최신값으로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
frontier_observed_at_main: e6817e38042c783be8169f6c385230e75f1253db
last_frontier_change_pr: 42
current_state_receipt: docs/fiction-ops/CURRENT_STATE_RECEIPT.json
delivery_state: QA_VERIFIED
repository_promotion_state: PARTIAL
current_candidate: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_candidate_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
reconciled_prefix_end: 25
legacy_tail_starts_at: 26
boundary_after_chapter: 25
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/026-030.md
```

`frontier_observed_at_main`과 `last_frontier_change_pr`은 마지막 **production frontier 변경**을 가리킨다. 이 handoff가 저장소의 영구적인 최신 SHA나 최신 PR 번호를 주장하지 않도록 재개 시 GitHub를 fresh-read한다.

재개 순서:
`latest Coc-Fiction main → open PR → AGENTS → CURRENT_STATE_RECEIPT → ACTIVE_CONTEXT → HANDOFF → CANON_REGISTRY → SCENE_PASS_REGISTRY → candidate manifest/QA → next bounded bundle`

## 현재 완료 상태

- PR #29 Canon reconciliation.
- PR #30 exact 17-file candidate manifest.
- PR #31 QA_GREEN integrated candidate evidence.
- PR #32 current Ch006–010 bounded promotion.
- PR #36 current Ch011–015 bounded promotion.
- PR #39 current Ch016–020 bounded promotion.
- **PR #42 current Ch021–025 bounded promotion merged at `e6817e38042c783be8169f6c385230e75f1253db`.**
- current repository prefix: **001–025**.
- next bounded promotion: **026–030**.

## Current candidate / repository authority 분리

```yaml
artifact_coverage: [1, 161]
candidate_state: QA_GREEN
repository_verified_prefix: [1, 25]
legacy_tail: [26, 225]
```

QA_GREEN 외부/통합 산출물은 GitHub production 전체 승격과 동일하지 않다. verified prefix 밖 저장 원고는 자신의 bounded reconciliation 전까지 legacy다.

## Ch021–025 보호 readback

- Ch20→21: current continuity PASS; 지도 확보·배수로 도주가 current Ch21의 같은 탈출선으로 직접 이어진다.
- Ch21: Ian은 마법·기억의 unknown을 `확인` 상태로 남기며 계획 없는 구조 돌입을 하지 않는다.
- Ch22: Jooan은 정찰/추적 회피 중 몸의 힘을 자동 해결책으로 쓰지 않고 제동을 자기 선택으로 유지한다.
- Ch23: 데이비드를 놓고 엘리스를 받는 구조 행동과 설명되지 않은 신체 반응을 구별한다.
- Ch24: `반응 → 멈춤 → 이유 → 선택`을 개인 의지가 아니라 팀 지원 가능한 실제 전술로 확장한다.
- Ch25: 실제 위험을 확인한 뒤 엘리스에게 `갈 겁니까?`라고 묻고 중앙 선택을 대신하지 않는다.
- Ch25의 `제3세력` 표현은 임시 현장 협력/작전 표현이다. 정식 신규 조직 Canon으로 올리지 않으며 Part2 D01 외부 회수망과 구분한다.

## Current migration truth

```yaml
left_current: 25
right_legacy: 26
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

Ch25→26은 fail-closed boundary다. 인접 번호를 근거로 현재 연속성을 추정하지 않는다.

## 다음 정확한 작업

`fiction/manuscript/part-1/026-030.md`

1. latest main/open PR 재조회.
2. locked QA_GREEN candidate에서 Ch26–30 exact 추출.
3. Ch25 종료 상태와 앞 경계 검증.
4. Canon/원본/사용자 Decision 대조.
5. manuscript/index/reverse-outline/scene-card/registry/router/validator 동시 갱신.
6. exact-head hosted CI Green + review thread 0 + main freshness.
7. squash merge 후 main readback + Notion sync.

## 장기 보호 Canon

- central question: 선의·보호·사랑이 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 정신 능력은 선택 보호, 지배 아님.
- Ian: unknown을 사실로 승격하지 않음.
- D01/D02/D03 및 sword 공동봉인 규칙 유지.
- Alice Carter 한국어 정본은 `엘리스`.
- POV는 Scene-Locked Hybrid.

## 금지

- old-head Green을 current-head Green으로 재사용하지 않는다.
- 파일명의 `최종`만으로 production authority를 부여하지 않는다.
- verified frontier를 validation 없이 이동시키지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
- Base adoption pin을 자동 상승시키지 않는다.
