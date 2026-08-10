# Coc-Fiction Base Integration Adversarial Review — 2026-08-10

## Exact review baseline

- project base main: `27e0dd4e429d447145596ee8aa36ecdb58ac9161`
- reviewed integration head before final report commit: `8f05594adc023809bc8a3312b4ba717ff73cf904`
- Base adoption baseline: `53e63f7ebefbb5b2fc0dc528e335252692801421`
- PR: #13
- source stale PR: #9
- selective-delta evidence PR: #12

## Attack lenses

- stale branch/canon resurrection
- Base/project double authority
- untouched current-state consumers
- false manuscript/canon completion claim
- stale CI/evidence transfer
- unrelated story-manuscript mutation
- fixed project rule accidentally promoted to Base general rule
- rollback/scope isolation
- latest user Decision vs repository Canon drift

## Findings

### MUST_FIX — RESOLVED — next-work reference freshness propagation

**Attack:** `ACTIVE_CONTEXT.md`와 `HANDOFF.md`만 `001-105 canon reconciliation`을 다음 작업으로 바꾸고, 다른 활성 소비자가 `176-180`을 계속 즉시 다음 작업으로 가리키면 어느 파일을 먼저 읽느냐에 따라 작업 방향이 갈린다.

**Validated evidence:**

- `[소설]/00_운영체계/START_HERE.md`: `176-180`을 `다음 시작 묶음`으로 고정.
- `fiction/FICTION_MASTER.md`: `다음: 176-180` 중복 상태.
- `fiction/analysis/REVERSE_OUTLINE_REPORT.md`: `다음 수동 대상 176-180`.
- `fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md`: `다음 작업 176-180`.
- `fiction/analysis/SCENE_PASS_REGISTRY.json`: `next_bundle_passes=[176-180]`.
- `tools/check_fiction_scene_passes.py`: 위 stale next bundle을 contract로 강제.

**Refine:**

- TDD RED head `b00ecb190d50af620dc484b59df96e5d7fcecf12`에서 checker가 `EXTERNAL_ARTIFACT_CANON_RECONCILIATION / 001-005 next / 176-180 deferred`를 먼저 요구하도록 변경.
- exact-head hosted run `31351025397`: expected `FAILURE`.
- `SCENE_PASS_REGISTRY`와 START_HERE / FICTION_MASTER / REVERSE_OUTLINE_REPORT / REPRESENTATIVE_CHAPTER_GATES를 같은 방향으로 전파.
- final refinement head `8f05594adc023809bc8a3312b4ba717ff73cf904`에서 hosted `Fiction operating system` run `31351123715`: `SUCCESS`.

**Regression:** completed bundle records 006-010, 091-095와 해당 chapter SHA는 건드리지 않았다. `176-180`은 삭제가 아니라 `deferred_bundle_passes`로 보존했다.

### MUST_FIX — SEPARATE SAME-CYCLE PR — latest user Decision vs Canon Registry drift

**Attack:** 운영 Handoff가 최신 사용자 결정을 말해도 더 높은 작품 Canon Registry가 과거 설정을 Canon으로 유지하면, 다음 원고 작업에서 폐기 설정이 정본 근거로 되살아날 수 있다.

**Validated evidence:** current `fiction/CANON_REGISTRY.json`에는:

- `juan.obedience-conditioning`이 `CANON`이며 summary에 `복종인자`가 남아 있음.
- 최신 사용자 결정인 **2부 `버실라 / 바실라 / Versilla / Woff` 직접 등장·개인 서사·독립 기능 복원 금지**가 validation rule로 등록돼 있지 않음.
- 현재 프로젝트 대화의 승인된 작업에서는 `복종인자`가 폐기/금지 설정으로 취급되고, 아킴은 허용·버실라는 2부 금지로 정정되어 있음.

**Disposition:** `MUST_FIX`, 그러나 PR #13에 섞지 않는다. #13은 운영/Skill/reference-freshness PR이며 Story Canon mutation을 보호 범위에서 제외했다. #13 병합 후 **별도 project Canon-sync PR**을 current main에서 만들고, 기존 사용자 승인 증거를 재사용해 Canon Registry·직접 소비자·validation을 함께 고친다. 동일 범위 재승인은 요청하지 않는다.

**Merge impact:** PR #13 자체의 운영 변경을 막는 P0는 아니지만, 제1~105 manuscript reconciliation을 시작하기 전에는 반드시 닫아야 하는 선행 Gate다.

### SHOULD_FIX — RESOLVED BY WORDING — Base commit pin is an adoption baseline, not live remote freshness

**Attack:** project checker의 `EXPECTED_BASE_COMMIT`이 현재 SHA와 같다는 것만으로 향후 Base 최신성을 자동 검증한다고 오해할 수 있다.

**Validated critique:** checker는 remote Base를 네트워크 조회하지 않는다. 따라서 향후 Base가 advance해도 자동 발견하지 않는다.

**Refine:** `BASE_ADOPTION_AUDIT.md`에서 `base_commit`을 **호환성 감사 기준점**으로 정의하고, 향후 Base main은 자동 호환으로 간주하지 않으며 재감사한다고 명시했다. 현재 작업에서는 실제 Base main/Registry/active skill view를 connector로 읽어 `53e63f7e...`와 대조했다.

**Why no network CI:** 프로젝트 CI가 외부 Base main을 매 실행마다 동적으로 조회하면 재현성·가용성 의존성이 생긴다. pinned adopted baseline + 별도 freshness audit가 더 안전하다.

### DEFER — external 001-105 artifact is not yet GitHub Canon

외부 통합 ZIP/DOCX가 최신 대화 산출물이라는 사실과 GitHub 225화 Markdown 정본에 전파됐다는 사실은 다르다. 이번 PR에서는 원고를 덮어쓰지 않고 `EXTERNAL_ARTIFACT / GITHUB_CANON_PROPAGATION_NOT_RUN`으로 분리했다.

다음 실제 원고 작업은 `001-005`부터 `KEEP / APPLY / REWORK / REJECT`를 판정하는 reconciliation이다.

### REJECTED_CRITIQUE — stale PR #9를 rebase해서 병합해야 한다

기각. #9는 current main 대비 diverged이며 #12가 동일 고유 2파일 patch를 current main 위에 재구성했다. #9 전체를 살리면 과거 정본/branch context를 불필요하게 다시 섞는다. 현재 PR은 #12의 고유 delta만 기존 Skill mode에 흡수한다.

### REJECTED_CRITIQUE — Base serial-fiction Skill을 Coc-Fiction의 여섯 번째 Skill로 복제해야 한다

기각. Base BCP-009는 이미 공용 작법 책임을 소유한다. Coc-Fiction의 source-log·Canon·합성 파생자료 전파만 기존 5-Skill 구조에 남기면 된다. `REUSE + ABSORB`로 충분하다.

### REJECTED_CRITIQUE — 프로젝트의 `1~3 POV` 규칙을 Base 전역 표준으로 승격해야 한다

기각. `1~3`은 현재 《폭풍의 눈》의 production value다. 공용화 가능한 것은 숫자가 아니라 `새 POV가 독립 정보·감정·가치 판단·외부 평가를 추가해야 한다`, `명시적 장면 경계로 head-hopping을 피한다`는 원리뿐이다. Base BCP-009/serial-fiction Skill의 현재 coverage를 다시 비교한 뒤에만 proposal 후보로 판단한다.

### BLOCKED_UNVERIFIED — local clone validation

현재 Python runtime은 외부 DNS가 막혀 `git clone https://github.com/...`가 `Could not resolve host: github.com`으로 실패했다. 이를 PASS로 처리하지 않았다.

대신 PR exact HEAD에서 동일 repository workflow를 실행했고:

- initial contract RED `5e7a2913...` → run `31350624205` FAILURE
- minimal Base/serial-arc GREEN `5c56676c...` → run `31350856664` SUCCESS
- current-task propagation RED `b00ecb190...` → run `31351025397` FAILURE
- refinement GREEN `8f05594adc...` → run `31351123715` SUCCESS

으로 TDD 증거를 확보했다.

## Scope / rollback review

- manuscript bundle changed: `0`
- `CANON_REGISTRY.json` changed: `0` in PR #13
- source PDF/inventory changed: `0`
- Base active repository changed: `0`
- project new Skill added: `0`
- stale #9 direct merge/rebase: `0`
- rollback: PR #13 단일 merge revert 가능

## Current merge verdict

```yaml
P0_on_PR13: 0
P1_on_PR13: 0
separate_project_must_fix: CANON_REGISTRY_LATEST_DECISION_SYNC
exact_head_ci_8f05594a: PASS
unresolved_review_threads_last_checked: 0
behind_last_checked_before_refinement: 0
merge_gate: RECHECK_EXACT_HEAD_AFTER_THIS_REVIEW_DOC_COMMIT
```

이 문서 자체의 commit으로 head가 바뀌므로 최종 merge 전 새 exact-head CI·changed files·review threads·behind/mergeability를 다시 조회해야 한다.
