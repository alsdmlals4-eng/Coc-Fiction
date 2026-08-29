# ACTIVE CONTEXT

갱신: 2026-08-29

## Resume-first

이 문서는 live router다. 저장된 SHA를 영구 최신 포인터로 사용하지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
work_mode: IMPLEMENT / REVIEW
portfolio_state: POLICY_CORRECTION_COMPLETE / MANUSCRIPT_PROMOTION_PAUSED
workspace: REPOSITORY_ONLY_CURRENT
workspace_policy: docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md
frontier_observed_at_main: 1de8beef60612ecc8113b4d7b8146ba7733d96d6
last_frontier_change_pr: 61
pending_frontier_change_pr: null
current_state_receipt: docs/fiction-ops/CURRENT_STATE_RECEIPT.json
current_source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx
current_bundle_source_sha256: 84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496
derived_cross_check_only: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
delivery_state: QA_VERIFIED
delivery_evidence_ceiling: AUTOMATED_AND_REPOSITORY_ONLY
repository_promotion_state: CLOSED_THROUGH_055
reconciled_prefix_end: 55
legacy_tail_starts_at: 56
boundary_after_chapter: 55
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/056-060.md
manuscript_promotion_state: PAUSED_UNTIL_EXPLICIT_RESUME
source_coverage_gap: 101-105
```

새 세션 첫 행동:

```text
latest main
→ open PR
→ AGENTS.md
→ repository autonomy policy
→ CURRENT_STATE_RECEIPT
→ ACTIVE_CONTEXT
→ CANON_REGISTRY
→ SCENE_PASS_REGISTRY
→ USER_SOURCE_CHUNK_MANIFEST
→ current manuscript consumer
```

## Current truth

- PR #61은 2026-08-24 병합됐다.
- Ch051–055 원고와 coupled consumers는 main에 존재한다.
- 2026-08-29 정책 교정은 미종결 receipt/router를 `001–055`로 닫았으며 원고 frontier를 새로 이동시키지 않았다.
- current production prefix: `001–055`.
- current fail-closed boundary: `055→056`.
- next bounded bundle after explicit resume: `fiction/manuscript/part-1/056-060.md`.
- Part 1 main conflict: `001–040`.
- Aftermath & 8-year Bridge: `041–066`.
- Part 2 entry: `067+`.
- whole-manuscript continuity: `NOT_YET_CLAIMED`.
- source gap `101–105`: `SOURCE_NOT_PROVIDED`.

## Workspace authority

```text
latest direct user decision
→ AGENTS.md
→ repository autonomy policy
→ current GitHub production canon
→ user-designated per-range source DOCX
→ registries / actual manuscript / tests
→ adopted Base owner
→ historical migration or external reference
```

- GitHub repository가 current human/structured/manuscript/evidence owner다.
- 과거 Notion summary/Event/Relation/page/database/attachment는 `HISTORICAL_MIGRATION_REFERENCE_ONLY`이며 current sync/readback/completion target이 아니다.
- user-designated DOCX는 reconstruction source authority다. source authority는 automatic production authority가 아니다.
- derived integrated candidate는 cross-check only다.

## Completed promotion milestones

- PR #29: Canon reconciliation.
- PR #30: exact source candidate manifest.
- PR #31: QA_GREEN integrated candidate evidence.
- PR #32/#36/#39: Ch006–020 bounded promotions.
- PR #42: Ch021–025 bounded promotion.
- PR #47: Talon/Milly/Hatem direct-user Canon protection.
- PR #48: Ch026–030 bounded promotion.
- PR #50: Ch031–035 bounded promotion.
- PR #55: Ch036–040 bounded promotion.
- PR #57: Bridge Ch041–045 bounded promotion.
- PR #59: Bridge Ch046–050 bounded promotion.
- PR #61: Bridge Ch051–055 bounded promotion.

Historical promotion receipts remain in `fiction/analysis/SCENE_PASS_REGISTRY.json`, per-bundle Scene Cards, Revision Reports and contract tests. 이 live router에 장별 세부 내용을 중복 복제하지 않는다.

## Canon protection

- central question: 보호·사랑·선의가 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 인간을 포함한 정신 대상의 인지·판단·행동을 조작할 수 있다. 외부 정신간섭 차단·환각 필터도 가능하다. 선택 보존은 능력 제한이 아니라 사용 방식에 대한 자기규율이다.
- Ian: `관찰 → 가설 → 검증 → 기록`; unknown은 unknown으로 유지한다.
- Milly: 실제 남성. Miskatonic의 여성 presentation은 하템 외형을 이용한 위장·사회적 인식이다.
- Hatem: 실제 여성. 기본 외형은 검은 가면의 광신도. Ch27 육체적 사망 뒤에는 새 객관 정보 없는 환각/기억만 허용한다.
- Talon: Part 1 `CORE_ANTAGONIST`; 높은 화면 안 전투 위상을 보존한다.
- D01: bounded external acquisition network.
- D02: +2h 사진은 fixed future가 아니라 authentic non-current cross-loop evidence.
- D03: 다른 회차 세 시신은 명시적 사건 전까지 물리적 경찰 증거.
- Elliott sword: 귀속 미정 / joint seal; 반응·형상변화는 후계 인증이 아니다.
- Alice Carter 한국어 정본: `엘리스`.
- POV: Scene-Locked Hybrid; scene break 없는 head hopping 금지.

## Bounded promotion gate

프로젝트가 명시적으로 재개되면:

```text
exact source/body receipt
→ latest direct-user Canon conflict scan
→ previous/current/next boundary check
→ manuscript/index/reverse-outline/scene-card/registry/router propagation
→ targeted current research when material
→ production feasibility judgement
→ minimum five adversarial-review loops
→ exact-head Fiction operating-system CI
→ unresolved review thread 0
→ main freshness
→ permitted merge
→ new main + repository destination readback
→ receipt/context successor closure
→ remaining-work recalculation
```

Notion sync/readback은 Gate가 아니다. source/static/automated evidence를 reader experience, whole-manuscript continuity 또는 publication readiness로 확대하지 않는다.

## Research / long-term / automation

중요한 작품·운영·시각 결정은 current canon과 실제 원고를 먼저 읽고 최신 공식/1차 자료, 직접 관련 성공·실패·혼합 사례와 실질 대안을 비교한다. `ADOPT / ADAPT / REJECT`, `FEASIBLE / PARTIAL / BLOCKED_UNVERIFIED`를 사용한다.

장기 일관성, 재개 가능성, 검증 가능성, 중복 감소, rollback과 독자 경험을 빠른 국소 수정보다 우선한다. 미래 가능성만을 위한 중복 schema·dashboard·index·process 문서는 만들지 않는다.

승인 범위의 fresh-read, 조사, source receipt, bounded propagation, 자동 검사, readback, 가역적 교정, 남은 작업 재계산과 문제→원인→수정→회귀방지 학습 loop는 routine 재승인 없이 계속한다. 사용자는 중심 의미·Canon·최종 Visual lock·외부 공개·비용·권리·되돌리기 어려운 변경만 결정한다.

## Next exact work

현재 policy/context correction이 끝난 뒤 manuscript promotion은 paused 상태를 유지한다. 프로젝트가 명시적으로 재개되면 `fiction/manuscript/part-1/056-060.md`를 사용자 지정 `051–060` source와 SHA-256 receipt에서 bounded promotion한다.

`101–105`는 실제 user-designated source가 제공되기 전까지 생성·추론·파생 후보로 보충하지 않는다.
