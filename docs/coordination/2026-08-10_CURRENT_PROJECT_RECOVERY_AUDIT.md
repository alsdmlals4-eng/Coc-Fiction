# Coc-Fiction 현재 프로젝트 회수·분류 감사 — 2026-08-10

## 기준선

- 프로젝트: `alsdmlals4-eng/Coc-Fiction`
- 프로젝트 main: `27e0dd4e429d447145596ee8aa36ecdb58ac9161`
- Base main: `53e63f7ebefbb5b2fc0dc528e335252692801421`
- 작업 branch: `agent/coc-fiction-base-integration-20260810`
- 프로젝트 Work Mode: `REVIEW → 필요한 최소 BUILD → REVIEW`
- Manuscript Stage: `REVISE`

이번 감사는 현재 프로젝트만 대상으로 한다. 다른 게임 프로젝트의 PR·branch는 분류·병합하지 않는다.

## Responsibility Map

| 책임 | 현행 원본 |
|---|---|
| 프로젝트 진입 | `[소설]/00_운영체계/START_HERE.md` |
| 운영 생명주기 | `[소설]/00_운영체계/OPERATING_MODEL.md` |
| 프로젝트 Skill routing | `[소설]/00_운영체계/SKILL_REGISTRY.json` |
| 현재 상태 | `fiction/ACTIVE_CONTEXT.md` |
| 작품/Canon | `fiction/FICTION_MASTER.md`, `fiction/CANON_REGISTRY.json` |
| 원본 우선순위 | `fiction/SOURCE_MANIFEST.md`, `fiction/sources/PRIMARY_SOURCE_INVENTORY.md` |
| 원고 색인 | `fiction/MANUSCRIPT_INDEX.json` + 승인 override 합성 |
| 퇴고·회귀 | `skills/fiction-revision-and-validation/SKILL.md` |
| Base 적용 경계 | `docs/fiction-ops/BASE_ADOPTION_AUDIT.md` |
| Handoff | `fiction/HANDOFF.md` |
| 자동 검증 | `tools/check_fiction_operating_system.py`, `tools/check_fiction_content.py`, reverse-outline/scene-pass 검사 |

## PR 전수 회수

### MERGED / 현재 main 이력

| PR | 판정 | 근거 |
|---|---|---|
| #1 `소설 작성·퇴고 운영체계와 작법 검증 구조 추가` | `MERGED / HISTORICAL_BASELINE` | 5개 프로젝트 Skill과 초기 Base 25기능 mapping을 설치. 현행 main의 운영 구조 조상. |
| #3 `최신 정본·225화 확장 원고·구형 참조 격리 통합` | `MERGED / CANON_BASELINE` | #2를 대체해 최신 main 위에서 225화 원고·정본 구조 통합. |
| #4 `활성 문서의 구형 작업 단계 표현 제거` | `MERGED / REFERENCE_FRESHNESS_FIX` | 구형 작업 단계 표현 회귀 방지. |
| #5 `225화 구조 역개요와 대표 품질 게이트 구축` | `MERGED / ANALYSIS_BASELINE` | 원고를 바꾸지 않고 reverse-outline·대표 게이트 구축. |
| #7 `제10·95·180화 파일럿 퇴고 ... v2` | `MERGED / SUPERSEDES_#6` | #6 전송 실패를 대체한 검증된 파일럿. |
| #8 `제6화~제10화 묶음 장면 카드와 연속성 교정` | `MERGED / SCENE_PASS` | 006-010 연속성 패스와 합성 baseline/override 운영을 current canon에 반영. |
| #10 `제91화~제95화 원본 직접 대조와 외전1 종결 복원` | `MERGED / CURRENT_MAIN` | merge commit이 현재 main `27e0dd4e...`; 091-095 직접 대조와 외전1 종결 복원. |

### CLOSED / UNMERGED

| PR | 판정 | 근거 |
|---|---|---|
| #2 `폭풍의 눈 정본·... 편집형 문서로 통합` | `SUPERSEDED` | 운영체계 병합 전 기준에서 diverged. PR #3가 최신 main 위에서 대체 통합했다고 명시. `DO_NOT_MERGE`. |
| #6 `제10·95·180화 파일럿 ...` | `SUPERSEDED` | 긴 인코딩 payload 체크섬 불일치로 적용 전 중단. PR #7이 완전 대체. `DO_NOT_MERGE`. |
| #12 `docs: refresh serial arc revision mode on current canon` | `NEEDS_UPDATE / DELTA_SOURCE_ONLY` | base가 현 current main이고 head는 1 ahead / 0 behind, 변경은 정확히 Registry+revision Skill 2파일. 그러나 PR 자체는 closed/unmerged이며 닫힌 이유는 PR 메타데이터에서 확인되지 않음. 동일 delta를 더 넓은 현재 reconciliation branch에 선택적으로 흡수하고 #12 자체를 재병합하지 않는다. |

### OPEN

| PR | 상태 | 판정 | 근거 |
|---|---|---|---|
| #9 `docs: add serial arc revision mode` | Draft / open | `SUPERSEDED_PENDING_CLEANUP` | head `9bf665cd...`는 current main 대비 `ahead 2 / behind 1 / diverged`. #12가 동일한 2파일 고유 patch를 current main 위 단일 커밋으로 재구성함. stale branch 전체를 병합하지 않는다. |

## #9 → #12 delta 검증

#9와 #12의 실제 patch를 다시 비교했다. 두 PR 모두 고유 변경은 다음 두 파일뿐이며 patch 내용이 동일하다.

1. `[소설]/00_운영체계/SKILL_REGISTRY.json`
   - trigger: `serial-arc`, `chapter-batch`, `scene-pass`, `representative-gate`, `canon-propagation`
   - mode: `serial-arc-pass`
2. `skills/fiction-revision-and-validation/SKILL.md`
   - `serial-arc-pass` mode
   - 앞뒤 경계 화 연속성, 부별 기능, 대표 게이트 대조, 파생 소비자 전파, 자동 지표의 finding-only 경계

따라서 stale #9를 rebase/merge할 이유가 없다. 현재 reconciliation은 **#12의 고유 delta만 선택적으로 재적용**한다.

## 현재 Base drift

프로젝트 Registry·`BASE_ADOPTION_AUDIT.md`는 Base `41a20584...` 및 활성 기능 25개를 기준으로 한다. 현재 Base main은 `53e63f7e...`, generated active Skill은 30개이며, 이 사이에 `developing-and-revising-serial-fiction`이 BCP-009로 구현됐다.

Coc-Fiction이 이미 가진 5개 프로젝트 Skill을 6개로 늘릴 근거는 없다. Base 공용 연재소설 Skill은 다음처럼 **REUSE**하고 프로젝트 고유 책임은 유지한다.

- Base 공용: Reader Promise, Episode Value, POV/voice, Local Payoff/Open Loop, 반복 변주, consequence memory, setup/payoff debt, reader-feedback evidence.
- Coc-Fiction 고유: 작품 Canon·TRPG/source-log 우선순위, 특정 인물/세계관, 합성 manuscript index/override, Scene Pass Registry, Revision Report SHA 전파, 작품별 금지 설정.

## 현재 Active Context/Handoff drift

`fiction/ACTIVE_CONTEXT.md`는 2026-07-23 상태로, repository main 기준의 마지막 직접 대조 작업을 정확히 기록하지만 2026-08-10 대화에서 완료된 제1~105화 POV·후크·캐릭터 재퇴고 산출물은 반영하지 않는다.

주의: 해당 1~105화 DOCX 통합본은 현재 GitHub `fiction/manuscript/`에 자동 반영됐다는 증거가 없다. 따라서 운영 문서에는 **외부/대화 산출물로 완료된 작업과 GitHub canon 반영 상태를 분리**하여 기록해야 한다. 이를 곧바로 `225화 GitHub 원고 수정 완료`로 승격하지 않는다.

## Task 1 최종 분류

```yaml
PR_9: SUPERSEDED_PENDING_CLEANUP
PR_12: NEEDS_UPDATE_DELTA_SOURCE_ONLY
serial_arc_delta: ABSORB_INTO_EXISTING_PROJECT_SKILL
new_project_skill: NO_PROMOTION
base_30_skill_refresh: NEEDS_UPDATE
base_serial_fiction_skill: REUSE
active_context_handoff: NEEDS_UPDATE
story_canon_manuscript_mutation: DO_NOT_MERGE_IN_THIS_PR
```

## 다음 Gate

1. 운영 검사기에 current Base adoption + serial-arc recovery를 요구하는 RED contract를 먼저 추가한다.
2. 최소 프로젝트 운영 변경으로 GREEN을 만든다.
3. exact-head 적대적 검토·Actions·review thread·behind 상태를 확인한다.
4. same-scope 승인 범위 안에서 merge-ready일 때만 병합한다.
5. merged main을 다시 읽은 뒤 #9를 superseded로 닫는다.
