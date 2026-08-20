# 제6화~제10화 Current Candidate 장면 카드·연속성 패스

상태: **CURRENT_RECONCILED / BUNDLE_006_010 / PROMOTION_CANDIDATE**  
갱신: 2026-08-20

## 범위와 근거

- 대상 원고: `fiction/manuscript/part-1/006-010.md`
- current candidate: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- candidate SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- 경계: current 제5화 / legacy 제11화
- 판정: 제6~10화 5/5 `APPLY`.

## 제6화 · 따뜻한 피난처

```yaml
scene_id: P1-006
pov_time_place: 엘리스 → 이안 → 주안 / 제5화 직후 / 해안·절벽·감옥
starting_state: 엘리스는 해안에서 이안을 깨우고 주안의 단방향 신호를 기다리며, 주안은 별도 감옥에서 각성한다.
immediate_goal_or_focus: 엘리스와 이안은 생존자·주안을 찾고, 주안은 포로들을 풀고 감옥 상황을 파악한다.
opposition_and_cost: 주민의 함정·시체 절벽·총격, 감옥의 무장 주민, 비정상적으로 커진 주안의 힘.
turn_or_discovery: 이안·엘리스는 시체더미 속 생존자를 발견하고, 주안은 창살을 부순 뒤 노란 가면의 거인과 재회한다.
ending_state: 주안은 수신기가 받기만 한다는 한계를 확인하며 `울릴 때까지 살아남는 것`을 선택한다.
protected_rule: 호출기/신호기는 GPS·문자·음성이 없는 단방향 비상 신호다.
```

## 제7화 · 죽은 척해야 사는 곳

```yaml
scene_id: P1-007
pov_time_place: 이안 → 엘리스 → 이안 / 절벽 아래·숲·동굴
starting_state: 시체더미 속 생존자와 함께 주민에게 발각되지 않아야 한다.
immediate_goal_or_focus: 즉흥 자살돌격 대신 잡혀간 사람들의 이동 경로를 기억하고 생존 통로를 만든다.
opposition_and_cost: 무장 주민·추격·시체더미의 공포·부상자 이동 불가.
turn_or_discovery: 동굴에 `죽은 척해야 산다`는 흔적과 장기 생존자의 이름이 남아 있다.
ending_state: 이안과 엘리스는 `지금은 서로 편이면 충분`하다고 합의하고, 깊은 곳에서 익숙한 여성의 `선배?`를 듣는다.
```

## 제8화 · 같은 편은 아닙니다

```yaml
scene_id: P1-008
pov_time_place: 이안 → 주안 / 동굴·숲
starting_state: 밀리가 살아 나타나지만 황색과 제한적으로 협력하고 있어 친구와 안전 판정을 분리해야 한다.
immediate_goal_or_focus: 이안·엘리스는 정보와 탈출 실마리를 얻고, 주안은 하템과 세실리아를 찾는 방향으로 이동한다.
opposition_and_cost: 밀리의 정보 독점, 황색·주민 외 제3의 위협, 하템의 미확인 계약.
turn_or_discovery: 하템은 자신이 황색이 아니며 계약이 다르다고 말한다.
ending_state: 주안과 하템은 같은 편이 아니지만 목적지가 같아 함께 움직이고, 비행형 괴물에게 추격당한다.
protected_rule: 하템과 밀리는 별도 인물이며 하템은 육체를 가진 계약자다.
```

## 제9화 · 카터라는 이름

```yaml
scene_id: P1-009
pov_time_place: 엘리스 → 이안 / 동굴 기록실
starting_state: 동굴 벽의 오래된 이름 중 `CARTER`가 발견된다.
immediate_goal_or_focus: 카터와 섬의 연결을 증거와 추론으로 분리해 확인한다.
opposition_and_cost: 오래된 기록들이 서로 충돌하고, 엘리스에게는 아버지를 즉시 의심할 감정적 압력이 있다.
turn_or_discovery: 이안은 석판의 서술을 사실/주장/불명으로 나누고 엘리스는 결론보다 탁본을 먼저 남긴다.
ending_state: 밀리가 이안의 가방에 손을 뻗었다 거두며 `친구가 진짜`와 `친구가 안전`이 다른 문장으로 남는다.
```

## 제10화 · 친구를 쏜 날

```yaml
scene_id: P1-010
pov_time_place: 이안 → 엘리스 → 이안 / 오두막 주변
starting_state: 밀리는 피난처를 제안하지만 이안과 엘리스는 그녀가 누구와 연락하는지 확인하지 못한다.
immediate_goal_or_focus: 밀리의 의도와 접근하는 위협을 판별하면서 생존한다.
opposition_and_cost: 밀리의 얼굴 변화·강제 제압·카터 가문에 대한 원한, 이안의 친구 관계와 현재 위험 판단 충돌.
turn_or_discovery: 밀리는 엘리스를 인질, 이안을 필요한 사람으로 분류하고 둘을 강제로 제압한다.
ending_state: 이안이 밀리를 쏘지만 시체·피 없이 사라져 본체/분신/투영체 여부와 객관적 죽음은 미확정이다. 엘리스는 `살아 있으면 직접 물어봐`라고 현재 증거 경계를 되돌려준다.
protected_rule: `밀리 사망`은 이안의 정서적 상실이지 객관적 정사 확정이 아니다.
```

## 경계 연속성

| 경계 | 상태 이월 | 판정 |
|---|---|---|
| `제5→6화` | 엘리스+이안 해안 / 주안 감옥 → 같은 두 전선 즉시 재개 | `PASS / CURRENT` |
| `제6→7화` | 절벽 시체더미 속 생존자 발견 → 죽은 척하며 추적 회피 | `PASS` |
| `제7→8화` | 동굴 깊은 곳 `선배?` → 밀리 생존 재등장 | `PASS` |
| `제8→9화` | 동굴 기록 탐사 → CARTER/석판 기록 분석 | `PASS` |
| `제9→10화` | 밀리 신뢰 경계 → 실제 강제 제압/배신 압력 | `PASS` |
| `제10→11화` | current Ch10 종료 뒤 저장 제11화는 아직 legacy | `MIGRATION_BOUNDARY / NOT_YET_CLAIMED` |

## Finding-first 판정

- `APPLY 5/5`: QA_GREEN current candidate의 제6~10화를 production bundle로 승격한다.
- `KEEP`: 제5→6 current continuity와 신호기 단방향 제한.
- `KEEP`: 밀리의 생존/배신/소실은 객관적 사망 확정이 아니라 증거 불충분 상태.
- `KEEP`: 하템은 황색과 동일 소속으로 단정하지 않는 별도 계약자.
- `REJECT`: 구 제10화의 폐기 복종 프레이밍과 구 `히템` 표기.
- `BOUNDARY`: 제11화 이후는 다음 reconciliation 전까지 legacy tail.
