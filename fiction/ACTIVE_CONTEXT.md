# ACTIVE CONTEXT

갱신: 2026-08-12

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- 현재 세션 상태: `PAUSED_FOR_HANDOFF` — 새 본문 작업은 시작하지 않고 인수인계·운영 학습·검증을 닫는다.
- 최신 전체 구조 감사는 PR #23에서 잠겼고, Rift Accord 제156~161화 설계·집필·QA·전달 증거는 PR #24에서 병합됐다.
- 다음 작품 작업의 우선순위는 **외부 최신 제1~161화 산출물 회수 → 001~161 통합 최종본 제작/전역 적대적 검토 → GitHub production manuscript 승격 전략 재판정**이다.
- bounded repository migration을 계속하는 경우 현재 frontier를 보존하고 `006-010`부터 재개한다. 이 경로는 삭제된 것이 아니라 다음 통합본 확인 뒤 선택할 실행 전략이다.
- 현재 프로젝트 주 책임: `fiction-project-operations: artifact-promotion-gate / checkpoint / handoff / execution-report`.
- 작품 작업 재개 시 주 전문 책임: `fiction-canon-and-research: source-log / canon-audit / continuity-map / timeline-and-state`, `fiction-revision-and-validation: serial-arc-pass / adversarial-loop / regression-check / pr-review`.
- Base 공용 작법 adoption pin은 `7a49390bd840f5f5dc80fe661b44ad45e9ebeb7f`로 유지한다. 2026-08-12 관측 Base 최신 main은 `1d6cc79ae95ffb67ba4de618f010a6540fc6e02c`지만 별도 adoption audit 없이 pin을 자동 갱신하지 않는다.

## Source authority for current story audit

```text
최신 사용자 Decision
→ Google Drive/Library 실제 원본 로그·문서 및 원본사건감사
→ 현재 외부 최신 재퇴고 산출물
→ GitHub에서 production 승격이 검증된 원고 범위
→ 구 225화 전체 압축본/legacy storage topology(비교·migration 자료)
→ 구형 기획·archive
```

- `원본`은 실제 로그/원본 문서를 뜻한다.
- 구 225화 전체 압축본은 원본과 동일 권위가 아니며 사건 기능·인물 동선·하이라이트·migration delta 비교 자료다.
- 외부 산출물의 `최종`/`final` 파일명만으로 GitHub current Canon authority를 부여하지 않는다.
- 최신 사용자 Decision이 원본/구각색과 충돌하면 최신 승인 Canon을 따른다.

## Continuation State

```yaml
baseline:
  default_branch: main
  state_observed_at_main: 0ef8161f918eeb4b951fd6de38f8f7c512274a4d
  last_integrated_pr: 24
  work_merge_main_sha: 0ef8161f918eeb4b951fd6de38f8f7c512274a4d
  open_project_prs_observed: 0
  resume_rule: FETCH_LATEST_MAIN_BEFORE_USE

authority:
  latest_user_decisions:
    - Rift Accord is treaty-first; Juan-Alice reconciliation/apology/confession only; relationship remains open-ended
    - Ian materially participates in Accord while Bruce Massy remains official Miskatonic representative
    - Largo first reader-facing [규율] reveal occurs at the Accord with "회의 중입니다."
    - Dabin residual [잔재] is not free rewind or stable precognition
    - Jumin silver sword transforms to a silver scalpel but custody/ownership remains unresolved
  protected_scope:
    - no manuscript or Canon rewrite during this handoff cycle
    - no blind overwrite of the legacy 225-chapter storage topology

progress:
  completed_verified:
    - external latest chapters 001-005 production reconciliation
    - side-story-lake 091-095 primary-source matched pass
    - Coc-Fiction PR #21 character/opponent integrity + Largo instructor/affection Canon merge
    - Coc-Fiction PR #22 craft benchmark refresh merge
    - Coc-Fiction PR #23 whole-work story architecture / reader-knowledge / payoff ledger merge
    - Coc-Fiction PR #24 Rift Accord design + approved amendment + execution plan + adversarial review + delivery manifest merge
    - Rift Accord Ch156-161 external DOCX QA and delivery evidence
  analyzed_not_integrated:
    - PR #19 contains 006-010 reconciliation evidence but did not produce a verified production promotion; do not count it as reconciled prefix 10
  in_progress: []
  ready_next:
    - recover the actual external revised artifact set covering Ch001-161 and verify overlap/gaps
    - build a consolidated Ch001-161 final candidate artifact
    - run whole-work adversarial review and machine/document QA on that candidate
    - choose repository promotion execution strategy from current evidence; if bounded migration continues, resume at 006-010
  deferred:
    - stored 176-180 primary-source pass until the 001-161 consolidation/promotion strategy is settled

artifacts:
  rift_accord_156_161:
    filename: 폭풍의눈_2차퇴고_2부외전_제156-161화_Rift_Accord_협약완결본.docx
    coverage: [156, 161]
    sha256: f9ddf90970a4760652f9bbac21c315daa24a51b47a32bfccfd47ef22a865f8d5
    delivery_state: DELIVERED
    repository_promotion_state: PENDING
    evidence: docs/fiction-ops/2026-08-12_RIFT_ACCORD_DELIVERY_MANIFEST.md
  ending_146_155:
    filename: 폭풍의눈_2차퇴고_제146-155화_최종선택_후일담_가독성강화본.docx
    coverage: [146, 155]
    sha256: fc3e781772439b3d39f76f4510bebc4057eae9c67bfaaf0221cb024a187f60de
    delivery_state: QA_VERIFIED
    repository_promotion_state: PENDING
    note: current handoff does not re-run this file's prior document QA; recover from Library before 001-161 consolidation

migration:
  legacy_repository_topology: 225-chapter migration storage container
  reconciled_prefix_end: 5
  legacy_tail_starts_at: 6
  boundary_after_chapter: 5
  whole_manuscript_continuity: NOT_YET_CLAIMED
  next_bounded_bundle_if_resumed: fiction/manuscript/part-1/006-010.md
  repository_promotion_state: PARTIAL
```

`state_observed_at_main`은 이 문서 자신의 merge SHA를 무한 추적하는 값이 아니다. 새 세션은 반드시 GitHub `main`과 열린 PR을 먼저 다시 조회한다.

## Artifact Promotion Gate

`delivery_state`와 `repository_promotion_state`는 별도 판정이다.

```text
QA_VERIFIED / DELIVERED
!=
PROMOTED_TO_GITHUB_PRODUCTION_MANUSCRIPT
```

- 외부 DOCX의 검수/전달이 끝나도 GitHub migration frontier가 그대로면 repository promotion은 `PENDING` 또는 `PARTIAL`이다.
- staged migration에서 candidate data나 delivery manifest가 존재한다는 이유만으로 verified prefix를 늘리지 않는다.
- 다음 세션은 artifact filename/coverage/SHA, current repository topology, verified frontier, migration boundary, validation gate를 함께 읽는다.
- promotion을 실제 수행하기 전에는 현재 원고·index·reverse outline·Scene Pass Registry 등 coupled consumer를 다시 inventory한다.

## 2026-08-11 구조 감사용 작법 Gate — 계속 유효

### 1. Character — CHOICE_PROOF

주요 인물마다 다음을 실제 장면 선택으로 증명한다.

```yaml
core_value_or_wound:
initial_choice_pattern:
pressure_tests:
regression_or_contradiction:
threshold_choice:
late_choice_echo:
aftermath_behavior:
```

- 성장 선언이나 캐릭터 소개문만으로 아크 완료를 주장하지 않는다.
- 후반 선택은 앞의 작은 선택을 다시 보면 가능성이 있었던 `SURPRISING_BUT_COHERENT`를 지향한다.
- 회귀·실수·모순은 결함이 아니라 아크의 압력 증거가 될 수 있다.

### 2. Highlight — IDENTITY + COMPETENCE + COST + CHOICE + CONSEQUENCE

- `IDENTITY`: 다른 인물로 바꾸면 같은 장면이 되지 않는가.
- `COMPETENCE`: 설정상 능력·직업·지위가 실제 화면에서 작동하는가.
- `COST`: 저항·손실·포기 가능성이 있는가.
- `CHOICE`: 결정적 행동을 해당 인물이 소유하는가.
- `CONSEQUENCE`: 관계·정보·몸·자원·목표가 이후 실제로 바뀌는가.
- 조연 하이라이트는 강하게 만들되 해당 부 주연의 중앙 결정권과 결말을 빼앗지 않는다.

### 3. Information — WITHHOLD_INFORMATION_NOT_CONTEXT

중요 사건은 필요할 때 `READER_KNOWLEDGE_MATRIX`를 사용한다.

```yaml
pov_knows:
pov_suspects:
other_character_knows:
reader_knows:
reader_needs_now:
hidden_truth:
withholding_reason:
behavioral_trace:
reveal_trigger:
post_scene_information_change:
```

- 답·배후·괴이 원리는 숨길 수 있다.
- 현재 POV·즉시 목표·위험·행동 결과처럼 독자가 장면을 따라갈 맥락은 숨기지 않는다.
- POV가 이미 아는 사실을 독자만 속이려고 부자연스럽게 감추면 `FALSE_SUSPENSE_BY_POV_SUPPRESSION`이다.
- 인물이 타인에게 정보를 숨기면 character-specific reason과 행동 흔적이 필요하다.

### 4. Foreshadow — staged payoff ladder

```text
SETUP
→ RECALL
→ RECONTEXTUALIZE
→ PARTIAL_PAYOFF
→ PAYOFF
→ AFTERMATH
```

Rift Accord에서 이미 회수된 장기축은 통합본 전역 검수 때 setup→payoff→aftermath 연결을 다시 확인한다.

우선 감사 대상:

- Juan–Alice 선택/감정 불확실성 → Ch159 사과·고백·열린 관계 aftermath
- Ian–Milly–Hatem 동일 얼굴/상실/광기 구조 → Accord의 `신규 정보 없음` aftermath
- Elliott의 조기 노출 → Dabin의 최종 선택 → Jumin의 메스 재맥락화
- Largo의 1부 위화감 → 8년 교관 관계 → Rift Accord `[규율]`
- William/Alice, Choseikan/outer armor, Elliott/Dabin의 `보호가 선택을 빼앗는 순간` 주제 변주 → Accord 제도화 위험

### 적대적 실패 코드

- `CONTEXT_WITHHELD_AS_MYSTERY`
- `FALSE_SUSPENSE_BY_POV_SUPPRESSION`
- `ARC_TOLD_NOT_PROVEN`
- `UNSEEDED_CHARACTER_TURN`
- `HIGHLIGHT_WITHOUT_COST_OR_CHOICE`
- `SPECTACLE_WITHOUT_CHARACTER`
- `COMPETENCE_CLAIM_WITHOUT_PROOF`
- `FORESHADOW_WITHOUT_PAYOFF`
- `PAYOFF_WITHOUT_SETUP`
- `PAYOFF_WITHOUT_AFTERMATH`

## 현재 캐릭터·관계 Canon 핵심

### 주안–앨리스

- 앨리스가 먼저 지속적으로 호감을 표현했고, 주안은 나이 차이·경호원/아가씨·신분·직업윤리 때문에 알고도 선을 그었다.
- 공동 생존 뒤 주안도 실제 호감이 생겼지만 윌리엄의 설계가 드러난 뒤 자기 감정뿐 아니라 앨리스의 마음까지 의심하며 8년을 회피했다.
- Ch155에서 `상대의 선택은 묻는다.`까지 도달했고, Rift Accord에서 실제로 재회해 **앨리스의 마음까지 의심한 일을 먼저 사과하고 현재의 선택으로 좋아한다고 고백했다.**
- 객관적 감정 순수성 증명은 하지 않았다.
- 화해와 고백은 이루어졌지만 **두 사람이 어떤 관계를 만들지는 열린 상태**다. `공식 연애 확정`이나 8년의 상처 삭제로 닫지 않는다.

### 라르고–앨리스

- 1부의 라르고는 윌리엄의 평범하고 유능한 비서로 보이며 실제 최상위 능력은 숨겨졌다.
- 주안 이탈 뒤 8년 동안 라르고는 앨리스의 실제 교관/훈련 담당자였다.
- 라르고는 앨리스를 가르치고 성장·실패·고집·선택을 오래 지켜보는 과정에서 좋아하게 됐지만, 앨리스가 주안을 사랑함을 알고도 경쟁하거나 정보를 막지 않는다.
- Rift Accord 회의에서 `회의 중입니다.`와 함께 `[규율]`이 최초 공개됐다.
- `[규율]`은 합의된 회의 규칙 위반을 중단시키는 장면 기능으로 사용됐으며 협정 결론·사상·정책을 대신 결정하는 권한으로 확장하지 않는다.

### 2부 후일

- 다빈: 타임리프 인자는 제거됐고 시간마법의 `[잔재]`만 남는다. 자유 회귀·확정 미래예지가 아니라 시간잔향·기시감·짧은 선행감각이 불완전하게 발현한다.
- 주민: 의사 정체성과 후유증을 유지한다. 공동 보관 중인 엘리엇의 은검은 외전에서 주민의 손에 백은의 메스로 변했지만 `귀속 미정`이며 후계자 인증으로 확정하지 않는다.
- 다빈·주민: 델타그린에 소유되는 것이 아니라 자기 조건을 건 협력 방향이다.
- 이안·미스캐토닉: 브루스 매시가 Accord 공식 대표이고 이안은 보좌·현장 마도사·기술보고/검증 실무 담당이다. 하템 환각은 신규 정보를 제공하지 않는다.
- Great Rift: 대균열은 하나이며 태평양 전선이 실제로 존재한다. 공개 설명은 불완전하고 DG가 과거 사건을 만들었다고 소급하지 않는다.

## 캐릭터·상대 위상 공통 검수

- 주요 인물은 `관찰 필터 / 말투·사고 / 문제 해결 / 화면 안 유능함 증명 / 인간적 매력 / 대가를 만드는 결점 / 대표 하이라이트`가 서로 교환 가능하지 않아야 한다.
- 설정상 강한 주요 인물은 중요도에 비례한 화면 안 증명 장면을 갖는다.
- 중요 상대는 최소 한 번 자신의 규칙을 강제하는 `own turn`과 실제 성공·비용을 갖는다.
- 주인공을 강하게 보이게 하려고 상대를 갑자기 약화·우둔화하지 않는다.
- 팽무악은 원본/구압축본에서 확인되는 순수 검술 강자 기능을 `RESTORE` 우선으로 처리한다.
- 황진청은 능글맞은 강자이며 설정문·전투 흔적만으로 끝내지 않고 실제 전투를 배치해 약하지 않음을 증명한다.
- 조연의 강함 증명은 다빈·주민·앨리스 등 해당 부 주연의 중앙 결정권과 결말을 대신하지 않는다.

## Base 적용·제안 상태

```yaml
base_repository: alsdmlals4-eng/Base
project_adoption_pin: 7a49390bd840f5f5dc80fe661b44ad45e9ebeb7f
base_main_observed_2026_08_12: 1d6cc79ae95ffb67ba4de618f010a6540fc6e02c
adoption_pin_auto_advanced: false

reused_base_change_proposals:
  - id: BCP-2026-012-serial-fiction-canon-migration-debt
    status_on_base_main: IMPLEMENTED
    project_action: REUSE_EXISTING_BCP
  - id: BCP-2026-017-serial-fiction-reconciliation-frontier-and-derived-continuity-guard
    status_on_base_main: IMPLEMENTED
    project_action: REUSE_EXISTING_BCP
  - id: BCP-2026-013-post-merge-continuation-state-reconciliation
    status_on_base_main: IMPLEMENTED
    project_action: REUSE_EXISTING_BCP

same_goal_base_new_bcp_needed: false
other_project_base_changes_preserved: true
base_write_this_handoff_cycle: NONE_UNLESS_FRESH_PREFLIGHT_PROVES_NEW_MATERIAL_GAP
continuous_work_active: false
```

Base에 공용 판단 규칙만 두고 《폭풍의 눈》 고유 캐릭터·관계·전투 위치·회차 값은 Coc-Fiction이 소유한다.

## 변경 금지

- 이번 인수인계 사이클에서 작품 본문·Canon Registry를 수정하지 않는다.
- 외부 산출물의 `최종` 표기만으로 남은 미이관 원고를 자동 덮어쓰지 않는다.
- GitHub의 225화 storage topology를 최신 narrative numbering의 최종 편성으로 되돌리지 않는다.
- verified frontier가 5인데 candidate/evidence만 보고 10으로 승격하지 않는다.
- 자동 역개요를 원고 수정 명령으로 사용하지 않는다.
- 구형 통합 초안·archive·구 225화 전체 압축본을 실제 원본보다 높은 권위로 취급하지 않는다.
- 하템 사후의 새 정보·새 주문·실제 물리 행위를 허용하지 않는다. 사후 하템은 이안의 환각/환청이며 이안이 모르는 새 정보를 제공하지 않는다.
- Handoff 자신의 merge SHA를 기록하기 위해 상태 PR을 무한 생성하지 않는다.
