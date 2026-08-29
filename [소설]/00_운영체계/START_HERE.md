# Coc-Fiction 소설 작업 시작 지점

갱신: 2026-08-29

## 최초 읽기

```text
docs/coordination/CONCURRENT_WORK.md
→ AGENTS.md
→ docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md
→ [소설]/00_운영체계/OPERATING_MODEL.md
→ fiction/FICTION_MASTER.md
→ docs/fiction-ops/CURRENT_STATE_RECEIPT.json
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ 현재 묶음 Scene Card·Revision Report
→ fiction/analysis/REVERSE_OUTLINE_REPORT.md
→ fiction/MANUSCRIPT_INDEX.json
→ fiction/STYLE_GUIDE.md
→ 현재 원고 묶음
```

`CURRENT_STATE_RECEIPT.json`의 SHA/PR은 production frontier가 마지막으로 바뀐 증거다. 저장소의 영구 최신 포인터가 아니므로 실제 작업 전 최신 `main`과 open PR을 다시 조회한다.

## 현재 단계

```yaml
work_mode: IMPLEMENT / REVIEW
manuscript_stage: REVISE / PROMOTE_BOUNDED
portfolio_state: POLICY_CORRECTION_COMPLETE / MANUSCRIPT_PROMOTION_PAUSED
workspace: REPOSITORY_ONLY_CURRENT
workspace_policy: docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md
source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx
current_bundle_source_sha256: 84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496
derived_cross_check_only: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
repository_reconciled_prefix: 001-055
legacy_tail_starts_at: 056
boundary_after_chapter: 055
whole_manuscript_continuity: NOT_YET_CLAIMED
last_frontier_change_pr: 61
frontier_observed_at_main: 1de8beef60612ecc8113b4d7b8146ba7733d96d6
pending_frontier_pr: null
next_bundle: fiction/manuscript/part-1/056-060.md
source_coverage_gap: 101-105
```

PR #61은 2026-08-24에 병합됐고 Ch051–055의 원고와 연결 consumer가 `main`에 존재한다. 2026-08-29 정책 교정에서 unfinished receipt만 닫았으며 새 원고 묶음은 승격하지 않았다.

`manuscript_promotion_state`는 `PAUSED_UNTIL_EXPLICIT_RESUME`다. 정책·정본 교정은 완료할 수 있지만 Ch056–060 본문 승격은 별도의 프로젝트 재개 지시 전 시작하지 않는다.

## Workspace authority

```text
latest direct user decision
→ AGENTS.md
→ repository autonomy policy
→ bounded reconciled GitHub production canon
→ user-designated per-range source DOCX
→ structured registries / actual manuscript / exact tests
→ adopted Base owner
→ external reference / historical migration material
```

- GitHub repository가 현재 사람용 작품 정본, 구조화 Canon, production frontier, 검사·evidence와 handoff의 단일 활성 owner다.
- 과거 Notion summary/Event/Relation/page/database/attachment는 `HISTORICAL_MIGRATION_REFERENCE_ONLY`다. current 작업의 read/write/sync/readback 또는 완료 조건이 아니다.
- 구간별 `폭풍의눈_2차퇴고_...` DOCX 묶음은 reconstruction source authority다. source authority가 존재한다는 사실만으로 production authority가 되지 않는다.
- 파생 통합본은 cross-check only다.
- 현재 source set에는 `101–105`가 없으므로 다른 자료에서 자동 보충하지 않는다.

## 작업 생명주기

- Work Mode: `PLAN → BUILD → REVIEW`
- Manuscript Stage: `DISCOVER → OUTLINE → DRAFT → REVISE → POLISH`

현재는 BUILD/REVIEW 안의 bounded promotion + REVISE 단계다. GitHub 225화/45묶음 경로는 migration container이며 current narrative 최종 numbering 선언으로 사용하지 않는다.

## 현재 production / legacy boundary

```yaml
left_current: 55
right_legacy: 56
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

- Part 1 main conflict: `001–040`
- Aftermath & 8-year Bridge: `041–066`
- Part 2 entry: `067+`
- current production: `001–055`
- next bounded bundle after explicit resume: `056–060`
- whole-manuscript continuity: `NOT_YET_CLAIMED`

## Bounded promotion gate

프로젝트가 명시적으로 재개되면 각 5화 묶음마다 다음을 수행한다.

```text
exact user-source extraction + source SHA receipt
→ latest direct-user Canon conflict scan
→ previous/current/next boundary verification
→ manuscript + index + reverse outline + scene cards + registry + routers propagation
→ targeted current factual/craft/production research when material
→ production feasibility judgement
→ minimum five full adversarial-review loops
→ exact-head Fiction operating-system CI
→ unresolved review thread 0
→ main freshness
→ permitted squash merge
→ new main + repository destination readback
→ receipt/context successor closure
→ remaining-work recalculation
```

Notion sync/readback은 Gate가 아니다. 자동 검사 Green은 whole-manuscript continuity, 독자 경험 또는 출판 준비 증거가 아니다.

## 장기 보호 Canon

- Central question: 보호·사랑·선의가 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 인간을 포함한 정신 대상의 인지·판단·행동을 조작할 수 있다. 외부 정신간섭 차단·환각 필터도 가능하다. 선택 보존은 능력 제한이 아니라 사용 방식에 대한 자기규율이다.
- Ian: `관찰 → 가설 → 검증 → 기록`; unknown을 사실로 승격하지 않는다.
- Milly: 실제 남성. 미스캐토닉의 여성 presentation은 하템의 여성 외형을 이용한 위장·사회적 인식이다.
- Hatem: 실제 여성. 기본 외형은 검은 가면의 광신도. Ch27 육체적 사망 뒤 화면은 새 객관 정보 없는 환각/기억으로 제한한다.
- Talon: Part 1 핵심 적대 / 황색 수호사제 / 높은 화면 안 전투 위상 유지.
- D01: bounded external acquisition network.
- D02: +2h 사진은 fixed future가 아닌 authentic non-current cross-loop evidence.
- D03: 다른 회차 세 시신은 명시적 사건이 바꾸기 전까지 물리적 경찰 증거.
- Elliott sword: 귀속 미정·공동봉인; 반응/형상변화는 후계 인증이 아니다.
- Alice Carter 한국어 정본은 `엘리스`.
- POV: Scene-Locked Hybrid; scene break 없는 head hopping 금지.

## 조사·장기 최적화·자동화

중요한 작품·운영·시각 결정은 현재 Canon과 실제 원고를 먼저 읽고 최신 공식/1차 자료, 직접 관련 성공·실패·혼합 사례와 실질 대안을 비교한다. 결과는 `ADOPT / ADAPT / REJECT`와 `FEASIBLE / PARTIAL / BLOCKED_UNVERIFIED`로 기록한다.

빠른 국소 수정보다 장기 연속성, 검증 가능성, 재개 가능성, 중복 감소, rollback과 독자 경험을 우선한다. 단, 미래 가능성만을 위한 중복 schema·dashboard·index·process 문서는 만들지 않는다.

사용자 관여는 작품 중심 의미, 주요 Canon, 최종 Visual Direction, 외부 공개·비용·권리·되돌리기 어려운 변경으로 제한한다. 안전한 fresh-read, 조사, bounded propagation, 검사, readback, 가역적 교정, 남은 작업 재계산과 문제→원인→수정→회귀방지 학습 loop는 승인 범위에서 연속 진행한다.

## 금지

- 구 저장 편성이나 파생 통합본을 user source authority로 되돌리지 않는다.
- source 파일명의 `최종`이나 QA label만으로 자동 승격하지 않는다.
- migration boundary를 정상 next chapter로 가정하지 않는다.
- `101–105`를 추론이나 다른 파일로 자동 보충하지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
- 과거 CI Green을 current exact head Green으로 재사용하지 않는다.
- paused 상태에서 Ch056–060을 자동 promotion하지 않는다.
