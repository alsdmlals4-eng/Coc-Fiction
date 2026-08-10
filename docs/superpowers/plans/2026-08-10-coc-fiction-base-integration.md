# Coc-Fiction Base Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. This environment has no separate subagent executor, so execution is inline with exact-head checkpoints.

**Goal:** Reconcile the current Coc-Fiction repository against current Base, recover only valid stale PR deltas, merge approved project-only operating improvements, post-merge verify the new main, and submit only genuinely reusable gaps to Base `[수정제안서]`.

**Architecture:** Keep Coc-Fiction's five project skills and fiction canon as the project authority. Reuse Base's current shared skills, especially `developing-and-revising-serial-fiction`, adversarial review, reference freshness, handoff, and BCP management; absorb only missing project-specific routing into existing Coc-Fiction skills. Treat stale PRs as evidence/delta sources, never as merge authority. Base changes remain proposal-only and use a separate Base branch/PR.

**Tech Stack:** GitHub repository/PR/Actions APIs, Markdown, JSON, Python 3.12 contract validators, existing Coc-Fiction `fiction-ops-validation.yml`, Base proposal validator/workflows.

## Global Constraints

- Project execution scope is only `alsdmlals4-eng/Coc-Fiction`.
- `alsdmlals4-eng/Base` may be changed only under `[수정제안서]/**` in proposal-only scope unless a pre-existing approval explicitly authorizes active implementation.
- Do not merge stale PR #9 directly.
- Do not resurrect `[SUPERSEDED]`, reference-only, or old canon material.
- Do not change Coc-Fiction story canon/manuscript content in this operating-system reconciliation PR.
- Reuse existing approval for the current integration scope; do not ask the same approval again.
- Every merge claim must be verified again on the new `main` SHA.
- Past CI evidence is not current exact-head evidence.
- `NOT_RUN` and `BLOCKED_UNVERIFIED` are not PASS.
- Prefer `REUSE → ABSORB → REFACTOR → BUILD_NEW`.

---

### Task 1: Freeze Current Authority and Classify Repository Work

**Files:**
- Create: `docs/coordination/2026-08-10_CURRENT_PROJECT_RECOVERY_AUDIT.md`
- Read: `[소설]/00_운영체계/START_HERE.md`
- Read: `[소설]/00_운영체계/OPERATING_MODEL.md`
- Read: `[소설]/00_운영체계/SKILL_REGISTRY.json`
- Read: `fiction/ACTIVE_CONTEXT.md`
- Read: `fiction/HANDOFF.md`
- Read: `docs/fiction-ops/BASE_ADOPTION_AUDIT.md`
- Read: relevant PRs/branches through GitHub API

**Interfaces:**
- Consumes: Coc-Fiction main `27e0dd4e429d447145596ee8aa36ecdb58ac9161`, Base main `53e63f7ebefbb5b2fc0dc528e335252692801421`.
- Produces: one auditable classification matrix used by all later tasks.

- [ ] **Step 1: Re-read main and PR inventory**
  - Record current main SHA, all open PRs, recently closed/unmerged PRs, merged PRs relevant to the current fiction operating goal, and surviving remote branches.
  - Explicitly include PR #9 and #12.

- [ ] **Step 2: Compare stale PR delta rather than branch history**
  - Use PR file list/patch for #9 and #12.
  - Confirm whether #12 is a byte/semantic refresh of #9's unique delta and whether its two-file change still applies to current main.

- [ ] **Step 3: Write classification matrix**
  - For each relevant item record: `MERGE_READY / NEEDS_UPDATE / NEEDS_FIX / BLOCKED / SUPERSEDED / REFERENCE_ONLY / DO_NOT_MERGE / USER_DECISION_REQUIRED`.
  - Record source/base/head SHA, unique delta, current-main overlap, evidence freshness, and disposition.

- [ ] **Step 4: Commit audit**
  - Commit only the audit file.

### Task 2: Add a RED Contract for Current Base Adoption and Serial-Arc Recovery

**Files:**
- Modify: `tools/check_fiction_operating_system.py`
- Test target: `python tools/check_fiction_operating_system.py`

**Interfaces:**
- Consumes: current Base active skill list and approved project architecture.
- Produces: fail-closed assertions for the exact operating-state changes required by Task 3.

- [ ] **Step 1: Add current Base capability expectation**
  - Add `developing-and-revising-serial-fiction` to `EXPECTED_BASE_CAPABILITIES`.
  - Add a contract that project Registry `base_commit` equals the approved/current adoption baseline recorded by this reconciliation.
  - Add a contract that `fiction-revision-and-validation` exposes `serial-arc-pass` if the audit classifies #12's delta as valid.

- [ ] **Step 2: Run the validator on the branch and capture RED**
  - Run: `python tools/check_fiction_operating_system.py`
  - Expected failure before Task 3: Base capability mapping mismatch and/or missing `serial-arc-pass` and stale Base adoption identity.

- [ ] **Step 3: Commit RED test/validator change**
  - Commit the failing contract separately so the expected failure is attributable.

### Task 3: Implement the Minimal Coc-Fiction Operating Reconciliation

**Files:**
- Modify: `[소설]/00_운영체계/SKILL_REGISTRY.json`
- Modify: `skills/fiction-revision-and-validation/SKILL.md`
- Modify: `docs/fiction-ops/BASE_ADOPTION_AUDIT.md`
- Modify: `fiction/ACTIVE_CONTEXT.md`
- Modify: `fiction/HANDOFF.md`
- Modify if learning evidence warrants: `skills/FICTION_SKILL_LEARNING_LOG.md`

**Interfaces:**
- Consumes: Task 1 disposition matrix and Task 2 RED contract.
- Produces: current project operating state with no new project Skill and no manuscript/canon mutation.

- [ ] **Step 1: Absorb valid serial-arc delta**
  - Apply only #12's valid unique change to existing `fiction-revision-and-validation`: `serial-arc-pass` mode plus `serial-arc / chapter-batch / scene-pass / representative-gate / canon-propagation` triggers.
  - Preserve the contract that automatic reverse-outline/length statistics are findings, not edit commands.

- [ ] **Step 2: Refresh Base adoption boundary**
  - Update Registry `base_commit` to the exact Base main used for this reconciliation only after documenting the compatibility audit.
  - Update `BASE_ADOPTION_AUDIT.md` from the old 25-capability snapshot to the current relevant mapping, explicitly adding Base's `developing-and-revising-serial-fiction` as `REUSE/ADAPT`, not duplicating it as a sixth project Skill.
  - Preserve project-owned canon/source-log/derived-artifact propagation responsibilities.

- [ ] **Step 3: Refresh current context and handoff**
  - Record the current 1~105 integrated revision result as externally completed work/evidence without pretending the GitHub 225-chapter manuscript has been fully rewritten to that state unless the actual repository files prove it.
  - Replace stale “next exact task” text with the true next repository task after this reconciliation.
  - Keep canon/manuscript completion ceilings explicit.

- [ ] **Step 4: Run GREEN validation locally/hosted equivalent**
  - Run: `python tools/check_fiction_operating_system.py`
  - Also run existing content/reverse-outline/scene-pass validators if branch access permits.
  - Expected: PASS for every executed validator; unavailable runs remain `NOT_RUN/BLOCKED_UNVERIFIED`.

- [ ] **Step 5: Commit minimal implementation**
  - Keep changed files limited to operating docs/registry/skill/checker/context/handoff and the current audit/spec/plan artifacts.

### Task 4: Adversarial Review and Exact-Head Project PR Gate

**Files:**
- Create: `docs/coordination/2026-08-10_COC_FICTION_INTEGRATION_ADVERSARIAL_REVIEW.md`
- Review: exact branch diff, current main, PR #9/#12, active project canon routes.

**Interfaces:**
- Consumes: Task 3 exact branch head.
- Produces: `MUST_FIX / SHOULD_FIX / DEFER / REJECTED_CRITIQUE / BLOCKED_UNVERIFIED` findings and merge decision.

- [ ] **Step 1: Attack**
  - Check stale canon resurrection, duplicated Base/project authority, missing consumers, wrong Base SHA claims, unrelated manuscript mutation, false completion claims, stale CI, duplicate PRs, rollback.

- [ ] **Step 2: Validate critiques**
  - Re-check every critique against exact files, current Base owners, and project canon. Mark false attacks `REJECTED_CRITIQUE`.

- [ ] **Step 3: Refine only validated in-scope findings**
  - Apply minimal fixes and rerun relevant regression validators.

- [ ] **Step 4: Open project PR**
  - Base: `main`; head: `agent/coc-fiction-base-integration-20260810`.
  - PR body must list baseline SHA, changed files, #9/#12 disposition, exact-head tests, protected canon/manuscript scope, rollback.

- [ ] **Step 5: Exact-head merge gate**
  - Confirm changed files, Actions for current head, unresolved review threads, behind count/mergeability, P0/P1 findings, and inherited approval scope.

### Task 5: Merge Project Work and Perform Post-Merge Verification

**Files:**
- No new product/canon file by default.
- Update handoff in a follow-up only if the merge SHA itself must be recorded and cannot be known pre-merge.

**Interfaces:**
- Consumes: merge-ready project PR exact head.
- Produces: verified new Coc-Fiction main and stale-PR cleanup state.

- [ ] **Step 1: Merge only if gate is fully green**
  - Use expected head SHA.
  - Do not merge if exact-head validation or review state is stale.

- [ ] **Step 2: Re-read new main**
  - Record actual merge commit/new main SHA.
  - Verify the intended files and serial-arc/Base adoption state exist on new main.

- [ ] **Step 3: Post-merge validation**
  - Check push/main workflow runs when available.
  - Recheck Registry, active context/handoff, canonical references, no manuscript/canon mutation.

- [ ] **Step 4: Clean stale PR state**
  - Close PR #9 as superseded if its unique valid delta is now present on main.
  - Preserve #12 as historical closed/unmerged recovery evidence; do not reopen just to merge duplicate content.

### Task 6: Extract Project Learning and Apply Existing-Solution-First

**Files:**
- Create: `docs/fiction-ops/2026-08-10_PROJECT_TO_BASE_LEARNING_REVIEW.md`

**Interfaces:**
- Consumes: verified merged project state plus the recent 1~105 POV/hook/character revision evidence.
- Produces: classification table and only evidence-backed Base candidates.

- [ ] **Step 1: Record project findings**
  - For each finding record problem, root cause, fix, failed approach, validation, recurrence prevention, reusable portion, project-specific boundary, counterexample.

- [ ] **Step 2: Classify**
  - `PROJECT_ONLY / BASE_CANDIDATE / SPLIT / NO_PROMOTION`.

- [ ] **Step 3: Existing Solution First**
  - Compare candidates with BCP-009, `developing-and-revising-serial-fiction`, adversarial review, reference freshness, handoff, approval reuse, post-merge review.
  - Record `REUSE / ABSORB / REFACTOR / BUILD_NEW / NO_PROMOTION`.

- [ ] **Step 4: Identify likely POV candidate carefully**
  - Keep project-specific `1~3 POV per chapter` as `PROJECT_ONLY`.
  - Generalize only if evidence supports: a POV switch should add distinct information/value/voice; supporting/extras are valid POVs when they reveal a perspective unavailable to principals; switching must have explicit scene boundaries and should not become unmarked head-hopping.
  - If current Base already fully covers this, mark `REUSE/NO_PROMOTION` instead of forcing a BCP.

### Task 7: Benchmark Any Surviving Base Candidate

**Files:**
- Add benchmark section to `docs/fiction-ops/2026-08-10_PROJECT_TO_BASE_LEARNING_REVIEW.md`.

**Interfaces:**
- Consumes: only candidates that survived Task 6.
- Produces: source-backed gap decision.

- [ ] **Step 1: Research current primary/reputable sources**
  - For PR/workflow candidates: GitHub official docs first.
  - For fiction POV/serial pacing candidates: reputable writing craft/education sources and current professional guidance; avoid copying living-author style.

- [ ] **Step 2: Record comparison**
  - `external approach → Base current approach → difference → adoptable principle → rejected surface detail`.

- [ ] **Step 3: Adversarially re-review promotion**
  - Reject one-project overgeneralization, fixed POV counts, duplicate BCPs, needless new Skill, or policy that adds maintenance cost without an independent consumer.

### Task 8: Submit Base Proposal Only If a Real Gap Remains

**Files (Base repository, separate branch):**
- Create if needed: `[수정제안서]/BCP-2026-012-<slug>/PROPOSAL.md`
- Create if needed: `[수정제안서]/BCP-2026-012-<slug>/evidence/<evidence>.md`
- Modify if needed: `[수정제안서]/PROPOSAL_REGISTRY.json`

**Interfaces:**
- Consumes: Task 6/7 `BASE_CANDIDATE` with `ABSORB/REFACTOR/BUILD_NEW` verdict.
- Produces: `SUBMITTED` proposal-only Base PR. If no candidate survives, produces explicit `NO_NEW_BCP` evidence instead.

- [ ] **Step 1: Check proposal ID and current registry again**
  - Do not assume `012` remains free; re-read Base main immediately before writing.

- [ ] **Step 2: Write proposal/evidence using current template**
  - Include Source, Problem, Evidence, Root Cause, Existing Base Coverage, Existing Solution Verdict, Proposed General Rule, Project-Specific Boundary, Use/Do Not Use, Counterexample, Benchmark, Benefits, Risks, Consumers, Validation, Regression, Rollback, Adversarial Findings, Knowledge Level.

- [ ] **Step 3: Keep proposal-only scope**
  - No active Base Skill/Template/Test/Workflow changes.
  - Registry status `SUBMITTED`.

- [ ] **Step 4: Open Base proposal PR and validate**
  - Exact-head proposal validator/CI, changed-file scope, review threads, rollback.
  - Do not implement active Base changes in this task.

### Task 9: Final Handoff and Verification-Before-Completion

**Files:**
- Modify: `fiction/HANDOFF.md` if merged-main/Base proposal final identities need closure.
- Create/Update: project integration audit/learning documents as required.

**Interfaces:**
- Consumes: new Coc-Fiction main, optional Base proposal PR, executed validation evidence.
- Produces: resume-ready project state and final report.

- [ ] **Step 1: Fresh verification**
  - Re-read Coc-Fiction main, project PR state, stale PR state, Base main/proposal state, exact files, and current CI evidence.

- [ ] **Step 2: Handoff refresh**
  - Keep it concise: current state, actual result, remaining work, risks/not-run, first next action, validation/rollback.

- [ ] **Step 3: Final adversarial regression pass**
  - Verify no project canon/manuscript was changed accidentally; no Base active implementation leaked into proposal-only work; no stale evidence is reported as fresh.

- [ ] **Step 4: Final report**
  - Use the 14-section reporting order from the approved integrated work instruction.
