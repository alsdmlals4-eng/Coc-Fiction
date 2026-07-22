# Coc-Fiction Skill Learning Log

반복 가능한 실제 교훈만 기록한다.

## 2026-07-22 — Base 소설용 분화

- 사용: `PLAN → BUILD → REVIEW`
- 결과: 공용 운영·정본·코어·가지치기·적대적 검토 기능을 5개 소설 Skill로 통합.

## 2026-07-22 — 최신 원고 판별과 정본 복구

- 사용: `BUILD → REVIEW` / `fiction-canon-and-research: canon-audit, canon-update, reference-freshness` / `fiction-revision-and-validation: continuity-check, adversarial-loop, regression-check, pr-review`.
- 상황: 통합 문서와 별도 압축 초안이 동시에 존재했고 제목만으로는 어느 원고가 최신인지 판단하기 어려웠다.
- 발견한 실패: 별도 압축 초안을 먼저 사용해 구형 상태를 기반으로 산출물을 만들었으나 게시 전 전수 비교에서 통합 문서 안에 225화 최신 확장 원고가 있음을 확인했다.
- 실제 변경: 임시 산출물을 폐기하고 최신 통합 원고에서 225화를 다시 추출했으며 화별 SHA·분량 색인을 추가했다.
- 검증·증거: 225화 모두 2,000자 이상, 45개 묶음, 폐기 명칭 0건, 원문 SHA 일치.
- 재사용 가능한 교훈: 파일명이나 인수인계 상태만으로 최신성을 추정하지 않는다. 동일 화수 원고가 여러 곳에 있으면 `수정 시각 → 실제 분량 → 내용 차이 → Canon 잔존어 → 사용자 완료 선언`을 함께 비교한다.

## 2026-07-22 — 225화 역개요와 대표 품질 게이트

- 사용: `REVIEW` / `fiction-story-development: plot-and-causality, representative-chapter-gate, stress-test` / `fiction-revision-and-validation: structural-reverse-outline, scene-diagnostic, adversarial-loop, regression-check, evidence-report` / `fiction-canon-and-research: reference-freshness`.
- 상황: 225화의 분량과 SHA는 검증됐지만 어느 구간부터 어떤 기준으로 심화 퇴고할지 구조적 우선순위가 없었다.
- 실제 변경: 원고를 건드리지 않고 모든 화의 구조 증거를 추출한 역개요 JSON, 부별 진단 보고서, 대표 게이트 12화를 만들었다.
- 재사용 가능한 교훈: 장편 역개요는 `재현 가능한 추출 기준선 → 대표 화 수동 판정 → 원본 장면 대조 → 5화 단위 확장` 순서가 안전하다. 정량 플래그는 수동 검토 신호이지 자동 수정 명령이 아니다.

## 2026-07-23 — 대표 3화 파일럿과 Canon 소비자 전파

- 사용: `REVIEW → BUILD → REVIEW` / `fiction-revision-and-validation: scene-diagnostic, continuity-check, adversarial-loop, regression-check, evidence-report, pr-review` / `fiction-drafting: approved-rewrite, pov-and-distance, action-and-reaction, rhythm-and-voice` / `fiction-canon-and-research: canon-audit, continuity-map, source-log, reference-freshness`.
- 상황: 제10·95·180화 파일럿을 검토하던 중 제95화의 중복 결말과 2부 여러 회차에 남은 비정본 장기 조직 기능을 발견했다.
- 실패 원인: 폐기된 고유명사만 검사하고 협상·장비 공급·장기 회수라는 **기능적 복원**은 검사하지 않았다. 이름이 바뀌어도 책임·권한 구조가 같으면 Canon 폐기가 완료된 것이 아니다.
- 실제 변경: 제10화의 동일 자아 보호 반응과 후유증 연결, 제95화의 중복 종결 통합, 제180화의 동의·중단·장비 권한 재배치, 제177화~제225화 소비자 전파 교정을 수행했다.
- 검증·증거: 변경 26화의 분량·SHA 재색인, 225화 역개요 재생성, 모든 화 2,000자 이상, 폐기 별칭 활성 원고 0건.
- 재사용 가능한 교훈 1: `reference-freshness`는 단어 검색뿐 아니라 `누가 장비를 주는가 / 누가 보관하는가 / 누가 중단하는가 / 누가 증거를 가진가` 같은 기능 그래프를 검사해야 한다.
- 재사용 가능한 교훈 2: 대표 화 수정 중 인접·후속 소비자에서 같은 오류가 발견되면 한 화만 고치지 말고 영향 범위를 먼저 확정한다.
- 재사용 가능한 교훈 3: 원본 파일명이 알려져도 본체가 없으면 원본 대조 완료로 표시하지 않는다. 파생본은 사건 뼈대 비교에만 사용하고 정본 권한을 주지 않는다.
- Skill·reference 변경: Style Guide에 파일럿 규칙을 추가하고 콘텐츠 검사 금지 목록을 Canon Registry에서 읽도록 변경했다.
- 다음 재검토 조건: `006-010`, `091-095`, `176-180` 묶음 전체 수동 장면 카드 완료 후 규칙의 과잉 일반화 여부를 재평가한다.
