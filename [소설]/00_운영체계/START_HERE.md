# Coc-Fiction 소설 작업 시작 지점

## 최초 읽기

```text
docs/coordination/CONCURRENT_WORK.md
→ [소설]/00_운영체계/OPERATING_MODEL.md
→ fiction/FICTION_MASTER.md
→ docs/fiction-ops/CURRENT_STATE_RECEIPT.json
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ 현재 묶음 Scene Card·Revision Report
→ fiction/analysis/REVERSE_OUTLINE_REPORT.md
→ fiction/MANUSCRIPT_INDEX.json
→ fiction/STYLE_GUIDE.md
→ 현재 원고 묶음
```

`CURRENT_STATE_RECEIPT.json`의 SHA/PR은 production frontier가 마지막으로 바뀐 증거다. 저장소 최신값을 고정하는 포인터가 아니므로 실제 작업 전 최신 `main`과 open PR을 다시 조회한다.

색인과 역개요는 immutable baseline + 승인 bundle override를 합성한다. baseline을 직접 수정하지 않는다.

## 현재 단계

```yaml
work_mode: IMPLEMENT / REVIEW
manuscript_stage: REVISE / PROMOTE_BOUNDED
source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제031-040화_밀리최종_쇼거스결전_정치클라이맥스_가독성강화본(1).docx
current_bundle_source_sha256: 89fa4cdbd5e9037ed65e829b958783adaa00b363720e7d178e52426752d3da10
derived_cross_check_only: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
repository_candidate_prefix: 001-040
legacy_tail_starts_at: 041
whole_manuscript_continuity: NOT_YET_CLAIMED
last_frontier_change_pr: 50
pending_frontier_pr: 55
next_bundle_after_merge: fiction/manuscript/part-1/041-045.md
source_coverage_gap: 101-105
```

## Source authority

1. 최신 사용자 직접 결정
2. 사용자 지정 구간별 `폭풍의눈_2차퇴고_...` DOCX
3. bounded reconciliation을 통과한 GitHub production canon
4. Notion 승인 요약/Event/Relation
5. 파생 통합본·Legacy 분석

Source authority가 존재한다는 사실만으로 production authority가 되지 않는다. 각 5화 묶음은 exact body receipt·Canon conflict scan·consumer propagation·적대적 검토·exact-head CI를 통과해야 한다.

현재 source set에는 `101–105`가 없으므로 다른 자료에서 자동 보충하지 않는다.

## lifecycle vocabulary

- Work Mode: `PLAN → BUILD → REVIEW`
- Manuscript Stage: `DISCOVER → OUTLINE → DRAFT → REVISE → POLISH`
- 현재는 BUILD/REVIEW 안의 bounded promotion + REVISE 단계다.

GitHub 225화/45묶음 경로는 migration container이며 current narrative 최종 numbering 선언으로 사용하지 않는다.

## 현재 보호 규칙

- Alice Carter 한국어 정본은 `엘리스`.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise 정신 능력: 인간을 포함한 정신 대상의 인지·판단·행동을 조작할 수 있다. 외부 정신간섭 차단·환각 필터도 가능하다. 선택 보존은 능력의 한계가 아니라 사용 방식에 대한 자기규율이다.
- Ian: 기록·검증, unknown을 사실로 승격하지 않음.
- Milly: 실제 남성. 미스캐토닉에서는 하템의 여성 외형을 이용해 위장했기 때문에 `밀리 양`으로 인식됨.
- Hatem: 실제 여성. 기본 외형은 검은 가면의 광신도. Ch27 사망 뒤에는 새 정보 없는 환각/기억만 허용.
- Talon: Part 1 핵심 적대 / 황색 수호사제 / 높은 화면 안 전투 위상 유지.
- D01: bounded external acquisition network.
- D02: +2h 사진은 fixed future가 아닌 authentic non-current cross-loop evidence.
- D03: 다른 회차 세 시신은 명시적 사건이 바꾸기 전까지 물리적 경찰 증거.
- Elliott sword: 귀속 미정·공동봉인; 반응/형상변화는 후계 인증 아님.
- POV: Scene-Locked Hybrid; scene break 없는 head hopping 금지.

## current production prefix / migration boundary

- GitHub `main` production: `001–035` (PR #50).
- PR #55 pending candidate: `001–040`; 아직 main production 완료가 아니다.
- candidate continuity는 `035→036`까지 연결 검증됨.
- Ch40 reverse outline: `next_chapter=null`.
- legacy Ch41 reverse outline: `previous_chapter=null`.
- `040→041`: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.

## 현재 작업

현재 PR #55 후보 묶음:
`fiction/manuscript/part-1/036-040.md`

병합 후 다음 묶음:
`fiction/manuscript/part-1/041-045.md` · 사용자 지정 `041–050` source를 사용한다.

```text
Ch35→36 boundary verification
→ exact source Ch36-40 extraction
→ latest direct-user Canon conflict scan
→ manuscript/index/reverse-outline/Scene Pass/router propagation
→ 5× adversarial review
→ exact-head CI
→ review thread 0 / main freshness
→ squash merge
→ receipt closure + Notion readback
```

## 금지

- 구 저장 편성이나 파생 통합본을 user source authority로 되돌리지 않는다.
- source 파일명의 `최종`만으로 자동 승격하지 않는다.
- migration boundary를 정상 next chapter로 가정하지 않는다.
- `101–105`를 추론이나 다른 파일로 자동 보충하지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
- 과거 CI Green을 current exact head Green으로 재사용하지 않는다.
