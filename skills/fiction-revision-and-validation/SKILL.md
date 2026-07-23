---
name: fiction-revision-and-validation
description: 원고를 구조·인과·연속성·장면·문장·교정 층으로 분리해 검토하고, 적대적 비판을 검증한 뒤 승인된 최소 수정과 회귀·PR 검수를 수행한다.
---

# Fiction Revision and Validation

## Modes

`contract-check | developmental-edit | structural-reverse-outline | serial-arc-pass | scene-diagnostic | continuity-check | line-edit | copyedit | proofread | reader-feedback | adversarial-loop | regression-check | evidence-report | pr-review`

한 번에 필요한 mode만 실행한다. `proofread`를 구조 검토보다 먼저 하지 않는다.

## Baseline

수정 전에 다음을 고정한다.

- 사용자 요청과 허용된 수정 층
- 작품 코어·Canon·Style Guide
- 현재 원고와 장면 목록
- 반드시 보존할 장점·복선·문장·이미지
- 현재 실패 사례와 기대 결과
- 동시 작업 중인 브랜치·겹치는 파일

## Serial arc pass

장편 연재의 묶음 단위 퇴고에는 `serial-arc-pass`를 사용한다. 이 mode는 새 장르 공식이나 별도 Canon을 만들지 않고, 기존 역개요·Scene Card·Canon·원고 색인을 같은 기준 커밋으로 묶어 다음을 검증한다.

1. 작업 묶음의 앞·뒤 경계 화를 포함해 시간, 위치, POV, 지식, 부상, 소지품, 관계, 비밀 상태를 비교한다.
2. 해당 묶음이 부별 약속·주제·인물 선택·복선·다음 압력에 어떤 기능을 하는지 한 문장으로 판정한다.
3. 대표 화 품질 게이트와 변경 묶음의 장면 카드를 대조해 같은 문제를 전체 원고 결함으로 일반화하지 않는다.
4. 원고를 바꾸면 `MANUSCRIPT_INDEX`, 역개요 override, Scene Pass Registry, Revision Report의 SHA·화수·제목·POV·분량 소비자를 같은 변경 범위에서 재생성·검증한다.
5. 자동 역개요·분량 통계는 finding 후보일 뿐 수정 명령이 아니다. 원고 문맥과 Canon 근거로 재판정한다.

결과는 `묶음 진단 / 경계 연속성 / 최소 수정 / Canon 전파 / 파생 자료 재생성 / 전체 감사로 일반화하지 않은 범위 / 다음 묶음`으로 보고한다.

## 층별 검토

### Developmental

독자 약속, 중심 질문, 인물 아크, 주제, 결말, 장르 충족, 전체 분량 균형.

### Structural reverse outline

각 장면의 POV·목표/초점·갈등·전환·새 정보·상태 변화·다음 압력·분량을 추출한다. 중복, 누락, 늦은 시작, 이른 종료, 서브플롯 고립, 긴장 평탄화를 찾는다.

### Scene diagnostic

장면 전후 변화, 인물 의도, 장애, 대가, 정보 공개의 공정성, 정서 변화, 장면 연결을 본다. Goal-Conflict-Setback과 Reaction-Dilemma-Decision은 선택적 렌즈다.

### Continuity

연표·이동·지식·부상·소지품·관계·세계 규칙·POV·호칭·복선 회수를 검사한다.

### Line edit

의미 명료성, 문장 리듬, 반복, 추상어, 필터 표현, 시점 거리, 대화 서브텍스트, 묘사 선택, 문단 호흡을 본다. 문체를 평균화하지 않는다.

### Copyedit·Proofread

맞춤법·띄어쓰기·문장 부호·고유명사·표기 통일을 확인한다. 의도적 구어·방언·파편문은 오류와 연출을 구분한다. 최종 교정은 다른 수정이 끝난 뒤 한 오류 유형씩 집중한다.

## 적대적 루프

```text
attack
→ validate-critique
→ MUST_FIX / SHOULD_FIX / DEFER / REJECT / UNVERIFIED
→ 승인된 MUST_FIX·SHOULD_FIX만 최소 수정
→ regression-check
→ evidence-report
```

공격 렌즈:

- 인과 단절·편의적 우연·해결의 무대책성
- 인물 동기 붕괴·능력과 선택의 편의적 변화
- 독자에게만 숨기는 부정직한 정보
- 감정 비약·결과 없는 장면·반복되는 기능
- 세계 규칙의 선택적 적용
- 주제 설명 과잉·대사 정보 덤프
- 장르 약속과 톤 위반
- 진부한 전개·참고작 의존
- AI 상투어·균질한 말투·과도한 정리
- 수정으로 사라진 장점·복선·리듬

비판도 취향일 수 있으므로 사실성·영향·발생 가능성·범위·수정 비용을 재판정한다.

## Reader feedback

독자 의견을 그대로 요구사항으로 사용하지 않는다.

- `COMPREHENSION`: 이해하지 못한 사실·인과
- `EXPECTATION`: 장르·복선·약속 기대
- `ENGAGEMENT`: 흥미가 상승·하락한 위치
- `CHARACTER`: 감정·동기·호감이 아니라 믿을 수 있는지
- `PACING`: 빠름·느림의 위치와 이유
- `PREFERENCE`: 개인 취향
- `SOLUTION_SUGGESTION`: 독자가 제안한 해법

반복 위치·구체적 반응·작품 코어와의 관계를 보고 반영 여부를 판정한다.

## PR review

- 모든 changed file과 삭제·이동을 확인한다.
- 최신 main·열린 PR과 겹치는 파일을 재확인한다.
- 작품 코어·Canon·원고·장면 카드의 변경 전파를 확인한다.
- 수정 권한을 넘은 의미·톤·사건 변경을 찾는다.
- 자동 검사와 실제 원고 검수를 구분한다.
- 미검증과 롤백을 기록한다.

## Output

finding-first로 작성한다. 각 finding에 위치, 증거, 심각도, 영향, 판정, 승인된 수정, 회귀 결과를 연결한다.

## Quality gate

모든 비판을 자동 반영하거나, 표면 문장만 고쳐 구조 결함을 숨기거나, 사용자 문체를 AI 문체로 바꾸거나, 테스트·문서를 삭제해 문제를 없애거나, 수정 뒤 회귀 검토를 생략하면 실패다.

Learning Log: `skills/FICTION_SKILL_LEARNING_LOG.md`
