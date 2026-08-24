# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-24

## Resume-first

이 문서는 재개용 live router다. 저장된 SHA를 절대 최신값으로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
frontier_observed_at_main: null
last_frontier_change_pr: 50
pending_frontier_change_pr: 55
current_state_receipt: docs/fiction-ops/CURRENT_STATE_RECEIPT.json
source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx
current_bundle_source_sha256: 89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10
delivery_state: QA_VERIFIED
repository_promotion_state: PARTIAL
reconciled_prefix_end: 40
legacy_tail_starts_at: 41
boundary_after_chapter: 40
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/041-045.md
source_coverage_gap: 101-105
```

`frontier_observed_at_main: null`은 PR #55가 아직 pending candidate임을 뜻한다. 마지막 실제 main frontier 변경은 PR #50의 `001–035`이며, PR #55 병합 전 `001–040`을 main production으로 부르지 않는다.

재개 순서:
`latest main → open PR → AGENTS → CURRENT_STATE_RECEIPT → ACTIVE_CONTEXT → HANDOFF → CANON_REGISTRY → SCENE_PASS_REGISTRY → USER_SOURCE_CHUNK_MANIFEST → next bounded bundle`

## 현재 상태

- PR #42: Ch021–025 bounded promotion merged.
- PR #47: `탈론=핵심 적대`, `밀리=남성/미스캐토닉 여성 위장`, `하템=여성/기본 가면` Canon merged.
- PR #48: Ch026–030 user-source bounded promotion merged.
- **PR #50: Ch031–035 user-source bounded promotion merged.**
- **PR #55: Ch036–040 user-source bounded promotion pending candidate.**
- main production prefix: `001–035`; pending candidate prefix: `001–040`.
- candidate fail-closed boundary: `40→41`.
- next bundle after PR #55 merge: `041–045` from the user-designated 041–050 source.

## Source authority

1. 최신 사용자 직접 결정
2. 구간별 사용자 지정 `폭풍의눈_2차퇴고_...` DOCX
3. bounded reconciliation을 통과한 GitHub production canon
4. Notion 승인 요약/Event/Relation
5. 파생 통합본/Legacy

이전 `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`는 derived cross-check only다. 현재 사용자 source set에는 `101–105`가 없으므로 자동 보충하지 않는다.

## Ch026–035 보호 readback

- Ch25→26, Ch30→31: current continuity PASS.
- Ch26: 엘리스는 이 장면에서 쇼거스를 직접 정신조작하지 않고 질문/책임으로 자기 판단을 바꾸게 한다. 이는 엘리스에게 인간·비인간 정신조작 능력이 없다는 뜻이 아니다. 탈론은 쇼거스 다수를 정면 상대하는 core antagonist 위상.
- Ch27: 밀리는 남성 현재 몸으로 재등장. 하템은 별도 여성 인물로 이안을 보호하다 육체적으로 사망.
- Ch28: 사후 하템은 환각/기억이며 새 정보 제공 금지. 엘리스는 이안 허락 후 정신 경계 지원만 한다.
- Ch29: 이안/밀리는 친구였던 과거와 현재 반대편 행동을 동시에 유지. 주안은 몸이 창을 원한다는 이유로 창을 잡지 않는다.
- Ch30: 밀리 storm-walk, 쿠바라 창의 연결 절단을 관찰하지만 기원·전체 기능·소유권은 확정하지 않는다.
- Ch31: 주안은 쿠바라를 죽이는 대신 이동을 막고, 엘리스는 창을 필요에 따라 사용하되 자동 소유권을 주장하지 않는다. 밀리와 하템은 별개의 인물·별개의 죽음이다.
- Ch32: 쇼거스 다중 핵 공략 단서를 확인. 엘리스의 행동 명령은 D04와 정합하며 인간 대상 조작 가능 범위를 삭제하지 않는다.
- Ch33: 주안의 위험한 변형은 자기선택이며 이름·장소·목표 확인 절차를 유지한다.
- Ch34: 붉은 핵의 노출·제한·파괴를 반복 가능한 공략으로 정리한다.
- Ch35: 4인 협업으로 쇼거스 핵을 소진하고 세실리아를 생존 상태로 노출한다. 세실리아가 쇼거스 안에 있었던 원인은 아직 미확정이다.

## Current migration truth

```yaml
left_current: 40
right_legacy: 41
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

PR #55 candidate에서 Ch35→36은 exact source와 consumer 검증으로 연결되며, 새 fail-closed candidate 경계는 Ch40→41이다. main은 PR #55 병합 전까지 001–035 production이다.

## 다음 정확한 작업

현재: PR #55 exact-head validation → review thread 0 → main freshness → squash merge.

병합 뒤: `fiction/manuscript/part-1/041-045.md`를 사용자 지정 `041–050` 원본으로 bounded promotion한다.

## 장기 보호 Canon

- central question: 선의·보호·사랑이 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 인간을 포함한 정신 대상의 인지·판단·행동을 조작할 수 있다. 외부 정신간섭 차단·환각 필터도 가능하다. 선택 보호는 능력의 한계가 아니라 사용 방식에 대한 자기규율이다.
- Ian: unknown을 사실로 승격하지 않음.
- Milly: male; Miskatonic female disguise uses Hatem's appearance.
- Hatem: female; default black-mask cultist; Ch27 death, later no-new-info hallucination only.
- Talon: Part 1 core antagonist; high on-screen combat competence.
- D01/D02/D03 및 sword 공동봉인 규칙 유지.
- Alice Carter 한국어 정본은 `엘리스`.
- POV는 Scene-Locked Hybrid.

## 금지

- old-head Green을 current-head Green으로 재사용하지 않는다.
- source authority를 자동 production authority로 승격하지 않는다.
- verified frontier를 validation 없이 이동시키지 않는다.
- `101–105`를 파생 자료로 자동 보충하지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
