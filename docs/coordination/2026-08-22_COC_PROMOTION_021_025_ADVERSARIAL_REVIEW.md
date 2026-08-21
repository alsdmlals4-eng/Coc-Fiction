# 2026-08-22 Coc-Fiction Ch021–025 Promotion · 5× Adversarial Review

Status: `FIVE_FULL_LOOPS_COMPLETE / PREMERGE_CLEAN_CANDIDATE`

## Scope

- locked QA_GREEN candidate Ch21–25 exact transfer;
- Ch20→21 current continuity;
- Ch25→26 fail-closed migration boundary;
- Canon/reader-value non-regression;
- manuscript index / reverse outline / Scene Pass / routers / current-state receipt propagation;
- exact-head hosted validation;
- post-merge GitHub→Notion closure sequencing.

Baseline main: `2fc103b6762425d3b7db317c6e9bb4629c0e0386`.

Target promotion state:

```yaml
current_prefix: 001-025
legacy_tail_starts_at: 026
boundary_after_chapter: 025
next_bounded_bundle: fiction/manuscript/part-1/026-030.md
whole_manuscript_continuity: NOT_YET_CLAIMED
```

---

## Loop 1 — source-authority / exact-transfer attack

### Attack

Assume stored legacy Ch21–25 was accidentally retained, hand-edited, or reconstructed instead of taking the locked current candidate exactly.

### Evidence

The source artifact remains:

- `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- SHA256 `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`.

Exact body receipts installed in `fiction/manuscript/part-1/021-025.md`:

| Ch | title | body chars | SHA256 |
|---:|---|---:|---|
| 21 | 삼 분만 기다립니다 | 6472 | `feb8df2a30c678e174a8cafbbeb8e33ec4d64042339f514a8b771e3b5b61b389` |
| 22 | 다음에는 냄새부터 지워라 | 5916 | `6ae4dba9533cad99139cfef11fdadfbddf5a381bf95091bc939296694c68e801` |
| 23 | 떨어지면 받겠습니다 | 6779 | `cd506e7449f718dfdda9d67db3aba654619457991ffb0fe0cba2ef43f660c40b` |
| 24 | 한 박자 늦게 | 6961 | `c111f79f73c034a6bc2f5dea8606e8b35c687b6a55842a6fd873adbda18b8549` |
| 25 | 승자를 만들지 않기로 했다 | 5870 | `09a945739b8438e30b3721c4c777a0f1c4736f5d6ac7a0684f02877e399869e8` |

TDD RED run `32493979664` proved the new contract failed before production propagation while all pre-existing validation remained Green.

### Verdict

`EXACT_SOURCE_CONFIRMED / NO_MATERIAL_FOLLOWUP`

---

## Loop 2 — Canon / reader-value attack

### Attack

Assume the promoted text turns Jooan's body response into obedience/ownership, makes Elise's voice a domination shortcut, makes Ian treat hypotheses as facts, or creates a new faction Canon accidentally.

### Evidence

- Ch21: Ian continues fact/hypothesis separation and the team preserves a planned wait instead of reflex rescue.
- Ch22–24: Jooan's fast body response is repeatedly followed by pause, reason, and explicit choice; the team does not treat Elise as a one-person control solution.
- Ch25: Jooan asks Elise's choice before acting against the new threat.
- blocked-variant scan over exact Ch21–25: `0` hits.

### Validated interpretation-risk finding

Ch25 contains the in-scene expression `제3세력`. The surrounding prose immediately rejects a flag/name and defines cooperation by current action, but the phrase could later be misread as a formal organization or conflated with the Part2 D01 external acquisition network.

### Minimal correction

Do **not** rewrite the exact candidate body. Record in Scene Card and Revision evidence that Ch25 `제3세력` is temporary tactical shorthand only, not a formal new faction Canon and not D01.

### Verdict

`INTERPRETATION_RISK → FIXED_IN_DERIVED_EVIDENCE / SOURCE_BODY_PRESERVED`

---

## Loop 3 — boundary / regression attack

### Attack

Assume promotion silently modifies Ch26+, destroys the prior Ch20 boundary receipt, or falsely claims whole-manuscript continuity.

### Evidence

- Ch20 body SHA preserved: `dc78dd2f3ab00d853225ca4c98a85832d5fbb088df0b304258172e2ffd754523`.
- stored Ch26 body SHA preserved: `13e7273f2f7a685fc7548edfc28963da673c77936ad0575f2f31ac7830cf1d13`.
- no changed path under `fiction/manuscript/` exists beyond `part-1/021-025.md`.
- current Ch20→21 is restored as direct continuity.
- Ch25 `next_chapter=null` and Ch26 `previous_chapter=null` remain the new fail-closed migration boundary.
- `whole_manuscript_continuity` remains `NOT_YET_CLAIMED`.
- the prior Ch21 legacy hash is retained as historical boundary evidence rather than silently discarded.

### Verdict

`BOUNDARY_CLEAN / NO_CH26_PLUS_MUTATION`

---

## Loop 4 — coupled-consumer omission attack

### Attack

Assume manuscript changed but one or more consumers still advertise prefix 20 / legacy 21 / next 021–025.

### Evidence

The promotion branch updates the coupled current consumers:

- manuscript index manifest + Ch21–25 override;
- reverse-outline manifest + Ch21–25 override;
- resolved Ch20→21 connection + new Ch26 legacy boundary;
- Scene Cards + Revision report;
- Scene Pass registry;
- `START_HERE`, `ACTIVE_CONTEXT`, `FICTION_MASTER`, `HANDOFF`;
- machine-readable current-state receipt;
- scene-pass and current-state regression contracts;
- workflow execution of the Ch021–025 promotion contract.

The receipt intentionally remains in a **pending PR #42** state before merge; it does not invent the future squash-main SHA.

After temporary source-transfer material was used, it was removed. No `.staging/` path remains in the final base-to-head diff.

### Verdict

`COUPLED_PROPAGATION_COMPLETE / POSTMERGE_RECEIPT_CLOSURE_REQUIRED`

---

## Loop 5 — integration / false-completion attack

### Attack

Assume a Green branch is enough to call the promotion complete before main freshness, review-thread, squash merge, final-main receipt closure, and Notion readback.

### Premerge evidence

- final cleaned promotion head before this review: `775cb63eac4304c6750ae69b7c2960278e3eac98`;
- workflow run `32502236202`: SUCCESS, including Base reuse, fiction operating system, content/Canon, reverse-outline reproducibility, reverse-outline analysis, Scene Passes, current-state closure, DOCX packaging, and Ch021–025 promotion contract;
- unresolved review threads: `0`;
- baseline main remained `2fc103b6762425d3b7db317c6e9bb4629c0e0386` during review;
- branch was ahead with no incompatible base movement;
- only PR #42 was open.

This review document itself changes the exact head, so **the workflow must be Green again on the new head before merge**.

### Required postmerge sequence

1. squash PR #42 with expected exact head;
2. fetch the resulting main SHA and verify promoted tree;
3. clear `pending_frontier_change_pr` through a bounded receipt-closure PR without changing the frontier again;
4. set `frontier_observed_at_main` to the PR #42 squash SHA and `last_frontier_change_pr` to `42`;
5. revalidate and merge receipt closure;
6. update Notion CURRENT production boundary to `001–025 / 026+ / next 026–030` and registry Repo Main SHA to final latest main;
7. read back both destinations before reporting `SYNCED`.

### Verdict

`PREMERGE_GATE_CLEAN / COMPLETION_NOT_YET_CLAIMED`

---

## Five-loop result

Validated material finding:

1. Ch25 `제3세력` future-interpretation ambiguity → fixed in derived evidence without altering exact source body.

Rejected/unvalidated attacks:

- source-body drift: not present;
- Canon regression: not present;
- Ch26+ mutation: not present;
- whole-manuscript completion overclaim: not present;
- coupled-consumer omission before merge: not present;
- temporary transfer artifacts left in final diff: not present.

The candidate may proceed only after the workflow re-runs successfully on the exact head containing this review evidence.
