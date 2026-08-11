# ACTIVE CONTEXT

갱신: 2026-08-11

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- 현재 작품 작업 순서: `캐릭터 정본 → 주요 사건/하이라이트 → 복선·정보 구조 → 전체 본문 퇴고`.
- 현재 프로젝트 주 책임: `fiction-canon-and-research: source-log / canon-audit / continuity-map / timeline-and-state`
- 현재 프로젝트 보조 책임: `fiction-story-development: character-and-opponent-integrity / character-and-arc / plot-and-causality / scene-card`, `fiction-revision-and-validation: character-opponent-integrity / serial-arc-pass / adversarial-loop / regression-check / pr-review`, `fiction-project-operations: checkpoint / handoff / execution-report`.
- Base 공용 작법: `developing-and-revising-serial-fiction`의 Canon/각색 경계, POV·voice, 캐릭터 개성·상대 위상, 회차 가치, Local Payoff/Open Loop를 선택적으로 재사용한다.
- 2026-08-11 작법 재조사 결과를 `docs/fiction-ops/CRAFT_RESEARCH.md`와 Base serial-fiction knowledge hub에 반영 중이며, 본문 대규모 퇴고 전 구조 감사에 우선 적용한다.

## Source authority for current story audit

```text
최신 사용자 Decision
→ Google Drive 실제 원본 로그/문서 및 원본사건감사
→ 현재 활성 원고
→ 구 225화 전체 압축본(비교자료)
→ 구형 기획·archive
```

- `원본`은 Google Drive 실제 로그/원본 문서를 뜻한다.
- 구 225화 전체 압축본은 원본과 동일 권위가 아니며, 사건 기능·인물 동선·하이라이트 후보를 비교하는 자료다.
- 원본에 있던 강함·관계·위협 증명 기능이 현행 압축 과정에서 사라졌다면 신규 창작 전에 `KEEP / RESTORE / REWORK / NEW / REMOVE`로 판정한다.
- 최신 사용자 Decision이 원본/구각색과 충돌하면 최신 승인 Canon을 따른다.

## Continuation State

```yaml
baseline:
  default_branch: main
  last_observed_main_sha: 43a307b1cd8a5b1f39ba859a44dadfb517b77f74
  last_integrated_pr: 21
  merge_commit_sha: 43a307b1cd8a5b1f39ba859a44dadfb517b77f74

progress:
  completed_verified:
    - external latest chapters 001-005 production reconciliation
    - side-story-lake 091-095 primary-source matched pass
    - Base PR #281 character/opponent integrity mode merge
    - Coc-Fiction PR #21 character/opponent integrity + Largo instructor/affection canon merge
  analyzed_not_integrated:
    - PR #19 produced source/canon audit cards and a report for external latest chapters 006-010, but the merged PR did not propagate the approved production body, manuscript index, reverse outline, or Scene Pass Registry. This is not counted as completed migration.
  in_progress:
    - 2026-08-11 external craft benchmark refresh and project application
    - character canon / event-highlight / foreshadow-information architecture audit before prose rewrite
    - external latest chapters 001-105 gradual GitHub canon reconciliation
  ready_next:
    - finish craft refresh verification
    - apply CHOICE_PROOF / highlight proof / foreshadow ladder / reader knowledge matrix to global story audit
    - migrate external latest chapters 006-010 as one atomic production pass when manuscript migration resumes
  deferred:
    - full prose rewrite until global story architecture is locked
    - stored 176-180 primary-source pass until current external reconciliation priority is reassessed

migration:
  artifact: 폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip
  target_chapters: [1, 105]
  reconciled_prefix_end: 5
  legacy_tail_starts_at: 6
  boundary_after_chapter: 5
  whole_manuscript_continuity: NOT_YET_CLAIMED
  next_bundle: fiction/manuscript/part-1/006-010.md
```

`last_observed_main_sha`는 이 문서 자신의 새 commit을 무한 추적하는 값이 아니다. 새 세션은 GitHub `main`과 열린 PR을 먼저 재조회한다.

## 2026-08-11 구조 감사용 작법 Gate

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

대표 장면마다 필요한 범위에서 확인한다.

- `IDENTITY`: 다른 인물로 바꾸면 같은 장면이 되지 않는가.
- `COMPETENCE`: 설정상 능력·직업·지위가 실제 화면에서 작동하는가.
- `COST`: 저항·손실·포기 가능성이 있는가.
- `CHOICE`: 결정적 행동을 해당 인물이 소유하는가.
- `CONSEQUENCE`: 관계·정보·몸·자원·목표가 이후 실제로 바뀌는가.

조연 하이라이트는 강하게 만들되 다빈·주민·엘리스 등 해당 부 주연의 중앙 결정권과 결말을 빼앗지 않는다.

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

장기 복선은 필요할 때 다음으로 추적한다.

```text
SETUP
→ RECALL
→ RECONTEXTUALIZE
→ PARTIAL_PAYOFF
→ PAYOFF
→ AFTERMATH
```

특히 1부 → Ch45–60 → 2부 → Rift Accord 사이의 장기 seed가 단순 재등장이 아니라 **두 번째 의미**를 얻는지 본다.

우선 감사 대상:

- Juan–Alice 선택/감정 불확실성
- Ian–Milly–Hatem 동일 얼굴/상실/광기 구조
- Elliott의 Ch47 조기 노출과 2부 antagonist payoff
- Largo의 1부 위화감 → 8년 교관 관계 → 2부 유능한 교관 → Rift Accord `[규율]`
- William/Alice, Choseikan/outer armor, Elliott/Dabin의 `보호가 선택을 빼앗는 순간` 주제 변주

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

이 Gate를 통과하기 전에는 전체 본문 line edit로 넘어가지 않는다.

## 현재 캐릭터·관계 Canon 핵심

### 주안–엘리스

- 엘리스가 먼저 지속적으로 호감을 표현한다.
- 주안은 초기에 나이 차이, 경호원/아가씨, 신분 차이, 직업윤리 때문에 알고도 거절한다.
- 공동 생존 뒤 주안도 실제 호감이 생긴다.
- 윌리엄의 설계가 드러난 뒤 주안은 자기 감정뿐 아니라 엘리스의 마음까지 외부 영향이 있었을지 확신하지 못해 회피한다.
- 2부 외전에서 엘리스의 선택까지 의심했던 일을 사과한 뒤 주안이 `좋아한다`고 고백하며 관계 아크를 닫는다.

### 라르고–엘리스

- 1부의 라르고는 윌리엄의 평범하고 유능한 비서로 보인다. 실제 최상위 전투력은 공개하지 않는다.
- 1부 최종 윌리엄–엘리스 협상에는 라르고가 곁에 있으며, 주안의 신체 경계와 이안의 `질서` 감각은 윌리엄 탓으로 오인 가능해야 한다.
- 주안 이탈 뒤 8년 동안 라르고는 **엘리스의 실제 교관/훈련 담당자**다.
- 라르고는 엘리스를 직접 가르치고 성장·실패·고집·선택을 오래 지켜보는 과정에서 좋아하게 된다.
- 엘리스가 주안을 사랑한다는 사실을 알고도 경쟁하거나 주안 정보를 질투로 막지 않는다.
- 다른 사람에게는 업무적이고 엘리스에게만 능글맞고 장난스러운 교관 관계가 두드러진다.
- `[규율]`과 실제 최상위 능력의 최초 공개는 2부 외전 Rift Accord 회의까지 보존한다.

### 2부 후일

- 다빈: 타임리프 인자 제거 뒤 시간마법의 `[잔재]`가 남은 각성자. 자유 회귀·확정 미래예지가 아니라 시간잔향·기시감·짧은 선행감각이 불완전하게 발현한다.
- 주민: 엘리엇의 검을 보관/계승하고 외전에서 백은의 메스로 형상변화한다. 델타그린 협력 초상외과의 방향을 암시한다.
- 다빈·주민: 델타그린에 소유되는 것이 아니라 자기 조건을 건 협력 각성자 방향으로 활동한다.
- 이안·미스캐토닉: 브루스 생존 Canon을 전제로 외전 Rift Accord의 공식 대표는 브루스, 이안은 보좌·현장 마도사·기술보고 담당으로 배치한다.

## 캐릭터·상대 위상 공통 검수

- 주요 인물은 `관찰 필터 / 말투·사고 / 문제 해결 / 화면 안 유능함 증명 / 인간적 매력 / 대가를 만드는 결점 / 대표 하이라이트`가 서로 교환 가능하지 않아야 한다.
- 설정상 강한 주요 인물은 중요도에 비례한 화면 안 증명 장면을 갖는다.
- 중요 상대는 최소 한 번 자신의 규칙을 강제하는 `own turn`과 실제 성공·비용을 갖는다.
- 주인공을 강하게 보이게 하려고 상대를 갑자기 약화·우둔화하지 않는다.
- 팽무악은 원본/구압축본에서 확인되는 순수 검술 강자 기능을 `RESTORE` 우선으로 처리한다.
- 황진청은 능글맞은 강자이며, 설정문·전투 흔적만으로 끝내지 않고 실제 전투를 배치해 약하지 않음을 증명한다.
- 조연의 강함 증명은 다빈·주민·엘리스 등 해당 부 주연의 중앙 결정권과 결말을 대신하지 않는다.

## Base 적용 상태

```yaml
base_repository: alsdmlals4-eng/Base
base_pr: 281
base_commit: 069f0c9654a6cde7cea6f3343dd2fa81c6248d5d
base_skill: developing-and-revising-serial-fiction
base_mode: character-and-opponent-integrity
craft_refresh_pr: 282
craft_refresh_status: IN_PROGRESS
project_modes:
  - fiction-story-development: character-and-opponent-integrity
  - fiction-revision-and-validation: character-opponent-integrity
base_implementation_authority: USER_APPROVED_AND_MERGED
new_broad_skill_created: false
second_project_pilot: NOT_RUN
human_reader_quality: NOT_RUN
```

Base에는 공용 판단 규칙만 두고 《폭풍의 눈》 고유 캐릭터·관계·전투 위치·회차 값은 Coc-Fiction이 소유한다.

## 변경 금지

- 전체 캐릭터·사건·복선 구조가 잠기기 전에 본문 대규모 재작성으로 넘어가지 않는다.
- 외부 산출물의 `최종` 표기만으로 남은 미이관 원고를 자동 덮어쓰지 않는다.
- GitHub의 225화 storage topology를 최신 narrative numbering의 최종 편성으로 되돌리지 않는다.
- 자동 역개요를 원고 수정 명령으로 사용하지 않는다.
- 구형 통합 초안·archive·구 225화 전체 압축본을 Google Drive 실제 원본보다 높은 권위로 취급하지 않는다.
- 라르고의 `[규율]`·최상위 전투력을 1부/2부 본편에서 객관적으로 공개하지 않는다.
- 하템 사후의 새 정보·새 주문·실제 물리 행위를 허용하지 않는다. 사후 하템은 이안의 환각/환청이며 이안이 모르는 새 정보를 제공하지 않는다.
