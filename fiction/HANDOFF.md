# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-12

## Resume-first

이 문서는 재개용 live router다. 저장된 SHA를 절대 최신값으로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
state_observed_at_main: 0ef8161f918eeb4b951fd6de38f8f7c512274a4d
last_integrated_pr: 24
work_merge_main_sha: 0ef8161f918eeb4b951fd6de38f8f7c512274a4d
open_project_prs_observed: 0
handoff_cycle_branch: ops/rift-accord-handoff-20260812
self_merge_sha_required_in_file: false
```

새 세션의 첫 행동은 반드시 `Coc-Fiction main → open PR → ACTIVE_CONTEXT → 이 HANDOFF → current Base main/open proposal PR` 순으로 fresh-read한다.

## 먼저 읽을 파일

1. `fiction/ACTIVE_CONTEXT.md`
2. `fiction/CANON_REGISTRY.json`
3. `fiction/bible/04_PART2_STORY_BIBLE.md`
4. `docs/fiction-ops/2026-08-12_RIFT_ACCORD_DELIVERY_MANIFEST.md`
5. `docs/fiction-ops/2026-08-12_RIFT_ACCORD_SIDE_STORY_ADVERSARIAL_REVIEW.md`
6. `fiction/analysis/2026-08-11_GLOBAL_STORY_ARCHITECTURE_AUDIT.md`
7. `fiction/analysis/2026-08-11_GLOBAL_READER_KNOWLEDGE_MATRIX.md`
8. `fiction/analysis/2026-08-11_GLOBAL_FORESHADOW_PAYOFF_LEDGER.md`
9. `fiction/analysis/SCENE_PASS_REGISTRY.json`
10. `fiction/MANUSCRIPT_INDEX.json`
11. `skills/fiction-project-operations/SKILL.md`
12. bounded migration을 실제 재개할 때만 `fiction/manuscript/part-1/006-010.md`

## 현재 완료 상태

- PR #21: 캐릭터 개성·강적 위상 프로젝트 mode와 라르고 8년 교관/호감 Canon 반영·병합.
- PR #22: 최신 작법 벤치마크와 정보/선택/하이라이트/복선 Gate 반영·병합.
- PR #23: 전역 캐릭터·사건·하이라이트·복선·Reader Knowledge 구조 감사 잠금·병합.
- PR #24: **Rift Accord 제156~161화 설계, 최신 사용자 보정, 실행계획, 적대적 검토, 최종 외부 산출물 전달 매니페스트 병합.**
- PR #24 merge main `0ef8161f918eeb4b951fd6de38f8f7c512274a4d`의 post-merge `Fiction operating system`은 SUCCESS로 확인됐다.
- 이번 인수인계 사이클은 본문/Canon을 새로 쓰지 않고 운영 state와 학습 계약만 정리한다.

## 외부 산출물과 repository 승격 상태

### Rift Accord Ch156–161

```yaml
artifact: 폭풍의눈_2차퇴고_2부외전_제156-161화_Rift_Accord_협약완결본.docx
coverage: [156, 161]
sha256: f9ddf90970a4760652f9bbac21c315daa24a51b47a32bfccfd47ef22a865f8d5
delivery_state: DELIVERED
repository_promotion_state: PENDING
repository_evidence: docs/fiction-ops/2026-08-12_RIFT_ACCORD_DELIVERY_MANIFEST.md
```

### Ch146–155

```yaml
artifact: 폭풍의눈_2차퇴고_제146-155화_최종선택_후일담_가독성강화본.docx
coverage: [146, 155]
sha256: fc3e781772439b3d39f76f4510bebc4057eae9c67bfaaf0221cb024a187f60de
delivery_state: QA_VERIFIED
repository_promotion_state: PENDING
recovery: Library에서 실제 파일을 다시 찾아 001-161 통합 전에 해시/내용을 재확인한다.
```

**중요:** `DELIVERED`/`QA_VERIFIED`는 외부 산출물 자체 상태다. GitHub production manuscript 승격 완료를 뜻하지 않는다.

## Rift Accord 최종 회수

- 중심은 연애가 아니라 협약 자체의 이해관계·검증·관할·자율권·관리된 묵인·비상공동목표·탈퇴/인계다.
- 주안–앨리스: 재회 → 주안의 사과 → 현재 선택으로 고백. 화해는 시작됐지만 관계는 열린 상태다.
- 이안: 브루스 매시의 공식 대표 지위를 침범하지 않고 미스캐토닉 실무·검증·기록 축으로 협상에 참여한다.
- 하템 환각: `신규 정보 없음` 계약 유지.
- 라르고: `회의 중입니다.`와 `[규율]` 최초 공개 완료. 협상 결론을 강제하는 권력으로 쓰지 않는다.
- 다빈: `[잔재]`는 자유 회귀/확정 미래예지가 아니다.
- 주민: 은검→백은의 메스 최초 변형이 발생했지만 `귀속 미정`·공동보관 유지. 후계자 인증으로 만들지 않는다.
- 대균열: 하나의 Great Rift와 태평양 전선이 실제이며, 공개 설명은 불완전하다. DG가 과거 사건을 만든 것으로 소급하지 않는다.

## GitHub migration truth

```yaml
legacy_repository_role: migration storage topology
legacy_stored_chapters: 225
reconciled_prefix_end: 5
legacy_tail_starts_at: 6
boundary_after_chapter: 5
whole_manuscript_continuity: NOT_YET_CLAIMED
repository_promotion_state: PARTIAL
next_bounded_bundle_if_resumed: fiction/manuscript/part-1/006-010.md
deferred_source_pass: fiction/manuscript/part-2/176-180.md
```

- PR #19의 006~010 자료/보고는 역사적 증거지만 검증된 production promotion으로 세지 않는다.
- 새 제5화와 legacy tail 사이의 미검증 경계를 derived consumer가 정상 previous/next로 자동 연결하지 않는다.
- `006-010`은 삭제된 다음 작업이 아니다. **bounded migration 전략을 계속하기로 했을 때의 정확한 다음 단위**다.

## 다음 정확한 작업

사용자가 작품 작업을 재개하면 다음 순서가 기본 권장 실행 경로다.

1. latest `main`, open PR, Base main을 다시 조회한다.
2. Library/현재 대화 산출물에서 최신 재퇴고 **제001~161화 전체 artifact set**을 실제로 회수한다.
3. 배치 간 중복·누락·화수·제목·POV·해시를 대조해 `001-161` 통합 최종 후보를 만든다.
4. 통합 후보에 전역 적대적 검토와 machine/document QA를 수행한다.
5. 그 결과를 기준으로 GitHub promotion 전략을 재판정한다.
   - 안전하면 bounded reconciliation을 frontier `5→...` 방식으로 계속한다.
   - 전체 정본 구조를 새로 세우는 편이 더 안전하면 별도 migration design/plan을 만든다.
6. bounded 전략을 유지하면 첫 실제 작업은 `006-010` source/Canon reconciliation이다.
7. 어떤 전략이든 `DELIVERED`를 `PROMOTED`로 자동 승격하지 않는다.

현재 통합 `001-161` 단일 최종본은 **NOT_BUILT_IN_THIS_HANDOFF**다. 인수인계 때문에 작품 작업을 멈춘 것이므로 여기서 임의로 생성하지 않는다.

## 프로젝트 운영 개선 — artifact-promotion-gate

이번 사이클의 프로젝트 학습은 새 sixth Skill이 아니라 기존 `fiction-project-operations`에 흡수한다.

```yaml
mode: artifact-promotion-gate
states:
  delivery_state: DRAFT | QA_VERIFIED | DELIVERED
  repository_promotion_state: NOT_REQUIRED | PENDING | PARTIAL | PROMOTED
required_evidence:
  - artifact filename / coverage / sha256
  - authority and source
  - current repository topology
  - promotion target
  - verified prefix or scope
  - migration boundary / legacy debt
  - validation gate
  - next executable step
```

Registry trigger와 `tools/check_fiction_operating_system.py`가 이 mode/state handoff를 회귀검사한다.

## Base Existing Solution First / 동시 BCP 충돌 방지

2026-08-12 인수인계 preflight 관측:

```yaml
base_main_observed: 1d6cc79ae95ffb67ba4de618f010a6540fc6e02c
open_base_prs_observed_at_preflight: 0
project_adoption_pin: 7a49390bd840f5f5dc80fe661b44ad45e9ebeb7f
adoption_pin_auto_advanced: false
continuous_work_active: false
```

이번 프로젝트 교훈의 공용 부분은 새 BCP를 만들지 않는다.

```yaml
base_disposition: REUSE_EXISTING_BCP
reused:
  - BCP-2026-012-serial-fiction-canon-migration-debt
  - BCP-2026-017-serial-fiction-reconciliation-frontier-and-derived-continuity-guard
  - BCP-2026-013-post-merge-continuation-state-reconciliation
new_base_proposal_required: false
other_project_bcp_registry_entries_modified: false
other_project_branches_or_prs_modified: false
```

근거:
- BCP-012는 Canon 권위와 legacy migration 완료 상태를 분리한다.
- BCP-017은 verified prefix/frontier/legacy tail, candidate-vs-verified, external artifact의 자동 Canon 권위 금지를 이미 다룬다.
- BCP-013은 병합 뒤 live continuation state를 fresh repository truth와 다시 맞추는 lifecycle을 다룬다.
- 세 제안은 현행 Base Registry에서 `IMPLEMENTED` 상태다.

따라서 현재 Base에 같은 Goal의 새 proposal을 추가하면 중복이다. 다른 채팅에서 새 Base BCP가 생길 수 있으므로 **향후 Base write가 정말 필요해진 경우에만** latest Base main + open proposal-only PR + Registry + same-goal을 다시 조회한다.

## 최근 적용 가능한 교훈

### LESSON-COC-HANDOFF-001 — 외부 전달과 정본 승격 혼동

```yaml
symptom: 최종 DOCX는 완성·전달됐는데 GitHub legacy topology에는 아직 승격되지 않음
impact: 다음 세션이 같은 원고를 다시 쓰거나, legacy 원고를 최신 정본으로 오인할 수 있음
fast_recovery_steps:
  - artifact filename/coverage/hash 확인
  - delivery_state 확인
  - repository_promotion_state 확인
  - current verified frontier/migration boundary 확인
  - promotion 전 coupled consumer inventory 재조회
owner_source: skills/fiction-project-operations/SKILL.md#artifact-promotion-gate
knowledge_state: VALIDATED_PATTERN
```

### LESSON-COC-HANDOFF-002 — candidate frontier를 verified prefix로 오인

```yaml
symptom: 원고/파생자료 일부가 저장됐다는 이유로 reconciliation 완료 범위를 늘림
fast_recovery_steps:
  - declared validation gate 결과 확인
  - SCENE_PASS_REGISTRY와 actual manuscript/index/outline 상태 대조
  - Green이 아니면 verified frontier 유지
owner_source: Base BCP-017 + fiction/ACTIVE_CONTEXT.md
knowledge_state: VALIDATED_PATTERN
```

### LESSON-COC-HANDOFF-003 — Handoff 자신의 merge SHA 추적 무한루프

```yaml
symptom: closure PR 병합 뒤 그 merge SHA를 Handoff에 적기 위해 또 PR 생성
fast_recovery_steps:
  - state_observed_at_main과 historical merge evidence를 분리
  - closure PR 자체 merge SHA는 GitHub history에서 읽음
  - 다음 세션은 FETCH_LATEST_MAIN_BEFORE_USE
owner_source: Base BCP-013 / maintaining-project-context-and-handoff
knowledge_state: VALIDATED_PATTERN
```

## 실패 시 금지

- old-head Green을 current-head Green으로 재사용하지 않는다.
- 외부 파일명의 `최종`만으로 blind overwrite하지 않는다.
- 구 저장 화 번호를 최신 narrative numbering보다 우선하지 않는다.
- verified frontier를 validation 없이 이동시키지 않는다.
- duplicate override guard, content validator, reference freshness를 약화해 Green을 만들지 않는다.
- Base active Skill/Template/Test/Tool/Workflow를 BCP handoff 단계에서 수정하지 않는다.
- 다른 프로젝트의 BCP/Registry entry/branch/PR을 rename·rewrite·close·merge하지 않는다.
- `CONTINUOUS_WORK_ACTIVE`를 현재 세션에 기록하지 않는다. exact opt-in literal이 없었다.
