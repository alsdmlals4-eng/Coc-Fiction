---
name: fiction-project-operations
description: Coc-Fiction 요청을 PLAN·BUILD·REVIEW와 원고 단계로 라우팅하고, 동시 채팅 충돌을 피하며 작업 계약·순서·체크포인트·PR 인수인계를 관리한다.
---

# Fiction Project Operations

## Modes

`route → contract → coordinate-concurrent-work → decompose-and-sequence → checkpoint → handoff → execution-report`

필요한 mode만 실행한다.

## 핵심 규칙

- 최신 `main`, 열린 PR, 현재 브랜치와 겹치는 파일을 작업 전·PR 전에 확인한다.
- 원고·설정 이전 브랜치와 운영체계·퇴고 브랜치를 분리한다.
- 사용자는 Skill·mode를 고를 필요가 없다.
- 작업의 주 Work Mode와 주 전문 Skill은 각각 하나로 둔다.
- 사용자 승인 없이 작품 코어·결말·인물성·문체·대량 파일 구조를 확정하거나 변경하지 않는다.
- 긴 작업은 검증 가능한 결과 단위와 재개 가능한 checkpoint를 남긴다.
- 비동기 완료·시간 예측을 약속하지 않고 현재 응답에서 실제 결과를 남긴다.

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

## Output

```md
## Work Mode·Stage·선택 Skill과 이유
## 범위·제외·보호 대상
## 동시 작업 상태와 겹치는 파일
## 완료한 결과·변경 파일
## 검증·증거
## 미검증·충돌·롤백
## 다음 정확한 작업
```

## Quality gate

반복 질문, 사용자 확인 없는 대규모 변경, force push, 다른 브랜치 원고 덮어쓰기, 진행 중을 완료로 표시, checkpoint 없는 장기 작업은 실패다.

Learning Log: `skills/FICTION_SKILL_LEARNING_LOG.md`
