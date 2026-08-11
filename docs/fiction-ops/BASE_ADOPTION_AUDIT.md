# Base → Coc-Fiction 적용·가지치기 감사

## 기준

- Base 저장소: `alsdmlals4-eng/Base`
- 현재 호환성 감사 기준 커밋: `7a49390bd840f5f5dc80fe661b44ad45e9ebeb7f`
- Base current active Skill view: 30개
- 목표: Base의 공용 작업 능력은 재사용하고, Coc-Fiction의 작품 Canon·원본 로그·원고 파생자료처럼 프로젝트 고유 책임은 프로젝트에 남긴다.
- 전략: Base Skill을 복제하지 않고 **기존 5개 Coc-Fiction Skill과 조건부 Base 공용 Skill**을 조합한다.
- Existing Solution First: `REUSE → ABSORB → REFACTOR → BUILD_NEW`; 새 프로젝트 Skill은 마지막 선택지다.

`base_commit`은 “Base 전체를 프로젝트 안에 복제했다”는 뜻이 아니다. 이 커밋의 활성 Registry·책임 원본과 프로젝트 adapter/mapping을 대조한 **호환성 감사 기준점**이다. 이후 Base가 바뀌면 자동으로 PASS를 승계하지 않고 다시 freshness를 확인한다.

## Base 공용 책임 → Coc-Fiction mapping

아래 26개는 기존 프로젝트 운영체계가 직접 소비하거나 소설 작업에 공용 원리로 재사용하는 Base 책임이다.

| Base Skill | 판정 | Coc-Fiction 보존·소비 위치 |
|---|---|---|
| `managing-project-intake-and-work-contract` | ADAPT | `fiction-project-operations`의 route·contract·decompose |
| `managing-game-project-operating-system` | ADAPT | 운영 모델·Documentation Map·검증 도구; 게임 고유 부분은 사용하지 않음 |
| `managing-design-documents` | ADAPT | Canon 책임 원본 정책과 문서 지도 |
| `evolving-project-discipline-skills` | ADAPT | 5-Skill Registry와 Learning Log; 새 Skill보다 mode 통합 우선 |
| `pruning-stale-and-nonfunctional-material` | CONSOLIDATE | 운영·퇴고의 KEEP·MERGE·ARCHIVE·DELETE 판정 |
| `simplifying-skill-bodies` | CONSOLIDATE | 짧은 Skill 본문 + `docs/fiction-ops` reference |
| `refactoring-with-contract-preservation` | CONSOLIDATE | 승인된 의미·문체 보존형 재작성과 회귀 검증 |
| `synchronizing-local-and-github-state` | ADAPT | 동시 작업 규칙·PR 전 최신 main 대조 |
| `maintaining-long-running-task-continuity` | ADAPT | checkpoint·partial delivery·resume |
| `governing-game-user-research-coverage` | ADAPT | `reader-feedback`의 독자 반응 coverage만 전이; 게임 전용 11영역은 비사용 |
| `creating-user-learning-notes` | ADAPT | `FICTION_SKILL_LEARNING_LOG.md` |
| `building-project-visual-dashboards` | DEFER | 원고 상태 대시보드가 실제 소비될 때만 |
| `diagnosing-game-engine-runtime-failures` | EXCLUDE | 게임 엔진 전용이며 소설 원고에 소비자 없음 |
| `maintaining-project-context-and-handoff` | ADAPT | `ACTIVE_CONTEXT.md`·`HANDOFF.md`를 압축 라우터로 유지 |
| `analyzing-and-refining-game-concepts` | ADAPT | 기존 프로젝트의 작품 코어·플롯 사고법 중 매체 독립 원리만 `fiction-story-development`에 보존 |
| `identifying-project-core` | ADAPT | `core-audit` |
| `establishing-project-core` | ADAPT | `core-contract`과 사용자 승인 상태 |
| `running-adversarial-review-and-refinement` | CONSOLIDATE | 프로젝트 `adversarial-loop` + Base 독립 공격·비판 검증 절차 |
| `designing-vertical-slices` | ADAPT | `representative-chapter-gate`; 게임 제작 Gate 자체는 비사용 |
| `orchestrating-deepseek-worktrees` | ADAPT_ON_DEMAND | 외부 AI 격리·결과 검수에만 사용 |
| `reviewing-and-validating-project-changes` | ADAPT | revision의 계약·층별 검수·PR review와 실제 diff 검증 |
| `auditing-canonical-reference-freshness` | ADAPT | canon의 `reference-freshness`, untouched consumer·파생본 검사 |
| `designing-art-prompts-and-technique-cards` | DEFER | 표지·삽화·시각 참고가 승인된 경우만 |
| `auditing-and-refining-ui-art` | EXCLUDE | 게임/Web UI 전용 |
| `managing-base-change-proposals` | ADAPT | 프로젝트 교훈의 공용성 판정과 proposal-only 제출 |
| `developing-and-revising-serial-fiction` | REUSE | Reader Promise·Episode Value·POV/voice·정보/맥락 분리·`READER_KNOWLEDGE_MATRIX`·`CHOICE_PROOF`·대표 하이라이트 proof·캐릭터 개성/상대 위상·원본 기능 복원·Local Payoff/Open Loop·반복 변주·결과 기억·setup/payoff debt·장기 복선 `RECONTEXTUALIZE/AFTERMATH`·독자 반응 근거. 프로젝트 고유 Canon/원본/파생자료는 복제하지 않음 |

## 현재 Base 30개 중 프로젝트 adapter에 직접 넣지 않은 추가 책임

현재 Base에는 위 mapping 외에도 게임 개발 YouTube 제작, legacy archive governance, Godot asset/plugin 평가, AI 모델·Prompt 비용 최적화 책임이 있다. 이들은 Base에서 유효하지만 **현재 Coc-Fiction 원고 운영의 상시 프로젝트 Skill 소비자가 아니므로** 프로젝트 5-Skill Registry에 복제하거나 억지로 매핑하지 않는다. 실제 요청이 생기면 Base의 해당 Skill을 직접 선택적으로 호출한다.

## Base 공용 연재소설 Skill과 프로젝트 5-Skill의 경계

### Base가 소유하는 공용 원리

- Reader Promise와 Episode Value
- POV를 카메라가 아니라 정보·가치·어휘 필터로 쓰는 원리
- **답을 숨기더라도 현재 장면의 목표·위험·선택·결과 같은 맥락은 숨기지 않는 원리**
- 중요 정보 비대칭을 `READER_KNOWLEDGE_MATRIX`로 분리해 POV 지식·독자 지식·지금 필요한 맥락·숨은 진실·공개 트리거를 감사하는 원리
- 캐릭터 변화가 설정 설명이 아니라 압박 속 선택의 반복·회귀·변형으로 증명되는 `CHOICE_PROOF`
- 후반의 큰 선택이 앞선 가치·상처·작은 행동과 연결되는 `SURPRISING_BUT_COHERENT`
- 대표 캐릭터 하이라이트를 `IDENTITY + COMPETENCE + COST + CHOICE + CONSEQUENCE`로 감사하되 기계적 점수표로 사용하지 않는 원리
- 캐릭터별 관찰 필터·voice·문제 해결 방식·결점·대표 하이라이트 구분
- 중요 적대자의 화면 안 위협 증명과 `own turn`
- 승리를 위해 상대를 약체화·우둔화하지 않는 위상 보존
- 원작·로그·구초안의 기능을 `KEEP / RESTORE / REWORK / NEW / REMOVE`로 대조하는 각색 원리
- Local Payoff + Open Loop
- 반복 구조의 의미 있는 변주
- 선택·피해·능력 사용의 consequence memory
- setup/payoff debt
- 장기 복선·반전에서 필요할 때 `SETUP → RECALL → RECONTEXTUALIZE → PARTIAL_PAYOFF → PAYOFF → AFTERMATH`를 추적하는 원리
- 독자 피드백을 Canon이 아닌 evidence로 처리하는 절차
- 특정 작가 문체를 복제하지 않는 벤치마킹 경계

### Coc-Fiction이 소유하는 프로젝트 고유 책임

- 《폭풍의 눈》 작품 Canon·인물·세계관·사건 결과·금지 설정
- TRPG/PDF/source-log 우선순위와 각색 허용 경계
- 구 225화 전체 압축본을 원본과 분리한 비교자료로 취급하는 프로젝트 우선순위
- 황진청·팽무악 등 작품별 강자·전투 하이라이트의 실제 배치와 횟수
- 주안–엘리스, 라르고–엘리스 등 작품 고유 관계 Canon
- Juan–Alice, Ian–Milly–Hatem, Elliott Ch47, Largo `[규율]` 등 작품별 복선 ladder의 실제 위치와 회수 방식
- 작품별 `READER_KNOWLEDGE_MATRIX`의 실제 지식 상태와 숨김 이유
- 5화 묶음과 앞뒤 경계 화 직접 대조
- `MANUSCRIPT_INDEX` baseline+override 합성
- reverse-outline override
- `SCENE_PASS_REGISTRY.json`
- Revision Report의 SHA·화수·제목·POV·분량 전파
- 작품별 호출기/장비/관계/정보 상태 등 고유 연속성 규칙

따라서 Base 공용 serial-fiction Skill이 확장됐다는 이유로 Coc-Fiction 프로젝트 Skill을 삭제하거나 여섯 번째 복제 Skill을 만들지 않는다. 공용 원리는 `REUSE`, 프로젝트 고유 실행 계약은 기존 5개 Skill의 mode로 `ABSORB`한다.

## Serial arc pass 판정

stale PR #9와 closed/unmerged PR #12를 비교한 결과, 유효 고유 delta는 기존 `fiction-revision-and-validation`의 묶음 퇴고 mode뿐이다. 새 Skill이 아니라 `serial-arc-pass`로 흡수한다.

이 mode는 Base 공용 작법을 재정의하지 않는다. Coc-Fiction에서만 필요한 다음 연결을 소유한다.

```text
묶음 앞·뒤 경계
→ 원본 사건/Canon/POV/상태 비교
→ 대표 게이트 대조
→ 승인된 최소 원고 수정
→ MANUSCRIPT_INDEX·역개요 override·Scene Pass Registry·Revision Report 전파
→ regression
```

자동 역개요·분량 통계는 finding 후보이며 원고 수정 명령이 아니다.

## 유지한 핵심 계약

- `PLAN / BUILD / REVIEW`
- trigger 기반 최소 Skill 자동 선택
- 한 질문당 단일 책임 원본
- 작품 코어와 변경 가능한 외피 분리
- 사용자 승인 없는 코어 확정·대량 변경 금지
- 기능·의미·문체 보존형 가지치기·리팩토링
- 적대적 공격과 비판 검증 분리
- 정본·경로·참조 변경의 untouched 소비자 감사
- 미실행을 `PASS`로 보고하지 않는 증거 기준
- 동시 작업·장기 작업의 브랜치·체크포인트·인수인계
- stale PR은 전체 rebase보다 고유 delta 선택적 재적용 우선

## 소설 프로젝트 고유 기능

- 작품 코어 계약: 독자 약속·주제 질문·인물 욕망·POV·톤·결말 방향
- Canon 상태와 인물·연표·지식·소지품·부상·관계 변화 추적
- 인과 플롯과 장면 전후 상태 변경 검사
- 장면 카드 기반 집필
- 캐릭터 `CHOICE_PROOF`, 개성·강적 위상·승리 개연성의 프로젝트 적용 감사
- 대표 하이라이트 proof와 작품별 highlight tier
- 작품별 복선 ladder와 `READER_KNOWLEDGE_MATRIX`
- POV 거리·대화 서브텍스트·묘사·행동-반응·문장 리듬 모드
- Developmental→Structural→Continuity→Line→Copyedit→Proofread 순서
- 참고문장·연출을 저작권 안전한 Reference Card로 추상화
- 대표 장면/대표 장의 품질 게이트
- source-log과 합성 파생자료의 작품별 전파 계약

## 현재 검증 경계

이번 2026-08-11 호환성 갱신은 Base PR #281과 #282 병합 결과인 `7a49390bd840f5f5dc80fe661b44ad45e9ebeb7f`의 serial-fiction 공용 계약과 Coc-Fiction의 Registry·5-Skill 운영 파일·작법 Research를 대조했다. Base의 향후 commit은 자동 호환으로 간주하지 않는다.

현재 외부 최신 원고와 GitHub migration 컨테이너는 아직 전면 동기화 완료 상태가 아니다. GitHub 저장 225화 topology를 최신 narrative numbering의 최종 편성으로 간주하지 않으며, 원고 이관은 검증된 prefix 단위로 계속 진행한다.

이번 작법 재조사의 공용 계약과 프로젝트 적용 문서는 자동 검증 가능하지만, **사람 독자 만족·상업 성과·특정 플랫폼 전환율은 검증하지 않았다.** 외부 편집·작가 자료는 진단 Evidence이며 작품 정본이나 판매 인과의 증거가 아니다.

## 미검증·다음 확인

- 제6~105화 외부 통합본과 GitHub manuscript/canon/source의 실제 production delta 재대조·정본 승격: `IN_PROGRESS / 006-010 ANALYZED_NOT_INTEGRATED`
- 이후 106화 이상 새 원고의 GitHub Canon 전파: `NOT_RUN`
- 실제 독자 반응 기반 reader-feedback gate: `HUMAN_READER_NOT_RUN`
- Base의 향후 새 main에 대한 자동 호환성: `UNVERIFIED_UNTIL_REAUDIT`
- Base `character-and-opponent-integrity` 및 새 정보/하이라이트 Guide의 두 번째 별도 소설 프로젝트 pilot과 사람 독자 효용: `NOT_RUN`
