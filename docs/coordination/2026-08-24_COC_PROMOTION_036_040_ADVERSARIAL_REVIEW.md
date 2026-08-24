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

`CLEAN_REVIEW_EXIT` contingent on exact-head hosted validation Green.
