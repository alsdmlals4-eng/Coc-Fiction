# Revision Report — 225화 구조 역개요

날짜: 2026-07-22  
상태: **REVIEW CHECKPOINT**

## 목표

현행 225화 원고를 수정하지 않은 상태에서 구조 역개요 기준선과 대표 품질 게이트를 구축하고, 다음 심화 퇴고의 우선순위를 증거 기반으로 확정한다.

## 변경 범위

- 신규: `fiction/analysis/REVERSE_OUTLINE_001_225.json`
- 신규: `fiction/analysis/REVERSE_OUTLINE_REPORT.md`
- 신규: `fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md`
- 신규: 역개요 생성·검증 도구
- 갱신: 정본 지도, 시작 문서, 현재 상태, 인수인계, 학습 기록, CI
- 미변경: `fiction/manuscript/` 전체, 기존 `MANUSCRIPT_INDEX.json` 본문 SHA, 작품 코어·Canon

## 핵심 결과

- 225화가 정확히 한 번씩 역개요에 포함됨
- 각 화의 제목·POV·분량·묶음 경로·본문 SHA가 현행 색인과 일치
- 부·외전별 문단 밀도·대사 비중·주제어 분포 기준선 생성
- 대표 품질 게이트 12화 선정
- 다음 파일럿을 제10화·제95화·제180화로 설정

## 주요 판정

- `SHOULD_FIX`: 외전1 장문단 밀집
- `SHOULD_FIX`: 외전2 진입부 시간 전환과 설명 밀도
- `SHOULD_FIX`: 외전3·2부 주제 직접표현 집중
- `SHOULD_FIX`: 2부 중반 절차·책임 논점 반복 위험
- `SHOULD_FIX`: 제96화·제166화 시간·POV 인계
- `REJECT`: 제37화/제47화와 제81화/제84화/제89화를 구조 중복으로 즉시 통합하는 비판
- `UNVERIFIED`: 원본 TRPG 로그·PDF와 225화 전체의 장면 충실도

## 검증

- 기존 운영체계 검사
- 기존 Canon·225화 원고 검사
- 역개요 생성 재현성 검사
- 역개요 화수·필드·12개 게이트 검사
- 색인 제목·POV·분량·묶음 경로·본문 SHA 일치 검사
- 구형 문서 식별자·구형 단계 문구·폐기 명칭의 활성 분석 파일 유입 검사

## 롤백

분석본과 상태 문서만 되돌리면 된다. 원고 본문을 수정하지 않았으므로 원고 SHA 롤백은 발생하지 않는다.
