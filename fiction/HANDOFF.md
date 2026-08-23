# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-24

## Resume-first

이 문서는 재개용 live router다. 저장된 SHA를 절대 최신값으로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
frontier_observed_at_main: null
last_frontier_change_pr: 42
pending_frontier_change_pr: 48
current_state_receipt: docs/fiction-ops/CURRENT_STATE_RECEIPT.json
source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제021-030화_상실광기_강적위상_가독성강화본(1).docx
current_bundle_source_sha256: e15c8fb4ed4ab1b6980c2c57f3979986bdbfa02f77aafef3cc84d3652cb70547
repository_promotion_state: PARTIAL
reconciled_prefix_end: 30
legacy_tail_starts_at: 31
boundary_after_chapter: 30
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/031-035.md
source_coverage_gap: 101-105
```

PR #48 merge 전에는 `001–030`을 main production 완료라고 부르지 않는다. `frontier_observed_at_main=null`은 의도적인 fail-closed 상태다.

재개 순서:
`latest main → open PR → AGENTS → CURRENT_STATE_RECEIPT → ACTIVE_CONTEXT → HANDOFF → CANON_REGISTRY → SCENE_PASS_REGISTRY → USER_SOURCE_CHUNK_MANIFEST → next bounded bundle`

## 현재 상태

- PR #42: Ch021–025 bounded promotion merged.
- PR #47: `탈론=핵심 적대`, `밀리=남성/미스캐토닉 여성 위장`, `하템=여성/기본 가면` Canon merged.
- **PR #48: Ch026–030 user-source bounded promotion 진행 중.**
- candidate prefix: `001–030`.
- fail-closed boundary: `30→31`.
- next source bundle after merge: `031–035` from user-designated 031–040 DOCX.

## Source authority

1. 최신 사용자 직접 결정
2. 구간별 사용자 지정 `폭풍의눈_2차퇴고_...` DOCX
3. bounded reconciliation을 통과한 GitHub production canon
4. Notion 승인 요약/Event/Relation
5. 파생 통합본/Legacy

이전 `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`는 derived cross-check only다. 현재 사용자 source set에는 `101–105`가 없으므로 자동 보충하지 않는다.

## Ch026–030 보호 readback

- Ch25→26: current continuity PASS.
- Ch26: 엘리스는 쇼거스를 조종하지 않고 질문/책임으로 자기 판단을 바꾸게 한다. 탈론은 쇼거스 다수를 정면 상대하는 core antagonist 위상.
- Ch27: 밀리는 남성 현재 몸으로 재등장. 하템은 별도 여성 인물로 이안을 보호하다 육체적으로 사망.
- Ch28: 사후 하템은 환각/기억이며 새 정보 제공 금지. 엘리스는 이안 허락 후 정신 경계 지원만 한다.
- Ch29: 이안/밀리는 친구였던 과거와 현재 반대편 행동을 동시에 유지. 주안은 몸이 창을 원한다는 이유로 창을 잡지 않는다.
- Ch30: 밀리 storm-walk, 쿠바라 창의 연결 절단을 관찰하지만 기원·전체 기능·소유권은 확정하지 않는다.

## Current migration truth

```yaml
left_current: 30
right_legacy: 31
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

Ch30→31은 fail-closed boundary다. 인접 번호를 근거로 현재 연속성을 추정하지 않는다.

## 다음 정확한 작업

현재: PR #48 consumer propagation → adversarial review 5회 → exact-head CI Green → review thread 0/main freshness → squash merge → receipt closure → Notion sync.

그 후:
`fiction/manuscript/part-1/031-035.md`

사용자 지정 `031–040` 원본을 기준으로 동일한 bounded pass를 반복한다.

## 장기 보호 Canon

- central question: 선의·보호·사랑이 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 정신 능력은 선택 보호, 지배 아님.
- Ian: unknown을 사실로 승격하지 않음.
- Milly: male; Miskatonic female disguise uses Hatem's appearance.
- Hatem: female; default black-mask cultist; Ch27 death, later no-new-info hallucination only.
- Talon: Part 1 core antagonist; high on-screen combat competence.
- D01/D02/D03 및 sword 공동봉인 규칙 유지.
- Alice Carter 한국어 정본은 `엘리스`.
- POV는 Scene-Locked Hybrid.

## 금지

- old-head Green을 current-head Green으로 재사용하지 않는다.
- source authority를 자동 production authority로 승격하지 않는다.
- verified frontier를 validation 없이 이동시키지 않는다.
- `101–105`를 파생 자료로 자동 보충하지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
