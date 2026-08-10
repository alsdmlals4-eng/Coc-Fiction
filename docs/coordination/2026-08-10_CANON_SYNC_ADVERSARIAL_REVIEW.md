# Coc-Fiction Latest Canon Sync Adversarial Review — 2026-08-10

## Scope

- base main: `b963a4cf05295408a659482eeaa251749c834874`
- PR: #14
- user-approved decisions reused: 주안 자기통제 프로토콜, 2부 버실라/Woff 제외, 아킴 허용, 폐기 설정 회귀 금지
- protected boundary: 현재 GitHub DRAFT 원고를 원본 대조 없이 기계 치환하지 않는다.

## Attack → validate-critique → refine → regression

### MUST_FIX — resolved — old Canon still treated obedience-factor framing as current

**Evidence:** `CANON_REGISTRY.json`, `bible/01_PROJECT_CORE.md`, `02_CANON_AND_CONTINUITY.md`, `03_PART1_STORY_BIBLE.md`가 과거 독립 설정명을 현행 갈등의 중심 설명으로 유지했다.

**Fix:** `juan.self-control-protocol`을 CANON으로 만들고 `juan.obedience-conditioning`은 SUPERSEDED로 전환했다. 주안의 현재 판단 규칙은 `반응 → 멈춤 → 이유 → 선택`; 주안–엘리스 관계는 명령/복종으로 단순화하지 않는다.

### MUST_FIX — resolved — Part 2 Versilla/Woff exclusion and Akim permission were not canonicalized

**Evidence:** 기존 Part 2 Bible·Registry에 최신 사용자 결정이 없었다.

**Fix:** `part2.versilla-exclusion`, `part2.akim-allowed`, `forbidden_in_part2_manuscript`를 추가했다. 아킴은 지원 가능하지만 세 주연의 중앙 선택을 대신하지 않으며 폐기 인물축의 자동 대체자가 아니다.

### MUST_FIX — resolved — first validator design forced blind legacy-DRAFT rewriting

**Initial hypothesis error:** 최신 폐기 설정을 전부 `forbidden_in_active_manuscript`에 넣으면 안전하다고 가정했다.

**Fresh evidence:** exact-head run `31351564487`은 현재 GitHub DRAFT에 `복종인자` debt가 11개 bundle, `블랙킹` debt가 1개 bundle 남아 있음을 드러냈다. 이 상태에서 자동 치환하면 source/canon reconciliation을 우회한다.

**Root cause:** strict-global ban과 post-decision reconciliation debt의 lifecycle이 한 필드에 섞였다.

**Refine:** validator 계약을 다음으로 분리했다.

- `forbidden_in_active_manuscript`: 현재 DRAFT에서도 즉시 없어야 하는 strict terms
- `forbidden_in_new_or_revised_manuscript`: 앞으로 새로 쓰거나 재퇴고한 원고에서 금지
- `known_manuscript_reconciliation_debt`: 오래된 GitHub DRAFT에 남은 정확한 bundle set; 새 위치로 debt가 늘어나면 CI 실패
- `forbidden_in_part2_manuscript`: 2부 Versilla/Woff는 역사 debt 없이 즉시 strict

TDD 재설계 RED head `9089b26f...`, run `31351678017`: expected FAILURE. 최소 registry/core 수정 후 head `97c4dff1...`, run `31351757414`: SUCCESS.

### SHOULD_FIX — resolved — immutable baselines were being treated as active prose consumers

`check_fiction_content.py`의 active-file sweep가 `analysis/baselines/`까지 검사하고 있었다. FICTION_MASTER는 baseline을 immutable historical machine baseline으로 정의하므로 active prose와 같은 stale-term rewrite 대상으로 보는 것은 책임 위반이다. `baselines`를 active-file sweep에서 제외했다. 실제 composed/current consumers는 별도 index/reverse-outline 검증이 계속 책임진다.

### REJECTED_CRITIQUE — all 11 old bundles should be edited now

기각. 현재 작업은 Canon synchronization이고, 외부 제1~105 최신본과 GitHub DRAFT의 source/canon reconciliation이 다음 별도 단계다. 단어 치환만으로 기존 장면 의미·사건 인과를 바꾸면 사용자 승인한 원본 우선 절차를 위반한다. 대신 debt를 exact path로 fail-closed 등록했다.

### REJECTED_CRITIQUE — ban every use of the word `복종`

기각. 삭제된 것은 독립 고유 설정명과 그 설명 축이지, 인물 대사·주제에서 일반 언어로 쓰이는 ‘복종’ 개념 전체가 아니다. validator는 exact superseded term을 다룬다.

### REJECTED_CRITIQUE — Part 2 Versilla exclusion should be global to all parts

기각. 최신 사용자 Decision은 명시적으로 2부 범위다. `forbidden_in_part2_manuscript`로 범위를 보존한다.

## Current evidence

- initial contract RED `43aa7393...` → run `31351462921`: FAILURE as expected
- initial strict-global attempt `1224a418...` → run `31351564487`: FAILURE, legacy DRAFT debt exposed
- lifecycle-separation RED `9089b26f...` → run `31351678017`: FAILURE as expected
- corrected GREEN `97c4dff1...` → run `31351757414`: SUCCESS

## Scope check

- actual manuscript files changed: 0
- manuscript index/SHA changed: 0
- source evidence changed: 0
- active Base changed: 0
- Canon/Bible/validator only: yes
- new story direction beyond approved decisions: 0

## Merge gate

This review document changes the head, so the final exact-head workflow, changed-file set, review threads, and main behind status must be refreshed before merge.
