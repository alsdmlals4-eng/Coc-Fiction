# Base → Coc-Fiction 적용·가지치기 감사

## 기준

- Base 저장소: `alsdmlals4-eng/Base`
- 기준 커밋: `41a20584dd2ee51d917e5c9d7cab6838e1ceba7e`
- 목표: 게임 개발용 Base의 공용 작업 능력은 보존하고, 소설 기획·집필·퇴고에 불필요한 엔진·UI·성능 전용 구조는 제거한다.
- 전략: Base Skill을 복제하지 않고 **5개 소설 Skill과 조건부 reference**로 통합한다.
- 충돌 방지: 원고·설정 이전 브랜치를 수정하지 않고 새 경로만 추가한다.

## Base 25개 활성 기능 판정

| Base Skill | 판정 | Coc-Fiction 보존 위치 |
|---|---|---|
| `managing-project-intake-and-work-contract` | ADAPT | `fiction-project-operations`의 route·contract·decompose |
| `managing-game-project-operating-system` | ADAPT | 운영 모델·Documentation Map·검증 도구 |
| `managing-design-documents` | ADAPT | Canon 책임 원본 정책과 문서 지도 |
| `evolving-project-discipline-skills` | ADAPT | 5-Skill Registry와 Learning Log |
| `pruning-stale-and-nonfunctional-material` | CONSOLIDATE | 운영·퇴고의 KEEP·MERGE·ARCHIVE·DELETE 판정 |
| `simplifying-skill-bodies` | CONSOLIDATE | 짧은 Skill 본문 + `docs/fiction-ops` reference |
| `refactoring-with-contract-preservation` | CONSOLIDATE | 승인된 의미·문체 보존형 재작성과 회귀 검증 |
| `synchronizing-local-and-github-state` | ADAPT | 동시 작업 규칙·PR 전 최신 main 대조 |
| `maintaining-long-running-task-continuity` | ADAPT | checkpoint·partial delivery·resume |
| `governing-game-user-research-coverage` | ADAPT | `reader-feedback`의 독자 반응 coverage |
| `creating-user-learning-notes` | ADAPT | `FICTION_SKILL_LEARNING_LOG.md` |
| `building-project-visual-dashboards` | DEFER | 원고 상태 대시보드가 실제 필요해질 때만 |
| `diagnosing-game-engine-runtime-failures` | EXCLUDE | 게임 엔진 전용이며 소설 작업 목표와 무관 |
| `maintaining-project-context-and-handoff` | ADAPT | operations의 handoff·현재 상태 압축 |
| `analyzing-and-refining-game-concepts` | ADAPT | `fiction-story-development`의 작품 코어·플롯·검증 |
| `identifying-project-core` | ADAPT | `core-audit` |
| `establishing-project-core` | ADAPT | `core-contract`과 사용자 승인 상태 |
| `running-adversarial-review-and-refinement` | CONSOLIDATE | revision의 `adversarial-loop` |
| `designing-vertical-slices` | ADAPT | `representative-chapter-gate` |
| `orchestrating-deepseek-worktrees` | ADAPT_ON_DEMAND | operations의 외부 AI 격리·결과 검수 규칙 |
| `reviewing-and-validating-project-changes` | ADAPT | revision의 계약·층별 검수·PR review |
| `auditing-canonical-reference-freshness` | ADAPT | canon의 `reference-freshness` |
| `designing-art-prompts-and-technique-cards` | DEFER | 표지·삽화·시각 참고가 승인된 경우만 |
| `auditing-and-refining-ui-art` | EXCLUDE | Godot·Web UI 전용 |
| `managing-base-change-proposals` | ADAPT | 반복 검증된 교훈만 Learning Log에서 별도 제안 |

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

## 소설용으로 새로 추가한 기능

- 작품 코어 계약: 독자 약속·주제 질문·인물 욕망·POV·톤·결말 방향
- Canon 상태와 인물·연표·지식·소지품·부상·관계 변화 추적
- 인과 플롯과 장면 전후 상태 변경 검사
- 장면 카드 기반 집필
- POV 거리·대화 서브텍스트·묘사·행동-반응·문장 리듬 모드
- Developmental→Structural→Continuity→Line→Copyedit→Proofread 순서
- 참고문장·연출을 저작권 안전한 Reference Card로 추상화
- 독자 피드백을 사실·취향·혼란·기대 위반으로 분류
- 대표 장면/대표 장의 품질 게이트

## 제외가 기능 약화를 뜻하지 않는 이유

게임 엔진, 런타임, 프레임 시간, 터치 접근성, UI 아트, 플레이 빌드처럼 **소설 원고에 소비자가 없는 기능**만 제외했다. 조사·기획·정본·검증·적대적 리뷰·동기화처럼 매체를 넘어 필요한 기능은 소설 언어로 모두 매핑했다.

## 미검증

- 다른 채팅이 이전하는 실제 원고·설정과의 Canon 경로 연결
- 작품 고유 코어·POV·시제·문체 확정
- 실제 원고를 사용한 구조·연속성·문장 퇴고 회귀
- 독자 피드백·대표 장 품질 게이트 실행

위 항목은 원고 이전이 끝난 뒤 별도 작업에서 실행한다.
