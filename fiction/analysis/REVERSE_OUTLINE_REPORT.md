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

- `001-005`: current source/canon reconciliation, Ch5→6 continuity 재연결
- `006-010`: QA_GREEN current candidate 적용 + source/canon reconciliation + **Ch10 migration boundary**
- `091-095`: 제91~95화 외전1 원본 직접 대조 재구성

## 3. 현재 분석값의 증거 한계

이 보고서는 **mixed migration 상태의 GitHub 저장 원고**를 설명한다. `001-010`은 current candidate와 대조된 production prefix이지만, 제11화 이후 stored chapter는 자신의 reconciliation을 통과하기 전까지 최신 external narrative와의 연속성을 주장할 수 없다.

자동 evidence와 structural flag는 탐색 단서다. 원본·Canon·수동 장면 카드보다 우선하지 않으며 자동 수정 명령으로 사용하지 않는다.

## 4. 부·외전별 정량 기준선

- 기존 파일 경로 기준: 1부 70화, 외전1 25화, 외전2 35화, 외전3 35화, 2부 60화의 총 225 stored chapter.
- 45개 저장 묶음과 각 stored chapter의 최소 분량 검사는 합성 색인과 원고를 함께 본다.
- 이 숫자를 current 001–161 narrative의 부별 최종 화수로 재해석하지 않는다.

## 5. 전체 구조 지도

- 저장소는 225화·45개 묶음 토폴로지를 migration 컨테이너로 유지한다.
- **225화 저장 토폴로지는 최신 narrative numbering의 최종 편성 선언이 아니다.**
- current revision input은 `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx` / SHA256 `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`다.
- `reconciled_prefix_end=10`, `legacy_tail_starts_at=11`, `whole_manuscript_continuity=NOT_YET_CLAIMED`다.
- 제5화는 제6화 current 장면과 정상 연결한다.
- 제10화는 `RECONCILIATION_MIGRATION_BOUNDARY`; 합성 역개요에서 `next_chapter=null`이다.
- 저장 구 제11화는 다음 reconciliation 전까지 `LEGACY_TAIL_BOUNDARY`; current 제10화의 정상 다음 사건으로 자동 해석하지 않는다.
- `091-095` source-pass 및 과거 저장 편성의 검증은 역사적 증거로 보존한다.
- `176-180` source-pass는 deferred backlog로 보존한다.

## 6. Finding-first 판정

### MUST_FIX — resolved

과거 5→6 경계에서는 current Ch5 뒤에 legacy Ch6를 붙일 때 사건 되감기가 발생했다. QA_GREEN current Ch6~10을 승격하면서 Ch5→6은 실제 해안/감옥 상태로 재연결됐다.

새 fail-closed 경계는 **10→11**이다. current Ch10의 밀리 소실/이안 상실 상태 뒤에 저장 legacy Ch11을 자동 연결하지 않는다.

### KEEP HISTORICAL EVIDENCE

- `001-005` reconciliation
- `091-095` 원본 source pass
- representative pilots

위 증거는 수행 당시 범위의 실제 검증이다. 범위를 인접 legacy chapter에 자동 확대하지 않는다.

### REJECTED

- QA_GREEN 001–161 파일이 존재한다는 이유로 11–161을 GitHub production authority로 한 번에 승격.
- 225 stored topology를 current narrative numbering보다 높은 정본으로 간주.
- 자동 역개요 플래그를 원고 수정 명령으로 사용.

## 7. 보호 범위

- 원본 사건·최신 사용자 Decision·Canon이 파생 역개요보다 우선한다.
- migration boundary 밖 legacy tail을 current narrative의 정상 다음 화로 자동 해석하지 않는다.
- 저장 토폴로지와 narrative numbering을 분리한다.
- 밀리의 Ch10 소실은 객관적 사망 확정이 아니다.

## 8. 검증 상태

합성 색인·본문 SHA·역개요 재현성·Scene Pass 계약을 current exact HEAD에서 함께 검증한다. 과거 Green을 현재 Green으로 재사용하지 않는다.

## 9. 다음 정확한 작업

현재 운영 순서는 `ACTIVE_CONTEXT.md`와 `SCENE_PASS_REGISTRY.json`을 따른다.

1. 제1~10화 production prefix와 제10→11 migration boundary를 exact-head CI로 검증한다.
2. Green/merge/readback 뒤 다음 묶음 `fiction/manuscript/part-1/011-015.md`를 current candidate와 대조한다.
3. 원본·최신 Canon으로 `KEEP / APPLY / REWORK / REJECT`를 판정한다.
4. 승인된 delta가 생길 때 manuscript/index/reverse-outline override/Scene Pass Registry/Revision Report를 함께 갱신한다.
5. `176-180` 원본 직접 대조는 deferred 상태를 유지한다.
