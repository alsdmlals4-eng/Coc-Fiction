# AGENTS.md

이 저장소는 **Coc-Fiction / 장편 서사 프로젝트**다. 게임 런타임 프로젝트가 아니며 Godot 관련 실행·Scene·Resource 규칙은 `NOT_APPLICABLE`이다.

## 권한 순서

1. 사용자의 최신 직접 지시
2. 이 `AGENTS.md`
3. `fiction/ACTIVE_CONTEXT.md`와 승인된 작업 계약
4. 작품 정본과 실제 원고·구조화 데이터·검사
5. 프로젝트 내부 운영 문서와 채택된 Base 계약
6. Base current completed main
7. 현재 공식·1차 자료, 직접 관련된 현업·출판·도구 근거와 historical reference

과거 채팅·메모리·Library·외부 workspace는 탐색 단서일 뿐 current truth를 대신하지 않는다.

## 최초 읽기

```text
[소설]/00_운영체계/START_HERE.md
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ docs/fiction-ops/CURRENT_STATE_RECEIPT.json
→ 현재 묶음 Scene Card / Revision Report / 실제 manuscript
→ latest completed main / same-goal open or recent PR / exact validators
```

`CURRENT_STATE_RECEIPT.json`의 SHA/PR은 마지막 readback 증거다. 영구적인 latest pointer가 아니므로 재개할 때 current GitHub 상태를 다시 조회한다.

## Repository-first 정본 경계

```text
REPOSITORY_PRIMARY_CANON
NOTION_LEGACY_MIGRATION_ONLY
GOOGLE_SHEETS_MIGRATION_ONLY
```

- repository가 사람용 작품 설명·Canon·Scene Card·결정, 구조화 데이터, 실제 원고, 검사, production handoff와 evidence의 active owner다.
- Notion·Google Sheets는 unique 미이관 자료가 실제로 남고 사용자가 bounded migration을 승인한 경우에만 read-only input으로 사용한다.
- 새 기획·결정·원고 승인·visual lock·완료를 위해 Notion CURRENT 페이지를 만들거나 갱신하거나 readback하지 않는다.
- 과거 Notion page/database/attachment는 `HISTORICAL_REFERENCE_ONLY`이며 current truth, write target, approval owner 또는 completion gate가 아니다.
- 외부/Library의 `QA_GREEN` candidate는 revision input이며 자동으로 production authority가 되지 않는다.
- GitHub production authority는 `SCENE_PASS_REGISTRY.json`의 bounded reconciliation frontier가 책임진다.
- `current prefix / legacy tail / migration boundary`를 인접 화수만으로 자동 연결하지 않는다.
- `whole_manuscript_continuity=NOT_YET_CLAIMED`를 전체 연속성 완료로 확대 해석하지 않는다.
- Canon과 사용자 Decision이 파생 역개요·자동 진단보다 우선한다.

## 보호 규칙

- 진행 중 `open/draft/ready` PR은 사용자가 현재 작업에서 PR 번호와 허용 동작을 명시하지 않는 한 read-only다.
- 닫힌 RED/diagnostic PR과 과거 migration 자료는 역사 증거이며 임의 삭제·재병합하지 않는다.
- `엘리스`가 Alice Carter의 현행 한글 Canon 표기다.
- 주안의 `반응 → 멈춤 → 이유 → 선택`, Scene-Locked Hybrid, D01/D02/D03/N04 및 귀속 미정 공동봉인 규칙을 회귀시키지 않는다.
- 기존 5화 bounded promotion을 대규모 일괄 승격으로 바꾸지 않는다.
- 사용자 승인 없이 핵심 인물 동기, 사건 인과, 세계관 규칙, 결말 방향, 작품의 정서적 약속을 변경하지 않는다.

## 조사·실현 가능성·장기 품질

```text
IMPLEMENTATION_FEASIBILITY_BEFORE_COMMITMENT
CURRENT_OFFICIAL_PRIMARY_RESEARCH_REQUIRED
DIRECTLY_RELEVANT_FIELD_EVIDENCE_REQUIRED
ACTUAL_PROJECT_STRUCTURE_FEASIBILITY_REQUIRED
LONG_TERM_QUALITY_OVER_LOCAL_SPEED
ROOT_CAUSE_AND_REUSE_BEFORE_REPEATED_MANUAL_PATCH
MINIMUM_SUFFICIENT_COMPLEXITY
SPECULATIVE_OVERENGINEERING_REJECTED
PLAYABLE_OR_OPERATIONAL_VALUE_OVER_DOCUMENT_VOLUME
```

material한 서사 구조, 사실 조사, 연속성 체계, 원고 format, packaging, validator, 자동화 또는 배포 구조를 확정하기 전에 다음을 수행한다.

1. current Canon·Decision·실제 원고·Scene Pass·validator를 읽는다.
2. repository와 current Base에 이미 있는 해결책을 먼저 찾는다.
3. 외부 사실, 실존 제도·기술·문화·시대성, 출판·format·도구 동작이 결과를 바꿀 수 있으면 최신 공식·1차 자료와 직접 관련된 성공·실패·혼합 사례를 조사한다.
4. 최소한 작품 가치, 서사 일관성, 실제 원고 구조, registry/schema, validator, packaging, 비용·권리·보안, migration·rollback을 대조한다.
5. 결과를 `FEASIBLE | PARTIAL | BLOCKED_UNVERIFIED`로 기록한다.

순수 창작 취향이나 외부 사실이 결론을 바꿀 수 없는 기계적 rename·formatting만 `MECHANICAL_NO_EXTERNAL_DEPENDENCY` 사유를 남길 수 있다. 조사 없이 사실성·현업 타당성·출판 가능성을 주장하지 않는다.

빠른 문장 patch가 다른 Scene·Canon·registry에서 반복 충돌을 만들면 root cause와 owner를 고친다. 반대로 현재 작품 가치가 없는 범용 framework, dashboard, duplicate registry, 대규모 추상화는 만들지 않는다.

## 시각 후보 제작과 확정

표지·인물·장면·관계·홍보·검수용 시각자료가 실제 consumer 또는 명시적으로 계획된 deliverable에 필요하면 `CANDIDATE_FIRST_VISUAL_PRODUCTION`을 사용한다.

```text
VISUAL_NEED_CONFIRMED
→ CURRENT_PROJECT_AND_VISUAL_CANON_READBACK
→ ACTUAL_OR_EXPLICITLY_PLANNED_CONSUMER_REQUIRED
→ EXISTING_APPROVED_ASSET_AND_CANDIDATE_REUSE_CHECK
→ BOUNDED_BRIEF_READY
→ IMAGE_MODEL_GENERATES_ONE_CANDIDATE
→ OBJECTIVE_QA_AND_BOUNDED_CORRECTION
→ PRESENT_FOR_USER_FINAL_LOCK
```

- current Canon, 인물·시대·장소·상징, 기존 승인 이미지·시안, consumer, 규격, Keep/Avoid/Do Not Drift와 rights/provenance를 먼저 읽는다.
- preflight가 끝나면 동일 내용을 다시 승인받기 위해 멈추지 않고 bounded candidate 한 건을 만든다.
- 실제 이미지 산출물은 host image generation/editing model로 제작한다. SVG/vector, Canvas, Python drawing 또는 기타 직접 그리기 방식으로 대체하지 않는다.
- 객관 결함만 같은 deliverable 안에서 bounded correction한다. 다른 인물·장면·Art Direction·독립 variant는 새 scope다.
- 사용자는 결과를 본 뒤 `LOCK / REVISE / REJECT / RETAIN_AS_REFERENCE`를 결정한다.

```text
NEEDED
→ BRIEF_READY
→ GENERATED_CANDIDATE
→ USER_FINAL_LOCKED
→ CANON_REGISTERED
→ PUBLISHED_OR_IMPLEMENTED
→ CONSUMER_VERIFIED
```

```text
GENERATED_CANDIDATE != USER_FINAL_LOCKED
USER_FINAL_LOCKED != PROJECT_ASSET_APPROVED
CANDIDATE_PRODUCTION_IS_NOT_PUBLICATION_AUTHORITY
```

후보·final lock·repository 등록·실제 문서/표지/홍보물 적용·consumer 검증을 분리한다. 구조·관계·Flow·체크리스트는 Markdown·표·JSON·Mermaid 같은 text-native artifact를 우선한다.

## 사용자 개입 최소화와 학습

```text
MINIMIZE_USER_INTERVENTION_WITH_SAFE_FINAL_CONTROL
INCIDENT_SOLUTION_LESSON_AUTOMATION_LOOP
```

AI는 fresh-read, 조사, 대안 비교, bounded candidate·revision 준비, validator 실행, 안전한 문서·registry 교정, readback, 회귀검사와 남은 작업 재계산을 반복 승인 없이 진행한다.

사용자에게 올릴 항목은 핵심 인물·세계관·사건 인과·정서·결말·표현 수위·Art Direction, 객관적 우열이 없는 취향, 큰 범위·비용, 외부 공개·출판, 권리·보안, 비가역 삭제와 current Canon 충돌이다. visual final lock과 production promotion은 사용자 결정이다.

```text
problem → reproducible evidence → root cause → correction → regression prevention → repository owner/readback → reusable lesson → Base BCP when cross-project evidence exists
```

대화 기억을 학습 정본으로 사용하지 않는다. 반복 가능한 교훈은 repository owner, validator, test, template, checklist 또는 승인된 Base proposal로 남긴다.

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

추가 테스트가 도입된 변경은 해당 테스트도 실행한다. 과거 Green을 current head의 Green으로 재사용하지 않는다. source/static, validator, manuscript readback, packaged output, human literary judgment와 publication readiness를 서로 구분한다.

## 실제 적대적 검토와 교정

material 변경 후 current Base whole-state review를 실제 수행한다.

```text
ACTUAL_POST_COMPLETION_ADVERSARIAL_REVIEW_REQUIRED
FULL_LOOP_COUNT_MINIMUM: 5
EXECUTION_EVIDENCE_REQUIRED
CORRECT_VALIDATED_FINDINGS
NO_REVIEW_COMPLETION_CLAIM_WITHOUT_EVIDENCE
CLEAN_REVIEW_EXIT
```

각 loop는 같은 final-state lineage의 전체 승인 범위를 다시 공격한다.

```text
FULL_SCOPE_REVIEW
→ FIND
→ VALIDATE_CRITIQUE
→ CORRECT_VALIDATED_FINDINGS
→ VERIFY_AND_REGRESSION_RECHECK
→ BETTER_ALTERNATIVE_SEARCH
→ LONG_TERM_PLAN_FIT_RECHECK
→ RE_ATTACK
```

input head, evidence delta, 발견, 검증된 finding, 교정, verification, 더 나은 대안, 장기 적합성, unresolved와 output head를 기록한다. 최소 5회 뒤에도 Canon 충돌, 연속성 오류, stale reference, validator 회귀, evidence 과장이 남으면 계속한다.

## 완료

```text
remaining-work recalculation
→ Canon/manuscript/registry/consumer/PR/evidence correction rescan
→ valid finding? correct + verify + recalc
→ minimum five whole-state loops and clean exit
→ exact PR head validators
→ merge when authorized
→ new main readback
→ repository destination readback
→ current scope remaining work = 0
```

GitHub 병합 뒤 새 `main`과 repository destination을 다시 읽어야 완료다. Notion CURRENT 갱신·동기화·readback은 완료 조건이 아니다.

완료 보고는 scope·보호 대상, before/after, 실제 변경, 조사·대안, validator/evidence class, 적대적 finding과 실제 교정, exact PR/merge/main identity, repository readback, `NOT_RUN`과 남은 위험을 구분한다. 실행하지 않은 검사, 전체 연속성, human quality 또는 publication readiness를 PASS로 쓰지 않는다.
