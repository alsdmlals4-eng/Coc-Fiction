# Revision Report — External Canon Reconciliation 001–005

날짜: 2026-08-10

## Finding first

외부 최신 제1~105화 산출물과 GitHub 225화 원고는 **같은 화 번호를 쓰지만 같은 편성이 아니다.** 외부 최신본은 초반 사건을 압축 재편성했고, GitHub current manuscript는 구 225화 저장 토폴로지를 유지한다. 따라서 외부 제1~5화를 current로 승격한 뒤 구 제6화를 곧바로 다음 화로 연결하면 선박 침몰·섬 감옥 진입 뒤 다시 선상 저녁 전조로 돌아가는 사건 회귀가 발생한다.

이번 패스는 이를 다음처럼 처리했다.

```text
external latest Ch1-5
→ raw COC + latest Canon 대조
→ 5/5 APPLY
→ GitHub Ch1-5 current delta 적용
→ exact index/reverse-outline override
→ Ch5 migration boundary
→ stored Ch6 = legacy tail / continuity not claimed
→ next reconciliation = external Ch6-10
```

## 기준과 보호 범위

- 프로젝트 기준 main: PR 생성 시 `ee32ea7e08cc401cf502daa2cd66155054eb8bfc`
- 외부 산출물: `폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip`
- QA: `폭풍의눈_제001-105화_통합최종_QA보고서.md`
- 원본: `COC 1일차.pdf`, `COC 2일차.pdf`
- integrated navigation: `Coc 폭풍의 눈(주안편).xlsx`
- Canon: `fiction/CANON_REGISTRY.json`
- superseded 225화 압축 초안: 사용하지 않음
- Base active implementation: 없음

## 회차별 판정

| 화 | 외부 최신 제목 | 판정 | 핵심 근거 |
|---|---|---|---|
| 1 | 위대한 심연의 군주 | APPLY | 출항·짐 사고·고서 발견/해독 + 브루스/펜던트 계승을 source order 안에서 압축 |
| 2 | 내가 고른 경호원 | APPLY | 엘리스의 선택, 주안·밀리 벌꿀주스, 세실리아·데커 관계, 경호/통신 이상을 결합 |
| 3 | 식탁 아래의 축배 | APPLY | 식사→빈 테이블→위험 감지→식탁 아래 은신→축배→비야키→탈출 순서 보존 |
| 4 | 카르코사의 낭독 | APPLY | 선실 방어·브루고·노란 코트·정신 압박·주안 이유 회복·선체 붕괴 |
| 5 | 신호기를 잃지 마세요 | APPLY | 침몰·이안 별도 구조정·주안/탈론 동시 휩쓸림·엘리스/이안 해안·주안 감옥 |

구 GitHub 제1~5화는 현재 서사 정본으로 `REJECT`한 것이 아니라 **새 편성으로 superseded된 historical manuscript evidence**로 취급한다. 과거 body를 현재 파일 안에 이중 보존하지 않는다. Git history가 변경 이력을 보존한다.

## Current body evidence

| 화 | body chars | SHA256 |
|---|---:|---|
| 1 | 6047 | `68a7ef71ecb2ef804580a07a6acbb663ee055a8faa95cd917bd9d5895b26a175` |
| 2 | 6139 | `4a365526b359afa128989f9cd2a01def075e39b9a192495b6f7532580502d16e` |
| 3 | 6226 | `46fecaa8909019393038e4f34a13790bc17c0ff3596a831774b8583258e204e8` |
| 4 | 6850 | `61176e16405b95064210a7e071e5bcca7bc2f9435aed422235fca5a8df4a1747` |
| 5 | 5996 | `2b7d2e242e69cf43cc4063aad1dafd9a968b66c93d5d4c3f16f93bcaaf1b19e2` |

본문 해시는 명시적 POV 표식과 장면 구분선을 포함하고 제목/POV 메타 헤더와 source comment는 제외한 **현재 PR branch의 실제 GitHub manuscript body** 기준이다. 외부 DOCX staging copy와 branch body 사이의 미세한 문자 차이가 있더라도 GitHub 정본 소비자는 branch body exact SHA를 사용한다.

## Canon / character regression

- 주안: 독립 `복종인자` 설명축을 복원하지 않는다. 제4화의 흰 방은 본인도 기억/상상/공격 거짓 여부를 확정하지 않으며, 엘리스가 “내가 시켜서 말고”라고 이유 공간을 돌려준 뒤 주안이 “당신이 싫어서”라고 선택 이유를 다시 잡는다.
- 엘리스: 주안을 대신 결정하지 않고 선택 공간을 되돌리는 역할을 유지한다.
- 신호기: 단순 신호→수신 진동. GPS/문자/통화/위치추적 기능 없음.
- 아킴: 이번 1~5 직접 중심축이 아니며 등장 허용 Canon과 충돌 없음.
- 2부 버실라/Woff exclusion과 충돌 없음.
- 새/수정 원고 금지 설정명: `복종인자`, `블랙킹`, `조작된 감정`, `오션`, `앨리스`를 설명축으로 사용하지 않음.

## Mixed migration boundary

```yaml
reconciled_prefix_end: 5
legacy_tail_starts_at: 6
boundary_after_chapter: 5
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bundle: fiction/manuscript/part-1/006-010.md
```

기존 `006-010` 내부 연속성 패스는 삭제하지 않는다. 그것은 구 편성 내부에서 실제로 수행된 검증 증거다. 다만 새 압축 편성과의 5→6 경계를 검증한 증거는 아니므로 `EXTERNAL_RECONCILIATION_PENDING_LEGACY_TAIL`로 범위를 제한한다.

## Coupled consumers

이번 변경은 다음 owner/consumer를 함께 갱신한다.

- `fiction/manuscript/part-1/001-005.md`
- `fiction/MANUSCRIPT_INDEX.json`
- `fiction/analysis/MANUSCRIPT_INDEX_OVERRIDE_001_005.json`
- `fiction/analysis/REVERSE_OUTLINE_001_225.json`
- `fiction/analysis/REVERSE_OUTLINE_OVERRIDE_001_005.json`
- `fiction/analysis/REVERSE_OUTLINE_OVERRIDE_006_010.json`
- `fiction/analysis/SCENE_PASS_REGISTRY.json`
- `fiction/analysis/SCENE_CARDS_001_005.md`
- 대표 게이트·역개요 보고·FICTION_MASTER·START_HERE
- `tools/build_fiction_reverse_outline.py`
- `tools/check_fiction_scene_passes.py`

## TDD lineage

### RED

- exact head: `e3b08b06437ae01af95c25168f462c5653a97964`
- workflow: `Fiction operating system`
- run: `31354076010`
- result: expected `FAILURE`
- preceding content/index/reverse-outline steps: PASS
- failure owner: `Validate completed scene passes`
- exposed gap: 001-005 pass/외부 artifact/migration boundary/next 006-010가 아직 production data에 없음.

### GREEN

최종 exact-head workflow 결과는 PR의 최종 검증 후 이 보고와 PR 본문에 기록한다. Green 이전에는 완료로 주장하지 않는다.

## Project learning

### PROJECT_ONLY

- 외부 최신 001~105의 실제 재편성
- Ch5→legacy Ch6 경계 위치
- 각 회차 제목/POV/source 사건
- exact body SHA와 bundle path

### BASE_CANDIDATE

`new current prefix + unreconciled legacy tail` 상태에서 새 정본의 즉시 권위와 기존 artifact migration 완료 상태를 분리하고, false continuity를 차단해야 한다.

### Existing Base verdict

`REUSE_EXISTING_BCP` — `BCP-2026-012-serial-fiction-canon-migration-debt`가 이미 이 원리를 proposal-only로 보유한다. 새 중복 BCP를 만들지 않는다.

## 다음 실행 단계

`fiction/manuscript/part-1/006-010.md`를 외부 최신 제6~10화와 대조한다. 구 `006-010`의 내부 패스 증거는 보존하되, 회차별로 `KEEP / APPLY / REWORK / REJECT`를 다시 판정하고 새 제5화에서 이어지는 사건·인물 상태를 검증한다.
