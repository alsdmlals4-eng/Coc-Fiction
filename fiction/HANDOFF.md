# 《폭풍의 눈》 활성 인수인계

갱신: 2026-07-23

## 먼저 읽을 파일

1. `FICTION_MASTER.md`
2. `ACTIVE_CONTEXT.md`
3. `CANON_REGISTRY.json`
4. `SOURCE_MANIFEST.md`
5. `sources/PRIMARY_SOURCE_INVENTORY.md`
6. `../docs/coordination/SOURCE_PASS_176_180_WORK_CONTRACT.md`
7. `analysis/SCENE_PASS_REGISTRY.json`
8. 현재 묶음의 `analysis/SCENE_CARDS_*.md`
9. 최신 `reports/REVISION_*.md`
10. `analysis/REPRESENTATIVE_CHAPTER_GATES.md`
11. `analysis/REVERSE_OUTLINE_REPORT.md`
12. `MANUSCRIPT_INDEX.json`
13. 해당 부 Story Bible과 현재 작업 원고
14. `../[소설]/00_운영체계/SKILL_REGISTRY.json`
15. `../skills/fiction-revision-and-validation/SKILL.md`

## 현재 상태

- 225화·45개 묶음 정상
- `006-010` 내부 연속성 패스 완료
- `091-095` 원본 직접 대조 패스 완료
- 원본 PDF 인벤토리 확보, 전체 직접 감사는 진행 중
- `serial-arc-pass` 라우팅·검증·기획 문서 동기화 계약 활성화
- 다음 단계: `176-180` 원본 대조

## 외전1 종결 고정

- 제90화에서 주안·아킴·조세이칸이 한국에 도착한다.
- 제91화는 한국 도착 첫날 밤의 명시적 회상으로 비행 전날 티베트 야영지·이가레스 문답을 복원한다.
- 제92화는 세 사람의 한국 공동생활과 경주 관광을 닫는다.
- 제93화는 윌리엄의 과잉 보호와 엘리스의 주안 위치 질문, 세실리아·엘레인 이동을 다룬다.
- 제94화는 엘리스가 일반 전화로 이안에게 주안의 티베트·위구르 생존을 확인한다.
- 제95화는 다빈·예나의 호텔 앞 소문과 고기 약속으로 다음 이야기를 예고한다.
- 제96화는 ‘시간은 다시 여덟 해 전’으로 외전2 과거편을 연다.

## 원본·각색 상태

- 외전1 원본 113~147쪽 핵심 사건: `SOURCE_MATCHED`
- 오션 후일담·아프리카 임무·독립 마피아/동물 장기축: 최신 사용자 지시에 따라 제외
- 호출기: 비상 신호와 수신 확인만 가능. 제94화 연락은 일반 전화.
- 원본의 모든 농담·애드리브를 복제하지 않으며 인물 핵심·사건 결과·인계 기능을 우선한다.

## 다음 묶음 작업 절차

`fiction-canon-and-research`의 원본·Canon 감사와 `fiction-revision-and-validation: serial-arc-pass`를 함께 사용한다.

원본 파일·해시 확인 → 작업 계약의 범위·보호·제외 확인 → 현재 묶음과 앞뒤 경계 → Canon·폐기 설정 → 수동 장면 카드 → source finding → 적대적 재판정 → 승인 범위 수정 → index/outline override → Registry·Report·`ACTIVE_CONTEXT`·`HANDOFF`·현행 Google Docs → 구형 참조 회귀 → PR·CI·병합 순으로 진행한다.

현재 계약: `../docs/coordination/SOURCE_PASS_176_180_WORK_CONTRACT.md`

## 주의

- baseline·구형 자료·구형 Google Docs를 직접 작업 입력으로 사용하지 않는다.
- 원본 본체가 있어도 파일명만으로 정본을 판단하지 않는다.
- 원본 사건과 최신 사용자 지시가 충돌하면 사용자 지시를 우선하고 제외 근거를 기록한다.
- 완료 묶음의 규칙을 다른 묶음에 자동 일반화하지 않는다.
