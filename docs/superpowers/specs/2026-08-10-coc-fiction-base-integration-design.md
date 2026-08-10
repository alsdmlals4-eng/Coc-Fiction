# Coc-Fiction 프로젝트 정리·병합 + Base 공용 제안 통합 설계

날짜: 2026-08-10
승인 범위: 현재 프로젝트 `alsdmlals4-eng/Coc-Fiction`만 프로젝트 실행 대상으로 하고, `alsdmlals4-eng/Base`는 공용 책임 확인과 `[수정제안서]` 등록 대상으로만 사용한다.

## 1. 목표

이번 작업은 다음 한 사이클을 끝까지 닫는다.

```text
Base 최신 책임 구조 확인
→ Coc-Fiction 최신 상태 전수 회수
→ stale / mergeable / superseded / reference-only 분류
→ 적대적 검토
→ 기존 승인 범위의 프로젝트 변경 실제 병합·저장
→ merged main 재검증
→ 프로젝트 교훈 추출
→ PROJECT_ONLY / BASE_CANDIDATE / SPLIT / NO_PROMOTION 분류
→ Base Existing Solution First
→ 최신 외부 벤치마킹
→ 필요한 BCP만 [수정제안서] 등록
→ Coc-Fiction Handoff 최신화
```

다른 게임 프로젝트의 PR·branch·Decision은 이번 실행에서 읽기·병합 대상이 아니다.

## 2. 확인된 현재 책임 지도

### Base

- 진입 라우터: `START_HERE.md`
- 불변 운영 규칙: `AGENTS.md`
- 전체 생명주기: `docs/OPERATING_MODEL.md`
- Work Mode / Skill 라우팅: `docs/WORK_MODE_AND_SKILL_ROUTING.md`
- 활성 Skill 정본: `skills/SKILL_REGISTRY.json`
- 검토 대기 공용 변경: `[수정제안서]/PROPOSAL_REGISTRY.json` + 각 `PROPOSAL.md`
- 연재소설 공용 책임: `skills/developing-and-revising-serial-fiction/SKILL.md`
- 독립 적대적 검토: `running-adversarial-review-and-refinement`
- canonical drift: `auditing-canonical-reference-freshness`
- 프로젝트 Skill 통합/학습: `evolving-project-discipline-skills`
- Base 제안 생명주기: `managing-base-change-proposals`
- 현재 Base main: `53e63f7ebefbb5b2fc0dc528e335252692801421`

### Coc-Fiction

- 진입 라우터: `[소설]/00_운영체계/START_HERE.md`
- 운영 모델: `[소설]/00_운영체계/OPERATING_MODEL.md`
- 프로젝트 Skill 정본: `[소설]/00_운영체계/SKILL_REGISTRY.json`
- 현재 작품 상태: `fiction/ACTIVE_CONTEXT.md`
- 작품 정본: `fiction/FICTION_MASTER.md`, `fiction/CANON_REGISTRY.json`, `fiction/SOURCE_MANIFEST.md`
- 현재 원고 인덱스: `fiction/MANUSCRIPT_INDEX.json`
- 프로젝트 인수인계: `fiction/HANDOFF.md`
- 퇴고/검증 책임: `skills/fiction-revision-and-validation/SKILL.md`
- 현재 main: `27e0dd4e429d447145596ee8aa36ecdb58ac9161`

## 3. 현재 발견된 운영 문제

1. Coc-Fiction `SKILL_REGISTRY.json`의 `base_commit`은 `41a20584...`로 현재 Base main보다 오래되었다.
2. Base에는 이미 `developing-and-revising-serial-fiction` 공용 Discipline이 구현되어 있으므로, Coc-Fiction의 프로젝트 Skill과 Base 공용 Skill 간 책임 중복/상속 경계를 재검토해야 한다.
3. Draft PR #9 `docs: add serial arc revision mode`가 열린 채 남아 있다. base SHA는 `4ee143...`, 현재 main은 `27e0dd...`이므로 stale이다.
4. PR #12는 #9의 고유 delta만 최신 main 위에 재적용한 2파일 변경이지만 2026-08-10에 `closed / unmerged` 상태다. 따라서 #12를 단순 재개·병합할지, 같은 delta를 현재 작업 branch에 선택적으로 흡수할지 다시 판정해야 한다.
5. 현재 `ACTIVE_CONTEXT.md`는 2026-07-23 상태이며, 최근 1~105화 POV·후크·캐릭터 통합 퇴고 결과와 Base BCP-009 구현 이후의 공용 규칙이 반영되어 있지 않다.

## 4. 접근 대안

### A. 현행 유지

- #9/#12를 닫힌 역사로 두고 Coc-Fiction main도 그대로 둔다.
- 장점: 변경 최소.
- 단점: serial-arc-pass의 유효 delta, Base commit freshness, 최근 1~105화 작업 상태가 프로젝트 정본에 남지 않는다.
- 판정: 부적합.

### B. 기존 구조 개선 — 권장

- 새 프로젝트 Skill을 만들지 않는다.
- #9/#12의 유효한 serial-arc-pass delta는 현재 main에서 기존 `fiction-revision-and-validation` mode/trigger 확장으로 흡수한다.
- Base BCP-009의 공용 연재소설 원칙은 프로젝트 Skill을 삭제·대체하지 않고, 프로젝트 Canon·source-log·문서 전파 등 Coc-Fiction 고유 책임과 공용 작법 책임의 경계를 명시한다.
- Base commit / reference freshness와 ACTIVE_CONTEXT / HANDOFF를 현재 상태로 갱신한다.
- 공용으로 재사용 가능한 새 gap만 Base Proposal로 올린다.
- 장점: REUSE/ABSORB 우선, 중복 Skill 억제, 프로젝트 정본 유지.
- 단점: 책임 경계 문서와 regression test가 필요하다.
- 판정: 채택.

### C. 새 통합 Skill 생성

- Coc-Fiction에 Base 공용 Skill을 복제한 새 광역 Skill을 추가한다.
- 장점: 한 파일에서 많은 책임을 볼 수 있다.
- 단점: Base BCP-009와 중복, 프로젝트/공용 정본 이중화, 유지보수 비용 증가.
- 판정: `BUILD_NEW` 근거 없음, 기각.

## 5. 실행 설계

### Phase 1 — 상태 회수와 분류

- current main, branch, open/closed/merged PR, Actions, review thread, changed file을 재조회한다.
- 각 branch/PR을 `MERGE_READY / NEEDS_UPDATE / NEEDS_FIX / BLOCKED / SUPERSEDED / REFERENCE_ONLY / DO_NOT_MERGE / USER_DECISION_REQUIRED`로 분류한다.
- 특히 #9/#12는 전체 branch가 아니라 고유 delta만 비교한다.

### Phase 2 — 프로젝트 변경

승인 범위 안에서 다음 최소 변경만 허용한다.

- 기존 `fiction-revision-and-validation`에 serial-arc-pass가 여전히 필요한 경우 mode/trigger를 흡수.
- 프로젝트 Registry의 Base 기준점을 최신 호환 상태로 갱신하되, 단순 SHA 교체가 실제 호환성 증거를 대신하지 않도록 adoption audit와 함께 기록.
- Base 공용 연재소설 Discipline과 Coc-Fiction 프로젝트 Skill의 책임 경계 명시.
- 최근 1~105화 통합 퇴고 결과 및 현재 다음 작업을 `ACTIVE_CONTEXT.md` / `HANDOFF.md`에 반영.
- 오래된 PR/branch는 필요 시 `SUPERSEDED` 또는 reference-only로 정리.

프로젝트 Canon·원고 내용은 이번 운영 정리 PR에서 임의 변경하지 않는다.

### Phase 3 — 검증

- changed-file scope 검사.
- JSON registry parse.
- 기존 fiction ops validator 실행 또는 GitHub Actions exact-head 확인.
- 정본 링크/경로/reference freshness 검사.
- 적대적 루프: `attack → validate-critique → refine → regression-recheck → merge decision`.
- unresolved review thread 0, P0/P1 0, behind 0, exact-head evidence 확인.

### Phase 4 — 실제 병합

- 같은 승인 범위의 `MERGE_READY`만 병합한다.
- stale #9를 직접 병합하지 않는다.
- 병합 후 새 `main` SHA를 다시 읽고, 파일·Registry·Handoff·CI를 post-merge 재검증한다.

### Phase 5 — 교훈 추출과 Base 판정

각 finding을 `PROJECT_ONLY / BASE_CANDIDATE / SPLIT / NO_PROMOTION`으로 나눈다.

Base 후보는 반드시 먼저 현재 BCP-009 및 기존 공용 Skill을 검색해 다음 중 하나로 판정한다.

`REUSE / ABSORB / REFACTOR / BUILD_NEW / NO_PROMOTION`

특히 다음 후보를 검토한다.

- stale PR selective recovery
- project→Base learning loop
- approval reuse
- post-merge verification
- evidence freshness
- 장편 연재 묶음 단위 `serial-arc-pass`의 공용화 필요성

이미 BCP-009 또는 다른 Base Skill에 충분히 있으면 새 BCP를 만들지 않는다.

### Phase 6 — 벤치마킹과 BCP

Base 후보가 남을 때만 최신 외부 자료를 조사한다.

우선순위:
1. GitHub 공식 문서
2. 공식 engineering / architecture 문서
3. 실제 오픈소스 workflow
4. ADR/RFC/proposal 운영 사례
5. AI agent evaluation / handoff 사례

각 사례는 `외부 방식 → Base 현재 방식 → 차이 → 채택 → 비채택`으로 기록한다.

새 BCP가 필요한 경우 Base 활성 Skill을 수정하지 않고 `[수정제안서]` proposal + evidence + registry까지만 별도 Base branch/PR에 작성한다.

## 6. 오류 처리

- 과거 HEAD의 CI를 현재 HEAD PASS로 승격하지 않는다.
- connector/Actions 정보가 일시적으로 없으면 `BLOCKED_UNVERIFIED`로 해당 검사만 보류하고 독립 작업을 계속한다.
- `REFERENCE ONLY`, `DO NOT MERGE`, `SUPERSEDED` 전체 branch는 병합하지 않는다.
- 최신 project Canon과 충돌하는 옛 delta는 폐기한다.
- 새로운 작품 방향, Canon 변경, Base 활성 규칙 구현이 필요해지면 현재 승인 범위를 넘으므로 별도 Decision으로 분리한다.

## 7. 테스트와 완료 조건

완료 전 새 증거로 다음을 확인한다.

- Coc-Fiction main 정확한 새 SHA
- 프로젝트 변경 diff와 expected changed-file set
- Registry JSON parse PASS
- fiction ops validation PASS 또는 실패 원인 명시
- unresolved review thread 0
- mergeable/behind 상태
- post-merge main readback
- 프로젝트 Handoff 최신화
- Base 후보 분류표 완성
- 필요한 경우에만 BCP + Proposal Registry 실제 등록
- BCP 자체 validator PASS
- 미실행 항목은 `NOT_RUN` 또는 `BLOCKED_UNVERIFIED`

## 8. 롤백

- 프로젝트 변경은 하나의 범위가 명확한 PR로 유지한다.
- stale branch를 rebase해 과거 정본을 되살리지 않는다.
- 병합 후 문제 발생 시 해당 PR merge를 revert할 수 있게 unrelated change를 섞지 않는다.
- Base Proposal은 활성 구현과 분리해 proposal-only PR로 유지한다.

## 9. 범위 밖

- 다른 게임 프로젝트의 branch/PR 정리
- Coc-Fiction 작품 Canon/원고의 새로운 창작 방향 변경
- Base 활성 Skill/Template/Workflow 구현
- 225화 전체 원고 proofread 완료 주장
- 외부 자료를 작품 Canon으로 자동 승격
