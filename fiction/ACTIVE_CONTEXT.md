# ACTIVE CONTEXT

갱신: 2026-07-23

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- 주 Skill: `fiction-revision-and-validation: scene-diagnostic / continuity-check / adversarial-loop / regression-check / pr-review`
- 보조 Skill: `fiction-drafting: approved-rewrite / pov-and-distance / action-and-reaction / rhythm-and-voice`, `fiction-canon-and-research: canon-audit / reference-freshness`, `fiction-story-development: representative-chapter-gate / stress-test`, `fiction-project-operations: checkpoint / handoff / execution-report`

## 완료

- 제1화~제225화 최신 확장 원고와 45개 5화 묶음 유지
- 화별 제목·POV·분량·본문 SHA 색인과 구조 역개요 기준선 유지
- 대표 품질 게이트 12화 선정 및 수동 1차 판정
- 제10화·제95화·제180화 파일럿 scene diagnostic 수행
- 제10화의 보호 반응을 같은 자아의 내부 상태로 명료화하고 정신·육체 후유증 연결
- 제95화에 중복돼 있던 외전 종결 기능을 하나의 장면 흐름으로 통합
- 제180화의 환자 동의·중단 권한·장비 출처·기록 귀속 순서를 재구성
- 제177화~제225화에 전파된 비정본 임시 국제조직 장기축을 현행 2부 바이블의 기관·권한 구조로 교체
- 변경된 26개 화의 분량·SHA와 225화 역개요 재생성
- 폐기 명칭·구형 문서 ID·구형 편성·비정본 세력명 재등장 방지 검사 강화

## 현재 원고 상태

- 화수: 225
- 편집 묶음: 45
- 본문 최소: 2,045자
- 본문 최대: 3,946자
- 본문 평균: 약 2,321자
- 상태: `확장 원고 DRAFT / 구조 역개요 기준선 완료 / 대표 3화 파일럿 완료 / 원본 전체 감사 전`

파일럿은 사건 순서·동행·결말을 바꾸지 않는 최소 수정으로 수행했다. 원본 PDF·텍스트 본체는 현재 Drive와 파일 라이브러리에서 찾지 못했으므로 직접 원문 충실도는 계속 `UNVERIFIED`다.

## 파일럿에서 확정한 적용 규칙

1. 내부 보호 반응은 별개 존재처럼 확정하지 않고 같은 자아의 상태·기능으로 표현한다.
2. 외전 결말은 이미 앞 화에서 정한 기한·설명을 반복하지 않고, 다음 행동과 남은 모순을 장면으로 닫는다.
3. 의료 장면은 `환자 동의 → 중단 권한 → 장비 출처·보관 → 검사 → 이상 → 기관 충돌 → 현재 몸 확인` 순서로 읽히게 한다.
4. 장비 제공·보관·기술 운용·증거보전·의료 중단 권한을 한 조직에 몰아주지 않는다.
5. Canon에서 폐기된 세력을 이름만 바꾼 장기 조직으로 복원하지 않는다.

## 남은 구조 우선순위

1. 외전1 제71화~제94화의 장문단 밀집과 낮은 대사 비중
2. 외전2 제96화~제100화의 시간 전환·설명 밀도
3. 외전3·2부의 주제어 직접 설명 집중
4. 2부 중반의 절차·책임 논점 반복 위험
5. 제96화·제166화의 시간·POV 구간 인계

## 다음 정확한 작업

파일럿 규칙을 인접 5화 묶음에 적용해 `006-010 → 091-095 → 176-180` 순으로 전체 장면 카드를 수동 확정한다. 각 묶음에서 사건·인과·POV·동선·부상·정보 상태를 검수한 뒤 승인된 최소 수정만 수행한다.

## 변경 금지

`FICTION_MASTER.md`와 `CANON_REGISTRY.json`의 변경 금지 항목을 따른다. 자동 역개요와 통계 플래그를 원고 수정 명령으로 사용하지 않는다. 원고 수정 시 `MANUSCRIPT_INDEX.json`, 역개요, Revision Report를 같은 커밋에서 갱신한다.
