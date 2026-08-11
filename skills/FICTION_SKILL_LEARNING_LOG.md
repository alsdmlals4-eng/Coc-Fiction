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

## 2026-08-10 — stale PR 회수와 Base 공용 연재소설 책임 재사용

- 오래된 PR #9는 현재 main보다 뒤처져 있어 branch 전체를 살리지 않았다. #9의 고유 2파일 delta를 최신 main 위에서 재구성한 #12와 patch를 비교하고 동일한 `serial-arc-pass`만 기존 `fiction-revision-and-validation`에 흡수했다.
- Base에 `developing-and-revising-serial-fiction`이 생겼다고 프로젝트의 5개 Skill을 복제·대체하지 않는다. Reader Promise·Episode Value·POV/voice·payoff 같은 공용 작법은 Base에서 재사용하고, source-log·Canon·합성 색인·override·Scene Pass Registry 같은 작품 고유 전파는 프로젝트 mode가 소유한다.
- 대화/파일 산출물이 최신이어도 GitHub 원고 정본에 전파됐다는 증거가 없으면 `EXTERNAL_ARTIFACT`와 `GITHUB_CANON`을 분리한다. 파일명에 `최종`이 들어간다는 이유로 정본 상태를 자동 승격하지 않는다.
- 한 화에서 여러 POV를 쓰는 경우 숫자 자체보다 **새 시점이 다른 정보·가치 판단·감정·외부 평가를 실제로 추가하는지**를 먼저 본다. 조연·엑스트라도 독립 시점의 기능이 있으면 사용할 수 있지만, 무표식 head-hopping은 피한다.
- 작품별 `1~3 POV` 같은 production value는 프로젝트 규칙이며 Base 공용 규칙으로 승격하지 않는다.

## 2026-08-11 — 캐릭터 개성·상대 위상과 원본 기능 복원

- 사용자 승인으로 `fiction-story-development: character-and-opponent-integrity`와 `fiction-revision-and-validation: character-opponent-integrity`를 정규 mode로 추가했다. 새 broad Skill은 만들지 않고 Base 공용 원칙을 프로젝트 정본·원본 비교 절차에 연결했다.
- 원본은 Google Drive의 실제 로그/원본 문서이고, 225화 압축 초안은 별도 비교자료다. `최신 사용자 Decision → 원본/원본사건감사 → 활성 원고 → 225화 초안 → 구형 기획·archive` 순으로 충돌을 판정한다.
- 설정상 강하다고 적힌 인물이 실제 장면에서는 소문·전투 흔적만 남으면 독자는 강함을 체감하지 못한다. 황진청처럼 빈칸이 있는 경우 `NEW` 장면을 허용하되 원본 결과와 주연 결정권을 침범하지 않는다.
- 팽무악처럼 원본/225화에 실제 검술 위상 기능이 있었는데 압축 과정에서 빠진 경우 신규 설정을 덧대기보다 `RESTORE`가 우선이다. 원문 문장을 복제하는 것이 아니라 사건 기능·관계 변화·위상 증명을 최신 Canon에 맞게 복원한다.
- 주인공을 강하게 보이게 하려고 적대자의 판단력·훈련·위험성을 낮추면 상대뿐 아니라 승자의 위상도 함께 무너진다. 중요 상대는 최소 한 번 `own turn`으로 자기 규칙을 강제하고 실제 성공·비용을 남긴다.
- 여러 강자는 같은 화력 서열이 아니라 서로 다른 문제 해결 방식으로 분리한다. 황진청의 읽기·회피·능글맞음과 팽무악의 순수 축적 검술처럼 대표 하이라이트가 교환되지 않게 한다.
- 라르고는 1부에서 윌리엄의 평범한 비서로 보이고, 주안 이탈 뒤 8년 동안 엘리스의 실제 교관이 된다. 라르고의 호감은 비서 시절의 선행 짝사랑이 아니라 **엘리스를 직접 가르치고 성장과 선택을 오래 지켜보는 과정에서 생긴 감정**으로 정본화한다.
- 라르고는 엘리스가 주안을 사랑함을 알고도 경쟁·정보 차단을 하지 않는다. `좋아하니까 대신 결정하지 않는다`는 태도는 윌리엄의 보호 논리와 대비되며, 실제 `[규율]` 공개는 Rift Accord 외전까지 지연한다.

## 다음 재검토 조건

- 제1~105화 최신 외부 통합본을 GitHub manuscript/source/canon과 회차별로 대조해 실제 정본 delta를 회수한다.
- `006-010`은 확보된 1부 원본으로 재감사한다.
- 보류된 `176-180` 원본 직접 대조는 001-105 최신본의 GitHub 정본화 이후 우선순위를 다시 판정한다.
- 황진청·팽무악 전투 보강 시 원본 결과, 주연 결정권, 상대 위상 장부를 함께 회귀검사한다.
- 다른 장편 프로젝트에서도 `설정상 강자지만 약해 보임` 또는 `주인공 승리를 위해 적이 바보가 됨` 문제가 반복되면 Base 공용 mode의 두 번째 프로젝트 pilot 근거로 승격한다.
