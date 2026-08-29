# Coc-Fiction policy correction and PR #61 receipt closure — 2026-08-29

## Scope

이번 변경은 원고 production frontier를 새로 이동시키지 않는다.

```text
repository workspace correction
+ research / feasibility / long-term / automation policy
+ image candidate / final lock separation
+ already-merged PR #61 receipt closure
+ stale live router cleanup
```

Ch056–060 promotion은 포함하지 않는다.

## Before

- PR #61은 2026-08-24 병합됐고 Ch051–055 원고/consumer가 main에 존재했다.
- `CURRENT_STATE_RECEIPT`, `START_HERE`, `ACTIVE_CONTEXT`, `HANDOFF`는 여전히 `pending_frontier_change_pr: 61`, production `001–050` 또는 Notion sync requirement를 포함했다.
- root `AGENTS.md`도 Notion CURRENT 동기화/readback을 완료 조건으로 사용했다.

## After

```yaml
frontier_observed_at_main: 1de8beef60612ecc8113b4d7b8146ba7733d96d6
last_frontier_change_pr: 61
pending_frontier_change_pr: null
reconciled_prefix_end: 55
legacy_tail_starts_at: 56
boundary_after_chapter: 55
next_bounded_bundle: fiction/manuscript/part-1/056-060.md
whole_manuscript_continuity: NOT_YET_CLAIMED
manuscript_promotion_state: PAUSED_UNTIL_EXPLICIT_RESUME
```

- GitHub repository가 current human/structured/manuscript/evidence owner다.
- legacy Notion은 `HISTORICAL_MIGRATION_REFERENCE_ONLY`이며 sync/readback/completion target이 아니다.
- 새 current owner는 `docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md`다.
- 중요한 작품·운영 결정은 current canon/manuscript, targeted official/primary research, success/failure evidence, alternatives와 production feasibility를 확인한다.
- 장기 품질과 최소 복잡도를 우선한다.
- 승인 범위의 routine 작업은 연속 진행하고 사용자는 핵심 작품 의미·Canon·final Visual lock·고위험 변경에 집중한다.
- 실제 consumer가 있는 visual candidate는 먼저 제작할 수 있으나 final lock과 distribution promotion은 사용자에게 남긴다.

## Historical handoff disposition

`docs/coordination/2026-08-24_COC_PAUSE_HANDOFF.md`는 당시 pause와 미종결 상태를 증명하는 immutable historical receipt다.

그 문서의 다음 항목은 current instruction이 아니다.

```text
pending PR #61 receipt
production 001-050
Notion CURRENT sync/readback
```

현재 값은 root `AGENTS.md`, repository autonomy policy, `CURRENT_STATE_RECEIPT.json`, `ACTIVE_CONTEXT.md`, `HANDOFF.md`에서 읽는다.

## Evidence ceiling

- manuscript body changed: NO
- Scene/Canon/registry frontier moved: NO
- receipt/router corrected: YES
- automated repository validation: REQUIRED_AT_EXACT_HEAD
- reader/human review: NOT_RUN
- whole-manuscript continuity: NOT_YET_CLAIMED
- publication readiness: NOT_RUN
