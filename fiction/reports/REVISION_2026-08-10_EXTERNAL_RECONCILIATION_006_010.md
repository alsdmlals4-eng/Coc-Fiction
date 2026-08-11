# Revision Report — External Canon Reconciliation 006–010

날짜: 2026-08-10  
정정: 2026-08-11

## Status correction

```yaml
source_canon_analysis: COMPLETE_FOR_BUNDLE
candidate_external_body_checked: YES
production_manuscript_integrated: NO
manuscript_index_propagated: NO
reverse_outline_propagated: NO
scene_pass_registry_propagated: NO
migration_boundary_advanced: NO
verified_prefix_end: 5
legacy_tail_starts_at: 6
next_bundle: fiction/manuscript/part-1/006-010.md
completion_claim: NOT_ALLOWED
```

PR #19에서 제6~10화의 source/canon 비교 카드와 검증 아이디어는 작성됐지만, 최종 merge에는 **승인 후보 본문 `006-010.md` 교체와 그에 따른 index / reverse outline / Scene Pass Registry 전파가 포함되지 않았다.** 따라서 당시 보고서의 `5/5 APPLY → boundary 10→11 이동` 문장은 production 완료 증거로 사용할 수 없다.

현재 GitHub production은 제1~5화까지만 외부 최신 artifact와 검증된 prefix이고, 제6화부터는 legacy tail이다. 이 보고서는 **제6~10화의 source/canon 분석 증거와 다음 원고 migration 입력**으로만 사용한다.

## Source authority

```text
최신 사용자 Decision
→ Google Drive 실제 원본 로그/문서 및 원본사건감사
→ 현재 승인 외부 원고 artifact
→ 구 225화 전체 압축본은 비교자료
→ 구형 기획/archive
```

- 외부 원고 artifact: `폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip`
- 해당 묶음의 원본 기능은 `원본사건감사` 및 등록 source evidence의 3~4일차 사건과 대조했다.
- 구 225화 전체 압축본은 사건 기능·동선 비교에만 사용하며 원본보다 높은 권위를 갖지 않는다.
- 원본 전수 감사는 계속 `IN_PROGRESS`이며 이 보고서는 제6~10화 묶음만 다룬다.

## Source-function finding

외부 최신 제6~10화 후보는 다음 원본 기능을 현행 5화 이후에 이어 붙이는 방향으로 분석됐다.

| 후보 화 | 중심 사건 기능 | source-function 판정 |
|---|---|---|
| 제6화 `따뜻한 피난처` | 엘리스·이안 해안 생존/검증 + 주안 감옥·탈론 분리선 | `APPLY_CANDIDATE` |
| 제7화 `죽은 척해야 사는 곳` | 시체 절벽·납치 생존자·죽은 척 생존·동굴 진입 | `APPLY_CANDIDATE` |
| 제8화 `같은 편은 아닙니다` | 황색과 주민의 분리, 밀리 재회, 주안 감옥 탈출축 | `APPLY_CANDIDATE` |
| 제9화 `카터라는 이름` | 카터 가문과 섬의 과거 연결, 친구/안전 판단 분리 | `APPLY_CANDIDATE` |
| 제10화 `친구를 쏜 날` | 밀리 배신·이안 총격·첫 소멸/사망 오인 | `APPLY_CANDIDATE` |

이 판정은 **내용 선택 판정**이지 GitHub production 적용 완료 판정이 아니다.

## 2026-08-11 candidate artifact recheck

현재 업로드된 제006~010 DOCX를 다시 열어 로컬 통합 Markdown 후보와 모든 비어 있지 않은 본문 문단을 순서대로 비교했다.

```yaml
docx_paragraph_equality: 5/5 chapters MATCH
candidate_markdown_body_sha256:
  6: b22b54836e90bead8aa73c1cc5ed4bc0eb04edd3a2356effd9dd01ddcbffa28d
  7: d991ff8481d855a29502e81a40f55dfb803861b75640c0f15da0565a840711fd
  8: f2bc5ba78142e322df50da7dc8d19da5b0ab4bc27ed46ef1714f60b2f59981a6
  9: 9ff6f3aaf179aa37dc3aacb108b4af94aff5fa4c4b201ee30941f9604541fd28
  10: 279bae4d9a099f4f7564087c30af0973119cf003f373c51b002b65eef59c1dc9
```

이 SHA들은 **candidate Markdown body**의 증거이며 현재 GitHub production SHA가 아니다. 실제 migration 때 production Markdown 형식이 달라지면 body SHA를 그 형식으로 다시 계산하고, 같은 commit 범위에서 index·reverse outline·Scene Pass Registry를 함께 갱신해야 한다.

## Why production was not advanced in this correction

현재 작품 작업 순서는 다음과 같이 승인돼 있다.

```text
캐릭터 정본
→ 주요 사건/하이라이트
→ 복선·정보 구조
→ 전체 본문 퇴고
```

이번 2026-08-11 작업의 주 범위는 캐릭터 Canon과 캐릭터/상대 위상 정규 Skill 반영이다. 과거 PR의 누락을 발견했다는 이유로 본문 bundle을 즉석에서 덮어쓰지 않는다. 제6~10화 production migration은 별도 atomic pass에서 수행한다.

## Required atomic migration for 006–010

다음 pass에서 아래가 한 변경 범위로 모두 Green이어야 한다.

1. 업로드된 최신 DOCX에서 제6~10화 production body 재추출/검증
2. Google Drive 원본·원본사건감사와 사건 결과·정보 시점·관계 변화 재대조
3. `fiction/manuscript/part-1/006-010.md` 교체
4. `MANUSCRIPT_INDEX_OVERRIDE_006_010.json` 전 5화 SHA/POV/title 갱신
5. `REVERSE_OUTLINE_OVERRIDE_006_010.json` 및 5→6 / 10→11 boundary 갱신
6. `SCENE_PASS_REGISTRY.json` verified prefix를 10으로 이동
7. Scene Card·Revision Report를 production SHA에 다시 pin
8. `check_fiction_content.py`, `check_fiction_reverse_outline.py`, `check_fiction_scene_passes.py` 모두 Green
9. 그 뒤에만 `reconciled_prefix_end: 10`을 주장

## Current truthful state

```text
verified external-production prefix = Ch1-5
migration boundary = Ch5 → legacy Ch6
Ch6-10 = source/canon analyzed candidate, NOT integrated production
whole-manuscript continuity = NOT_YET_CLAIMED
next production migration = Ch6-10
```
