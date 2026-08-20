# ACTIVE CONTEXT

갱신: 2026-08-20

## Resume-first

이 문서는 live router다. 저장된 SHA를 최신값으로 믿지 않는다.

```yaml
work_mode: IMPLEMENT / REVIEW
state_observed_at_main: 60bc62ed3ee4f7870656c8ed5b4ab6b035c71930
current_candidate: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_candidate_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
candidate_state: QA_GREEN
repository_promotion_state: PARTIAL
reconciled_prefix_end: 10
legacy_tail_starts_at: 11
boundary_after_chapter: 10
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/011-015.md
```

새 세션 첫 행동:

```text
latest Coc-Fiction main
→ open PR
→ this ACTIVE_CONTEXT
→ CANON_REGISTRY
→ SCENE_PASS_REGISTRY
→ current-candidate manifest/QA
→ next bounded bundle
```

## Current candidate authority

- Library artifact: `/coc 소설/폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- provenance: `docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json`
- QA: `docs/fiction-ops/2026-08-20_WORKING_001_161_CANDIDATE_QA.md`
- chapter coverage: 001–161 / missing 0 / duplicate 0
- forbidden/superseded variant: 0 in the QA_GREEN integrated candidate
- candidate Green does **not** auto-promote GitHub manuscript authority.

## Completed implementation milestones

- PR #29: 2026-08-20 Canon reconciliation. D01/D02/D03, sword custody, `엘리스`, current Part2 numbering synced.
- PR #30: exact 17-file current-candidate manifest and hashes locked.
- PR #31: QA_GREEN current candidate evidence locked.
- current bounded promotion target: 006–010 current candidate, with frontier moving to 10 only after exact-head CI/merge.

## Current prefix 001–010 contract

### Ch5→6

Current continuity is direct:
- Ch5: 엘리스+이안 해안 / 주안 감옥.
- Ch6: same shore and prison fronts resume.
- old false continuity into a pre-disaster shipboard scene is no longer allowed.

### Ch6–10 protected state

- Ch6: one-way signal receiver limitation remains explicit.
- Ch8: Milly and Hatem are separate people; Hatem is a separate embodied contractor, not automatically Yellow.
- Ch9: `CARTER` evidence does not prove William knowingly caused the current event.
- Ch10: Ian shoots Milly, but no body/blood remains; objective death is unresolved. Emotional loss ≠ proven death.

## Current migration boundary

```yaml
left_current: 10
right_legacy: 11
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

Do not infer current Ch10→legacy Ch11 continuity from adjacent numbering.

## Canon protection

- central question: protection/love/good intentions do not grant authority to steal another person's choice.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: mental ability protects choice; it is not domination.
- Ian: observation → hypothesis → verification → record; unknown stays unknown.
- Dabin: owns decisions about body/future.
- Jumin: consent before optimization.
- Elliott: tragic counterexample; knowledge and repeated failure become paternalistic decision authority.
- D01: bounded external acquisition network = client → broker/old contact node → professional recovery team; top client/hierarchy unresolved.
- D02: +2h photo = authentic non-current cross-loop evidence, not fixed future.
- D03: dead trio remains physical police evidence unless an explicit later event changes its state.
- Elliott sword: ownership unresolved / joint seal; Jumin reaction or scalpel-form transformation is not succession proof.
- Alice Carter canonical Korean spelling: `엘리스`.
- POV: Scene-Locked Hybrid; no scene-internal head hopping.

## Promotion gate

For each 5-chapter bundle:

1. extract exact chapters from the locked QA_GREEN candidate;
2. compare front boundary to current prefix;
3. apply only current/canon-approved delta;
4. atomically update manuscript + composed index + reverse outline + scene cards + registry + routers + validators;
5. exact-head hosted Fiction operating-system CI must be Green;
6. unresolved review threads must be zero;
7. current main must not have moved incompatibly;
8. only then squash-merge and perform post-merge readback.

## Next exact work

`fiction/manuscript/part-1/011-015.md`

The next pass must start at the **Ch10→11 migration boundary**, not by trusting legacy Ch11. After Green propagation, move frontier to 15 and repeat.

Deferred `176-180` source audit remains recorded in `SCENE_PASS_REGISTRY.json`; it does not bypass the bounded migration order.

## Base / shared governance

- Do not auto-advance a stored Base adoption pin merely because Base main changes.
- Fresh-read the project reuse-profile/adoption manifest and current Base proposal state only when a Base write is actually required.
- Do not modify another workstream's open/draft/ready PR.
