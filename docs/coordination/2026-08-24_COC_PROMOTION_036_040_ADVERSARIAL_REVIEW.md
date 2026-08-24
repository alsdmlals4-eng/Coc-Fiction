# COC Promotion 036–040 · 5× Adversarial Review — 2026-08-24

1. Identity/life-state: Cecilia alive entering Ch36; Milly/Hatem separate; Lhazak UNKNOWN without proof. PASS.
2. Power/reveal timing: Elise D04 human-inclusive; Largo `[규율]` not revealed in Part 1. PASS.
3. Faction flattening: Yellow leadership loss != organization extinction; Garon negotiation != permanent faction conversion. PASS.
4. Agency/theme: Jooan self-check and Elise negotiation remain choices; William love does not erase wrongdoing. PASS.
5. Boundary/provenance: Ch35→36 candidate-current; Ch40→41 fail-closed; 101–105 gap and whole continuity unresolved. PASS.

## Validator follow-up
- RED correctly caught that the legacy `expanded DRAFT` label check was not frontier-aware after installing exact Ch036–040 source prose.
- Root cause: `tools/check_fiction_content.py` required the legacy DRAFT status line for every storage bundle, including bundles already registered in `SCENE_PASS_REGISTRY.completed_bundle_passes`.
- Fix: only unpromoted/uncompleted bundles retain the expanded-DRAFT label requirement; completed bounded bundles remain governed by exact manuscript/index/scene-pass/contract checks.
- The consumer materializer is now idempotent with respect to this review document so hosted validation can converge without bot-generated diff loops.

## Reverse-outline follow-up
- RED then caught stale derived reverse-outline evidence/metrics copied from the legacy Ch036–040 storage prose.
- Root cause: source title/POV/body SHA had been replaced correctly, but derived chapter function/evidence/metrics still came from the pre-promotion legacy outline.
- Fix: regenerate Ch35–41 reverse-outline entries from the current exact manuscript plus composed manuscript index, then reapply the fail-closed Ch40→41 boundary.
- The regeneration step is deterministic and runs before `build_fiction_reverse_outline.py --check`.

## Scene-pass follow-up
- RED then exposed hard-coded frontier=35 assumptions in `check_fiction_scene_passes.py`; exact manuscript and reverse-outline validation had already passed.
- Root cause: the checker still treated the old Ch36 legacy SHA as an active boundary, used chapter titles as body-substring invariants, and hard-coded the Ch35→36 migration boundary and `036–040` next bundle.
- Fix: derive the active frontier and migration boundary from `SCENE_PASS_REGISTRY`, treat superseded right-boundary SHAs as historical once a later pass promotes that chapter, and validate the next five-chapter range structurally.
- This makes Scene Pass validation reusable for subsequent bounded promotions instead of requiring a new hard-coded boundary patch each time.

## Pending-state closure follow-up
- RED then showed that candidate Scene Pass state had advanced to `001–040` while CURRENT_STATE_RECEIPT and live routers still described main `001–035` as if no PR were pending.
- Root cause: PR candidate truth and main production truth were not represented separately in the closure contract.
- Fix: while PR #55 is pending, receipt/router candidate fields are `001–040 / 041+ / boundary 40→41 / next-after-merge 041–045`, `pending_frontier_change_pr=55`, and `frontier_observed_at_main=null`; the prose explicitly preserves main production at `001–035` until merge.
- This matches `tests.test_current_state_closure` without falsely claiming a main production frontier move before merge.

`CLEAN_REVIEW_EXIT` contingent on exact-head hosted validation Green.
