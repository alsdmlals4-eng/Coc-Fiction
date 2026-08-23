# 2026-08-24 Coc-Fiction Ch026–030 Promotion · 5× Adversarial Review

Status: `FIVE_FULL_LOOPS_COMPLETE / PREMERGE_REVALIDATION_REQUIRED`

## Scope

- user-designated segmented source set adoption;
- exact Ch026–030 transfer and SHA receipts;
- latest direct user Canon protection;
- Ch25→26 continuity and Ch30→31 fail-closed migration boundary;
- manuscript/index/reverse-outline/Scene Pass/router/current-state coupled propagation;
- validator migration without gate weakening;
- no Ch031+ prose mutation;
- no 101–105 source-gap auto-fill;
- no image generation.

Baseline main: `4c19907b8deb8e491aa9dcd9313d83f4a4cfec6c`.

Validated pre-review head: `6927cfa73b5430f112b53efb7561aa18a0baf28b`.

Validated workflow: Fiction operating system run `32668074888` = SUCCESS.

Target candidate state before merge:

```yaml
source_authority: USER_DESIGNATED_SOURCE_CHUNK_SET
current_bundle_source: 폭풍의눈_2차퇴고_제021-030화_상실광기_강적위상_가독성강화본(1).docx
current_bundle_source_sha256: e15c8fb4ed4ab1b6980c2c57f3979986bdbfa02f77aafef3cc84d3652cb70547
candidate_prefix: 001-030
legacy_tail_starts_at: 031
boundary_after_chapter: 030
next_bounded_bundle: fiction/manuscript/part-1/031-035.md
whole_manuscript_continuity: NOT_YET_CLAIMED
source_coverage_gap: 101-105
```

---

## Loop 1 — source-authority contamination attack

### Attack

Assume the old integrated QA_GREEN DOCX, duplicate uploads, legacy GitHub prose, or generated visual boards can silently regain source authority.

### Evidence

`docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json` records the segmented user source set and hashes. The old integrated `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx` is explicitly `derived cross-check only`.

Duplicate source uploads for 031–040 and 126–135 were byte-identical and are represented as duplicate aliases rather than independent authorities.

The current source set has no 101–105 file. That gap is explicitly fail-closed and must not be filled from the old aggregate or legacy storage.

### Finding / correction

The initial work state still treated the aggregate file as the reconciliation artifact. This was corrected across Source Manifest, Scene Pass Registry, routers, current-state receipt, PR contract, and Notion SYSTEM Source Authority.

### Verdict

`PASS / SOURCE AUTHORITY CLEAN / 101-105 GAP PRESERVED`

---

## Loop 2 — Canon and character-distortion attack

### Attack

Assume exact source transfer reintroduces superseded character facts or weakens the user-confirmed character roles.

### Protected user decisions

- Milly Kosa: actual male; Miskatonic female disguise used Hatem's appearance.
- Hatem: female; default black-mask cultist appearance.
- Talon: Part 1 core antagonist with high on-screen combat competence.
- Part 1 and Part 2 must not be conflated.

### Evidence from Ch026–030 promotion

- Ch26 preserves Talon's high combat pressure: he directly fights multiple shoggoths rather than becoming disposable fodder.
- Ch27 presents Milly as a separate embodied person and Hatem as a separate person; Hatem dies while protecting Ian.
- Ch28 treats post-death Hatem as hallucination/memory; no new objective information is allowed through the hallucination.
- Ch29 preserves Ian/Milly's real past friendship while separating it from their present opposing choices.
- Ch30 preserves Milly's storm-walk and Kubara's spear observations without promoting unknown origin/function/ownership into fact.

`check_fiction_scene_passes.py` now includes the current bundle in superseded-term scans, while `tests/test_promote_026_030_contract.py` locks exact title/POV/body-char/SHA receipts.

### Finding / correction

A brittle Ch29 exact phrase assertion failed despite whole-body SHA matching. The redundant string assertion was removed; the stronger whole-body hash contract remains. No source body was rewritten to satisfy the test.

### Verdict

`PASS / USER CANON PRECEDENCE PRESERVED / NO TEST-DRIVEN SOURCE REWRITE`

---

## Loop 3 — boundary and over-promotion attack

### Attack

Assume promoting Ch026–030 silently validates Ch031+, changes Part numbering, or claims whole-manuscript continuity.

### Evidence

- Ch25 now links directly to current Ch26.
- Ch30 is the new `RECONCILIATION_MIGRATION_BOUNDARY`.
- Ch31 is `LEGACY_TAIL_BOUNDARY` with `previous_chapter=null`.
- `whole_manuscript_continuity` remains `NOT_YET_CLAIMED`.
- next bounded bundle is `fiction/manuscript/part-1/031-035.md`.
- branch compare contains no Ch031+ manuscript mutation.
- source gap 101–105 remains explicit.

### Finding / correction

The old reverse-outline overrides and Scene Pass validator initially retained the Ch25→26 fail-closed boundary. Official reverse-outline generation was rerun, then the validator was migrated to the Ch30→31 boundary.

### Verdict

`PASS / FRONTIER ADVANCES ONLY THROUGH 030 / NO CH031+ PROSE MUTATION`

---

## Loop 4 — coupled-consumer and validator-staleness attack

### Attack

Assume the manuscript changed while one of the operational consumers still advertises prefix 25, old source authority, old pending PR, or old next bundle.

### Coupled consumers reviewed

- `fiction/manuscript/part-1/026-030.md`
- `fiction/MANUSCRIPT_INDEX.json`
- `fiction/analysis/MANUSCRIPT_INDEX_OVERRIDE_026_030.json`
- reverse-outline composed artifact + 021–025/026–030/031-boundary overrides
- `fiction/analysis/SCENE_CARDS_026_030.md`
- `fiction/analysis/SCENE_PASS_REGISTRY.json`
- `fiction/reports/REVISION_2026-08-24_CURRENT_RECONCILIATION_026_030.md`
- `START_HERE`, `ACTIVE_CONTEXT`, `FICTION_MASTER`, `HANDOFF`
- `CURRENT_STATE_RECEIPT.json`
- Scene Pass validator
- current-state closure tests
- historical Ch021–025 promotion regression test
- new Ch026–030 promotion test
- Fiction operating-system workflow

### Findings / corrections

1. `delivery_state` disappeared from ACTIVE_CONTEXT/HANDOFF during propagation → restored.
2. reverse-outline composition stale → regenerated with official builder and rechecked.
3. Scene Pass validator hardcoded old aggregate source/frontier 25 → migrated to user chunk source/frontier 30 without removing historical invariants.
4. current-state closure hardcoded PR #42 and merged-style router vocabulary → generalized pending-vs-merged contract.
5. Ch021–025 historical promotion test incorrectly required the live frontier to remain 25 forever → converted to immutable historical body/receipt regression.
6. new Ch026–030 contract existed but workflow did not execute it → added as a mandatory CI step and trigger path.

### Verdict

`PASS / COUPLED CONSUMERS PROPAGATED / VALIDATORS EVOLVED INSTEAD OF BYPASSED`

---

## Loop 5 — integration, hygiene, and false-completion attack

### Attack

Assume temporary payload/workflow files remain, a previous-head Green is reused, the PR is merged before final exact-head validation, or Notion is marked synced before main exists.

### Evidence

Temporary transfer helpers/payloads and one-time regeneration workflows/triggers were removed from the final branch diff.

The validated pre-review exact head `6927cfa73b5430f112b53efb7561aa18a0baf28b` passed the complete Fiction workflow, including the newly wired Ch026–030 contract.

This review document creates a new head. Therefore that previous Green **cannot** be reused as the final merge gate.

### Required final sequence

1. run Fiction operating-system CI on the exact head containing this review;
2. verify all required steps Green, including Ch026–030 promotion contract;
3. verify unresolved review threads = 0 and main has not moved incompatibly;
4. mark PR #48 ready and squash merge;
5. fetch resulting main SHA and verify Ch026–030 tree + Ch30→31 boundary;
6. close pending receipt in a bounded post-merge receipt update without moving frontier again;
7. update Notion SYSTEM Source Authority / production boundary / Repo Main SHA;
8. read back Notion and GitHub before reporting `SYNCED`.

### Verdict

`PREMERGE REVIEW PASS / FINAL EXACT-HEAD REVALIDATION REQUIRED`

---

## Five-loop result

Material findings found and corrected during the five loops:

1. aggregate source authority persisted after user switched to segmented originals;
2. 101–105 source gap needed explicit fail-closed handling;
3. reverse-outline generation was stale after frontier movement;
4. Scene Pass validator still hardcoded source/frontier 25;
5. current-state closure hardcoded old pending PR and merged-style vocabulary;
6. old Ch021–025 test confused historical promotion state with live frontier state;
7. Ch026–030 contract was not actually wired into CI;
8. temporary transfer/regeneration files required cleanup before merge.

No validated remaining design/Canon blocker was found inside Ch026–030. Completion is **not** claimed until the new exact head passes CI and post-merge closure/readback is complete.
