# Rift Accord Handoff Closure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the current Coc-Fiction session with fresh continuation state, a routed artifact-promotion gate, and conflict-safe Base learning disposition without changing story manuscript or Canon.

**Architecture:** Keep the existing five project Skills. Absorb the new operational distinction into `fiction-project-operations`, route it through the existing project Registry, enforce it in the operating-system checker, and persist the current delivery-versus-repository-promotion state in `ACTIVE_CONTEXT` and `HANDOFF`. Reuse Base BCP-012/017/013 where they already own the generalized lifecycle rather than creating a duplicate Base proposal.

**Tech Stack:** Markdown project operations contracts, JSON Skill Registry, Python operating-system validator, GitHub PR/Actions evidence.

## Global Constraints

- Current target project is `alsdmlals4-eng/Coc-Fiction`; other projects are read-only comparison evidence.
- Do not modify fiction manuscript, story Canon, character decisions, or the final DOCX in this handoff cycle.
- Preserve exactly five project Skills; prefer ABSORB over creating a sixth Skill.
- Keep the project `base_commit` adoption pin unchanged unless a separate full Base-adoption audit is performed.
- Distinguish verified external delivery from repository production-manuscript promotion.
- Do not treat a filename such as `final` or `최종` as automatic Canon authority.
- Base writes, if any become necessary after Existing Solution First, are restricted to `[수정제안서]/**`; never modify Base active contracts in this cycle.
- Before any Base write and immediately before any Base proposal merge, re-read latest Base `main`, open proposal-only PRs, current Registry and same-goal proposals.
- Do not mark `CONTINUOUS_WORK_ACTIVE`; the exact opt-in literal was not supplied.

---

### Task 1: Add the project artifact-promotion gate

**Files:**
- Modify: `skills/fiction-project-operations/SKILL.md`
- Modify: `[소설]/00_운영체계/SKILL_REGISTRY.json`
- Modify: `tools/check_fiction_operating_system.py`
- Modify: `skills/FICTION_SKILL_LEARNING_LOG.md`

**Interfaces:**
- Consumes: existing `fiction-project-operations` handoff/checkpoint responsibilities and the current five-Skill Registry.
- Produces: routed `artifact-promotion-gate` mode with separate delivery and repository-promotion states plus a validator contract.

- [ ] **Step 1: Extend the existing operations Skill, not the Skill count.**
  Add `artifact-promotion-gate` to the mode chain and define these state fields:
  - `delivery_state: DRAFT | QA_VERIFIED | DELIVERED`
  - `repository_promotion_state: NOT_REQUIRED | PENDING | PARTIAL | PROMOTED`
  Require artifact filename/coverage/hash, repository topology, promotion target, known migration frontier/debt, and the next executable step when promotion is not complete.

- [ ] **Step 2: Route the gate from the Registry.**
  Add trigger tags `external-artifact`, `artifact-promotion`, `delivery-manifest`, and `canon-migration-handoff`; add `artifact-promotion-gate` to `fiction-project-operations.skill_modes`. Keep exactly five registered project Skills and keep `base_commit` unchanged.

- [ ] **Step 3: Make the operating-system validator fail closed if routing disappears.**
  Require the artifact-promotion trigger set and mode on the operations Registry entry and require the mode token in its Skill body. The validator must continue to enforce exactly five project Skills.

- [ ] **Step 4: Record the project learning.**
  Add a learning entry stating that delivery completion and repository Canon promotion are separate lifecycle states when an external final artifact and a migration-container repository coexist; record Base disposition as REUSE existing BCP-012/017 plus handoff BCP-013 unless a later preflight proves a material gap.

### Task 2: Reconcile current continuation state after PR #24

**Files:**
- Modify: `fiction/ACTIVE_CONTEXT.md`
- Modify: `fiction/HANDOFF.md`

**Interfaces:**
- Consumes: `main@0ef8161f918eeb4b951fd6de38f8f7c512274a4d`, merged PR #24, final Rift Accord delivery manifest, current reconciliation frontier.
- Produces: one live resume contract that does not confuse delivered prose with repository promotion.

- [ ] **Step 1: Update the live baseline and completed work.**
  Record PR #23 structural architecture lock and PR #24 Rift Accord delivery evidence as completed/merged; record the final side-story DOCX hash and the verified Ch156–161 delivery status.

- [ ] **Step 2: Preserve unresolved repository migration truth.**
  Keep `reconciled_prefix_end=5`, `legacy_tail_starts_at=6`, `whole_manuscript_continuity=NOT_YET_CLAIMED`; explicitly state that the external/latest manuscript line and repository production promotion are not the same completion claim.

- [ ] **Step 3: Replace the stale immediate next-work router.**
  Because the user is pausing for handoff, set resume priority to: fetch latest main/open PR → recover current delivered artifacts and migration frontier → build/verify the consolidated 001–161 final artifact before deciding whether to continue bounded repository migration or adopt a newer whole-work migration plan. Preserve 006–010 as the next bounded migration unit if that migration strategy is resumed; do not silently delete it.

- [ ] **Step 4: Store Base concurrency disposition.**
  Record latest Base observed main, existing reusable BCP-012/017/013 locators, `same_goal_state=REUSE_EXISTING_BCP`, no Base proposal branch/PR for this cycle unless a new material gap is later proven, and `other_project_changes_preserved=true`.

### Task 3: Exact-head validation, adversarial review, merge, and post-merge readback

**Files:**
- Verify: all files changed by Tasks 1–2 and this plan.

**Interfaces:**
- Consumes: final project branch head and fresh `main`/PR state.
- Produces: merged handoff closure with fresh CI and resumable state.

- [ ] **Step 1: Open a Draft PR from `ops/rift-accord-handoff-20260812` to `main`.**
  PR body must map user goals to changed files and state that manuscript/Canon are untouched.

- [ ] **Step 2: Verify exact-head GitHub Actions.**
  Require `Fiction operating system` success for the PR head. Do not reuse PR #24 CI as evidence for this new head.

- [ ] **Step 3: Run adversarial review.**
  Check stale state, duplicate current authority, accidental sixth Skill, Base pin drift, manuscript/Canon mutation, false promotion-complete claim, unrelated files, and same-goal PR overlap. Fix any verified MUST_FIX before merge.

- [ ] **Step 4: Merge without another approval prompt if all gates pass.**
  Use the exact reviewed head SHA as the merge guard.

- [ ] **Step 5: Read back new `main` and post-merge CI.**
  Confirm the changed handoff/operations files exist on new main, PR is merged, post-merge `Fiction operating system` succeeds, and no same-goal project PR remains open. Do not create another PR solely to write the closure PR’s own merge SHA into Handoff.

## Self-review

- Spec coverage: project handoff, project learning application, Base Existing Solution First, concurrency safety, exact-head validation, merge and non-recursive post-merge closeout are all mapped.
- Placeholder scan: no TBD/TODO/future implementation placeholders are used.
- Scope: manuscript/Canon and Base active implementation are explicitly excluded.
- Existing Solution First: project change is ABSORB; Base candidate is REUSE unless fresh evidence proves otherwise.
