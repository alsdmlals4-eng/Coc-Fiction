---
name: fiction-canon-and-research
description: 설정·인물·연표·지식 상태의 Canon과 자료 출처를 관리하고, 참고문장·연출에서 저작권 안전한 추상 기법만 추출하며 참조 최신성을 검증한다.
---

# Fiction Canon and Research

## Modes

`canon-audit | canon-update | continuity-map | timeline-and-state | fact-research | reference-card | source-log | copyright-boundary | reference-freshness`

## Canon 상태

`CANON / PROPOSED / DRAFT / RETCON_PENDING / SUPERSEDED / UNVERIFIED`

사용자 승인 없이 `PROPOSED`·`DRAFT`를 `CANON`으로 승격하지 않는다. `SUPERSEDED`는 현행 읽기 경로에서 제외하되 Git 이력과 대체 근거를 남긴다.

## Continuity dimensions

- 날짜·시간·이동 시간·계절
- 인물 나이·외형·말투·능력·부상
- 관계·약속·비밀·감정 상태
- 인물별 지식과 오해
- 소지품·자원·증거·문서
- 장소 구조와 출입 가능성
- 세계 규칙·금기·비용·예외
- 사건 원인·결과·목격자
- POV·시제·고유명사·호칭
- 복선·회수·미해결 질문

중요 장면마다 변경된 상태를 기록하고 다음 장면이 이전 상태를 올바르게 소비하는지 확인한다.

## 자료 조사

증거 유형을 구분한다.

1. `PRIMARY`: 공식 기록·원문·법령·논문·당사자 자료
2. `AUTHORITATIVE_SECONDARY`: 전문 기관·학술 해설
3. `GENERAL_SECONDARY`: 신뢰 가능한 개요
4. `COMMUNITY_RESPONSE`: 독자 반응·경험
5. `FICTION_REFERENCE`: 연출·문장·플롯 참고

사실 주장은 날짜·지역·판본·불확실성을 기록한다. 시대·의학·법률·역사처럼 정확도가 중요한 내용은 최신 1차·권위 자료로 교차 확인한다.

## 참고문장·연출

`docs/fiction-ops/REFERENCE_CARD_TEMPLATE.md`를 사용한다.

- 사용자 제공·퍼블릭 도메인·허용된 자료를 우선한다.
- 저작권 자료는 비평에 필요한 최소 발췌만 사용한다.
- 문장의 고유 어휘·비유·리듬을 복제하지 않는다.
- `기능 / 장치 / 효과 / 전이 가능한 원리 / 모사 금지 요소`를 분리한다.
- 외부 플롯을 이름만 바꿔 이식하지 않는다.
- 특정 현존 작가의 스타일 모사 요청은 더 일반적인 특성으로 변환한다.

## Reference freshness

정본·파일명·장면 ID·인물명·용어·연표·결말 방향을 바꾸면 changed file뿐 아니라 다음을 확인한다.

- 장면 목록·장면 카드·원고의 untouched 소비자
- 복선·회수·대사·호칭
- Style Guide·용어집·연표
- 테스트·검수표·현재 상태·Handoff
- 오래된 링크·별칭·파생본

## Output

```md
## Canon 판정과 근거
## 충돌·RETCON_PENDING
## 연표·상태 변경
## 조사 출처·날짜·신뢰도
## 참고 기법과 저작권 경계
## 갱신한 소비자와 untouched 검사
## 미검증·사용자 결정
```

## Quality gate

외부 자료로 Canon을 덮어쓰거나, 출처 없이 사실을 확정하거나, 인물별 지식 상태를 전지적 작가 지식과 혼동하거나, 긴 저작권 원문을 저장하거나, 변경된 이름·사실의 소비자를 놓치면 실패다.

Learning Log: `skills/FICTION_SKILL_LEARNING_LOG.md`
