# ACTIVE CONTEXT

갱신: 2026-08-10

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- 프로젝트 주 책임: `fiction-canon-and-research: source-log / canon-audit / continuity-map / timeline-and-state`
- 프로젝트 보조 책임: `fiction-revision-and-validation: serial-arc-pass / scene-diagnostic / adversarial-loop / regression-check / pr-review`, `fiction-story-development: scene-card / plot-and-causality / stress-test`, `fiction-drafting: approved-rewrite / pov-and-distance / dialogue-and-subtext`, `fiction-project-operations: checkpoint / handoff / execution-report`
- Base 공용 작법: `developing-and-revising-serial-fiction`의 Canon/각색 경계, POV·voice, 회차 가치, Local Payoff/Open Loop를 선택적으로 재사용한다.

## Continuation State

```yaml
baseline:
  default_branch: main
  last_observed_main_sha: 9a7b2e2419465bd76daf0cf09b96ed7c0cd7d54c
  last_integrated_pr: 17
  merge_commit_sha: 9a7b2e2419465bd76daf0cf09b96ed7c0cd7d54c

progress:
  completed_verified:
    - PR #13 project/Base operating reconciliation
    - PR #14 latest Canon synchronization
    - PR #15 Base proposal locator persistence
    - PR #16 post-merge live-router semantics correction
    - external latest chapters 001-005 source/canon reconciliation and merge
  in_progress:
    - external latest chapters 001-105 gradual canon reconciliation
  ready_next:
    - external latest chapters 006-010 versus stored legacy 006-010
  deferred:
    - stored 176-180 primary-source pass after current external reconciliation sequence

verification:
  pr17_exact_head: 31a4d959cef54ad77576672ff7cca8a53db72c42
  pr17_exact_head_ci: PASS
  pr17_exact_head_run: 31355669160
  post_merge_ci: PASS
  post_merge_run: 31355813027
  unresolved_pr_threads: 0

migration:
  artifact: 폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip
  target_chapters: [1, 105]
  reconciled_prefix_end: 5
  legacy_tail_starts_at: 6
  boundary_after_chapter: 5
  whole_manuscript_continuity: NOT_YET_CLAIMED
  next_bundle: fiction/manuscript/part-1/006-010.md

resume:
  next_executable_step: 제6~10 외부 최신본과 저장 legacy 006-010을 원본·최신 Canon 기준으로 KEEP/APPLY/REWORK/REJECT 판정
  stop_conditions:
    - USER_DECISION_REQUIRED
    - source/canon conflict that cannot be resolved from existing approved authority
    - P0/P1 that invalidates the approved reconciliation contract
  user_decision_needed: false
```

`last_observed_main_sha`는 이 live-router 문서가 자신의 새 commit SHA를 무한 추적하는 값이 아니다. 새 세션은 항상 GitHub `main`과 open PR을 먼저 재조회하고, 위 SHA는 마지막 검증된 integration checkpoint로만 사용한다.

## 현재 GitHub 원고 상태

- 저장소는 기존 225화·45묶음 **storage topology**를 migration 컨테이너로 유지한다.
- 이 225화 저장 토폴로지를 최신 narrative numbering의 최종 편성으로 사용하지 않는다.
- 외부 최신 제1~5화는 원본 사건·최신 Canon·현재 사용자 Decision과 대조 후 GitHub manuscript에 반영됐다.
- 합성 색인·역개요·Scene Pass Registry·대표 게이트·Revision Report가 같은 merge 기준으로 갱신됐다.
- 새 제5화 뒤의 저장 제6화는 아직 최신 서사의 다음 사건으로 간주하지 않는다.
- reverse outline에서 제5화 `next_chapter=null`, 저장 제6화 `previous_chapter=null`로 mixed-migration 경계를 fail-closed 처리한다.
- 기존 저장 `006-010` 내부 연속성 패스는 삭제하지 않고 역사적 검증 증거로 보존하되, 최신 외부 편성과의 reconciliation은 별도 `PENDING`이다.
- `091-095` 원본 직접 대조 패스도 실제 과거 검증 증거로 보존하며 최신 외부 묶음이 도달하면 원본 우선으로 다시 판정한다.

## 제1~5화 reconciliation 결과

- 제1화 `위대한 심연의 군주`: `APPLY`
- 제2화 `내가 고른 경호원`: `APPLY`
- 제3화 `식탁 아래의 축배`: `APPLY`
- 제4화 `카르코사의 낭독`: `APPLY`
- 제5화 `신호기를 잃지 마세요`: `APPLY`

보존한 핵심:

- 주안의 현재 판단은 `반응 → 멈춤 → 이유 → 선택`이다.
- 엘리스는 주안 대신 결론을 내리지 않고 선택 이유를 되찾도록 돕는다.
- 제4화의 흰 방 이미지는 인물 스스로도 기억·상상·정신공격이 만든 거짓 중 무엇인지 확정하지 않는다.
- 신호기는 단순 비상 신호와 수신 진동만 담당한다. 위치·문자·통화 기능을 추가하지 않는다.
- 제5화에서 이안의 구조 경로와 주안·탈론의 분리 경로를 원본 사건 순서에 맞게 분리한다.
- 최신 사용자 결정으로 제외된 축을 원본에 있다는 이유만으로 복원하지 않는다.

## Base 적용 상태

- 현재 재조회한 Base main: `16af66ff51027f74193b60469e7c20281a1cade6`
- Base BCP-009의 `developing-and-revising-serial-fiction`을 공용 작법·검수 owner로 재사용한다.
- Coc-Fiction 프로젝트 Skill은 기존 5개를 유지한다.
- 새 broad Skill을 만들지 않았다.

### Base proposal locator

```yaml
base_proposals:
  canon_migration_debt:
    id: BCP-2026-012-serial-fiction-canon-migration-debt
    proposal_pr: https://github.com/alsdmlals4-eng/Base/pull/234
    merged: true
    status: SUBMITTED
    existing_solution_verdict: ABSORB
    project_verdict_this_cycle: REUSE_EXISTING_BCP
  post_merge_continuation:
    id: BCP-2026-013-post-merge-continuation-state-reconciliation
    proposal_pr: https://github.com/alsdmlals4-eng/Base/pull/235
    merged: true
    status: SUBMITTED
    project_verdict_this_cycle: REUSE_EXISTING_BCP

base_boundary:
  proposal_storage_merge_authority: already_consumed_for_relevant_proposals
  base_implementation_authority: NOT_GRANTED_IN_THIS_STAGE
  active_base_files_changed_by_this_cycle: 0
  implementation_boundary: SEPARATE_FOLLOWUP_STAGE
```

이번 001-005 작업에서 발견한 `current prefix + unreconciled legacy tail` 문제는 BCP-012의 기존 범위로 충분하다. 새 중복 BCP를 만들지 않았다. post-merge live-router 문제도 BCP-013이 이미 Base main에 병합됐으므로 재사용한다. **두 제안의 병합은 Base 활성 구현 승인과 무관하다.**

## 다음 정확한 저장소 작업

`fiction/manuscript/part-1/006-010.md`를 현재 외부 최신 제6~10화와 대조한다.

```text
새 제5화 종료 상태 확인
→ 외부 최신 제6~10화 실제 원고 확보
→ 저장 legacy 006-010과 회차별 delta 생성
→ 원본 사건 기록·최신 사용자 Decision·Canon 대조
→ KEEP / APPLY / REWORK / REJECT
→ 승인된 delta만 manuscript에 반영
→ MANUSCRIPT_INDEX / reverse-outline override / Scene Pass Registry / Scene Cards / Revision Report 전파
→ reconciled_prefix_end를 10으로 확장
→ exact-head CI + adversarial review + PR merge + post-merge verification
```

## 변경 금지

- 외부 산출물의 `최종` 표기만으로 남은 제6~105화를 자동 덮어쓰지 않는다.
- 저장 225화 토폴로지를 최신 서사 화수표로 되돌리지 않는다.
- 자동 역개요를 원고 수정 명령으로 사용하지 않는다.
- 구형 통합 초안·archive·baseline을 current prose 입력으로 사용하지 않는다.
- Base proposal 병합을 Base 활성 구현 승인으로 해석하지 않는다.
