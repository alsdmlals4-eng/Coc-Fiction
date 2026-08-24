# Revision Report · Ch031–035 bounded reconciliation

## Status
- source authority: `폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx`
- source SHA256: `89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10`
- candidate frontier on PR #50: `001–035`
- next fail-closed boundary: `035→036`
- whole-manuscript continuity: `NOT_YET_CLAIMED`

## Exact-transfer receipt
| Chapter | Title | POV | Body chars | Body SHA256 |
| --- | --- | --- | ---: | --- |
| 31 | 창을 잡는 사람 | 주안 → 엘리스 → 주안 → 엘리스 → 주안 → 엘리스 → 이안 | 10305 | `c24a4c8b236e12b54825c44c810a96588e4b1360b02f8e8a9f4df5d26fd20353` |
| 32 | 전장 전체가 몸이었다 | 이안 → 주안 → 엘리스 → 이안 → 주안 | 6291 | `e55613d4b68fd0d6222a680d3eba1d0416033504322fc9aaae6cf09a9cdc6bce` |
| 33 | 괴물이 되어야 합니다 | 주안 → 엘리스 → 주안 → 엘리스 → 주안 | 5933 | `a6042d9b3c6dc9b82e603c2088a45d9a2f09b974ff224d0a3de618eb5c1d4cec` |
| 34 | 핵은 붉었다 | 주안 → 엘리스 → 이안 → 주안 → 엘리스 | 5935 | `ffbe4a8459f972bcdae6f9fa27416c63a64efb900c19006348d7718c9c20286d` |
| 35 | 완전 소 생물 | 이안 → 주안 → 엘리스 → 이안 → 주안 → 엘리스 | 6194 | `c4b02af3eb326dfd18ec0331c762c92655cb97525b8b3223d407e69ce912d5f2` |

## Canon conflict scan
- 엘리스: 인간을 포함한 정신 대상의 인지·판단·행동 조작 가능. 선택 보존은 윤리·자기규율.
- 주안: `반응 → 멈춤 → 이유 → 선택`; 보호행동을 소유/복종으로 환원하지 않음.
- 이안: 관찰 → 가설 → 검증 → 기록; 하템 환각은 신규 객관정보를 만들지 않음.
- 밀리/하템: 별도 인물·별도 죽음.
- 탈론: Part 1 core antagonist의 높은 화면 안 전투 위상 유지.

## Boundary
- Ch30→31: DIRECT CONTINUITY candidate PASS.
- Ch35→36: source-level DIRECT CONTINUITY를 확인했지만 Ch36은 별도 다음 bounded pass 전까지 legacy tail.

## 5× adversarial review
1. Source identity / exact body receipt: PASS.
2. Character identity / death-state / D04 capability drift: PASS.
3. Agency / ownership / obedience flattening: PASS.
4. Consumer propagation / rollback boundary: PASS.
5. Part boundary / future-tail overclaim / 101–105 source gap: PASS.

`CLEAN_REVIEW_EXIT` is conditional on exact-head hosted CI Green and unresolved review thread 0.

## Implementation Reality Gate
- manuscript exact source installed: YES
- index/reverse-outline/scene-pass/router consumers materialized: YES
- Ch36+ prose mutation: NO
- whole-manuscript continuity claimed: NO
- production merge claimed before CI: NO
