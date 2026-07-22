# 《폭풍의 눈》 제1화~제225화 구조 역개요 보고서

상태: **ACTIVE ANALYSIS / COMPOSED STRUCTURAL BASELINE**  
갱신: 2026-07-23

## 1. 판정 범위

현행 원고 45개 묶음과 합성된 `MANUSCRIPT_INDEX.json`·`REVERSE_OUTLINE_001_225.json`을 사용한다. 대형 기계 데이터는 고정 baseline과 승인된 묶음 override를 `tools/fiction_composed_data.py`로 합성하며 baseline을 직접 작업 입력으로 사용하지 않는다.

## 2. 사용 Skill·mode

- `fiction-project-operations`: `route`, `contract`, `checkpoint`, `handoff`, `execution-report`
- `fiction-story-development`: `scene-card`, `plot-and-causality`, `stress-test`
- `fiction-revision-and-validation`: `structural-reverse-outline`, `scene-diagnostic`, `continuity-check`, `adversarial-loop`, `regression-check`, `pr-review`
- `fiction-canon-and-research`: `timeline-and-state`, `continuity-map`, `source-log`, `reference-freshness`
- `fiction-drafting`: `approved-rewrite`, `pov-and-distance`, `action-and-reaction`

## 3. 검증 결과

- 화수 225화, 원고 묶음 45개, 중복·누락 없음
- 제목·POV·분량·묶음 경로·본문 SHA가 합성 색인 및 역개요와 일치
- 대표 품질 게이트 12화 유지
- 제6·7·9화만 추가 갱신하고 제8·10화와 나머지 220화 SHA 보존
- 원본 Drive 폴더 접근 불가로 직접 사건 충실도 `UNVERIFIED`

## 4. 부·외전별 정량 기준선

| 구간 | 화수 | 주요 검토 신호 |
|---|---:|---|
| 1부 | 70 | 초반 병행 시간선·후반 주제 설명 |
| 외전1 | 25 | 제71~94화 장문단 밀집 |
| 외전2 | 35 | 제96~100화 시간 전환·설명 밀도 |
| 외전3 | 35 | 주제어 직접 설명 집중 |
| 2부 | 60 | 절차·책임 논점 반복 위험 |

정량 신호는 결함 판정이 아니라 수동 검토 우선순위다.

## 5. 전체 구조 지도

1. 제1~10화: 출항과 파열 — 금서 반응, 황색 침투, 식당 학살, 세실리아 납치, 거짓 무전과 전투
2. 제11~20화: 표류와 선택 구조 — 섬의 규칙과 제3의 선택 가능성
3. 제21~70화: 왕·가족·자아 충돌에서 쇼거스전·협상·복종인자 폭로·주안 이탈까지
4. 제71~95화: 기억을 씻는 안전을 거부하고 다음 장소를 직접 고르는 외전1
5. 제96~130화: 엘리스가 레드퀸이 되고 강요하지 않는 연결을 선택하는 외전2
6. 제131~165화: 이안과 엘리엇의 지식·기록·통제 갈등
7. 제166~225화: 다빈의 선택권을 둘러싼 의료·기관·미래 갈등과 불확실한 결말

## 6. Finding-first 판정

### MUST_FIX — RESOLVED

- 2부 비정본 장기 세력 기능을 현행 권한 분산 구조로 교체
- 제5→6화 시간 되감기 무표지를 제6화 첫 문장 앵커로 교정
- 제9화에서 제5화의 아킴 승선을 다시 시작하던 중복 동선을 제거

### SHOULD_FIX — RESOLVED FOR CURRENT SCOPE

- 제7화 `다른 자신`을 같은 자아의 차가운 보호 반응으로 명료화

### SHOULD_FIX — REMAINING

- 제71~94화 장문단 밀집
- 제96~100화 시간·설명 밀도
- 외전3·2부의 행동 뒤 주제 재설명
- 2부 중반 절차·책임 기능 반복
- 제96·166화 구간 진입 인계

### REJECT

- 제8화의 흰 방 잔향과 제10화의 직접 정신 공격 통합: 설치→확대로 기능이 전진하므로 유지
- 정량 플래그에 맞춘 전 화 문체 평균화: 작품별 리듬을 훼손하므로 금지

### UNVERIFIED

사용자 제공 원본 Drive 폴더가 현재 연결 계정에서 열리지 않는다. 원본 대사·세부 동선·사건 순서의 직접 대조는 완료로 표시하지 않는다.

## 7. 대표 품질 게이트

제1·3·10·20·70·95·130·165·166·180·200·225화를 유지한다. 현재 판정은 `REPRESENTATIVE_CHAPTER_GATES.md`가 책임진다.

## 8. 완료된 묶음

- 대표 파일럿: 제10·95·180화
- 첫 전체 묶음: `006-010`
- 수동 장면 카드: `SCENE_CARDS_006_010.md`
- 완료·다음 묶음과 SHA: `SCENE_PASS_REGISTRY.json`

## 9. 다음 정확한 작업

1. `091-095` 묶음과 제90·96화 경계를 검수한다.
2. 이후 `176-180` 묶음과 제175·181화 경계를 검수한다.
3. 동일 결함이 확인된 경우에만 파일럿·묶음 규칙을 적용한다.
4. 원고 수정 시 색인·역개요 override·Scene Pass Registry·Revision Report를 같은 PR에서 갱신한다.
