# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-20

## Resume-first

이 문서는 재개용 live router다. 저장된 SHA를 절대 최신값으로 믿지 않는다.

```yaml
resume_rule: FETCH_LATEST_MAIN_BEFORE_USE
state_observed_at_main: b9d4523eb2c057215948598aa74beb451a0b5a67
work_mode: IMPLEMENT / REVIEW
open_project_prs_observed_before_branch: 0
self_merge_sha_required_in_file: false
```

새 세션은 반드시 `Coc-Fiction main → open PR → ACTIVE_CONTEXT → 이 HANDOFF → SCENE_PASS_REGISTRY → current candidate manifest/QA` 순으로 fresh-read한다.

## 현재 authority

```yaml
current_candidate: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_candidate_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
delivery_state: QA_VERIFIED
candidate_state: QA_GREEN
repository_promotion_state: PARTIAL
candidate_coverage: [1, 161]
reconciled_prefix_end: 15
legacy_tail_starts_at: 16
boundary_after_chapter: 15
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle_if_resumed: fiction/manuscript/part-1/016-020.md
```

`delivery_state`와 `repository_promotion_state`를 자동으로 동일시하지 않는다. 외부/통합 candidate가 Green이어도 GitHub production authority는 bounded reconciliation이 Green인 범위까지만 이동한다.

## 2026-08-20 implementation chain

- PR #29: Canon reconciliation merged.
- PR #30: 17-file current-candidate manifest + hashes merged.
- PR #31: 001–161 integrated working candidate QA_GREEN evidence merged.
- PR #32: current Ch006–010 bounded promotion merged; frontier 10→11까지 검증.
- current work: Ch011–015 bounded promotion. TDD RED는 closed-unmerged PR #34 / run `32331920404`에서 의도한 scene-pass contract failure로 확인.
- reverse-outline current Ch10–16 구조는 closed-unmerged diagnostic PR #35의 repository generator 출력으로 exact readback 후 override에 반영.

## Current prefix 001–015 protection

- Ch5→6, Ch10→11은 current continuity다.
- Ch11: 주안은 하템·아킴과 협력하지만 협력/신뢰/도덕 동의를 분리한다.
- Ch12: 하템은 밀리와 같은 얼굴을 가졌어도 별도 인물이다. 밀리 생존은 증언 수준에서 남긴다.
- Ch13: 윌리엄의 과거 죄를 엘리스에게 상속시키지 않는다.
- Ch14: 엘리스 보호 자아는 외부 존재가 아니라 같은 자아의 보호적 부분이다.
- Ch15: 데이비드와의 거래는 신뢰가 아니라 조건이 명시된 협상이다.
- current fail-closed boundary는 **Ch15→16**이다. legacy Ch16의 adjacent numbering을 current continuity 증거로 사용하지 않는다.

## Canon protection

- 중심 질문: 선의·보호·대의도 타인의 선택권을 자동으로 가져오지 않는다.
- 주안: `반응 → 멈춤 → 이유 → 선택`.
- 엘리스: 정신 능력은 지배가 아니라 외부 간섭 차단·선택 보존.
- 이안: 관찰·가설·검증·기록. 모르는 것은 모른다고 남긴다.
- 다빈: 자기 몸과 미래의 결정권.
- 주민: 치료 최적화보다 당사자 동의·현재 환자 우선.
- 엘리엇: 더 많이 안다는 이유로 타인의 미래를 대신 고정하는 비극적 반례.
- D01: 경계형 외부 회수망 `의뢰인 → 브로커/오래된 연락 노드 → 전문 회수팀`; 최상위 client/hierarchy 미확정.
- D02: +2h 사진은 fixed future가 아닌 authentic non-current cross-loop evidence.
- D03: 다른 회차 세 시신은 명시적 사건 전까지 물리적 경찰 증거.
- 백은검: 귀속 미정·공동봉인; 주민 반응/메스 변형은 후계 인증이 아니다.
- Alice Carter 한국어 정본 표기: `엘리스`.
- POV: Scene-Locked Hybrid.

## 다음 정확한 작업

Ch011–015 promotion이 exact-head CI + merge + post-merge readback까지 Green이면 다음은:

```text
fiction/manuscript/part-1/016-020.md
→ current candidate 016-020 추출
→ Ch15→16 경계 대조
→ Canon/source/readability 검증
→ manuscript + index + outline + scene pass + routers 원자 갱신
→ exact-head CI
→ squash merge
→ frontier 20→21 post-change readback
```

## 운영 금지

- open/draft/ready PR을 다른 후속 작업의 수정 대상으로 삼지 않는다.
- old-head Green을 current-head Green으로 재사용하지 않는다.
- 외부 파일명 `최종`만 보고 blind overwrite하지 않는다.
- verified frontier를 validation 없이 이동시키지 않는다.
- generator/validator를 약화해 Green을 만들지 않는다.
- `whole_manuscript_continuity`를 mixed migration 중 임의로 PASS 처리하지 않는다.
- Base adoption pin은 Base main이 바뀌었다는 이유만으로 자동 advance하지 않는다.
