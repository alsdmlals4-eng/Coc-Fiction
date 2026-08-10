# PR #19 006-010 Reconciliation Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** PR #19가 선언했지만 실제 production consumer에 전파하지 못한 외부 최신 제6~10화 canon reconciliation을 완성하고 mixed-migration boundary를 제10→11로 이동한다.

**Architecture:** 업로드된 제1~105화 2차 퇴고본 중 제6~10화를 현재 prose source로 사용한다. 기존 PR #19의 valid RED 계약과 revision/scene-card 판정을 보존하면서 manuscript, composed index override, reverse-outline override/manifest, scene-pass registry, live-router 문서를 동일 기준으로 동기화한다. 저장 제11화 이후는 검증 전 legacy tail로 fail-closed한다.

**Tech Stack:** Markdown manuscript, JSON composed overrides, Python validation scripts, GitHub Actions.

## Global Constraints

- 최신 사용자 지시와 현재 제1~105화 2차 퇴고 파일을 현재 작업 prose에 우선한다.
- Godot/게임 엔진 규칙은 적용하지 않는다.
- `CANON_REGISTRY.json`의 버실라/바실라/Versilla/Woff 제외, 아킴 제한 허용, 주안 자기통제 Canon을 보존한다.
- 제11화 이후 continuity는 이번 변경에서 주장하지 않는다.
- PR #19 exact-head 실패를 RED 증거로 사용하고, production 변경 뒤 동일 validator를 GREEN으로 확인한다.
- 원고 변경 시 MANUSCRIPT_INDEX, reverse outline, Scene Pass Registry, Revision Report, live router를 같은 변경 단위에서 전파한다.

---

### Task 1: Promote current Ch6-10 manuscript

**Files:**
- Modify: `fiction/manuscript/part-1/006-010.md`
- Test: `tools/check_fiction_scene_passes.py`

**Interfaces:**
- Consumes: current attached Ch6-10 DOCX prose and PR #19 source/canon reconciliation decision.
- Produces: current Ch6-10 Markdown bodies with stable chapter titles, POV sequence, and body hashes.

- [ ] **Step 1: Verify RED** — preserve PR #19 exact-head workflow failure and current main stale Ch6 invariant failure as the pre-change failure evidence.
- [ ] **Step 2: Replace only Ch6-10 bundle** with current attached prose, preserving explicit POV section markers.
- [ ] **Step 3: Add per-chapter `source-lines` marker** so the existing parser owns exactly the new body.
- [ ] **Step 4: Record exact body char/hash values** from the written Markdown representation.

### Task 2: Synchronize composed consumers and migration boundary

**Files:**
- Modify: `fiction/analysis/MANUSCRIPT_INDEX_OVERRIDE_006_010.json`
- Modify: `fiction/analysis/REVERSE_OUTLINE_OVERRIDE_006_010.json`
- Modify: `fiction/analysis/REVERSE_OUTLINE_001_225.json`
- Modify: `fiction/analysis/SCENE_PASS_REGISTRY.json`
- Keep/use: `fiction/analysis/REVERSE_OUTLINE_OVERRIDE_011_LEGACY_BOUNDARY.json`
- Test: `tools/check_fiction_scene_passes.py`
- Test: `tools/check_fiction_reverse_outline.py`

**Interfaces:**
- Consumes: Task 1 title/POV/body_chars/body_sha256.
- Produces: one effective current authority for Ch6-10; normal Ch5↔6 continuity; fail-closed Ch10→11 boundary.

- [ ] **Step 1: Update index override** for all five chapters, not a partial 6/7/9 subset.
- [ ] **Step 2: Update reverse-outline override** for all five chapters with current title/POV/source metadata and evidence.
- [ ] **Step 3: Move migration boundary consumer** from Ch5 override to Ch11 legacy-tail override in the composed manifest.
- [ ] **Step 4: Advance Scene Pass Registry** to `reconciled_prefix_end=10`, `legacy_tail_starts_at=11`, `boundary_after_chapter=10`, next bundle `011-015`.

### Task 3: Correct live routers and evidence report

**Files:**
- Modify: `[소설]/00_운영체계/START_HERE.md`
- Modify: `fiction/FICTION_MASTER.md`
- Modify: `fiction/ACTIVE_CONTEXT.md`
- Modify: `fiction/reports/REVISION_2026-08-10_EXTERNAL_RECONCILIATION_006_010.md`

**Interfaces:**
- Consumes: Tasks 1-2 current state.
- Produces: new-chat routing that points to 011-015 without claiming whole-manuscript continuity.

- [ ] **Step 1: Remove stale `1-5 / next 6-10` live claims.**
- [ ] **Step 2: Record Ch6-10 exact manuscript metadata and the moved boundary.**
- [ ] **Step 3: Keep whole-manuscript state `NOT_YET_CLAIMED`.**
- [ ] **Step 4: Set next executable bundle to external latest Ch11-15.**

### Task 4: Verify and adversarially review

**Files:**
- Test: `.github/workflows/fiction-ops-validation.yml`
- Review: all changed files in this branch.

**Interfaces:**
- Consumes: Tasks 1-3.
- Produces: exact-head validation and merge decision.

- [ ] **Step 1: Open a repair PR and run hosted validation.**
- [ ] **Step 2: Require scene-pass, reverse-outline, content, operating-system validators to pass.**
- [ ] **Step 3: Attack for stale 5→6 boundary, old Ch6-10 titles, forbidden Canon terms, untouched consumers, and accidental Ch11 continuity.**
- [ ] **Step 4: Validate criticisms; fix only MUST_FIX/approved SHOULD_FIX findings.**
- [ ] **Step 5: Re-run exact-head checks, verify no unresolved review threads, then merge and read back new main.**
