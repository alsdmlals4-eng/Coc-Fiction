# Coc-Fiction Current-State Closure Design

## Goal

Close the verified post-PR-#39 state across repository routers, Notion human-facing CURRENT pages, and external DOCX packaging evidence without changing story Canon or promoted manuscript prose.

## Baseline

- repository main at design time: `395f0af0120f5ab6949c86772d3b77b5b3eb9f3a`
- open pull requests at design time: `0`
- verified production prefix: `001–020`
- legacy tail starts: `021`
- current migration boundary: `020→021`
- next bounded promotion: `021–025`
- current revision input: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- revision-input SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- whole-manuscript continuity: `NOT_YET_CLAIMED`

## Protected authority

Do not change:

- Reader Promise or the central choice-preservation theme;
- `juan.self-control-protocol`;
- canonical Alice Carter Korean spelling `엘리스`;
- Scene-Locked Hybrid POV contract;
- D01/D02/D03/N04 and sword/joint-custody decisions;
- the `current prefix / legacy tail` mixed-migration model;
- five-chapter bounded promotion;
- the immutable source candidate or its existing SHA-based provenance;
- historical PRs, RED/diagnostic evidence, old migration containers, or dated audit pages merely because they are old.

## Root causes confirmed in the audit

### 1. Post-merge current-state propagation stopped short

The repository structured state advanced to `001–020`, but several human-facing/current consumers remained on the previous `001–015 / PR #39 open` state. A later Notion execution log contains the correct post-merge state, proving this is propagation drift rather than uncertainty about the authoritative frontier.

### 2. Repository cold-start routing lacks a root `AGENTS.md`

The project has a strong internal `START_HERE.md`, but no root-level agent router that tells a new Codex/AI where the project-specific authority and validation paths live.

### 3. DOCX packaging QA had a semantic-header blind spot

The source candidate body is structurally Green, but its single running header remains `폭풍의 눈 · 제001–010화` across later chapters. This is a packaging/header defect, not a story-body defect. The immutable candidate must remain unchanged; a corrected presentation derivative should be produced instead.

## Architecture

### A. One machine-readable current-state receipt

Create `docs/fiction-ops/CURRENT_STATE_RECEIPT.json` as the repository-owned compact current-state receipt. It records the observed main integration, verified prefix, boundary, next bundle, candidate identity, and evidence ceiling. It does not replace `CANON_REGISTRY.json` or `SCENE_PASS_REGISTRY.json`; validators cross-check it against those owners.

### B. Root `AGENTS.md` as router only

Add a short root router. It must point to project authorities and validation commands rather than duplicate full Base or fiction rules.

### C. Fail-closed current-state validation

Extend the existing fiction operating-system validator so stale current-state tokens cannot silently reappear in active routers. Add a dedicated unit test for current-state receipt parsing/cross-checking before implementation.

### D. External DOCX packaging derivative

Preserve the immutable QA_GREEN candidate. Create a new derivative with a neutral running header such as `폭풍의 눈 · 001–161 통합 검수본`. Record original/derivative hashes and a semantic header check in a dated QA addendum. The derivative is `PRESENTATION_ONLY_DERIVATIVE`, not new manuscript authority.

### E. GitHub first, Notion second

Merge the repository correction only after exact-head validation. Then fetch the exact new `main`, update only human-facing CURRENT Notion blocks/properties, and read them back. Historical pages stay historical.

## Notion CURRENT surfaces to update

At minimum:

- project home `Coc소설`: Repo Main SHA, current prefix, legacy tail, next promotion, PR #39 state, canonical `엘리스`, Sync State/Last Synced;
- `CURRENT · 작품 코어 & 보호 정본`: current production boundary and canonical spelling;
- `CURRENT · 주요 인물 선택 아크`: canonical spelling where the page is explicitly CURRENT;
- `CURRENT · 001–161 전체 구조 지도`: canonical spelling where the page is explicitly CURRENT.

Do not bulk-rewrite dated decisions, historical audits, or old PR evidence.

## Stale issue policy

Issue #11 is historical work-state debt that has been superseded by later merged work. Close it as completed/superseded only after the current-state correction is merged and read back; preserve its body as historical evidence.

## Testing and acceptance

Repository acceptance:

1. a RED test demonstrates that main lacks the new receipt/router contract;
2. minimal implementation makes the new test Green;
3. existing fiction operating/content/reverse-outline/scene-pass checks remain Green;
4. PR review threads are zero and main has not moved incompatibly;
5. squash merge;
6. fetch exact new main and rerun/read back relevant checks.

DOCX acceptance:

- original candidate bytes/SHA remain unchanged;
- derivative has the same 161 chapter headings and body text;
- derivative running header is neutral and no longer claims `001–010` on later pages;
- derivative SHA is recorded;
- visual/package QA claim is narrowed to what was actually checked.

Notion acceptance:

- human-facing CURRENT pages agree on repository `001–020 / next 021–025`;
- canonical spelling uses `엘리스` on CURRENT surfaces;
- project registry Repo Main SHA equals the post-merge main SHA;
- `Sync State = SYNCED` only after destination readback.

## Rollback

- Repository: revert the single squash merge; historical evidence remains intact.
- Notion: restore only the current-state snippets/properties from pre-change readback.
- DOCX: delete/ignore the presentation derivative; immutable original remains authoritative.
