# 저장 원고 구조 역개요 보고서

상태: **ACTIVE / COMPOSED BASELINE + APPROVED OVERRIDES / MIXED MIGRATION**  
갱신: 2026-08-20

## 1. 데이터 구조

- 고정 기준선: `analysis/baselines/`
- 승인 변경: `MANUSCRIPT_INDEX_OVERRIDE_*.json`, `REVERSE_OUTLINE_OVERRIDE_*.json`
- 활성 manifest: `MANUSCRIPT_INDEX.json`, `REVERSE_OUTLINE_001_225.json`
- 유일한 합성 소비자: `tools/fiction_composed_data.py`
- migration 상태: `analysis/SCENE_PASS_REGISTRY.json#/external_artifact_reconciliation`

baseline은 과거 활성 원고가 아니라 immutable 기계 기준선이다. 현재 값은 manifest가 승인 override를 합성한 결과다.

## 2. 완료 override

- `001–005`: current source/canon reconciliation
- `006–010`: QA_GREEN current candidate 적용 + Ch10→11 current continuity 복구
- `011–015`: QA_GREEN current candidate 적용 + Ch15→16 current continuity 복구
- `016–020`: QA_GREEN current candidate 적용 + Ch20→21 current continuity 복구
- `021–025`: QA_GREEN current candidate 적용 + **Ch25 migration boundary**
- `026`: legacy-tail boundary override
- `091–095`: 역사적 원본 직접 대조 source pass

## 3. 현재 분석값의 증거 한계

이 보고서는 **mixed migration 상태의 GitHub 저장 원고**를 설명한다. `001–025`는 current candidate와 대조된 branch-verified production prefix이지만, 제26화 이후 stored chapter는 자신의 reconciliation을 통과하기 전까지 최신 external narrative와의 연속성을 주장할 수 없다.

자동 evidence와 structural flag는 탐색 단서다. 원본·Canon·수동 장면 카드보다 우선하지 않으며 자동 수정 명령으로 사용하지 않는다.

## 4. 부·외전별 정량 기준선

- 기존 파일 경로 기준: 1부 70화, 외전1 25화, 외전2 35화, 외전3 35화, 2부 60화의 총 225 stored chapter.
- 45개 저장 묶음과 각 stored chapter의 최소 분량 검사는 합성 색인과 원고를 함께 본다.
- 이 숫자를 current 001–161 narrative의 부별 화수나 publication 편성으로 재해석하지 않는다.

## 5. 전체 구조 지도

```yaml
current_revision_input: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_revision_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
reconciled_prefix_end: 25
legacy_tail_starts_at: 26
boundary_after_chapter: 25
whole_manuscript_continuity: NOT_YET_CLAIMED
```

- 저장소는 225화·45개 묶음 토폴로지를 migration container로 유지한다.
- **225화 저장 토폴로지는 최신 narrative numbering의 publication 편성 선언이 아니다.**
- Ch5→6, Ch10→11, Ch15→16, Ch20→21은 current continuity로 정상 연결한다.
- Ch20은 current Ch21로 정상 연결한다.
- Ch25는 `RECONCILIATION_MIGRATION_BOUNDARY`; 합성 역개요에서 `next_chapter=null`이다.
- stored Ch26은 `LEGACY_TAIL_BOUNDARY`; current Ch25를 자신의 정상 previous chapter로 자동 주장하지 않는다.
- repository generator가 frontier 25 상태에서 Ch20–26을 재생성했고, Ch20/Ch21–25/Ch26 override는 current body/index 및 fail-closed boundary와 맞춘다.
- `091–095` source-pass 및 과거 저장 편성 검증은 역사적 증거로 보존한다.
- Ch26+는 자신의 bounded reconciliation 전까지 current narrative 연속성을 주장하지 않는다.

## 6. Finding-first 판정

### RESOLVED

- 과거 5→6 migration boundary는 Ch6–10 current promotion으로 제거됐다.
- 과거 10→11 boundary는 Ch11–15 current promotion으로 제거됐다.
- 과거 15→16 boundary는 Ch16–20 current promotion으로 제거됐다.
- 과거 20→21 boundary는 Ch21–25 current promotion으로 제거됐다.

### ACTIVE BOUNDARY

- 새 fail-closed 경계는 **25→26**이다.
- QA_GREEN 001–161 artifact 존재만으로 Ch26+ production authority를 자동 승격하지 않는다.

### KEEP HISTORICAL EVIDENCE

- `001–005` reconciliation
- `006–010` bounded promotion
- `011–015` bounded promotion
- `091–095` 원본 source pass
- representative pilots

위 증거는 수행 당시 범위의 실제 검증이다. 인접 legacy chapter로 자동 확대하지 않는다.

### REJECTED

- QA_GREEN 001–161 파일이 존재한다는 이유로 21–161을 GitHub production authority로 한 번에 승격.
- 225 stored topology를 current narrative numbering보다 높은 정본으로 간주.
- 자동 역개요 플래그를 원고 수정 명령으로 사용.

## 7. 보호 범위

- 원본 사건·최신 사용자 Decision·Canon이 파생 역개요보다 우선한다.
- migration boundary 밖 legacy tail을 current narrative의 정상 다음 화로 자동 해석하지 않는다.
- 저장 토폴로지와 narrative numbering을 분리한다.
- 주안의 반응적 보호는 복종·소유 증거가 아니다.
- 엘리스의 보호는 상대 선택을 보존하는 방향을 유지한다.
- 하템과 밀리는 별도 인물이며 same-face는 동일인 증명이 아니다.
- 이안의 관찰 → 가설 → 검증 → 기록 순서를 유지한다.
- Ch20은 지도 확보 성공과 잠입 실패를 함께 기록한다.

## 8. 검증 상태

exact HEAD에서 다음을 함께 검증한다.

- composed manuscript index ↔ 실제 body chars/SHA
- active Canon/manuscript
- reverse-outline reproducibility 225 chapters
- reverse-outline analysis
- completed Scene Pass registry
- current boundary `25→26`
- next bounded bundle `026–030`

과거 Green을 현재 Green으로 재사용하지 않는다.

## 9. 다음 정확한 작업

현재 운영 순서는 `ACTIVE_CONTEXT.md`와 `SCENE_PASS_REGISTRY.json`을 따른다.

1. 제1–25화 branch-verified prefix와 제25→26 migration boundary를 exact-head CI로 검증한다.
2. PR #42 Green/merge/readback 뒤 다음 묶음 `fiction/manuscript/part-1/026-030.md`를 QA_GREEN current candidate와 대조한다.
3. Ch25 종료 상태와 current candidate Ch26의 앞 경계를 먼저 확인하되 stored Ch26을 자동 current로 간주하지 않는다.
4. 원본·최신 Canon으로 `KEEP / APPLY / REWORK / REJECT`를 판정한다.
5. 승인된 delta가 생길 때 manuscript/index/reverse-outline override/Scene Pass Registry/Revision Report를 함께 갱신한다.
