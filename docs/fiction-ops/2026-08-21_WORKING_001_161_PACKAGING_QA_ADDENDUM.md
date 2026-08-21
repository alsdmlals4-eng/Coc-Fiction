# 2026-08-21 Working 001–161 Packaging QA Addendum

Status: `PACKAGING_CORRECTED / PRESENTATION_ONLY_DERIVATIVE / SOURCE_AUTHORITY_UNCHANGED`

## Scope

This addendum corrects one packaging-evidence overclaim from the 2026-08-20 QA_GREEN working candidate review. It does **not** change story prose, Canon, chapter authority, or GitHub production promotion.

## Immutable source

- source artifact: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- Library path: `/coc 소설/폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- SHA256 reverified: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- source bytes were not overwritten.

The existing 2026-08-20 story/content QA remains bounded evidence for its actual checks: chapter coverage, protected Canon checks, forbidden variants, POV scene-break contract, and the recorded prose changes. The previous broad visual statement `0 obvious visual defects` is narrowed because the running-header semantic defect below was missed.

## Root cause

The integrated source DOCX has one referenced global running header, `word/header1.xml`, containing:

`폭풍의 눈 · 제001–010화`

Because the artifact contains the current 001–161 candidate, that global header falsely labels later pages as though the document covered only Chapters 001–010. The defect is packaging metadata/layout text, not manuscript body content.

## Presentation-only derivative

- derivative: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_HEADER_FIXED.docx`
- Library path: `/coc 소설/폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_HEADER_FIXED.docx`
- SHA256: `d96eab6115f71d03657bfa07dad9bf3d27a4bbb28545d8b67ffffbb507e8e636`
- running header: `폭풍의 눈 · 001–161 통합 검수본`
- authority: `PRESENTATION_ONLY_DERIVATIVE`

The derivative is not a new source candidate and does not move repository promotion authority.

## Body preservation evidence

`word/document.xml` is byte-for-byte identical between source and derivative.

- source `word/document.xml` SHA256: `1920a28fa7109d3d42f5bcbc8b8ce2f392c1308ca12c6f6074da32369a8796fe`
- derivative `word/document.xml` SHA256: `1920a28fa7109d3d42f5bcbc8b8ce2f392c1308ca12c6f6074da32369a8796fe`

The observed chapter-number set remains exactly `1–161` with 161 unique chapter numbers. Existing dedicated candidate QA remains the authority for exact 161 heading / missing-0 / duplicate-0 evidence.

## Semantic header regression contract

New repository contract:

- `tests/test_fiction_docx_packaging.py`
- `tools/check_fiction_docx_packaging.py`

The checker follows the DOCX relationship graph to referenced running headers and rejects a single global explicit chapter-range header when it contradicts the declared artifact range.

TDD evidence:

- RED head: `8e152f394f24c420d32fc9256c7f43c97a40f78f`
- RED workflow run: `32487311975`
- all pre-existing fiction validators and the current-state closure contract were Green;
- only `Validate DOCX packaging contract` failed because the checker did not yet exist.
- GREEN implementation head: `20f5ace82adfb0db1fbbc5d9f17d38c0111b9640`
- GREEN workflow run: `32487404915`
- result: `SUCCESS`.

## Render / visual readback

The corrected derivative was rendered to a complete PDF:

- pages: `796`
- page size: Letter / 612 × 792 pt

Automated source-vs-derivative PDF comparison across all 796 pages:

- corrected neutral header detected: `796 / 796` pages;
- old `001–010` header detected in derivative: `0 / 796` pages;
- text blocks below the header band (`y > 45`) differing from the source render: `0 / 796` pages;
- running-header vertical bounds remained within approximately `y=22.72–34.30` on every page, with no body overlap.

Visual inspection evidence:

- 8 contact sheets covering pages `1–796` were inspected for obvious blank-page, clipping, overlap, and layout-collapse regressions;
- high-resolution spot checks inspected pages `1`, `185`, `400`, and `796`;
- no new obvious clipping, overlap, anomalous blank, or body-layout regression was observed.

The canonical DOCX rendering helper produced the complete PDF but timed out during full 796-page PNG rasterization. Therefore this addendum does **not** claim a completed canonical 796-PNG render. The complete PDF, all-page automated block comparison, all-page contact-sheet coverage, and high-resolution spot checks are the actual visual evidence used here.

## Evidence ceiling

`PACKAGING_CORRECTED` means the known running-header defect is corrected in the presentation derivative and guarded by a repository regression contract. It does not mean:

- whole-manuscript prose continuity is now claimed;
- 021–161 has been promoted to GitHub production;
- human reader/publication QA has been completed;
- the immutable source candidate has been replaced.

The repository production frontier remains `001–020`, with `021–025` as the next bounded promotion unit.
