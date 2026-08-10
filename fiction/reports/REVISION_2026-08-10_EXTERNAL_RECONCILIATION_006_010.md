# Revision Report — External Canon Reconciliation 006–010

날짜: 2026-08-10

## Finding first

제1~5화 reconciliation 이후 저장 구 제6~10화를 그대로 이어 붙이면 섬 해안·감옥까지 진행한 사건이 다시 선상 저녁과 공격 전조로 되감긴다. 구 `006-010` 내부 패스는 수행 당시 저장 편성의 실제 검증이지만, 외부 최신 압축 편성의 제6~10화를 검증한 증거는 아니다.

이번 패스는 외부 최신 제6~10화를 현재 원본 사건·최신 Canon·통합 시트의 섬/동굴 구간과 대조해 5/5 `APPLY`하고, mixed-migration boundary를 제5→6에서 제10→legacy 제11로 이동한다.

```text
reconciled Ch1-5
→ external latest Ch6-10 comparison
→ 5/5 APPLY
→ Ch5↔Ch6 current continuity restored
→ Ch10 migration boundary
→ stored Ch11 = legacy tail / continuity not claimed
→ next reconciliation = external Ch11-15
```

## 기준과 증거 한계

- 프로젝트 기준 main: `6fc534b5708cdbe7eb6b99597b6bd282b92b5703`
- 외부 산출물: `폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip`
- 원본 인벤토리: 1부 등록 원본 `COC 1일차(2).pdf`, `COC 2일차(2).pdf`, `CoC 3일차(2).pdf` 등
- current integrated navigation: workbook `1-EP 3`, `1-EP 4`
- 최신 Canon: `fiction/CANON_REGISTRY.json`
- 폐기 legacy 통합 초안: current prose 입력으로 사용하지 않음
- 원본 전수 감사: `IN_PROGRESS`; 이번 보고는 006–010 묶음의 사건/정보상태 대조만 주장한다.

## 회차별 판정

| 화 | 제목 | 판정 | 핵심 기능 |
|---|---|---|---|
| 6 | 따뜻한 피난처 | APPLY | 엘리스·이안 해안 / 주안 별도 감옥, 흉터 노인·절벽, 수신기 단방향 계약 |
| 7 | 죽은 척해야 사는 곳 | APPLY | 시체 더미 생존자, 주민/황색 은폐, 동굴 진입, 밀리 목소리 후크 |
| 8 | 같은 편은 아닙니다 | APPLY | 밀리 재회, 주안·아킴·히템 분기, 소속/지원/신뢰 분리 |
| 9 | 카터라는 이름 | APPLY | 성씨·점토판·벽화, 카터 과거 단서, 원문/해석/설명 분리 |
| 10 | 친구를 쏜 날 | APPLY | 책 요구·정체 충돌·이안 사격·불확실한 결과, 친구 손실의 비용 |

## Current body evidence

| 화 | body chars | SHA256 |
|---|---:|---|
| 6 | 5974 | `c3f5fa22dbc3738008628aee2d9dc0d95c57cd67292e0701505964742340ea69` |
| 7 | 6097 | `d497812fa56cbd08979b1632ba953f9bb26be0d279a12a224134112bbbfee507` |
| 8 | 5605 | `a7d3b0f7da47b5b5e33ef55f36718759e1b56c2a29ca9aefd22471225d1332e8` |
| 9 | 5956 | `f17c52eccd0ec5d2b318616892cbbd7a6ff5518f82b33c87c9cf5a1ea897a76d` |
| 10 | 6174 | `c111057621a81e4058ef662e28fdf3f6585cc48778136d1c93ee00a0f3893daa` |

본문 해시는 현재 PR branch의 manuscript body 기준으로 맞춘다. 파생 index/outline/Scene Pass Registry가 같은 SHA를 소비해야 한다.

## Canon / character regression

- 주안: 감옥 탈출과 아킴 합류에서도 자기 행동 이유를 현재 상황에서 다시 잡는다. 다른 인물의 소속·명령이 주안 선택을 대신하지 않는다.
- 엘리스: 아버지·밀리·이안에 대한 감정과 사실 판정을 분리한다. 좋아하거나 사랑한다는 이유로 안전/정당성을 자동 승인하지 않는다.
- 이안: source / 그림 / 타인 설명 / 자기 추론을 별도 기록한다. 밀리가 친구라는 사실과 안전 판정을 분리한다.
- 아킴: 허용된 지원 인물로 등장하며 주안의 중앙 선택을 대신하지 않는다.
- 신호 장치: 송신 버튼 → 주안 쪽 수신 진동만 유지한다. 역송신·위치·문자·음성 기능을 추가하지 않는다.
- 제10화 정체 충돌: 친구의 존재, 투영 여부, 본체 사망 여부를 현 시점에서 확정하지 않는다.
- active strict content scan은 current exact HEAD CI가 최종 판정한다.

## Mixed migration boundary

```yaml
reconciled_prefix_end: 10
legacy_tail_starts_at: 11
boundary_after_chapter: 10
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bundle: fiction/manuscript/part-1/011-015.md
```

- 제5화는 정상적으로 제6화와 다시 연결한다.
- 제6화는 제5화를 정상 previous로 갖는다.
- 제10화는 `RECONCILIATION_MIGRATION_BOUNDARY`로 `next_chapter=null`.
- 저장 제11화는 `LEGACY_TAIL_BOUNDARY`로 `previous_chapter=null`.
- 저장 제11화 이후를 최신 외부 편성의 자연스러운 다음 사건으로 자동 주장하지 않는다.

## Historical evidence policy

구 저장 `006-010`의 내부 패스는 삭제하지 않는다.

- historical cards: `fiction/analysis/SCENE_CARDS_006_010.md`
- historical report: `fiction/reports/REVISION_2026-07-23_SCENE_PASS_006_010.md`

이들은 `HISTORICAL_EVIDENCE / SUPERSEDED_BY_EXTERNAL_RECONCILIATION`으로 범위를 제한한다. current external owner는 `SCENE_CARDS_EXTERNAL_RECONCILIATION_006_010.md`와 본 보고서다.

## TDD lineage

### INVALID RED — rejected

- head: `9d60581ff6bb2b9f2e575bcf40d73fcb0c519e10`
- run: `31356379678`
- result: FAILURE
- disposition: `REJECTED_AS_TEST_BUG`
- 원인: 기존 migration 상태의 `next_chapter=null`을 test code가 dict로 가정해 `.get()`을 호출한 TypeError.
- 처리: production을 건드리지 않고 validator만 None-safe로 보정했다.

### VALID RED

- exact head: `6343a6e7ed7c2213349de080deb093b1b162cfdb`
- run: `31356440581`
- result: expected `FAILURE`
- 기존 operating/content/reverse-outline 회귀는 선행 PASS.
- 새 계약에서만 다음 누락을 검출: 최신 제6~10 본문 invariant, prefix=10, tail=11, Ch5↔6 재연결, Ch10→11 migration boundary, next 011-015.

### GREEN

최종 exact-head workflow 결과는 production consumer 동기화 후 PR 본문과 continuation checkpoint에 기록한다. Green 전에는 완료로 주장하지 않는다.

## Project learning

### PROJECT_ONLY

- 현재 제6~10화의 구체 사건·POV·인물 상태
- 제10→11 actual migration boundary 위치
- exact body SHA·저장 bundle

### BASE_CANDIDATE

current prefix가 늘어날 때 migration boundary를 앞으로 이동시키면서 이미 검증된 이전 경계를 정상 continuity로 복원하고, 새 legacy tail만 fail-closed 해야 한다.

### Existing Base verdict

`REUSE_EXISTING_BCP` — 이 lifecycle은 이미 `BCP-2026-012-serial-fiction-canon-migration-debt` 범위 안이다. 새 Base proposal을 만들지 않는다. Base active implementation도 이번 단계에서 수행하지 않는다.

## 다음 실행 단계

외부 최신 제11~15화를 저장 `fiction/manuscript/part-1/011-015.md`와 대조한다. 제10화 종료 상태를 앞 경계로 두고 회차별 `KEEP / APPLY / REWORK / REJECT`를 판정한다.
