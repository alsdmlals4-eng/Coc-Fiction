# 2026-08-21 Coc-Fiction Current-State Closure · 5× Adversarial Review

Status: `FIVE_FULL_LOOPS_COMPLETE / PREMERGE_CLEAN_CANDIDATE`

## Scope attacked in every loop

- root cold-start routing;
- repository current-state receipt and live routers;
- production frontier `001–020 / 020→021 / next 021–025`;
- story/Canon non-regression boundary;
- DOCX packaging correction and evidence ceiling;
- CI/TDD evidence;
- GitHub→Notion post-merge sequencing;
- stale Issue #11 closure timing;
- open-PR and main-freshness protection.

No loop treats a finding as valid until repository/file/CI evidence supports it.

## Baseline

- main at work start: `395f0af0120f5ab6949c86772d3b77b5b3eb9f3a`
- frontier-changing PR: `#39`
- source candidate SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- current prefix: `001–020`
- current boundary: `020→021`
- next bounded unit: `021–025`
- whole-manuscript continuity: `NOT_YET_CLAIMED`

---

## Loop 1 — self-stale state semantics attack

### Attack

Assume the new receipt and routers become wrong immediately after this correction PR merges.

### Validated finding

`last_integrated_pr: 39` and an unqualified stored-main field would become semantically false after PR #40 merged even though the frontier itself did not change.

### Minimal improvement

Reframe the receipt/router evidence as frontier-specific:

- `frontier_observed_at_main`
- `last_frontier_change_pr`

Explicitly state that these fields record the last production-frontier change and must not be interpreted as the repository's permanent latest SHA/PR.

### Regression evidence

A new test was made RED first:

- RED head: `2a651daa7f499a579c13c9676470c1dcc7ae0cfb`
- workflow run: `32488320635`
- existing fiction validators: Green;
- current-state contract: expected failure.

After the semantic correction, the full workflow returned Green before the next loop.

### Verdict

`MUST_FIX → FIXED`

---

## Loop 2 — unauthorized content / Canon drift attack

### Attack

Assume the operational cleanup accidentally rewrites prose, Canon, promoted chapter data, or advances the frontier.

### Evidence

Fresh base-to-head comparison showed changes only in:

- workflow/test/tool files;
- root `AGENTS.md`;
- current-state/QA/design/review docs;
- `fiction/ACTIVE_CONTEXT.md`;
- `fiction/HANDOFF.md`.

Changed paths under `fiction/manuscript/**`: `0`.

Changed `fiction/CANON_REGISTRY.json`: `0`.

`SCENE_PASS_REGISTRY.json` is not modified; it remains the structured frontier authority at 20→21.

### Critique validation

No content/Canon drift exists in the diff. Expanding scope to rewrite manuscript or Canon would be an invented change.

### Verdict

`NO_MATERIAL_FOLLOWUP`

---

## Loop 3 — cold-start consumer omission attack

### Attack

Assume a worker enters through the project's existing internal `START_HERE.md` rather than the new root AGENTS router.

### Validated finding

The first implementation linked `CURRENT_STATE_RECEIPT.json` from root `AGENTS.md` and live routers, but the existing internal START_HERE reading order could still skip the receipt.

### Minimal improvement

Add the receipt to the existing START_HERE reading order and state its frontier-evidence / fresh-main semantics.

### Regression evidence

A dedicated assertion was added first and observed RED:

- RED head: `dafb35488d8de241d0a51fb1664bca206c5b4303`
- workflow run: `32488570332`
- all pre-existing validators remained Green;
- only the current-state contract failed at the new START_HERE assertion.

After the START_HERE update:

- head: `2dff8a8f74d28025e06a597f5defa13fc3d77b7f`
- workflow run: `32488618074`
- result: `SUCCESS`.

### Verdict

`OMISSION → FIXED`

---

## Loop 4 — DOCX authority and evidence-overclaim attack

### Attack

Assume correcting the running header accidentally creates a new manuscript authority, changes body prose, or repeats the old false `visual QA complete` claim.

### Evidence

Immutable source:

- SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- original running header: `폭풍의 눈 · 제001–010화`.

Presentation-only derivative:

- SHA256: `d96eab6115f71d03657bfa07dad9bf3d27a4bbb28545d8b67ffffbb507e8e636`
- header: `폭풍의 눈 · 001–161 통합 검수본`.

`word/document.xml` source/derivative SHA is identical:

`1920a28fa7109d3d42f5bcbc8b8ce2f392c1308ca12c6f6074da32369a8796fe`

The QA addendum explicitly labels the derivative `PRESENTATION_ONLY_DERIVATIVE` and states that it does not move production authority.

Automated render comparison covered all 796 pages; body blocks below the header band differed on 0/796 pages. Eight all-page contact sheets and four high-resolution pages were inspected. The canonical helper's full PNG rasterization timeout is recorded instead of being hidden.

### TDD evidence

- packaging RED head: `8e152f394f24c420d32fc9256c7f43c97a40f78f`
- RED run: `32487311975`
- only the new packaging contract failed.
- implementation head: `20f5ace82adfb0db1fbbc5d9f17d38c0111b9640`
- GREEN run: `32487404915`.

### Rejected critiques

- Replace the immutable source candidate with the derivative: `REJECT`.
- Claim full 796-page manual high-resolution inspection: `REJECT`.
- Treat header packaging correction as 021–161 production promotion: `REJECT`.

### Verdict

`EVIDENCE_OVERCLAIM_RISK → FIXED / AUTHORITY_PRESERVED`

---

## Loop 5 — integration sequencing / false completion attack

### Attack

Assume a Green PR is enough to call the project synchronized before new-main and Notion destination readback.

### Evidence and guard

- Notion CURRENT pages are intentionally **not** updated before GitHub merge evidence.
- Issue #11 is intentionally still open before post-merge state synchronization.
- The branch does not modify 021+ manuscript data.
- The root AGENTS and project flow require exact new-main readback before Notion `SYNCED` completion.
- The original source candidate remains in Library unchanged; the corrected derivative is stored separately.

### Critique validation

No pre-merge Notion write or stale-issue closure should be pulled into this PR. Those are post-merge tasks whose correct values depend on the new exact main SHA.

### Verdict

`SEQUENCING_GUARD_CONFIRMED / POSTMERGE_WORK_REQUIRED`

---

## Five-loop result

Validated findings discovered across the five loops:

1. self-stale `last integrated` naming → fixed;
2. unauthorized manuscript/Canon drift → not present;
3. internal START_HERE receipt omission → fixed;
4. DOCX authority/evidence overclaim risk → bounded and fixed;
5. premature Notion/Issue completion → prevented by sequencing.

No new story direction, Canon change, 021+ promotion, Base pin bump, paid dependency, or historical bulk cleanup was introduced.

## Premerge clean-exit gate

The candidate may proceed to final exact-head CI / review-thread / main-freshness checks only if, after this review document itself is added:

- all Fiction operating-system workflow steps are Green;
- unresolved review threads are `0`;
- no conflicting new open PR appears;
- current main remains compatible with baseline `395f0af0120f5ab6949c86772d3b77b5b3eb9f3a`;
- changed-path review still shows no manuscript/Canon mutation.

Post-merge GitHub + Notion readback remains mandatory before final completion.
