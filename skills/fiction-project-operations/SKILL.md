---
name: fiction-project-operations
description: Coc-Fiction 요청을 PLAN·BUILD·REVIEW와 원고 단계로 라우팅하고, 동시 채팅 충돌을 피하며 작업 계약·순서·체크포인트·외부 산출물 승격·PR 인수인계를 관리한다.
---

# Fiction Project Operations

## Modes

`route → contract → coordinate-concurrent-work → decompose-and-sequence → checkpoint → artifact-promotion-gate → handoff → execution-report`

필요한 mode만 실행한다.

## 핵심 규칙

- 최신 `main`, 열린 PR, 현재 브랜치와 겹치는 파일을 작업 전·PR 전에 확인한다.
- 원고·설정 이전 브랜치와 운영체계·퇴고 브랜치를 분리한다.
- 사용자는 Skill·mode를 고를 필요가 없다.
- 작업의 주 Work Mode와 주 전문 Skill은 각각 하나로 둔다.
- 사용자 승인 없이 작품 코어·결말·인물성·문체·대량 파일 구조를 확정하거나 변경하지 않는다.
- 긴 작업은 검증 가능한 결과 단위와 재개 가능한 checkpoint를 남긴다.
- 비동기 완료·시간 예측을 약속하지 않고 현재 응답에서 실제 결과를 남긴다.
- 외부 DOCX/ZIP/PDF가 QA를 통과해 전달됐다는 사실과 GitHub production manuscript에 정본 승격됐다는 사실을 같은 완료 상태로 합치지 않는다.
- 파일명에 `최종`, `final`, `complete`가 있어도 사용자 Decision·Canon·원본·현재 repository topology 대조 없이 자동 정본 승격하지 않는다.

## 작업 계약

```yaml
objective:
manuscript_stage:
work_mode:
scope:
excluded_scope:
canonical_sources:
protected_core_and_prose:
concurrent_branches_and_overlap:
outputs:
acceptance_criteria:
validation:
rollback:
```

## 동시 작업 판정

- `SAFE_ADDITIVE`: 새 경로만 추가
- `SAFE_DISJOINT`: 기존 파일이지만 다른 작업과 무관
- `OVERLAP_REVIEW`: 같은 책임 원본 또는 소비자를 수정
- `DIVERGED`: 서로 다른 기준에서 같은 내용을 변경
- `BLOCKED`: 최신 상태·권한·정본을 확인할 수 없음

`OVERLAP_REVIEW` 이상이면 자동 덮어쓰지 않고 `KEEP / MERGE / UPDATE / DEFER` 처리표를 만든다.

## artifact-promotion-gate

외부 산출물을 사용자에게 전달하거나 새 채팅으로 인수인계할 때, **내용 완성/QA와 repository 정본 승격을 별도 축으로 기록**한다.

```yaml
artifact:
  filename:
  coverage:
  sha256:
  authority_and_sources:

delivery_state: DRAFT | QA_VERIFIED | DELIVERED
repository_promotion_state: NOT_REQUIRED | PENDING | PARTIAL | PROMOTED

repository:
  topology:
  promotion_target:
  verified_prefix_or_scope:
  migration_boundary:
  legacy_tail_or_debt:
  validation_gate:

resume:
  next_executable_step:
  resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
```

### 판정

- `QA_VERIFIED` 또는 `DELIVERED`는 외부 파일 자체의 검증/전달 상태다. 이것만으로 `PROMOTED`를 주장하지 않는다.
- `PENDING`: repository에 아직 승격하지 않았거나 승격 전략 자체가 다음 작업이다.
- `PARTIAL`: 검증된 prefix/범위만 정본 승격됐고 migration boundary 또는 legacy tail이 남아 있다.
- `PROMOTED`: 선언한 전체 promotion target이 현재 Canon·연속성·파생 consumer 검증을 통과했다.
- repository가 역사 보관/archive 역할만 하고 promotion이 필요 없는 경우에만 `NOT_REQUIRED`를 쓴다.
- staged migration에서는 검증되지 않은 경계 양쪽을 정상 연속으로 연결하지 않는다.
- delivery artifact의 해시·범위가 없거나 repository 상태를 확인할 수 없으면 해당 축을 `UNVERIFIED`로 보고 완료를 추정하지 않는다.

### Use when

- 외부 DOCX/ZIP/PDF가 최신 작업 산출물인데 GitHub 원고/Canon과 별도 lifecycle을 가진다.
- legacy 원고를 단계적으로 reconciliation 중이다.
- handoff에서 `원고는 끝났는데 저장소 정본화는 남음` 같은 두 상태를 동시에 보존해야 한다.

### Do not use when

- 산출물이 곧 repository current owner이고 같은 commit/검증으로 원자적으로 승격된다.
- archive/reference-only 자료라 current Canon promotion이 필요 없다.
- 단순 문장 교정처럼 외부 artifact와 repository lifecycle이 분리되지 않는다.

## Output

```md
## Work Mode·Stage·선택 Skill과 이유
## 범위·제외·보호 대상
## 동시 작업 상태와 겹치는 파일
## 완료한 결과·변경 파일
## 외부 산출물 delivery_state / repository_promotion_state
## 검증·증거
## 미검증·충돌·롤백
## 다음 정확한 작업
```

## Quality gate

반복 질문, 사용자 확인 없는 대규모 변경, force push, 다른 브랜치 원고 덮어쓰기, 진행 중을 완료로 표시, 외부 전달 완료를 GitHub 정본 승격 완료로 오인, checkpoint 없는 장기 작업은 실패다.

Learning Log: `skills/FICTION_SKILL_LEARNING_LOG.md`
