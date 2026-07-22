# Coc-Fiction Skill Learning Log

반복 가능한 실제 교훈만 기록한다.

## 2026-07-22 — Base 소설용 분화

- 사용: `PLAN → BUILD → REVIEW`
- 결과: 공용 운영·정본·코어·가지치기·적대적 검토 기능을 5개 소설 Skill로 통합.

## 2026-07-22 — 최신 원고 판별과 정본 복구

- 사용: `BUILD → REVIEW` / `fiction-canon-and-research: canon-audit, canon-update, reference-freshness` / `fiction-revision-and-validation: continuity-check, adversarial-loop, regression-check, pr-review`.
- 상황: 통합 문서와 별도 압축 초안이 동시에 존재했고 제목만으로는 어느 원고가 최신인지 판단하기 어려웠다.
- 발견한 실패: 별도 압축 초안을 먼저 사용해 구형 상태를 기반으로 산출물을 만들었으나, 게시 전 전수 비교에서 통합 문서 안에 225화 최신 확장 원고가 있음을 확인했다.
- 실제 변경: 임시 산출물을 폐기하고 최신 통합 원고에서 225화를 다시 추출했으며, 화별 SHA·분량 색인을 추가했다.
- 검증·증거: 225화 모두 2,000자 이상, 45개 묶음, 폐기 명칭 0건, 원문 SHA 일치.
- 재사용 가능한 교훈: 파일명이나 인수인계 상태만으로 최신성을 추정하지 않는다. 동일 화수 원고가 여러 곳에 있으면 `수정 시각 → 실제 분량 → 내용 차이 → Canon 잔존어 → 사용자 완료 선언`을 함께 비교한다.
- 작품 고유 정보와 공용 원리의 경계: 2부 세력명은 작품 고유 Canon이며, 다중 원고 최신성 판별과 SHA 색인은 다른 장편 프로젝트에도 적용 가능하다.
- Skill·reference 변경 여부: `reference-freshness`에 화별 내용 해시와 파생본 최신성 비교를 실제 운영 규칙으로 적용.
- 미검증·다음 재검토 조건: 원본 로그 전체 장면 대조, 대표 화 심화 퇴고, 독자 테스트.
