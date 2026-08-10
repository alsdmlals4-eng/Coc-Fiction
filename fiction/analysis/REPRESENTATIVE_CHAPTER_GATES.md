# 대표 품질 게이트 12화

상태: **ACTIVE REVIEW / PILOT 3 COMPLETE / BUNDLE 006-010 COMPLETE / SOURCE PASS 091-095 COMPLETE**
갱신: 2026-08-10

## 공통 게이트

작품 코어·POV 렌즈·목표·장애·선택·대가·상태 변화·정보 공개·원본 사건을 확인한다. 묶음별 직접 대조 여부는 Scene Pass Registry를 따른다.

## 현재 판정

| 화 | 제목·POV | 대표 기능 | 판정 | 다음 초점 |
|---:|---|---|---|---|
| 제1화 | 출항과 금서 · 이안 | 작품 진입 | PASS / SOURCE AUDIT PENDING | 최신 외부 제1~5화와 current canon 대조 |
| 제3화 | 벌꿀주스와 신입 경호원 · 주안 | 관계·명령 | PASS / SOURCE AUDIT PENDING | 최신 외부 제1~5화와 current canon 대조 |
| 제10화 | 거짓 무전과 브루고 · 주안 | 전투·능력 비용 | BUNDLE PASS / SOURCE AUDIT PENDING | 001-105 reconciliation에서 재대조 |
| 제20화 | 두 주인의 점토판 · 이안 | 세계 규칙 | CONDITIONAL PASS | 설명 행동화 |
| 제70화 | 응답하지 않는 호출기 · 주안 | 1부 결말 | PASS / SOURCE AUDIT PENDING | 결말 원본 대조 |
| 제95화 | 다음 이야기의 문 앞 · 다빈 | 외전1 종료·2부 예고 | SOURCE PASS | 외부 제91~95화와 원본 직접대조 결과 충돌 여부 확인 |
| 제130화 | 기다리지 않는 호출 · 엘리스 | 비강제적 연결 | PASS / SHOULD_FIX | 신호 뒤 설명 |
| 제165화 | 미래를 기록하는 사람 · 엘리엇 | 선의→통제 | PASS | 확신의 균열 |
| 제166화 | 눈 속의 오두막 · 윌리엄 | 2부 과거 프롤로그 | PASS / CONTINUITY CHECK | 제167~170화 회수 |
| 제180화 | 몸 안의 멈춘 시간 · 주민 | 의료 윤리·동의 | PILOT PASS / SOURCE REAUDIT DEFERRED | 제175·181화 경계 |
| 제200화 | 창을 지키는 사람 · 다빈 | 주체성 | PASS | 전투 지리 |
| 제225화 | 네가 없는 마을 · 이안 | 결말·기관 책임 | PASS / SHOULD_FIX | 요약 밀도 |

## 제95화 SOURCE PASS

- 원본의 다빈·예나 호텔 앞 소문과 고기 약속, `To Be Continued` 기능을 복원했다.
- 기존 주안의 서울 외곽 호수 종결은 원본 사건을 대체해 제거했다.
- 다빈 제한적 3인칭 밖의 인물 상태 서술을 적대적 검토에서 제거했다.
- 제96화 첫 문장의 ‘여덟 해 전’ 전환과 충돌하지 않는다.
- 호출기와 일반 전화를 분리했다.

이 판정은 현재 GitHub main에서 직접 원본 대조한 결과다. 외부 제1~105화 통합 재퇴고본이 다른 제91~95화 내용을 가진다면 자동으로 이 SOURCE PASS를 폐기하지 않고 원본·최신 사용자 지시를 기준으로 `KEEP / APPLY / REWORK / REJECT`를 재판정한다.

## 다음 작업

현재 즉시 시작할 묶음은 `fiction/manuscript/part-1/001-005.md`다. 목적은 제1~105 외부 통합 재퇴고본과 GitHub current manuscript의 canon reconciliation이다.

`176-180` 원본 2부 직접 대조는 `SCENE_PASS_REGISTRY.json#/deferred_bundle_passes`에 보존하며, 001-105 reconciliation 이후 다시 진행 순서를 판정한다.
