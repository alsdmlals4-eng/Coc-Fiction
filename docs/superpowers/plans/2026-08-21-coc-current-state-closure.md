# Coc-Fiction Current-State Closure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Coc-Fiction's active repository, Notion CURRENT surfaces, and DOCX packaging evidence agree with the verified post-PR-#39 state without changing story Canon or promoted manuscript prose.

**Architecture:** Add one compact machine-readable current-state receipt and a root AGENTS router, then make the existing fiction operating validator fail closed on stale active state. Preserve the immutable QA_GREEN DOCX and generate a presentation-only derivative with a neutral running header. Merge GitHub first; only after exact new-main readback update Notion CURRENT pages and close the superseded issue.

**Tech Stack:** Markdown, JSON, Python 3.12 standard library, GitHub Actions, DOCX OPC/XML (`zipfile` + XML), Notion CURRENT pages.

**Spec:** `docs/superpowers/specs/2026-08-21-coc-current-state-closure-design.md`

## Global Constraints

- Current authoritative baseline is main `395f0af0120f5ab6949c86772d3b77b5b3eb9f3a` unless fresh-read evidence changes it before merge.
- Open/draft/ready PRs are read-only; abort/rebase only if a new conflicting PR or main movement appears.
- Preserve story Canon, promoted manuscript bodies 001–020, current 20→21 fail-closed boundary, and five-chapter bounded promotion.
- Preserve original QA_GREEN candidate bytes and SHA256 `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`.
- No new paid service, API, or dependency.
- Notion current-state writes occur only after GitHub merge evidence.

---

### Task 1: RED contract for repository current-state closure

**Files:**
- Create: `tests/test_current_state_closure.py`
- Modify: `.github/workflows/fiction-ops-validation.yml`

**Interfaces:**
- Consumes: `fiction/ACTIVE_CONTEXT.md`, `fiction/HANDOFF.md`, `fiction/FICTION_MASTER.md`, `fiction/analysis/SCENE_PASS_REGISTRY.json`, future `docs/fiction-ops/CURRENT_STATE_RECEIPT.json`, future root `AGENTS.md`.
- Produces: unit-test contract proving current receipt/router must exist and match the 001–020/021–025 state.

- [ ] **Step 1: Write the failing test**

Create `tests/test_current_state_closure.py` using only Python standard library. The test must assert:

```python
ROOT / 'AGENTS.md' exists
ROOT / 'docs/fiction-ops/CURRENT_STATE_RECEIPT.json' exists
receipt['verified_prefix_end'] == 20
receipt['legacy_tail_starts_at'] == 21
receipt['boundary_after_chapter'] == 20
receipt['next_bounded_bundle'] == 'fiction/manuscript/part-1/021-025.md'
receipt['whole_manuscript_continuity'] == 'NOT_YET_CLAIMED'
```

It must also parse `SCENE_PASS_REGISTRY.json` and compare the same frontier fields, and assert active `ACTIVE_CONTEXT.md`/`HANDOFF.md` contain `PR #39` as merged/completed rather than `current branch` work.

- [ ] **Step 2: Run the RED test on the PR branch**

Update `.github/workflows/fiction-ops-validation.yml` to add:

```yaml
- name: Validate current-state closure contract
  run: python -m unittest tests.test_current_state_closure -v
```

Open a draft PR and let this step fail because `AGENTS.md` and `CURRENT_STATE_RECEIPT.json` do not yet exist. Verify all pre-existing validator steps remain Green and the new step is the intended RED.

- [ ] **Step 3: Record RED evidence in the PR body**

Record exact RED head SHA and workflow run ID. Do not count unrelated failures as valid TDD evidence.

---

### Task 2: Minimal repository current-state implementation

**Files:**
- Create: `AGENTS.md`
- Create: `docs/fiction-ops/CURRENT_STATE_RECEIPT.json`
- Modify: `fiction/ACTIVE_CONTEXT.md`
- Modify: `fiction/HANDOFF.md`
- Modify: `tools/check_fiction_operating_system.py`
- Test: `tests/test_current_state_closure.py`

**Interfaces:**
- `CURRENT_STATE_RECEIPT.json` is a compact state receipt, not a Canon owner.
- `AGENTS.md` is a router, not a duplicate of Base or fiction operating documentation.

- [ ] **Step 1: Create the receipt**

Use exactly these semantic fields:

```json
{
  "schema_version": 1,
  "observed_main_sha": "395f0af0120f5ab6949c86772d3b77b5b3eb9f3a",
  "last_integrated_pr": 39,
  "verified_prefix_end": 20,
  "legacy_tail_starts_at": 21,
  "boundary_after_chapter": 20,
  "next_bounded_bundle": "fiction/manuscript/part-1/021-025.md",
  "whole_manuscript_continuity": "NOT_YET_CLAIMED",
  "candidate_sha256": "248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9",
  "rule": "FETCH_LATEST_MAIN_BEFORE_USE"
}
```

`observed_main_sha` is evidence of the integration being closed, not a promise that the value will forever equal future main.

- [ ] **Step 2: Add root AGENTS router**

Keep it concise. It must route new agents to:

```text
[소설]/00_운영체계/START_HERE.md
fiction/ACTIVE_CONTEXT.md
fiction/CANON_REGISTRY.json
fiction/analysis/SCENE_PASS_REGISTRY.json
docs/fiction-ops/CURRENT_STATE_RECEIPT.json
```

It must state NARRATIVE/Godot N/A, candidate != production authority, open PR read-only rule, current-state fresh-read rule, and validation commands.

- [ ] **Step 3: Close stale wording in active routers**

In `ACTIVE_CONTEXT.md` and `HANDOFF.md`, replace post-PR-#39 pre-merge wording such as `current pass/current branch: Ch016–020` with completed integration wording:

```text
PR #39 merged: Ch016–020 bounded promotion complete.
current repository prefix: 001–020.
next bounded bundle: 021–025.
```

Do not change the current numerical frontier or story Canon.

- [ ] **Step 4: Extend the operating validator minimally**

In `tools/check_fiction_operating_system.py`, validate that:

- root `AGENTS.md` exists;
- current-state receipt parses;
- receipt frontier matches `SCENE_PASS_REGISTRY.json`;
- root AGENTS contains the required router paths;
- active routers do not describe Ch016–020 as the current unmerged branch/pass.

Do not make the validator depend on Notion or the external DOCX.

- [ ] **Step 5: Verify GREEN**

Run/observe:

```bash
python -m unittest tests.test_current_state_closure -v
python tools/check_fiction_operating_system.py
python tools/check_fiction_content.py
python tools/build_fiction_reverse_outline.py --check
python tools/check_fiction_reverse_outline.py
python tools/check_fiction_scene_passes.py
```

All must pass on the exact PR head.

---

### Task 3: DOCX packaging derivative and semantic QA evidence

**Files:**
- Preserve: Library original `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- Create: Library derivative `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_HEADER_FIXED.docx`
- Create: `tools/check_fiction_docx_packaging.py`
- Create: `tests/test_fiction_docx_packaging.py`
- Create: `docs/fiction-ops/2026-08-21_WORKING_001_161_PACKAGING_QA_ADDENDUM.md`
- Modify: `.github/workflows/fiction-ops-validation.yml`

**Interfaces:**
- `check_fiction_docx_packaging.py <path>` reads DOCX ZIP/XML and reports running header texts; it does not edit files.
- The derivative is `PRESENTATION_ONLY_DERIVATIVE`, not a new source or production authority.

- [ ] **Step 1: Write RED unit tests**

Create synthetic DOCX-like ZIP fixtures in a temporary directory using `zipfile` only. Test that a header containing `제001–010화` while the declared document range is `001–161` fails, and that `폭풍의 눈 · 001–161 통합 검수본` passes.

- [ ] **Step 2: Verify RED**

Run:

```bash
python -m unittest tests.test_fiction_docx_packaging -v
```

Expected failure: checker module/function does not yet exist.

- [ ] **Step 3: Implement minimal checker**

Read `word/_rels/document.xml.rels`, `word/document.xml`, and referenced `word/header*.xml` from the DOCX ZIP. Extract text nodes and reject narrow chapter-range headers that contradict the declared total range.

- [ ] **Step 4: Verify checker GREEN**

Run the unit test and existing repository validators.

- [ ] **Step 5: Generate presentation-only derivative**

Materialize the original Library DOCX. Verify its SHA equals the locked SHA. Modify only referenced header XML text to `폭풍의 눈 · 001–161 통합 검수본`; do not modify document body XML. Save the derivative under the new filename.

- [ ] **Step 6: Verify derivative**

Verify:

- original SHA unchanged;
- original `word/document.xml` hash equals derivative `word/document.xml` hash;
- 161 chapter headings preserved;
- checker fails on original and passes on derivative;
- derivative package opens/parses successfully;
- record derivative SHA256.

- [ ] **Step 7: Persist QA addendum**

Document root cause, original/derivative SHA, body-XML equality, chapter count, header result, and evidence ceiling. Explicitly state that PR #31's story/content QA remains valid while the former `0 obvious visual defects` packaging claim is narrowed by this newly found header defect.

---

### Task 4: PR adversarial review, exact-head validation, and merge

**Files:**
- No new scope unless a validated finding requires a minimal fix.

- [ ] **Step 1: Inspect complete PR diff**

Reject unrelated prose, Canon, 021+ manuscript promotion, broad Base pin updates, or historical cleanup.

- [ ] **Step 2: Run five full adversarial review loops**

Each loop attacks the full approved scope for omission, conflict, stale consumer, evidence overclaim, and regression. Validate findings before changing anything.

- [ ] **Step 3: Verify review threads and main freshness**

Requirements:

```text
unresolved review threads = 0
open conflicting PR = 0
base main still compatible with the original baseline
exact-head required workflow = Green
```

- [ ] **Step 4: Squash merge with expected head SHA**

Use squash merge only.

---

### Task 5: Post-merge GitHub readback and Notion CURRENT sync

**Files/Surfaces:**
- GitHub new main
- Notion project home `Coc소설`
- Notion `CURRENT · 작품 코어 & 보호 정본 · 2026-08-20`
- Notion `CURRENT · 주요 인물 선택 아크 · 2026-08-20`
- Notion `CURRENT · 001–161 전체 구조 지도 · 2026-08-20`

- [ ] **Step 1: Fetch exact new main**

Read new main SHA and confirm repository current-state receipt/router state from that main.

- [ ] **Step 2: Update project-home properties**

Set:

```text
Repo Main SHA = <new exact main SHA>
Sync State = SYNCED
Last Synced = 2026-08-21
```

Only set `SYNCED` after content updates and readback succeed.

- [ ] **Step 3: Update human-facing CURRENT content**

Change only current-state snippets:

```text
production prefix 001–020
legacy tail 021+
next 021–025
PR #39 merged/completed
canonical Korean spelling 엘리스
whole-manuscript continuity NOT_YET_CLAIMED
```

Do not rewrite dated historical audit/decision pages.

- [ ] **Step 4: Read back all updated Notion pages**

Confirm no active `001–015 / PR #39 open` current state remains on those surfaces and no CURRENT page uses `앨리스` for Alice Carter.

---

### Task 6: Close superseded issue and final progress readback

**Files/Surfaces:**
- GitHub Issue #11
- GitHub current main
- Notion CURRENT pages

- [ ] **Step 1: Close Issue #11 as completed/superseded**

Preserve body. Add a concise closure note pointing to the post-merge current-state correction and explaining that its old `176–180 / 006–010` next-work state has been superseded by `021–025`.

- [ ] **Step 2: Recalculate remaining work**

Expected remaining primary project work after this correction:

```text
021–025 bounded promotion
then sequential bounded promotion through 161
publication target/reader gate after production migration is stable
```

- [ ] **Step 3: Final verification-before-completion**

Re-fetch:

- main SHA;
- open PRs;
- Issue #11 state;
- Notion project home and CURRENT pages;
- Library original/derivative DOCX metadata.

Report actual changes, verification evidence, anything not verified, remaining risks, rollback, and whether any new Base promotion candidate was discovered.
