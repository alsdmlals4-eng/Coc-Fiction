# AGENTS.md

이 저장소는 **Coc-Fiction / 장편 서사 프로젝트**다. 게임 runtime 프로젝트가 아니며 Godot 관련 실행·Scene·Resource 규칙은 `NOT_APPLICABLE`이다.

## 권한 순서

1. 사용자의 최신 직접 지시.
2. 이 `AGENTS.md`.
3. `fiction/ACTIVE_CONTEXT.md`와 승인된 작업 계약.
4. 작품 정본과 실제 원고·구조화 데이터·검사.
5. 프로젝트 내부 운영 문서와 채택된 Base 계약.
6. 최신 공식/1차 외부 자료, 직접 관련된 실무 사례, 과거 대화·메모리·추정.

과거 대화·메모리·외부 자료는 current canon을 대체하지 않는다. 최신 Base remote도 프로젝트가 채택한 계약이나 작품 고유 의미를 조용히 덮어쓰지 않는다.

## 최초 읽기

```text
[소설]/00_운영체계/START_HERE.md
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ docs/fiction-ops/CURRENT_STATE_RECEIPT.json
→ 현재 묶음 Scene Card / Revision Report / 실제 manuscript
→ latest completed main / open PR / actual checker evidence
```

`CURRENT_STATE_RECEIPT.json`의 SHA/PR은 production frontier가 마지막으로 바뀐 readback 증거다. 저장소의 영구적인 최신 SHA/PR이 아니므로 재개할 때는 반드시 최신 completed `main`과 open PR 상태를 다시 조회한다.

## Repository-only 정본

```text
REPOSITORY_HUMAN_FACING_CANON
REPOSITORY_STRUCTURED_CANON
REPOSITORY_RUNTIME_OR_CHECKER_TRUTH
NOTION_AND_SHEETS_HISTORICAL_MIGRATION_ONLY
```

- GitHub repository가 사람용 작품 문서, Canon, Scene Card, 구조화 registry, actual manuscript, 검사기, packaging과 evidence의 단일 active owner다.
- Notion과 Google Sheets는 고유 미이관 자료가 남은 일회성 migration audit에서만 read-only input으로 사용할 수 있다.
- 신규 CURRENT 페이지 갱신, Notion sync/readback, Sheet 승인 로그 또는 외부 복제본은 완료 조건이 아니다.
- 사용자가 별도 migration 감사를 명시하면 고유 자료를 repository owner로 이관하고 readback receipt를 남긴 뒤 다시 historical 상태로 닫는다.
- 사용자용 PDF·DOCX·EPUB 등 publication output은 exact repository revision에서 생성한 파생 deliverable이며 별도 정본이 아니다.

## 정본 경계

- 외부/Library의 `QA_GREEN` candidate는 **revision input**이며 자동으로 GitHub production authority가 되지 않는다.
- GitHub production authority는 `SCENE_PASS_REGISTRY.json`의 bounded reconciliation frontier가 책임진다.
- `current prefix / legacy tail / migration boundary`를 인접 화수만으로 자동 연결하지 않는다.
- `whole_manuscript_continuity=NOT_YET_CLAIMED`를 전체 연속성 완료로 확대 해석하지 않는다.
- Canon과 사용자 Decision이 파생 역개요·자동 진단보다 우선한다.
- 원고 파일 존재, parser PASS, DOCX packaging PASS와 독자 체감·출판 준비·상업 release PASS를 구분한다.

## 보호 규칙

- 진행 중 `open/draft/ready` PR은 사용자가 현재 작업에서 PR 번호와 허용 동작을 명시하지 않는 한 **read-only**다.
- 닫힌 RED/diagnostic PR과 과거 migration 자료는 역사 증거이며 임의 삭제·재병합하지 않는다.
- `엘리스`가 Alice Carter의 현행 한글 Canon 표기다.
- 주안의 `반응 → 멈춤 → 이유 → 선택`, Scene-Locked Hybrid, D01/D02/D03/N04 및 귀속 미정 공동봉인 규칙을 회귀시키지 않는다.
- 기존 5화 bounded promotion을 대규모 일괄 승격으로 바꾸지 않는다.
- direct-main push, force push, admin/ruleset bypass, unrelated PR takeover를 하지 않는다.

## 현재 조사와 실제 제작 가능성

```text
CURRENT_RESEARCH_AND_IMPLEMENTATION_FEASIBILITY_REQUIRED
MINIMUM_MATERIALLY_DISTINCT_ALTERNATIVES: 3
ADOPT / ADAPT / TEST / REJECT
ACTUAL_PROJECT_BOUNDARY_MAPPING_REQUIRED
FEASIBLE | PARTIAL | BLOCKED_UNVERIFIED
RESEARCH_SUMMARY_IS_NOT_IMPLEMENTATION_PROOF
```

중요한 작품 운영·원고 구조·검사기·publication·배포·rights·시장 형식·도구 결정은 다음을 실제로 수행한다.

1. current canon, actual manuscript, registry/checker와 publication pipeline을 fresh-read한다.
2. 현재 프로젝트와 채택된 Base에 기존 해법이 있는지 먼저 찾는다.
3. 최신 공식/1차 문서와 직접 관련된 편집·연재·출판·디지털 배포의 성공·실패 사례를 조사한다.
4. 최소 세 개의 실질 대안을 같은 기준으로 비교하고 `ADOPT / ADAPT / TEST / REJECT`로 판정한다.
5. 선택안을 actual file owner, manuscript range, registry/schema, checker, packaging, release format, rights, rollback과 bounded work package에 연결한다.
6. `FEASIBLE | PARTIAL | BLOCKED_UNVERIFIED`를 명시한다.

외부 조사로 작품 Canon, 인물 동기, 사건 인과, 문체와 사용자 승인 서사 의미를 자동 변경하지 않는다. 외부 근거는 구조·가독성·운영·publication·rights·tool feasibility 판단의 evidence다.

실제 제작 가능성 기록에는 최소 다음을 포함한다.

```yaml
reader_or_editor_value:
actual_manuscript_range:
canon_and_scene_card_owners: []
registry_or_schema_changes: []
checker_and_packaging_changes: []
format_platform_rights_constraints: []
rollback_and_reconciliation_boundary:
verification_plan: []
bounded_implementation_package: []
feasibility: FEASIBLE | PARTIAL | BLOCKED_UNVERIFIED
```

검색 링크, 일반적 작법 조언, AI 평가, parser PASS 또는 sample output만으로 원고 전체 연속성·독자 체감·출판 준비를 증명하지 않는다.

## 장기 품질과 사용자 개입 최소화

```text
LONG_TERM_EFFICIENCY_AND_COMPLETENESS_FIRST
QUALITY_OVER_RESPONSE_SPEED
TOTAL_LIFECYCLE_COST
NO_UNSUPPORTED_OVERENGINEERING
MINIMUM_NECESSARY_COMPLEXITY
LOW_INTERVENTION_AUTOMATION_AND_LEARNING_LOOP
```

빠른 일괄 수정이나 임시 문서보다 Canon owner 명확성, bounded promotion, 자동 검사, reversible reconciliation, 장기 일관성과 완성도를 우선한다. 다만 실제 원고 consumer·acceptance·checker가 없는 범용 schema, 대형 framework, paid service 또는 미래 전용 자동화는 만들지 않는다.

승인 범위 안에서 다음을 routine reapproval 없이 연속 진행한다.

```text
fresh-read
→ research / compare
→ prepare bounded revision or checker package
→ execute safe reversible work
→ exact-head validation / readback
→ adversarial review
→ correct validated findings
→ regression / continuity recheck
→ incident / solution / lesson
→ project automation or Base promotion candidate
→ remaining work recalculation
```

사용자에게 올리는 결정은 핵심 Canon·인물·사건·결말·문체 방향, 객관적 우열이 닫히지 않는 취향, 큰 범위·비용, final cover/visual lock, 파괴적 migration·삭제·publication·외부 공개·권한·rights 위험으로 제한한다. 정본 충돌이나 안전하지 않은 입력은 `BLOCKED_UNVERIFIED`로 닫는다.

## 시각 후보와 표지 작업

이미지 작업은 게임 runtime 규칙이 아니라 작품의 구체적인 cover·character reference·promotional/distribution consumer 또는 현재 기획 비교용 planning-board에만 적용한다.

```text
NEED_DRIVEN_GENERATE_THEN_LOCK
CURRENT_APPROVED_VISUAL_ANCHOR_READBACK_REQUIRED
EXISTING_APPROVED_ASSET_REUSE_FIRST
GENERATE_ONE_CANDIDATE_BEFORE_LOCK
USER_LOCK_REVISE_REJECT_AFTER_GENERATION
NO_AUTOMATIC_IMAGE_CHAIN
```

구체적 필요가 확인되면 현재 작품 시각 정본, 승인 이미지·시안, 인물 Canon, consumer, 규격, rights/provenance와 기존 자산 재사용 가능성을 읽고 이미지 모델로 후보 1건을 먼저 만들 수 있다. 생성 뒤 사용자가 `LOCK / REVISE / REJECT`를 결정한다.

```text
GENERATED_CANDIDATE != USER_LOCKED != PROJECT_ASSET_APPROVED != PUBLISHED_OR_DISTRIBUTED
```

막연한 장식, consumer 없는 이미지, 다른 작품 스타일 복제 또는 자동 variant chain은 금지한다. `LOCK` 전에는 cover·promotion 정본이나 배포 asset으로 승격하지 않는다.

## 증거 기반 적대적 검토

```text
CLAIM_ONLY_ADVERSARIAL_REVIEW_INVALID
EXACT_HEAD_OR_STATE_REQUIRED
ACTUAL_READS_AND_CHECK_RESULTS_REQUIRED
VALIDATED_FINDING_REQUIRES_CORRECTION_OR_EXPLICIT_BLOCKER
MINIMUM_FULL_LOOPS_BEFORE_CLEAN_EXIT: 5
```

중요 retained change는 최소 5회의 실제 full-scope loop 뒤 clean exit까지 진행한다. 각 loop는 전체 승인 범위와 current manuscript/registry/checker를 다시 읽고 다음을 실제로 남긴다.

- input exact head/state와 actual reads.
- 실행한 command/check와 결과.
- 발견한 critique와 검증 근거.
- validated finding에 적용한 교정 또는 explicit blocker.
- continuity·canon·checker·packaging regression과 readback.
- untouched manuscript ranges/consumers의 재확인.
- 더 나은 대안 검색과 장기 적합성 재판정.
- output exact head/state.

`검토 완료`, `5회 확인`, `문제 없음`이라는 문장만으로는 loop를 계수하지 않는다. 5회 뒤에도 새 `MUST_FIX`, Canon drift, acceptance blocker, evidence ceiling 위반 또는 더 강한 in-scope 대안이 나오면 수정 후 계속한다.

## 학습과 재발 방지

```text
INCIDENT
→ ROOT_CAUSE
→ CORRECTION
→ VERIFICATION
→ REGRESSION_PREVENTION
→ PROJECT_OWNER_UPDATE
→ PROJECT_SPECIFIC | BASE_PROMOTION_CANDIDATE
```

문제와 해결을 대화 요약으로만 남기지 않는다. current owner, regression test/checker, schema, template, routing/freshness rule 또는 명시적 `NO_BASE_PROMOTION` 근거 중 하나에 반영한다. 프로젝트 고유 서사 의미를 공용 Base 규칙으로 과잉 일반화하지 않는다.

## 검증

소설/운영 변경은 exact head에서 최소 다음을 실행한다.

```bash
python tools/check_fiction_operating_system.py
python tools/check_fiction_content.py
python tools/build_fiction_reverse_outline.py --check
python tools/check_fiction_reverse_outline.py
python tools/check_fiction_scene_passes.py
python -m unittest tests.test_current_state_closure -v
python -m unittest tests.test_fiction_docx_packaging -v
```

추가 테스트가 도입된 변경은 해당 테스트도 함께 실행한다. 과거 Green을 현재 head의 Green으로 재사용하지 않는다. 실행할 수 없는 검증은 `NOT_RUN` 또는 `BLOCKED_UNVERIFIED`로 남긴다.

## 완료

GitHub PR을 승인된 방법으로 병합한 뒤 새 `main`을 다시 읽고 repository current owner와 publication output을 readback한다. Notion·Sheets sync는 완료 조건이 아니다.

완료 전 다음을 수행한다.

```text
remaining-work recalculation
→ canon / manuscript / registry / checker / PR / evidence rescan
→ validated finding correction + verification
→ minimum five evidence-backed full loops and clean exit
→ exact PR head checks
→ merge when authorized
→ new main readback
→ repository destination readback
→ current scope required work = 0
```

완료 보고는 승인 범위·실제 변경·조사와 대안·`BEFORE → AFTER → 기대효과 → trade-off`·exact verification·적대적 finding과 교정·automation/lesson 반영·`NOT_RUN / BLOCKED / 남은 위험`을 구분한다. 실행하지 않은 test, manuscript continuity, 독자 평가, publication, merge 또는 외부 배포를 완료로 주장하지 않는다.
