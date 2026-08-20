# 2026-08-20 · Current Candidate Reconciliation · 제006~010화

상태: **CURRENT_RECONCILIATION_COMPLETE / PROMOTION_GATE_PENDING**

## Authority

- source artifact: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- source SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- source artifact state: `QA_GREEN / NOT_PROMOTED`
- target: `fiction/manuscript/part-1/006-010.md`
- previous verified prefix: `001–005`
- current target frontier after Green propagation: `001–010`
- next legacy tail: `011+`

## Bundle decision

| 화 | current title | POV | decision |
|---:|---|---|---|
| 006 | 따뜻한 피난처 | 엘리스 → 이안 → 주안 | `APPLY` |
| 007 | 죽은 척해야 사는 곳 | 이안 → 엘리스 → 이안 | `APPLY` |
| 008 | 같은 편은 아닙니다 | 이안 → 주안 | `APPLY` |
| 009 | 카터라는 이름 | 엘리스 → 이안 | `APPLY` |
| 010 | 친구를 쏜 날 | 이안 → 엘리스 → 이안 | `APPLY` |

## Canon / continuity readback

### Ch5→6

Current Ch5 ends with:
- 엘리스+이안 해안 축
- 주안 별도 감옥 축
- 노란 가면의 거인 별도 감옥

Current Ch6 directly resumes those same states. The historical false continuity that returned to pre-disaster shipboard dinner is removed.

### Signal contract

Ch6 explicitly preserves the one-way receiver rule: Jooan cannot transmit a reply; he can only survive until Alice's emergency signal reaches him.

### Milly / Hatem

- Milly is alive in Ch8 and remains a genuine friend/history plus current operational threat.
- Hatem is a separate embodied contractor and explicitly rejects simple Yellow affiliation.
- Ch10 Milly disappearance leaves no body or blood. `Milly dead` remains Ian's emotional belief, not objective canon fact.

### Reader knowledge

Ch9 separates evidence from inference around the `CARTER` carving. Alice refuses to convert an old family name into proof that William knowingly caused the current event.

## Coupled-consumer contract

Promotion is valid only if the same exact PR head updates and passes:

- manuscript bundle
- composed manuscript index override
- reverse-outline Ch5 boundary override
- reverse-outline Ch6–10 override
- Ch1–5 and Ch6–10 scene cards
- Scene Pass Registry
- representative Ch10 gate
- reverse-outline report/router state
- live `FICTION_MASTER`, `ACTIVE_CONTEXT`, `START_HERE`
- scene-pass validator frontier assertions
- reverse-outline generator boundary logic

## New migration boundary

```yaml
reconciled_prefix_end: 10
legacy_tail_starts_at: 11
boundary_after_chapter: 10
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bundle: fiction/manuscript/part-1/011-015.md
```

The current candidate is Green through 161 as an external/revised artifact, but GitHub production authority moves only through Ch10 in this bounded PR.
