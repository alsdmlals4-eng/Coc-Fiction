# 대표 품질 게이트 12화

상태: **ACTIVE REVIEW / EXTERNAL 001-005 RECONCILED / MIXED MIGRATION / PILOT 3 COMPLETE / SOURCE PASS 091-095 COMPLETE**
갱신: 2026-08-10

## 공통 게이트

작품 코어·POV 렌즈·목표·장애·선택·대가·상태 변화·정보 공개·원본 사건을 확인한다. 묶음별 직접 대조 여부는 Scene Pass Registry를 따른다. 외부 최신 prefix와 legacy tail 사이 migration boundary에서는 인접 화 번호만으로 사건 연속성을 가정하지 않는다.

## 현재 판정

| 화 | 제목·POV | 대표 기능 | 판정 | 다음 초점 |
|---:|---|---|---|---|
| 제1화 | 위대한 심연의 군주 · 이안 | 작품 진입·고서 계승 | EXTERNAL CANON RECONCILED | 제2~5 상태와 source order 유지 |
| 제3화 | 식탁 아래의 축배 · 엘리스→주안→엘리스 | 일상→침입·관계 선택 | EXTERNAL CANON RECONCILED | 신호기 제한·세실리아 확보→제4화 연결 |
| 제10화 | 거짓 무전과 브루고 · 주안 | legacy 저장 대표 게이트 | LEGACY TAIL / EXTERNAL RECONCILIATION PENDING | 최신 외부 제6~10화 재대조 |
| 제20화 | 두 주인의 점토판 · 이안 | legacy 저장 세계 규칙 | CONDITIONAL / MIGRATION PENDING | 최신 외부 묶음 도달 시 재판정 |
| 제70화 | 응답하지 않는 호출기 · 주안 | legacy 저장 1부 결말 | MIGRATION PENDING | 외부 최신 numbering과 대조 전 current narrative 결말 주장 금지 |
| 제95화 | 다음 이야기의 문 앞 · 다빈 | 외전1 종료·예고 | SOURCE PASS / EXTERNAL CONFLICT CHECK PENDING | 외부 최신 제91~95화 도달 시 원본 우선 재판정 |
| 제130화 | 기다리지 않는 호출 · 엘리스 | legacy 저장 비강제적 연결 | MIGRATION PENDING | 외부 latest tail 도달 시 재판정 |
| 제165화 | 미래를 기록하는 사람 · 엘리엇 | legacy 저장 선의→통제 | MIGRATION PENDING | current narrative numbering으로 자동 간주 금지 |
| 제166화 | 눈 속의 오두막 · 윌리엄 | legacy 저장 2부 진입 | MIGRATION PENDING | 최신 사용자 numbering과 reconciliation 필요 |
| 제180화 | 몸 안의 멈춘 시간 · 주민 | 의료 윤리·동의 | PILOT PASS / SOURCE REAUDIT DEFERRED | `176-180` 대기는 001-105 migration 뒤 재개 |
| 제200화 | 창을 지키는 사람 · 다빈 | legacy 저장 주체성 | MIGRATION PENDING | 최신 구조 도달 시 재판정 |
| 제225화 | 네가 없는 마을 · 이안 | legacy 저장 종결 | MIGRATION PENDING | current narrative 최종 결말 주장 금지 |

## 제1·3화 EXTERNAL CANON RECONCILIATION

- 제1화는 COC 1일차의 출항·짐 사고·고서 제목 해독과 COC 2일차의 브루스/펜던트 기능을 압축하되 사건 원인과 정보 순서를 보존했다.
- 제3화는 즐거운 식사 → 빈 테이블 → 엘리스 위험 감지 → 주안·엘리스 식탁 아래 은신 → 축배 → 비야키 → 탈출 순서를 보존했다.
- 제3화 신호기는 위치·문자·통화가 없는 단순 비상 신호 장치다.
- 주안의 행동은 독립 폐기 설정을 사실화하지 않고 현재 선택 이유를 다시 확인하는 방식으로 읽는다.
- 세부 근거는 `SCENE_CARDS_001_005.md`와 `REVISION_2026-08-10_EXTERNAL_RECONCILIATION_001_005.md`가 책임진다.

## 제95화 SOURCE PASS

- 원본의 다빈·예나 호텔 앞 소문과 고기 약속, `To Be Continued` 기능을 복원했다.
- 기존 주안의 서울 외곽 호수 종결은 원본 사건을 대체해 제거했다.
- 다빈 제한적 3인칭 밖의 인물 상태 서술을 적대적 검토에서 제거했다.
- 제96화 첫 문장의 ‘여덟 해 전’ 전환과 충돌하지 않는다.
- 호출기와 일반 전화를 분리했다.

이 판정은 해당 source pass가 수행된 GitHub 저장 원고의 역사적 검증 증거다. 외부 제1~105화 통합 재퇴고본이 다른 제91~95화 내용을 가진다면 자동으로 폐기하지 않고 원본·최신 사용자 지시를 기준으로 `KEEP / APPLY / REWORK / REJECT`를 재판정한다.

## 다음 작업

현재 즉시 시작할 묶음은 `fiction/manuscript/part-1/006-010.md`다. 목적은 외부 최신 제6~10화와 legacy 저장 `006-010`의 canon reconciliation이며, 새 제5화의 종료 상태에서 앞 경계를 다시 검증한다.

`176-180` 원본 2부 직접 대조는 `SCENE_PASS_REGISTRY.json#/deferred_bundle_passes`에 보존한다.
