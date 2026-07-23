# Coc-Fiction Skill Learning Log

반복 가능한 실제 교훈만 기록한다. 상세 변경 증거는 각 `fiction/reports/REVISION_*.md`가 책임진다.

## 2026-07-22 — 소설용 Skill 분화

- `PLAN → BUILD → REVIEW`를 기준으로 운영·스토리 설계·집필·Canon·퇴고를 5개 Skill로 분리했다.
- 사용자는 Skill을 직접 고르지 않고 Registry가 최소 Skill을 라우팅한다.

## 2026-07-22 — 최신 원고 판별과 정본 복구

- 파일명이나 인수인계 상태만으로 최신성을 판단하지 않는다.
- 동일 화수 원고가 여러 개면 `수정 시각 → 실제 분량 → 내용 차이 → Canon 잔존어 → 사용자 완료 선언`을 함께 비교한다.
- 구 압축 초안 기반 임시 산출물을 폐기하고 최신 통합 원고에서 225화를 재추출했다.

## 2026-07-22 — 225화 역개요와 대표 게이트

- 장편은 `재현 가능한 추출 기준선 → 대표 화 수동 판정 → 원본 대조 → 5화 묶음 패스` 순서가 안전하다.
- 정량 플래그는 수동 검토 신호이며 자동 수정 명령이 아니다.

## 2026-07-23 — 대표 3화와 Canon 소비자 전파

- 폐기 고유명사뿐 아니라 장비 공급·보관·중단·증거 소유 같은 기능 그래프를 검사한다.
- 대표 화에서 후속 소비자까지 같은 오류가 발견되면 한 화만 고치지 않고 영향 범위를 먼저 확정한다.
- 원본 파일명이 알려져도 본체가 없으면 직접 대조 완료로 표시하지 않는다.

## 2026-07-23 — 첫 5화 묶음과 병행 시간선

- 사용: `fiction-revision-and-validation: scene-diagnostic, continuity-check, adversarial-loop, regression-check, pr-review`
- 보조: `fiction-story-development: scene-card, plot-and-causality, stress-test`, `fiction-canon-and-research: timeline-and-state, continuity-map, source-log, reference-freshness`, `fiction-drafting: approved-rewrite`
- 5화 묶음은 내부 화만 읽지 않고 직전·직후 화를 경계로 포함한다.
- 동일 사건을 다른 POV로 다시 보여주는 것과 이미 완료된 이동을 새 사건처럼 반복하는 것을 구분한다.
- 병행 장면이 더 이른 시점이면 첫 문단에 시간 앵커를 둔다.
- 결과: 제6화 시간 앵커, 제7화 동일 자아 표현, 제9화 중복 승선 교정. 제8·10화와 나머지 220화는 보존했다.

## 2026-07-23 — 원본 에필로그가 각색 장면으로 대체된 경우

- 사용: `fiction-canon-and-research: source-log / canon-audit`, `fiction-revision-and-validation: adversarial-loop / regression-check`, `fiction-story-development: scene-card`, `fiction-drafting: approved-rewrite`.
- 주제적으로 정교한 각색도 원본의 사건 순서·동행·결과·다음 이야기 인계를 대체하면 유지 근거가 부족하다.
- 원본 종결은 `source event map`을 먼저 만들고 현행 장면을 MATCH / ADAPTED / EXCLUDED로 판정한다.
- 원본에 있어도 최신 사용자 지시가 폐기한 축은 `ADAPTATION_EXCLUSION`으로 남기고 복원하지 않는다.
- 앞 화가 이미 이후 시간대에 도착했으면 선행 사건은 명시적 회상 앵커로 복원해 경계 SHA를 보존한다.
- 제한적 3인칭 패스에서는 다른 인물의 상태를 독자가 아는 사실이라는 이유로 현재 POV에 직접 넣지 않는다.

## 다음 재검토 조건

- `006-010`은 확보된 1부 원본으로 재감사한다.
- `176-180` 원본 직접 대조 뒤 의료·기관 절차 규칙의 과잉 각색 여부를 재평가한다.
