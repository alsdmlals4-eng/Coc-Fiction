# 2026-08-20 Current Candidate Reconciliation · Ch011–015

상태: **IMPLEMENTED_ON_BRANCH / AWAITING_EXACT_HEAD_GREEN**

## 목표

QA_GREEN integrated working candidate의 제11–15화를 GitHub production manuscript의 다음 5화 단위로 승격하고, verified frontier를 `10→11`에서 `15→16`으로 이동한다.

## 권위 입력

- artifact: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- candidate manifest: `docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json`
- structured canon: `fiction/CANON_REGISTRY.json`
- prior verified frontier: Ch10 / legacy tail Ch11+

## TDD RED

### 잘못된 첫 RED
- PR #33은 새 test가 `None` boundary를 잘못 역참조해 예외로 종료했다.
- production 의미의 실패가 아니므로 **병합 없이 폐기**했다.

### 유효 RED
- corrected draft PR #34 / workflow run `32331920404`.
- Base reuse / operating system / active content / reverse-outline validation은 기존 상태에서 Green.
- `Validate completed scene passes`만 의도한 이유로 실패:
  - 011–015 completed pass 부재
  - current Ch11–15 invariant 부재
  - legacy `히템` 잔존
  - frontier가 여전히 10→11
  - Ch10/11 old boundary 상태
  - Ch15/16 new boundary 부재
  - next bundle이 011–015로 남음
- PR #34는 병합 없이 닫았다.

## 적용 본문

| 화 | 제목 | POV | body chars | SHA256 |
|---|---|---|---:|---|
| 11 | 비야키를 타는 법 | 주안 | 7350 | `b868068e8036a7ea22fae778ec3c71059a3f1bf2bd3b9759cca0663c4e6da7f3` |
| 12 | 못 본 척 해줄게 | 이안 → 엘리스 → 이안 → 엘리스 → 이안 → 엘리스 → 이안 | 6269 | `b020e14d87c94884f2dceae271930bdc36953512091a9d5136a37030ff477cb2` |
| 13 | 아버지 대신 | 이안 → 엘리스 | 7410 | `6d5da0c205ecfd0626cb6977f62b6d274631127e940e0af55dd95f1c3aebbfc3` |
| 14 | 후회하지 않는 선택 | 엘리스 → 주안 → 이안 | 4787 | `9ae2e7b58baf3b9f91890f74b502e4ef2c09f4efb5f7f137c280a3f0b4d69182` |
| 15 | 섬의 왕과의 거래 | 엘리스 → 주안 | 6031 | `d26da36ff8d59d9fcad5393c28189b61f50579eb100aeb7965bf562e45e8692d` |

Source-line provenance retained:
- Ch11 `7531–7712`
- Ch12 `7715–7895`
- Ch13 `7898–8079`
- Ch14 `8082–8308`
- Ch15 `8311–8504`

## Canon/readability corrections realized by the current candidate

- `히템` legacy spelling → canonical `하템`.
- `앨리스`가 아니라 canonical `엘리스` 유지.
- Ch12–13에서 하템과 밀리의 같은 얼굴은 동일인 떡밥이 아니라 **별도 인물 + 얼굴 기원 미스터리**로 정리된다.
- 밀리 소실은 객관적 사망 확정이 아니다.
- Ch13–14에서 엘리스 보호 자아는 외부 존재가 아니라 같은 자아의 보호적 부분으로 유지된다.
- 윌리엄의 과거 죄는 엘리스의 선택권/책임으로 자동 상속되지 않는다.
- Ch15 데이비드는 인간적 애착과 잔혹성이 공존하는 유능한 상대이며, 협상 가능성이 면책을 뜻하지 않는다.

## 파생 consumer

- `MANUSCRIPT_INDEX_OVERRIDE_011_015.json`
- `REVERSE_OUTLINE_OVERRIDE_010_CURRENT_CONNECTION.json`
- `REVERSE_OUTLINE_OVERRIDE_011_015.json`
- `REVERSE_OUTLINE_OVERRIDE_016_MIGRATION_BOUNDARY.json`
- `SCENE_CARDS_011_015.md`
- `SCENE_PASS_REGISTRY.json`

Reverse-outline data는 임의 작성하지 않았다. 진단 PR #35에서 실제 repository generator가 frontier 15→16 상태로 생성한 Ch10–16 JSON을 CI 로그에서 회수해 exact override로 반영했고, 진단 PR은 병합하지 않고 닫았다.

## 새 경계

```yaml
reconciled_prefix_end: 15
legacy_tail_starts_at: 16
boundary_after_chapter: 15
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/016-020.md
```

- Ch10→11: `PASS / CURRENT`로 복구.
- Ch15→16: 새 `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.
- Ch16+ body는 이번 작업에서 수정하지 않는다.

## 최종 merge gate

1. exact-head `Fiction operating system` workflow의 모든 validation step SUCCESS.
2. reverse-outline reproducibility 225 composed chapters PASS.
3. scene-pass validation이 `001-015 current production prefix; migration boundary 15→16; 016-020 next`로 PASS.
4. unresolved review thread 0.
5. base `main`이 branch baseline에서 비호환하게 이동하지 않음.
6. squash merge 후 main에서 동일 gate를 다시 readback.
