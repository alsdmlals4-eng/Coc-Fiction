# ACTIVE CONTEXT

갱신: 2026-08-24

## Resume-first

이 문서는 live router다. 저장된 SHA를 절대 최신값으로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
work_mode: IMPLEMENT / REVIEW
frontier_observed_at_main: null
last_frontier_change_pr: 42
pending_frontier_change_pr: 48
current_state_receipt: docs/fiction-ops/CURRENT_STATE_RECEIPT.json
current_source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제021-030화_상실광기_강적위상_가독성강화본(1).docx
current_bundle_source_sha256: e15c8fb4ed4ab1b6980c2c57f3979986bdbfa02f77aafef3cc84d3652cb70547
derived_cross_check_only: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
delivery_state: QA_VERIFIED
repository_promotion_state: PARTIAL
reconciled_prefix_end: 30
legacy_tail_starts_at: 31
boundary_after_chapter: 30
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/031-035.md
source_coverage_gap: 101-105
```

`frontier_observed_at_main`과 `last_frontier_change_pr`은 **현재 production frontier의 마지막 merged 증거**다. PR #48이 merge되기 전에는 미래 main SHA를 기록하지 않는다.

새 세션 첫 행동:

`latest main → open PR → AGENTS → CURRENT_STATE_RECEIPT → ACTIVE_CONTEXT → CANON_REGISTRY → SCENE_PASS_REGISTRY → USER_SOURCE_CHUNK_MANIFEST → next bundle`

## Source-authority gate

```yaml
priority:
  1: latest direct user decision
  2: user-designated per-range source DOCX
  3: bounded reconciled GitHub production canon
  4: Notion approved summary / Event / Relation
  5: derived integrated candidate / legacy analysis
rule: source authority != automatic production authority
```

- 구간별 `폭풍의눈_2차퇴고_...` DOCX 묶음이 reconstruction source authority다.
- 이전 `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`는 derived cross-check only다.
- 현재 source set에는 `101–105`가 없으므로 다른 자료에서 자동 보충하지 않는다.
- `031–040`, `126–135`의 중복 업로드는 manifest에서 byte-identical duplicate로 기록한다.

## Completed implementation milestones

- PR #29: Canon reconciliation.
- PR #30: exact 17-file candidate manifest.
- PR #31: QA_GREEN integrated candidate evidence.
- PR #32: Ch006–010 bounded production promotion.
- PR #36: Ch011–015 bounded production promotion.
- PR #39: Ch016–020 bounded production promotion.
- PR #42: Ch021–025 bounded production promotion merged.
- PR #47: Talon/Milly/Hatem direct user Canon protections merged.
- **PR #48: Ch026–030 user-source bounded promotion in progress; production completion not yet claimed.**

## Current candidate prefix 001–030 contract

- Ch5→6, Ch10→11, Ch15→16, Ch20→21, Ch25→26: current continuity.
- Ch16: 위험한 해결책도 당사자 선택 없이 강행하지 않는다.
- Ch17: 주안의 반응성과 신체 회복은 복종·소유의 증거가 아니다.
- Ch18: 정보·힘 제공과 결정 대행을 분리한다.
- Ch19: 하템과 밀리는 별도 인물이며 같은 얼굴만으로 동일인 결론을 내리지 않는다.
- Ch19 Ian: `관찰 → 가설 → 검증 → 기록`; unknown은 unknown으로 남긴다.
- Ch20: 지도 확보 성공과 잠입 실패를 동시에 기록한다.
- Ch21–24: 계획·대기·한 박자 선택과 팀 중단 규칙을 구체화한다.
- Ch25: `제3세력`은 현장 임시 협력/작전 표현이며 정식 신규 조직 Canon이나 D01 외부 회수망이 아니다.
- Ch26: 엘리스는 쇼거스를 지배하지 않고 책임을 스스로 재판단하게 한다. 탈론은 쇼거스 다수를 정면 상대하는 핵심 적대 위상을 유지한다.
- Ch27: 밀리는 실제 남성으로 재등장한다. 하템은 별도 여성 인물이며 이안을 보호하다 육체적으로 사망한다.
- Ch28: 사후 하템은 이안의 환각/기억이며 새로운 객관 정보를 제공하지 않는다. 엘리스는 허락 후에만 정신 지원을 한다.
- Ch29: 밀리와 이안은 친구였던 시간을 지우지 않으면서 현재 반대편 행동을 구분한다. 주안은 몸이 창을 원한다는 이유로 오히려 창을 잡지 않는다.
- Ch30: 밀리의 storm-walk와 쿠바라 창의 연결 절단을 관찰하지만 기원·전체 기능·소유권은 과잉 확정하지 않는다.

## Current migration boundary

```yaml
left_current: 30
right_legacy: 31
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

Ch25→26 current continuity는 PASS다. 저장 화수가 인접하다는 이유만으로 current Ch30→legacy Ch31 연속성을 주장하지 않는다.

## Canon protection

- central question: 보호·사랑·선의가 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 정신 능력은 지배가 아니라 선택 보존.
- Ian: observation → hypothesis → verification → record.
- Milly: 실제 남성. 미스캐토닉에서는 하템의 여성 외형을 이용한 위장 신분 때문에 `밀리 양`으로 인식됨.
- Hatem: 실제 여성. 평소 기본 외형은 검은 가면을 쓴 광신도; unmasked는 별도 reveal state. Ch27 사망 이후 화면은 새 정보 없는 환각/기억으로 제한.
- Talon: Part 1 `CORE_ANTAGONIST`; 황색 수호사제이며 높은 화면 안 전투 위상을 유지.
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

각 bounded 묶음마다:
1. exact user-source 추출 + source SHA receipt
2. latest direct user Canon conflict scan
3. 앞 경계 검증
4. manuscript + index + reverse outline + scene cards + registry + routers + validators 동시 갱신
5. 5× adversarial review
6. exact-head Fiction operating-system CI Green
7. unresolved review thread 0
8. main freshness 확인
9. squash merge
10. post-merge main readback + receipt closure + Notion sync

## Next exact work

`fiction/manuscript/part-1/031-035.md`

다음 pass는 **Ch30→31 migration boundary**에서 사용자 지정 `031–040` source를 기준으로 시작한다. `101–105`는 원본 파일이 제공되기 전 자동 보충 금지다.

## Base / shared governance

- Base adoption pin은 별도 감사 없이 자동 상승시키지 않는다.
- 다른 workstream의 open/draft/ready PR은 수정하지 않는다.
