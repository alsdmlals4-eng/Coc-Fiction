# 2026-08-20 · Current Candidate Reconciliation · 제011~015화

상태: **CURRENT_RECONCILIATION_COMPLETE / PROMOTION_GATE_PENDING**

## Authority

- source artifact: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- source SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- source artifact state: `QA_GREEN / NOT_PROMOTED`
- prior individualized cross-check: `폭풍의눈_2차퇴고_제010화-제021화_모음.zip`
- target: `fiction/manuscript/part-1/011-015.md`
- previous production prefix: `001–010`
- target frontier after Green propagation: `001–015`
- next legacy tail: `016+`

## Source-boundary note

The current Files semantic lookup for original Part1 PDFs returned an authentication error, so this pass does **not** claim new direct-PDF source discoveries. It promotes the already approved QA_GREEN current candidate and cross-checks it against the prior individualized 10–21 final-correction bundle and current Canon. Any future direct-source discrepancy still outranks adaptation prose.

## Bundle decision

| 화 | current title | POV | decision |
|---:|---|---|---|
| 011 | 비야키를 타는 법 | 주안 | `APPLY` |
| 012 | 못 본 척 해줄게 | 이안 → 엘리스 → 이안 → 엘리스 → 이안 → 엘리스 → 이안 | `APPLY` |
| 013 | 아버지 대신 | 이안 → 엘리스 | `APPLY` |
| 014 | 후회하지 않는 선택 | 엘리스 → 주안 → 이안 | `APPLY` |
| 015 | 섬의 왕과의 거래 | 엘리스 → 주안 | `APPLY` |

## Exact body evidence

| 화 | chars | SHA256 |
|---:|---:|---|
| 011 | 13226 | `b21d107fee15795235ec518fee82e4d5192884ce4948665d1ed36317e691e96d` |
| 012 | 6650 | `075905093ff62858acc367e92e368eeb6e9aff69f5b472257040cac398571e41` |
| 013 | 7096 | `3d12e20c6a00efc1cba80baf2827b723b6115912f5427036e4a963226d95659c` |
| 014 | 6732 | `14d186deeba2eaf88ece52f55abaa11c48ab3c3abdda4fd7057e0cc1fd7b5544` |
| 015 | 7453 | `51017e43afd407efda9a9c745c6836cdaf23554942f848b6f65a12bca39fccb0` |

## Canon / continuity readback

### Ch10→11

This is an intentional parallel-front switch, not a rewind:
- Ch10 closes Ian/Elise's Milly disappearance evidence state.
- Ch11 returns to Jooan/Akim/Hatem's parallel movement toward Cecilia.
- No claim is made that Jooan observed Ch10.

### Ch11

Jooan rejects human sacrifice as a transport optimization even while cooperating with people who normalize it. `friend/cooperator` is not upgraded to blanket trust or moral approval.

### Ch12

Milly's disappearance remains evidence-incomplete. Hatem is explicitly separated from Milly despite the same face. Ian records friend / current hostile action / life-state unknown as separate facts.

### Ch13

Cecilia rescue gives Elise direct access to partial Carter-family history. The manuscript does not convert partial testimony into a complete verdict about William. Elise refuses inherited guilt as inherited decision authority.

### Ch14

Elise asks Cecilia how she wants to be protected. Jooan proves strength on screen while choosing nonlethal passage instead of killing a defeated opponent. His next route is his own stated choice.

### Ch15

David's deal makes coercive context explicit, but Elise still distinguishes why **she** accepts it. Jooan asks before physical reunion contact. The group coordinates priorities rather than one protector deciding for everyone. The final crown demand opens the next current arc.

## New migration boundary

```yaml
reconciled_prefix_end: 15
legacy_tail_starts_at: 16
boundary_after_chapter: 15
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bundle: fiction/manuscript/part-1/016-020.md
```

Current Ch15 ends on the Yellow-crown retrieval condition. Stored legacy Ch16 begins from an old prison/Hatem setup, so adjacent numbering must not imply continuity before the next bounded pass.

## Coupled-consumer contract

Promotion is valid only if the same exact PR head updates and passes:

- manuscript bundle
- composed manuscript index override
- reverse-outline Ch10 reconnection
- reverse-outline Ch11–15 current override
- reverse-outline Ch16 legacy boundary override
- scene cards
- Scene Pass Registry
- representative/report/router frontier wording
- live `FICTION_MASTER`, `ACTIVE_CONTEXT`, `START_HERE`
- scene-pass validator frontier assertions
- reverse-outline reproducibility

## Promotion boundary

The external/current candidate remains Green through 161, but GitHub production authority may move only through Ch15 in this bounded unit. Ch16+ remains legacy until its own promotion gate passes.
