# 《폭풍의 눈》 현행 정본·작업 기준

상태: **ACTIVE / SINGLE SOURCE OF TRUTH / MIXED MIGRATION**  
최종 갱신: 2026-08-24

## 1. 책임 원본

| 질문 | 현행 책임 원본 |
|---|---|
| 작품 정체성·주제·변경 금지 | `bible/01_PROJECT_CORE.md` |
| Canon 상태·별칭·폐기 | `CANON_REGISTRY.json` |
| 사용자 지정 원본 목록·SHA·누락 | `docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json` |
| 세계·인물·연속성 | `bible/02_CANON_AND_CONTINUITY.md`, 부별 Bible |
| POV·문체·표기 | `STYLE_GUIDE.md` |
| GitHub production manuscript | `manuscript/` |
| 제목·POV·본문 SHA | `MANUSCRIPT_INDEX.json` |
| 구조 역개요 | `analysis/REVERSE_OUTLINE_001_225.json`, `analysis/REVERSE_OUTLINE_REPORT.md` |
| 완료 bundle / frontier | `analysis/SCENE_PASS_REGISTRY.json` |
| 현재 작업 | `ACTIVE_CONTEXT.md` |
| 재개 | `HANDOFF.md` |

## 2. 정본 우선순위

1. 최신 사용자 직접 지시
2. 사용자 지정 구간별 `폭풍의눈_2차퇴고_...` DOCX
3. bounded reconciliation을 통과한 GitHub production canon
4. Notion 승인 요약·Event·Relation
5. 파생 통합본·Legacy 분석

파생 분석이 원본·Canon과 충돌하면 파생 자료를 갱신한다. 원본도 최신 사용자 직접 결정과 충돌하면 bounded reconciliation에서 최소 교정한 뒤 production으로 승격한다.

## 3. Source authority와 production authority

```yaml
source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx
current_bundle_source_sha256: 89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10
derived_cross_check_only: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
repository_promotion_state: PARTIAL
reconciled_prefix: 001-035
legacy_tail_starts_at: 036
boundary_after_chapter: 035
whole_manuscript_continuity: NOT_YET_CLAIMED
last_frontier_change_pr: 50
next_reconciliation: 036-040
source_coverage_gap: 101-105
```

Source authority는 reconstruction input의 권위다. GitHub production authority는 bounded reconciliation·Canon conflict scan·exact-head Green을 통과한 범위까지만 이동한다.

## 4. 저장 토폴로지

저장소의 225화/45 bundle 구조는 migration container다.

- stored `part-1`: 1–70
- stored `side-story-lake`: 71–95
- stored `side-story-alice`: 96–130
- stored `side-story-ian`: 131–165
- stored `part-2`: 166–225

이 구간은 current 001–161 narrative 최종 편성 선언이 아니다. `reconciled_prefix_end` 이후 stored chapter는 자신의 pass 전까지 legacy tail이다.

## 5. 현행 Canon 보호

- Jooan: `반응 → 멈춤 → 이유 → 선택`; 반응성을 복종으로 환원하지 않는다.
- Elise: 인간을 포함한 정신 대상의 인지·판단·행동에 개입·조작할 수 있는 정신계 능력자다. 외부 정신간섭 차단·환각 필터도 가능하다. 선택 보존은 능력의 한계가 아니라, 이 힘을 언제·왜·어디까지 쓸지에 대한 엘리스의 윤리·자기규율이다.
- Ian: 관찰·가설·검증·기록; 모르는 것을 정답으로 올리지 않는다.
- Milly: 실제 남성. 미스캐토닉에서는 하템 외형을 이용한 여성 위장 때문에 `밀리 양`으로 인식됐을 뿐이다.
- Hatem: 실제 여성. 평소 기본 외형은 검은 가면의 광신도. Ch27 사망 이후에는 새 정보 없는 환각/기억만 허용한다.
- Talon: Part 1 핵심 적대 / 황색 수호사제; 쇼거스와 정면 교전 가능한 높은 전투 위상 유지.
- Dabin: 자신의 몸과 미래를 선택할 권리.
- Jumin: 치료 가능성보다 당사자 동의·현재 환자 우선.
- Elliott: 반복 실패와 애정 때문에 타인의 미래를 대신 고정하려는 비극적 반례.
- D01: `의뢰인 → 브로커/오래된 연락 노드 → 전문 회수팀`; 최상위 client/hierarchy는 bounded ambiguity.
- D02: 교차회차 사진은 확정 미래가 아닌 실제 non-current evidence.
- D03: 다른 회차 세 시신은 명시적 사건 전까지 물리적 경찰 증거.
- 백은검: 귀속 미정·공동봉인; 반응/형상변화는 후계 인증 아님.
- Alice Carter 한국어 정본 표기: `엘리스`.
- POV: Scene-Locked Hybrid; scene-internal head hopping 금지.

## 6. current production prefix 001–035 readback

- 001–020: 이전 bounded pass Green 상태 유지.
- 021–025: 배수로 탈출→정찰→한 박자 선택 규칙→쇼거스 전면 압력으로 current continuity를 잇는다.
- 026 `네 책임은 지금`: 엘리스는 이 장면에서 쇼거스를 직접 정신조작하지 않고 책임을 재판단하게 한다. 이는 능력상 정신조작이 불가능하다는 뜻이 아니다. 탈론은 핵심 적대 전투 위상을 화면에서 증명한다.
- 027 `친구가 적진에 있었다`: 밀리는 남성 현재 몸으로 재등장하고, 하템은 별도 여성 인물로 이안을 지키다 사망한다.
- 028 `편해져도 된다는 말`: 사후 하템은 이안의 환각/기억이며 새 정보를 주지 않는다. 엘리스는 허락 후 경계 지원만 한다.
- 029 `친구를 막는 법`: 이안은 사람을 직접 쓰러뜨리기보다 의식 연결을 최소비용으로 끊고, 밀리와 친구였던 과거/현재 적대를 동시에 보존한다.
- 030 `폭풍을 걷는 자`: 밀리의 storm-walk와 쿠바라 창의 연결 절단을 관찰하지만 기원·전체 기능·소유권은 미확정으로 둔다.
- 031 `창을 잡는 사람`: 주안은 쿠바라의 이동을 막는 목표를 선택하고 엘리스는 필요 때문에 창을 사용하되 자동 소유권을 주장하지 않는다. 밀리는 최종 전투에서 사망한다.
- 032 `전장 전체가 몸이었다`: 쇼거스 분열과 다중 핵 구조를 관찰하고 반복 가능한 공략의 첫 근거를 확보한다.
- 033 `괴물이 되어야 합니다`: 주안은 위험한 자가변형을 스스로 선택하고 이름·장소·목표 확인으로 자기결정을 회수한다.
- 034 `핵은 붉었다`: 핵 노출·이동 제한·파괴를 반복 가능한 전술로 정리하며, 강해진 육체의 미확인 위험을 별도로 남긴다.
- 035 `완전 소 생물`: 주안·엘리스·이안·아킴의 협업으로 쇼거스 핵을 소진한다. 세실리아는 생존 상태로 노출되며, 왜 쇼거스 안에 있었는지는 아직 미확정이다.

## 7. current migration boundary

```yaml
left_current: 35
right_legacy: 36
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

Ch30→31 current continuity는 PASS다. 새 fail-closed 경계는 Ch35→36이며 Ch36은 별도 pass 전까지 legacy tail이다.

## 8. 실행 순서

마지막 production frontier 변경은 PR #50 병합이다.

`exact user-source extraction → latest Canon conflict scan → boundary 검증 → manuscript/index/outline/cards/registry/routers 동시 갱신 → 5× adversarial review → exact-head CI → review thread 0/main freshness → squash merge → receipt closure → Notion sync`

다음 bounded unit은 같은 사용자 지정 `031–040` 원본의 `036–040`이다. `101–105`는 원본이 제공되기 전 자동 보충 금지다.
