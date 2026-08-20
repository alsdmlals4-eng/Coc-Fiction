# 대표 품질 게이트 12화

상태: **ACTIVE REVIEW / EXTERNAL 001-010 RECONCILED / MIXED MIGRATION / PILOT 3 COMPLETE / SOURCE PASS 091-095 COMPLETE**  
갱신: 2026-08-20

## 공통 게이트

작품 코어·POV 렌즈·목표·장애·선택·대가·상태 변화·정보 공개·원본 사건을 확인한다. 묶음별 직접 대조 여부는 Scene Pass Registry를 따른다. current prefix와 legacy tail 사이 migration boundary에서는 인접 화 번호만으로 사건 연속성을 가정하지 않는다.

## 현재 판정

| 화 | 제목·POV | 대표 기능 | 판정 | 다음 초점 |
|---:|---|---|---|---|
| 제1화 | 위대한 심연의 군주 · 이안 | 작품 진입·고서 계승 | CURRENT CANON RECONCILED | 제2~5 상태와 source order 유지 |
| 제3화 | 식탁 아래의 축배 · 엘리스→주안→엘리스 | 일상→침입·관계 선택 | CURRENT CANON RECONCILED | 신호기 제한·세실리아 확보→제4화 연결 |
| 제10화 | 친구를 쏜 날 · 이안→엘리스→이안 | 친구/위협 동시성·증거 경계·상실 | **CURRENT CANON RECONCILED / PREFIX END** | 밀리 객관적 사망 확정 금지; 제11화는 legacy boundary |
| 제20화 | 두 주인의 점토판 · 이안 | legacy 저장 세계 규칙 | CONDITIONAL / MIGRATION PENDING | current 후보 011~020 도달 시 재판정 |
| 제70화 | 응답하지 않는 호출기 · 주안 | legacy 저장 1부 결말 | MIGRATION PENDING | current numbering과 대조 전 결말 주장 금지 |
| 제95화 | 다음 이야기의 문 앞 · 다빈 | 외전1 종료·예고 | SOURCE PASS / EXTERNAL CONFLICT CHECK PENDING | current 후보 해당 구간 승격 시 재판정 |
| 제130화 | 기다리지 않는 호출 · 엘리스 | legacy 저장 비강제적 연결 | MIGRATION PENDING | current 후보 해당 구간 승격 시 재판정 |
| 제165화 | 미래를 기록하는 사람 · 엘리엇 | legacy 저장 선의→통제 | MIGRATION PENDING | current narrative numbering으로 자동 간주 금지 |
| 제166화 | 눈 속의 오두막 · 윌리엄 | legacy 저장 2부 진입 | MIGRATION PENDING | 최신 사용자 numbering과 reconciliation 필요 |
| 제180화 | 몸 안의 멈춘 시간 · 주민 | 의료 윤리·동의 | PILOT PASS / SOURCE REAUDIT DEFERRED | `176-180` 대기 유지 |
| 제200화 | 창을 지키는 사람 · 다빈 | legacy 저장 주체성 | MIGRATION PENDING | 최신 구조 도달 시 재판정 |
| 제225화 | 네가 없는 마을 · 이안 | legacy 저장 종결 | MIGRATION PENDING | current narrative 최종 결말 주장 금지 |

## 제1·3·10화 Current Reconciliation

- 제1화는 출항·고서 발견과 이안의 지식 책임을 current opening으로 잠갔다.
- 제3화는 식사→노란 코트→비야키 학살→탈출과 단방향 신호기 계약을 유지한다.
- 제10화는 밀리가 이안·엘리스를 강제로 제압하는 현재 위협과 이안의 실제 친구 관계를 동시에 유지한다.
- 이안이 밀리를 쏜 뒤 시체·피가 남지 않으므로 본체/분신/투영체 여부와 객관적 죽음은 확정하지 않는다.
- 엘리스의 `살아 있으면 직접 물어봐`는 감정적 상실을 지우는 위로가 아니라 정보 경계를 복원하는 행동이다.
- 세부 근거는 `SCENE_CARDS_001_005.md`, `SCENE_CARDS_006_010.md`, 각 reconciliation report가 책임진다.

## 제95화 SOURCE PASS

- 원본의 다빈·예나 호텔 앞 소문과 고기 약속, `To Be Continued` 기능을 복원했다.
- 기존 주안의 서울 외곽 호수 종결은 원본 사건을 대체해 제거했다.
- 다빈 제한적 3인칭 밖의 인물 상태 서술을 적대적 검토에서 제거했다.
- 제96화 첫 문장의 ‘여덟 해 전’ 전환과 충돌하지 않는다.
- 호출기와 일반 전화를 분리했다.

이 판정은 해당 source pass가 수행된 GitHub 저장 원고의 역사적 검증 증거다. current candidate가 해당 구간에 도달하면 원본·최신 사용자 지시를 기준으로 다시 `KEEP / APPLY / REWORK / REJECT`를 판정한다.

## 다음 작업

current production prefix는 제1~10화다. 다음 bounded reconciliation은 `fiction/manuscript/part-1/011-015.md`이며, 제10화 current 종료 상태와 legacy 제11화 사이의 새 migration boundary에서 시작한다.

`176-180` 원본 직접 대조는 `SCENE_PASS_REGISTRY.json#/deferred_bundle_passes`에 보존한다.
