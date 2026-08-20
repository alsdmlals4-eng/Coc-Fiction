# Coc-Fiction Canon Reconciliation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reconcile the structured Coc-Fiction canon with the user-approved 2026-08-20 planning decisions before any current-candidate manuscript promotion.

**Architecture:** Keep story authority changes confined to the structured canon layer first. Update the registry and the two active canon/bible documents together, then validate with the existing fiction operating-system workflow; legacy manuscript text remains untouched in this change.

**Tech Stack:** Markdown, JSON, existing Coc-Fiction GitHub Actions / fiction validators.

**Spec:** Notion `PLANNING READY · 001–161 최종 기획 패키지 · 2026-08-20`.

## Global Constraints

- User-approved D01: bounded external acquisition network = client → broker/contact node → professional recovery team; do not promote it to a fully identified fourth megafaction or rogue Delta Green cell.
- Elliott's silver sword remains unassigned and jointly sealed; transformation near Jumin does not prove ownership or succession.
- Alice Carter canonical Korean spelling is `엘리스`; `앨리스` remains forbidden in active/new manuscript.
- Do not modify legacy/current manuscript in this canon-only change.
- Do not alter any open/draft/ready PR owned by another workstream.

---

### Task 1: Canon Registry

**Files:**
- Modify: `fiction/CANON_REGISTRY.json`

- [ ] Update `updated_at` to `2026-08-20`.
- [ ] Replace the stale one-off external-mercenary rule with the approved bounded external acquisition-network rule.
- [ ] Replace sword succession wording with unassigned/joint-custody wording while preserving the observed scalpel transformation.
- [ ] Remove stale `단발 외부 용병` wording from the superseded Russian-mafia replacement mapping.
- [ ] Parse the JSON successfully.

### Task 2: Canon / Part2 Bible Readback

**Files:**
- Modify: `fiction/bible/02_CANON_AND_CONTINUITY.md`
- Modify: `fiction/bible/04_PART2_STORY_BIBLE.md`

- [ ] Separate Yellow extremist pressure from the bounded external acquisition network.
- [ ] Record D01's client/broker/recovery-team boundary and keep client/hierarchy/Wilmarth ownership unresolved.
- [ ] Keep the temporary joint operations team distinct from the acquisition network.
- [ ] Replace sword inheritance language with joint custody / unresolved ownership language.
- [ ] Keep scalpel transformation as an observed phenomenon, not a successor certification.

### Task 3: Verification / Delivery

- [ ] Confirm the three authority files contain the same D01 and sword semantics.
- [ ] Confirm forbidden spelling `앨리스` was not introduced.
- [ ] Open a PR from `work/coc-planning-complete-20260820` to `main`.
- [ ] Require existing fiction operating-system checks to pass on the exact PR head.
- [ ] Re-check unresolved review threads and current main before merge.
- [ ] Squash-merge only after exact-head verification.
