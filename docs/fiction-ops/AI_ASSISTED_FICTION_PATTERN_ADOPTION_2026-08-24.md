# COC-Fiction · AI-Assisted Production Pattern Adoption — 2026-08-24

```yaml
status: USER_DIRECTED_ADAPTATION
work_mode: REVIEW_PLAN
runtime_gameplay: NOT_APPLICABLE
manuscript_mutation: NONE
source_base_merge: dff09d83c3892a70ba5fee86a59d36086889a6c5
open_pr_50: READ_ONLY_DO_NOT_TOUCH
whole_manuscript_continuity: NOT_YET_CLAIMED
```

## 결론

COC-Fiction은 게임 런타임 프로젝트가 아니다. 따라서 RNG/gameplay/runtime AI 패턴은 적용하지 않는다.

이번 흡수는 AI-assisted 제작 사례에서 확인한 **사람 주도 생성·누락 검증·맥락 예산·breadth 제한·player-visible output quality**를 장편 소설의 bounded revision/reconciliation 흐름에 맞게 변형한다.

현재 진행 중 PR #50의 Ch031–035 원고/정사/continuity 범위는 read-only로 유지한다.

## 판정

| Pattern | 판정 | COC-Fiction 적용 |
|---|---|---|
| HUMAN_DIRECTED_AI_BUILD_LOOP | ADOPT_HIGH | AI 초안/분석은 revision input, Canon 승격은 bounded human-directed reconciliation |
| SILENT_OMISSION_GATE | ADOPT_HIGH | 장면 목표/반응/멈춤/이유/선택/복선/귀속/consumer 누락 검사 |
| CONTEXT_SCOPE_AND_ARCHITECTURE_BUDGET | ADOPT_HIGH | 긴 채팅보다 Canon Registry + Scene Pass + current frontier 재수화 |
| BREADTH_AFTER_CORE_IDENTITY_LOCK | ADAPT_HIGH | 대량 화수 재작성보다 5화 bounded promotion 유지 |
| PLAYER_FEEDBACK_REBUILD_LOOP | ADAPT | 독자 반응은 evidence이며 Canon 자동 변경 금지 |
| AI_VISIBLE_OUTPUT_QUALITY_GATE | ADOPT | AI-assisted cover/reference/삽화 사용 시 consistency/rights/approval Gate |
| RNG_AGENCY_AND_RECOVERY | NOT_APPLICABLE | 게임 시스템 아님 |
| runtime generative AI | NOT_APPLICABLE | 제품 runtime 없음 |

## HUMAN_DIRECTED_AI_REVISION_LOOP

```text
current Canon + production frontier 재수화
→ 이번 bounded 장면/화 목표
→ AI 분석/초안/revision candidate
→ changed-scene audit
→ continuity / character / clue / ownership 검사
→ 사람의 서사·감정·문체 판단
→ accept | revise | reject
→ Scene Pass / registry / receipt 갱신
```

AI output은 `revision input`이며 스스로 production authority가 되지 않는다.

## SILENT_OMISSION_GATE

각 장면/화 revision 뒤 최소 다음을 공격한다.

- 장면이 무엇을 바꾸어야 하는지 빠졌는가.
- 주안의 `반응 → 멈춤 → 이유 → 선택` 중 한 단계가 사라졌는가.
- 캐릭터가 Canon상 알 수 없는 정보를 갑자기 아는가.
- 기존 복선/단서/귀속 관계의 consumer가 빠졌는가.
- D01/D02/D03/N04 및 공동봉인 규칙이 회귀했는가.
- `엘리스` 표기와 인물 identity가 drift했는가.
- 장면을 매끄럽게 만들면서 의도적 불편함/긴장/정보 제한을 삭제했는가.
- current prefix와 legacy tail을 근거 없이 연속으로 간주했는가.

## CONTEXT_SCOPE_AND_PROVENANCE_BUDGET

장편 작업에서 “모델이 긴 대화를 기억하도록” 의존하지 않는다.

```text
fiction/ACTIVE_CONTEXT.md
+ CANON_REGISTRY
+ SCENE_PASS_REGISTRY
+ CURRENT_STATE_RECEIPT
+ 현재 5화 packet
+ 필요한 실제 manuscript
```

만 재수화하고, 범위를 벗어난 전체 원고를 무조건 context에 넣지 않는다. context가 커져 drift가 생기면 더 큰 prompt보다 책임 범위를 줄인다.

## Breadth Gate

현재 5화 bounded promotion을 유지한다.

```text
5화 candidate
→ RED/focused continuity contract
→ bounded reconciliation
→ exact validation
→ main promotion/readback
→ 다음 묶음
```

AI로 30~100화를 한 번에 재작성하는 방식은 production default로 채택하지 않는다. 속도보다 frontier/provenance/rollback 가능성이 우선이다.

## 독자 피드백 경계

독자 반응은 다음을 찾는 evidence로 사용한다.

```text
CLARITY
PACING
EMOTIONAL_PAYOFF
CHARACTER_CREDIBILITY
FORESHADOW_VISIBILITY
```

그러나 작은 표본의 선호가 Canon이나 장기 플롯을 자동 변경하지 않는다. 반복 신호가 생기면 현재 Scene/Arc 목표와 충돌 여부를 검토한 뒤 별도 revision decision으로 승격한다.

## AI-visible output Gate

향후 표지/삽화/reference를 AI-assisted로 만들 경우:

- 정사 인물 identity/style consistency.
- 장면/시대/소품의 Canon 일치.
- 권리/provenance/reference independence.
- 사람 승인 전 production asset 승격 금지.
- 전체 이미지 반복 생성보다 승인된 개별 요소 조립/검수 우선.

## 현재 PR #50 보호

이 문서는 Ch031–035의 원고, Scene Card, revision report, frontier data를 수정하지 않는다. PR #50은 별도 current workstream이며 그대로 진행한다.

## IRG

현재 주장 가능: AI-assisted fiction production의 bounded workflow 계약이 문서화됨.

현재 주장 불가: PR #50 완료, Ch031–035 승격, whole-manuscript continuity 완료, 독자 반응 개선, AI visual asset 승인.

## 적대적 검토 5회

1. 게임 패턴을 소설에 억지 적용하지 않음: PASS.
2. AI candidate와 production authority 분리: PASS.
3. open PR #50 원고 범위 무변경: PASS.
4. 5화 bounded frontier 유지: PASS.
5. whole-manuscript continuity 과장 없음: PASS.

`CLEAN_REVIEW_EXIT`.
