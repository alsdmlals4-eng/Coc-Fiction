# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-29

## Resume-first

이 문서는 재개용 live router다. 저장된 SHA를 영구 최신 포인터로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
workspace: REPOSITORY_ONLY_CURRENT
workspace_policy: docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md
frontier_observed_at_main: 1de8beef60612ecc8113b4d7b8146ba7733d96d6
last_frontier_change_pr: 61
pending_frontier_change_pr: null
current_state_receipt: docs/fiction-ops/CURRENT_STATE_RECEIPT.json
source_manifest: docs/fiction-ops/2026-08-24_USER_SOURCE_CHUNK_MANIFEST.json
current_bundle_source: 폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx
current_bundle_source_sha256: 84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496
delivery_state: QA_VERIFIED
delivery_evidence_ceiling: AUTOMATED_AND_REPOSITORY_ONLY
repository_promotion_state: CLOSED_THROUGH_055
reconciled_prefix_end: 55
legacy_tail_starts_at: 56
boundary_after_chapter: 55
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/056-060.md
manuscript_promotion_state: PAUSED_UNTIL_EXPLICIT_RESUME
source_coverage_gap: 101-105
```

재개 순서:

```text
latest main
→ open PR
→ AGENTS.md
→ repository autonomy policy
→ CURRENT_STATE_RECEIPT
→ ACTIVE_CONTEXT
→ HANDOFF
→ CANON_REGISTRY
→ SCENE_PASS_REGISTRY
→ source manifest
→ exact next bundle
```

## Current stop point

- PR #61: Bridge Ch051–055 bounded promotion, merged 2026-08-24.
- frontier merge: `1de8beef60612ecc8113b4d7b8146ba7733d96d6`.
- source: `폭풍의눈_2차퇴고_제051-060화_기억외갑_선택회수_가독성강화본(1).docx`.
- source SHA-256: `84ad0be254a8c4faedb89f2dd9f8433143eaabfef1bc6ff57db1b418e0036496`.
- current production prefix: `001–055`.
- fail-closed boundary: `055→056`.
- next bounded bundle after explicit resume: `056–060`.
- Part 1 main conflict: `001–040`.
- Aftermath & 8-year Bridge: `041–066`.
- Part 2 entry: `067+`.
- source gap `101–105`: `SOURCE_NOT_PROVIDED`.
- whole-manuscript continuity: `NOT_YET_CLAIMED`.

2026-08-29 정책 교정은 PR #61의 미종결 receipt/router만 닫았으며 원고 frontier를 새로 이동시키지 않았다. 현재 manuscript promotion은 paused 상태다.

## Workspace and source authority

```text
latest user decision
→ AGENTS.md
→ repository autonomy policy
→ bounded reconciled GitHub production canon
→ user-designated per-range source DOCX
→ registries / manuscript / exact tests
→ adopted Base owner
→ historical migration or external reference
```

- GitHub repository가 current human/structured/manuscript/evidence owner다.
- 과거 Notion summary/Event/Relation/page/database/attachment는 `HISTORICAL_MIGRATION_REFERENCE_ONLY`다. current sync/readback/completion target이 아니다.
- source authority는 automatic production authority가 아니다.
- derived integrated candidate는 cross-check only다.

## Resume gate

프로젝트가 명시적으로 재개되기 전에는 Ch056–060 본문·consumer를 변경하지 않는다.

재개 후 첫 bounded unit:

```text
fiction/manuscript/part-1/056-060.md
→ exact source/body receipt
→ latest direct-user Canon conflict scan
→ Ch055→056 and Ch060→061 boundary check
→ manuscript + index + reverse outline + scene cards + registry + routers
→ targeted current research when material
→ production feasibility judgement
→ minimum five adversarial-review loops
→ exact-head Fiction operating-system CI
→ review thread 0 / main freshness
→ permitted merge
→ new main + repository destination readback
→ successor receipt/context
```

Notion sync/readback은 Gate가 아니다.

## Long-term Canon locks

- Central question: 선의·보호·사랑이 타인의 선택을 빼앗을 권리를 주지 않는다.
- Jooan: `반응 → 멈춤 → 이유 → 선택`.
- Elise: 인간을 포함한 정신 대상의 인지·판단·행동을 조작할 수 있다. 선택 보존은 능력 제한이 아니라 윤리·자기규율이다.
- Ian: observation → hypothesis → verification → record; unknown은 사실로 승격하지 않는다.
- Milly: male; Miskatonic female presentation은 Hatem 외형을 이용한 disguise/social perception이다.
- Hatem: female; default black-mask cultist; Ch27 physical death; 이후 새 객관 정보 없는 hallucination/memory only.
- Talon: Part 1 core antagonist; high on-screen combat competence.
- D01 bounded external acquisition network.
- D02 +2h photo는 authentic non-current cross-loop evidence, not fixed future.
- D03 other-loop three corpses는 명시적 변경 전 물리적 경찰 evidence.
- Elliott/silver sword ownership unresolved / jointly sealed; reaction·shape change is not successor certification.
- Alice Carter 한국어 정본: `엘리스`.
- POV: Scene-Locked Hybrid.

## Automation / learning

승인 범위 안의 fresh-read, source receipt, Canon scan, research, bounded propagation, exact checks, readback, 가역적 교정, remaining-work recalculation은 routine 재승인 없이 수행한다.

학습은 모델의 임의 영구 기억이 아니라 다음 repository loop다.

```text
problem
→ root cause
→ bounded fix
→ exact verification
→ regression guard
→ project owner / handoff
→ broadly reusable할 때 Base promotion candidate
```

사용자는 작품 중심 의미·Canon, 최종 Visual lock, 외부 공개·비용·권리, 되돌리기 어려운 삭제·renumbering·migration만 결정한다.

## 금지

- paused 상태에서 Ch056–060을 자동 promotion하지 않는다.
- old-head Green을 current-head Green으로 재사용하지 않는다.
- source authority를 자동 production authority로 승격하지 않는다.
- `101–105`를 파생 자료로 자동 보충하지 않는다.
- 다른 workstream의 open/draft/ready PR을 수정하지 않는다.
- 자동 검사 PASS를 whole-manuscript continuity, reader experience 또는 publication readiness로 확대하지 않는다.
