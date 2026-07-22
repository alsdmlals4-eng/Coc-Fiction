# ACTIVE CONTEXT

갱신: 2026-07-22

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- 주 Skill: `fiction-revision-and-validation: structural-reverse-outline / scene-diagnostic / adversarial-loop / regression-check / pr-review`
- 보조 Skill: `fiction-story-development: plot-and-causality / representative-chapter-gate / stress-test`, `fiction-canon-and-research: canon-audit / reference-freshness`, `fiction-project-operations: checkpoint / handoff / execution-report`

## 완료

- 소설 운영 Skill 5개를 `main`에 병합
- 최신 통합 문서와 별도 압축 초안의 최신성 충돌 판정
- 최신 통합 문서에서 제1화~제225화 원고를 다시 추출
- 225화 전부 본문 2,000자 이상 확인
- 5화 단위 편집 원고 45개와 화별 SHA·분량 색인 생성
- 활성 원고의 폐기된 2부 세력·인명 0건 확인
- 작품 코어 계약·Canon Registry·Style Guide·부별 바이블 설치
- 구형 편성과 구 Google Docs를 비활성 자료로 격리
- 새 현행 기획서와 활성 인수인계 Google Docs 생성·본문 읽기 검증
- 자동 검사로 번호·분량·원문 SHA·금지 명칭·구형 문서 ID·JSON 검증
- 제1화~제225화 구조 역개요의 재현 가능한 추출 기준선 생성
- 각 화의 제목·POV·분량·본문 SHA·묶음 경로를 역개요와 재대조
- 대표 품질 게이트 12화 선정 및 수동 1차 판정
- 부·외전별 문단 밀도·대사 비중·주제 직접표현 분포 진단

## 현재 원고 상태

- 화수: 225
- 편집 묶음: 45
- 본문 최소: 2,045자
- 본문 최대: 3,946자
- 본문 평균: 약 2,319자
- 상태: `확장 원고 DRAFT / 구조 역개요 기준선 완료 / 원본 장면 감사 전`

역개요의 증거 필드는 현행 원고 문장을 자동 추출한 탐색 기준선이다. 최종 장면 카드나 수정 명령이 아니며, 원본 로그 대조와 대표 화 scene diagnostic을 거쳐야 한다.

## 확인된 구조 우선순위

1. 외전1 제71화~제95화의 장문단 밀집과 낮은 대사 비중
2. 외전2 제96화~제100화의 시간 전환·설명 밀도
3. 외전3·2부의 주제어 직접 설명 집중
4. 2부 제179화~제195화와 제203화~제221화의 절차·책임 논점 반복 위험
5. 제96화·제166화의 시간·POV 구간 인계

현재 단계에서 확정적인 Canon 붕괴나 화수·SHA 불일치는 발견되지 않았다.

## 대표 품질 게이트

제1·3·10·20·70·95·130·165·166·180·200·225화를 사용한다. 상세 판정은 `analysis/REPRESENTATIVE_CHAPTER_GATES.md`가 책임진다.

## 다음 정확한 작업

제10화·제95화·제180화를 파일럿으로 원본 장면과 대조하고 `scene-diagnostic → continuity-check → adversarial-loop`를 수행한다. 사용자 승인 범위 안에서만 최소 수정하며, 수정 시 원고·분량·SHA·Revision Report를 함께 갱신한다.

## 변경 금지

`FICTION_MASTER.md`와 `CANON_REGISTRY.json`의 변경 금지 항목을 따른다. 자동 역개요의 추출 문장을 근거로 원고를 기계적으로 수정하지 않는다. `MANUSCRIPT_INDEX.json`의 본문 SHA를 바꾸는 수정은 승인 범위와 Revision Report 없이 수행하지 않는다.
