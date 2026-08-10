# 저장 원고 구조 역개요 보고서

상태: **ACTIVE / COMPOSED BASELINE + APPROVED OVERRIDES / MIXED MIGRATION**
갱신: 2026-08-10

## 1. 데이터 구조

- 고정 기준선: `analysis/baselines/`
- 승인 변경: `MANUSCRIPT_INDEX_OVERRIDE_*.json`, `REVERSE_OUTLINE_OVERRIDE_*.json`
- 활성 manifest: `MANUSCRIPT_INDEX.json`, `REVERSE_OUTLINE_001_225.json`
- 유일한 합성 소비자: `tools/fiction_composed_data.py`
- migration 상태: `analysis/SCENE_PASS_REGISTRY.json#/external_artifact_reconciliation`

baseline은 과거 활성 원고가 아니라 immutable 기계 기준선이다. 현재 값은 manifest가 승인 override를 합성한 결과다.

## 2. 완료 override

- `001-005`: 외부 최신 제1~5화 source/canon reconciliation + Ch5 migration boundary
- `006-010`: 구 저장 편성 내부 제6·7·9화 교정; external latest reconciliation은 `PENDING_LEGACY_TAIL`
- `091-095`: 제91~95화 외전1 원본 직접 대조 재구성

## 3. 현재 분석값의 증거 한계

이 보고서는 **mixed migration 상태의 GitHub 저장 원고**를 설명한다. `001-005`는 최신 외부본과 대조된 current prefix이지만, 제6화 이후 stored chapter는 자신의 reconciliation을 통과하기 전까지 최신 외부 narrative와의 연속성을 주장할 수 없다.

자동 evidence와 structural flag는 탐색 단서다. 원본·Canon·수동 장면 카드보다 우선하지 않으며 자동 수정 명령으로 사용하지 않는다.

## 4. 부·외전별 정량 기준선

- 기존 파일 경로 기준: 1부 70화, 외전1 25화, 외전2 35화, 외전3 35화, 2부 60화의 총 225 stored chapter.
- 45개 저장 묶음과 각 stored chapter의 최소 분량 검사는 합성 색인과 원고를 함께 본다.
- 이 숫자를 external latest narrative의 부별 최종 화수로 재해석하지 않는다.

## 5. 전체 구조 지도

- 저장소는 225화·45개 묶음 토폴로지를 migration 컨테이너로 유지한다.
- **225화 저장 토폴로지는 최신 narrative numbering의 최종 편성 선언이 아니다.**
- 외부 최신 제1~105화는 사건을 압축 재편성했고, 2026-08-10 현재 제1~5화만 GitHub manuscript에 source/canon 대조 후 적용됐다.
- `reconciled_prefix_end=5`, `legacy_tail_starts_at=6`, `whole_manuscript_continuity=NOT_YET_CLAIMED`다.
- 제5화는 `RECONCILIATION_MIGRATION_BOUNDARY`; 합성 역개요에서 `next_chapter=null`이다.
- 저장 구 제6화는 `LEGACY_TAIL_BOUNDARY`; 합성 역개요에서 `previous_chapter=null`이다.
- 이 경계는 새 제5화의 감옥/해안 종료 뒤 구 제6화의 선상 저녁으로 사건이 되감기는 false continuity를 차단한다.
- 제95화 source-pass 및 기존 006-010 내부 패스는 역사적 검증 증거로 보존한다. 다른 numbering의 최신 외부본이 있다고 자동 폐기하지 않는다.
- `176-180` source-pass는 deferred backlog로 보존한다.

## 6. Finding-first 판정

### MUST_FIX — resolved

새 압축 제1~5화를 적용하고 구 제6화를 정상 next chapter로 두면 사건이 침몰/섬 진입에서 다시 선상 저녁으로 되감긴다.

**해결:** generator wrapper와 override 모두에서 5→6 migration boundary를 명시하고 자동 `previous/next` 연속성 주장을 끊었다.

### KEEP HISTORICAL EVIDENCE

- 구 `006-010` 내부 패스
- `091-095` 원본 source pass
- representative pilots

위 증거는 수행 당시 저장 편성에 대한 실제 검증이다. 다만 external latest numbering과의 경계 검증으로 범위를 확대하지 않는다.

### REJECTED

- 외부 `최종` 파일명만으로 1~105 전체를 blind overwrite.
- 225 stored topology를 최신 사용자 narrative numbering보다 높은 정본으로 간주.
- 자동 역개요 플래그를 원고 수정 명령으로 사용.

## 7. 보호 범위

- 원본 사건·최신 사용자 Decision·Canon이 파생 역개요보다 우선한다.
- migration boundary 밖 legacy tail을 current narrative의 정상 다음 화로 자동 해석하지 않는다.
- 저장 토폴로지와 narrative numbering을 분리한다.

## 8. 검증 상태

합성 색인·본문 SHA·역개요 재현성·Scene Pass 계약을 current exact HEAD에서 함께 검증한다. 과거 Green을 현재 Green으로 재사용하지 않는다.

## 9. 다음 정확한 작업

현재 운영 순서는 `ACTIVE_CONTEXT.md`와 `SCENE_PASS_REGISTRY.json`을 따른다.

1. `fiction/manuscript/part-1/006-010.md`를 최신 외부 제6~10화와 대조한다.
2. 새 제5화 종료 상태에서 앞 경계를 다시 검증한다.
3. 원본·최신 Canon으로 `KEEP / APPLY / REWORK / REJECT`를 판정한다.
4. 승인된 delta가 생길 때 manuscript/index/reverse-outline override/Scene Pass Registry/Revision Report를 함께 갱신한다.
5. reconciled prefix가 10까지 확장되면 다음 5화로 이동한다.
6. `176-180` 원본 직접 대조는 deferred 상태를 유지한다.
