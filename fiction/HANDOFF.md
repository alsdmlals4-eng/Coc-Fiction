# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-10

## 먼저 읽을 파일

1. `FICTION_MASTER.md`
2. `ACTIVE_CONTEXT.md`
3. `CANON_REGISTRY.json`
4. `SOURCE_MANIFEST.md`
5. `sources/PRIMARY_SOURCE_INVENTORY.md`
6. `analysis/SCENE_PASS_REGISTRY.json`
7. `analysis/SCENE_CARDS_001_005.md`
8. `reports/REVISION_2026-08-10_EXTERNAL_RECONCILIATION_001_005.md`
9. `analysis/REPRESENTATIVE_CHAPTER_GATES.md`
10. `analysis/REVERSE_OUTLINE_REPORT.md`
11. `MANUSCRIPT_INDEX.json`
12. `manuscript/part-1/001-005.md`
13. 다음 작업 대상 `manuscript/part-1/006-010.md`

## Resume-first 기준

```yaml
repository:
  default_branch: main
  last_observed_main_sha: 9a7b2e2419465bd76daf0cf09b96ed7c0cd7d54c
integration:
  last_merged_pr: 17
  merge_commit_sha: 9a7b2e2419465bd76daf0cf09b96ed7c0cd7d54c
verification:
  pr17_exact_head: 31a4d959cef54ad77576672ff7cca8a53db72c42
  pr17_exact_head_run: 31355669160
  pr17_exact_head_ci: PASS
  post_merge_run: 31355813027
  post_merge_ci: PASS
```

이 SHA는 마지막 검증 checkpoint다. 새 세션은 이 문서만 믿지 말고 `main`과 open PR을 먼저 다시 조회한다.

## 현재 완료 상태

- PR #13: Base/프로젝트 운영 통합 완료.
- PR #14: 최신 Canon synchronization 완료.
- PR #15~16: Base proposal locator와 post-merge continuation semantics 저장 완료.
- PR #17: **외부 최신 제1~5화 source/canon reconciliation 완료·병합.**
- 제1~5화의 manuscript, 합성 색인, 역개요 override, Scene Pass Registry, Scene Cards, Revision Report, 대표 게이트, 시작 문서가 함께 동기화됨.
- PR #17 merge 후 `main@9a7b2e24...` push workflow까지 `SUCCESS`.

## 현재 migration 상태

```yaml
external_artifact: 폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip
reconciled_prefix: 1-5
legacy_tail_starts_at: 6
boundary_after_chapter: 5
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bundle: fiction/manuscript/part-1/006-010.md
deferred_source_pass: fiction/manuscript/part-2/176-180.md
```

저장소의 225화·45묶음 구조는 **migration storage topology**다. 현재 최신 narrative numbering의 최종 화수표가 아니다. 새 제5화와 저장 구 제6화 사이에는 사건 되감기 위험이 있으므로 reverse outline의 정상 next/previous 연결을 끊었다.

기존 저장 `006-010`의 내부 연속성 검증은 실제 역사적 증거로 보존한다. 다만 외부 최신 제6~10화와의 정본 reconciliation을 대신하지 않는다.

## 제1~5화에서 확정한 작품 규칙

- 주안 판단: `반응 → 멈춤 → 이유 → 선택`.
- 주안–엘리스 관계를 일방 지시/따름으로 단순화하지 않는다.
- 엘리스는 주안에게 선택 이유를 돌려주는 쪽으로 기능한다.
- 제4화 흰 방의 정체는 현재 인물 지식상 확정하지 않는다.
- 신호기는 버튼 입력과 수신 진동만 사용한다. 위치·문자·통화 기능 없음.
- 제5화 침몰에서 이안의 구조 경로와 주안·탈론 경로를 분리한다.
- 최신 사용자 지시로 제외된 사건·인물축은 원본에 존재해도 자동 복원하지 않는다.
- 실제 POV는 장면 기능이 있을 때 명시적 경계로 전환한다. 작품별 수치를 Base 전역 규칙으로 승격하지 않는다.

## Base 상태

현재 재조회 Base main: `16af66ff51027f74193b60469e7c20281a1cade6`.

```yaml
base_proposal_012:
  id: BCP-2026-012-serial-fiction-canon-migration-debt
  pr: https://github.com/alsdmlals4-eng/Base/pull/234
  merged: true
  status: SUBMITTED
  this_project_action: REUSE_EXISTING_BCP

base_proposal_013:
  id: BCP-2026-013-post-merge-continuation-state-reconciliation
  pr: https://github.com/alsdmlals4-eng/Base/pull/235
  merged: true
  status: SUBMITTED
  this_project_action: REUSE_EXISTING_BCP

base_active_implementation:
  authority: NOT_GRANTED_IN_THIS_STAGE
  changed_by_this_cycle: 0
  next_stage: SEPARATE_FOLLOWUP_STAGE
```

이번 프로젝트의 새 finding은 위 BCP들로 이미 커버된다. Base에 중복 proposal을 만들지 않는다.

## 다음 작업자의 첫 행동

1. GitHub `main`, open PR, current Base main을 재조회한다.
2. `ACTIVE_CONTEXT.md`와 `SCENE_PASS_REGISTRY.json`의 migration 상태가 repo truth와 같은지 확인한다.
3. 외부 최신 **제6~10화** 실제 원고를 확보한다.
4. 저장 `fiction/manuscript/part-1/006-010.md`와 회차별 delta를 만든다.
5. 새 제5화의 종료 상태를 앞 경계로 둔다.
6. 원본 사건·최신 사용자 Decision·Canon을 우선해 `KEEP / APPLY / REWORK / REJECT`를 판정한다.
7. 승인된 원고 delta만 적용하고 index·역개요 override·Scene Pass Registry·Scene Cards·Revision Report를 같은 기준으로 갱신한다.
8. `reconciled_prefix_end=10`이 되기 전 제11화 이후를 최신 제10화의 정상 연속으로 자동 주장하지 않는다.
9. exact-head CI → 적대적 검토 → PR merge → post-merge push CI → continuation checkpoint 순으로 닫는다.

## 실패 시 금지

- old-head Green을 current-head Green으로 재사용하지 않는다.
- 외부 파일명의 `최종`만으로 blind overwrite하지 않는다.
- 구 저장 화 번호를 최신 narrative numbering보다 우선하지 않는다.
- duplicate override guard, content validator, reference freshness를 약화해 Green을 만들지 않는다.
- Base active Skill/Template/Test/Tool/Workflow를 이번 단계에서 구현하지 않는다.
