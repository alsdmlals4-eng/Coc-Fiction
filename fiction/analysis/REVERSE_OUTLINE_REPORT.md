# 225화 구조 역개요 보고서

상태: **ACTIVE / COMPOSED BASELINE + APPROVED OVERRIDES**
갱신: 2026-08-10

## 데이터 구조

- 고정 기준선: `analysis/baselines/`
- 승인 변경: `MANUSCRIPT_INDEX_OVERRIDE_*.json`, `REVERSE_OUTLINE_OVERRIDE_*.json`
- 활성 manifest: `MANUSCRIPT_INDEX.json`, `REVERSE_OUTLINE_001_225.json`
- 유일한 합성 소비자: `tools/fiction_composed_data.py`

baseline은 과거 활성 원고가 아니라 immutable 기계 기준선이다. 현재 값은 manifest가 모든 승인 override를 합성한 결과다.

## 완료 override

- `006-010`: 제6·7·9화 내부 연속성 교정
- `091-095`: 제91~95화 외전1 원본 직접 대조 재구성

## 현재 구조 판정

- GitHub current manuscript는 225화·45개 묶음 유지
- 모든 화 2,000자 이상
- 제95화 대표 게이트는 `SOURCE PASS`로 갱신
- 제90→91화는 명시적 회상 전환
- 제95→96화는 외전1 현재 종결 뒤 ‘여덟 해 전’ 과거편 전환
- 기존 미완료 source-pass 대상 `176-180`은 유효한 backlog로 유지
- 현재 대화의 제1~105 통합 재퇴고본은 GitHub 원고에 전파되지 않았으므로, **현재 운영 우선순위는 001-005부터의 external-artifact canon reconciliation**이다.

## 현재 분석값의 증거 한계

이 보고서는 현재 GitHub `manuscript/`와 합성 override를 설명한다. 대화에서 생성된 제1~105화 최신 DOCX가 이 보고서의 구조 데이터에 반영됐다는 뜻이 아니다.

따라서 제1~105 reconciliation 동안 기존 역개요 플래그를 최신 외부 원고보다 우선하는 수정 명령으로 사용하지 않는다. 회차별 source/canon/manuscript delta가 승인돼 GitHub 원고가 실제 변경될 때 해당 override와 본 보고서를 함께 갱신한다.

## 사용 제한

자동 evidence와 structural flag는 탐색 단서다. 원본·Canon·수동 장면 카드보다 우선하지 않으며 자동 수정 명령으로 사용하지 않는다.

## 4. 부·외전별 정량 기준선

- 1부 70화, 외전1 25화, 외전2 35화, 외전3 35화, 2부 60화의 총 225화를 유지한다.
- 45개 원고 묶음과 모든 화 2,000자 이상 조건은 합성 색인과 현재 원고를 함께 검사한다.
- 정량 플래그는 검토 우선순위이며 자동 수정 명령이 아니다.

## 5. 전체 구조 지도

- 1부: 출항과 선상 재난에서 섬의 규칙·세력 충돌·쇼거스전·행동 편향 폭로·주안 이탈까지.
- 외전1: 주안의 답 탐색과 티베트 문답, 한국 정착, 엘리스의 생존 확인, 다빈·예나의 다음 이야기 예고까지.
- 외전2·외전3: 엘리스와 이안의 독립 성장 및 2부 연결.
- 2부: 다빈·주민·엘리스가 정해진 안전보다 선택 가능한 미래를 되찾는 과정.

이 구조 지도는 GitHub current DRAFT의 요약이다. 최신 사용자 지시와 외부 재퇴고본에서 폐기된 설정이 발견되면 Canon reconciliation에서 재판정한다.

## 6. Finding-first 판정

- `MUST_FIX`: 원본 종결을 대체한 제91~95화의 비정본 결말 구조를 원본 핵심 사건으로 복원했다.
- `SHOULD_FIX`: 제95화의 제한적 3인칭 밖 인물 상태 서술을 다빈 관찰 범위로 제한했다.
- `REJECT`: 사용자 지시로 폐기된 인물 후일담·독립 동물 서사·장기 조직축은 원본에 있어도 복원하지 않았다.
- 제90·96화 원고는 수정하지 않고 역개요의 앞뒤 화 메타데이터만 제90~96화 경계까지 갱신했다.

## 9. 다음 정확한 작업

현재 운영 순서는 `ACTIVE_CONTEXT.md`와 `SCENE_PASS_REGISTRY.json`을 따른다.

1. `fiction/manuscript/part-1/001-005.md`부터 제1~105 최신 외부 통합본과 GitHub current manuscript를 source/canon 기준으로 대조한다.
2. 승인된 delta가 생길 때만 manuscript/index/reverse-outline override/Scene Pass Registry/Revision Report를 갱신한다.
3. 기존 `fiction/manuscript/part-2/176-180.md` 원본 직접 대조와 `006-010` 원본 1부 재감사는 backlog로 유지한다.
