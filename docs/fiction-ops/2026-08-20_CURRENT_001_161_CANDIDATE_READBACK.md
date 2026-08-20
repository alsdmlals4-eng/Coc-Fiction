# 2026-08-20 · Current 001–161 Candidate Readback

Status: `CURRENT_CANDIDATE_MANIFEST_LOCKED_ON_BRANCH`

## Method

The 17 latest range-by-range DOCX artifacts under Library folder `/coc 소설/` were materialized and inspected directly.

For each bundle:

1. calculate SHA256 from the actual DOCX bytes;
2. parse `word/document.xml` and extract chapter headings;
3. compare declared filename range against observed chapter headings;
4. count known canonical-name / superseded-name variants that must be normalized before promotion.

The authoritative machine-readable result is:

`docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json`

## Coverage result

```text
bundle_count: 17
observed_chapter_headings: 161
coverage: 001–161
missing_chapters: 0
duplicate_chapters: 0
coverage_status: PASS
repository_promotion_state: NOT_PROMOTED
verified_repository_prefix_end: 005
legacy_tail_starts_at: 006
```

This proves the current external candidate set is complete by chapter-heading coverage. It does **not** by itself mean the prose has been normalized, revised, or promoted to GitHub manuscript authority.

## Source authority order

The current range-by-range artifacts take precedence over the older integrated 001–105 ZIP for current-candidate reconstruction.

| Range | Artifact | SHA256 |
|---|---|---|
| 001–010 | `폭풍의눈_2차퇴고_제001-010화_몰입도입부_가독성강화본.docx` | `ee2ec785a6e66bb06cba80d3d3dbe1954934ad14e6c568408222906ad7892f96` |
| 011–020 | `폭풍의눈_2차퇴고_제011-020화_캐릭터복선_가독성강화본.docx` | `559ceeaa00cbf59a839b4bdb75b19165db2c49037940769e5ffb6852b1372e56` |
| 021–030 | `폭풍의눈_2차퇴고_제021-030화_상실광기_강적위상_가독성강화본.docx` | `e15c8fb4ed4ab1b6980c2c57f3979986bdbfa02f77aafef3cc84d3652cb70547` |
| 031–040 | `폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본.docx` | `89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10` |
| 041–050 | `폭풍의눈_2차퇴고_제041-050화_가족재회_선택불확실성_8년브리지_가독성강화본.docx` | `9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad` |
| 051–060 | `폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본.docx` | `84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496` |
| 061–070 | `폭풍의눈_2차퇴고_제061-070화_2부진입_타임리프도입_가독성강화본.docx` | `74108e1494342b43f0c3e19d60e84e0db45e2f30d03fc530ae044db251862f14` |
| 071–080 | `폭풍의눈_2차퇴고_제071-080화_다빈엘리엇_앨리스합류_가독성강화본.docx` | `b29257351c0f08813d1a428857c623c824df3d581e896bef4faa9cc52184db62` |
| 081–090 | `폭풍의눈_2차퇴고_제081-090화_동행신뢰_금기의료_가독성강화본.docx` | `7e729cf378fade4f362b7e34bbdbdf3f2e2e433057ac1f6bcc91ab16d53f18dc` |
| 091–100 | `폭풍의눈_2차퇴고_제091-100화_정본복원_강자위상_금기진단_가독성강화본.docx` | `24de4c716fd1c01165fc046406fb341ca65b0c2a7193a2ccd8a87948107348d8` |
| 101–105 | `폭풍의눈_2차퇴고_제101-105화_팽무악검전_동기교정_가독성강화본.docx` | `6ef7643aae8ffa358dcd0b5594dc73ac978aedc59b4b597ddda895e508c2b15b` |
| 106–115 | `폭풍의눈_2차퇴고_제106-115화_시신소유권_금기수술_반복증명_가독성강화본.docx` | `e19fe8c97fd33dd9fe14326d71cf1af2b63409cdeccdf4728df19c774755e192` |
| 116–125 | `폭풍의눈_2차퇴고_제116-125화_주독역보호_독립공동전선_가독성강화본.docx` | `ae75ec7308e835763b5cbf3eb6f7b8070ef6245f46d5fa1570457d258b0f2716` |
| 126–135 | `폭풍의눈_2차퇴고_제126-135화_세력전쟁_강자위상_선택권_가독성강화본.docx` | `4f6d4a8ded7ddb606789fe1f86e983fbf33729d2d2bf988ee3293665dbed40fa` |
| 136–145 | `폭풍의눈_2차퇴고_제136-145화_반복수술_실패기억_시간잔류_가독성강화본.docx` | `85d2448b209c8b1dbbe21362cf05a05674640435ed7a3abeca62e1ce8300f17f` |
| 146–155 | `폭풍의눈_2차퇴고_제146-155화_최종선택_후일담_가독성강화본.docx` | `fc3e781772439b3d39f76f4510bebc4057eae9c67bfaaf0221cb024a187f60de` |
| 156–161 | `폭풍의눈_2차퇴고_2부외전_제156-161화_Rift_Accord_협약완결본.docx` | `f9ddf90970a4760652f9bbac21c315daa24a51b47a32bfccfd47ef22a865f8d5` |

The 146–155 and 156–161 hashes match the previously recorded Handoff evidence.

## Normalization debt measured from the actual current artifacts

```text
canonical `엘리스`: 1363 occurrences
alternate `앨리스`: 1103 occurrences
canonical `패닝턴`: 18 occurrences
alternate `페닝턴`: 2 occurrences
canonical `쵸세이칸`: 157 occurrences
alternate `조세이칸`: 3 occurrences
forbidden legacy `쵸르브라트`: 1 occurrence
obsolete `히템`: 0 occurrences
canonical `하템`: 170 occurrences
```

Important placement:

- `앨리스` begins in the 051–060 bundle and continues through 156–161.
- `페닝턴` appears once in 051–060 and once in 156–161.
- `조세이칸` appears three times in 041–050.
- `쵸르브라트` appears once in 041–050.
- `히템` is already zero in the current artifacts.

## Locked next mutation order

1. make a working copy of this exact 17-bundle candidate;
2. normalize canonical names / forbidden variants without changing source artifacts in-place;
3. apply mandatory P0 prose payoffs:
   - Ch121: D02 photo practical evidence-class payoff;
   - Ch151: Dabin–Lee Hyang-bok incomplete reunion / relationship-right renegotiation;
   - 155→156: minimal chronology label;
4. apply bounded POV hotspot and exposition-compression passes;
5. re-run whole-candidate QA;
6. only after Green, resume repository promotion from 006–010.

Source DOCX files remain immutable evidence inputs. Revised integrated output must be a new artifact with its own hash and promotion state.
