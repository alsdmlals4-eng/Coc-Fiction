---
name: fiction-story-development
description: 작품 코어·주제·인물·인과 플롯·장면 목록과 장면 카드를 설계하고, 반례와 대표 장 품질 게이트로 구조를 검증한다.
---

# Fiction Story Development

## Modes

`core-audit | core-contract | premise-and-theme | character-and-arc | character-and-opponent-integrity | plot-and-causality | progressive-outline | scene-list | scene-card | representative-chapter-gate | stress-test`

## Required inputs

- 최신 사용자 의도와 승인 기록
- 현재 작품 코어·설정·인물·플롯·원고
- 장르·독자 약속·분량·금지 범위
- POV·시제·톤·결말 방향
- 충돌·미확정·보존할 장점
- 원본·225화 압축 초안·현행 원고 사이에서 보존/복원/재작업할 인물 기능과 적대자 위상

## 설계 원칙

- 작품 코어와 바꿀 수 있는 외피를 구분한다.
- 플롯은 사건 목록이 아니라 `인물 의도 → 선택 → 대가 → 상태 변화 → 다음 압력`으로 연결한다.
- 인물은 장기 욕망·내적 필요·장면 목표·두려움·거짓 믿음·변화 압력을 구분한다.
- 주요 인물은 관찰 필터·말투/사고·문제 해결 방식·실제 유능함 증명·인간적 매력·대가를 만드는 결점·대표 하이라이트가 서로 교환 가능하지 않아야 한다.
- 설정상 강한 조연·적대자는 중요도에 비례한 화면 안 증명을 갖는다. 주인공을 강하게 만들기 위해 상대를 갑자기 약화·우둔화하지 않는다.
- 주요 상대는 최소 한 번 자신의 규칙을 주인공에게 강제하는 `own turn`을 갖고, 승리·생존 이유는 주인공 고유의 숙련·전술·규칙 해석·관계/협상 중 하나 이상으로 설명한다.
- 원본에 있던 강함·관계·매력 증명 기능이 압축 과정에서 사라졌다면 새 장면을 발명하기 전에 `KEEP / RESTORE / REWORK / NEW / REMOVE`로 기능을 대조한다.
- 주제는 설명문이 아니라 서로 충돌하는 선택과 대가로 드러낸다.
- 복선은 미래 정보를 숨기는 것이 아니라 현재 장면에서도 자연스러운 기능을 가진다.
- 장면은 사건·인식·관계·정서 중 최소 하나를 의미 있게 바꾼다.
- Snowflake, 3막, 5막, Story Circle, Scene/Sequel 등은 진단 렌즈이며 작품에 맞지 않으면 부분 적용하거나 기각한다.

상세 감사 필드는 `references/character-and-opponent-integrity.md`를 사용한다.

## 작품 코어 최소 필드

```yaml
reader_promise:
central_character:
desire_need_and_stakes:
central_conflict_and_story_question:
theme_question:
genre_tone_and_emotional_target:
pov_tense_and_distance:
ending_direction:
invariants:
changeable_shell:
reapproval_triggers:
```

`CORE_CONFIRMED`는 사용자 승인 없이는 부여하지 않는다.

## 장면 카드

```yaml
scene_id:
pov_time_place:
starting_state:
immediate_goal_or_focus:
opposition_and_cost:
turn_or_discovery:
ending_state:
revealed_and_withheld_information:
character_world_state_changes:
protected_image_line_or_emotion:
next_pressure:
continuity_dependencies:
```

전투·추격·협상 등 상대 위상이 중요한 장면은 필요 시 다음을 추가한다.

```yaml
opponent_threat_rule:
opponent_own_turn:
protagonist_crisis:
win_or_survival_reason:
post_defeat_dignity:
```

## 대표 장 품질 게이트

대표 장 또는 대표 장 묶음으로 다음을 확인한다.

- 작품 코어와 장르 약속이 실제 문장에서 느껴지는가
- 인물·갈등·정보 공개·톤·POV가 함께 작동하는가
- 이름을 지운 대사·판단·행동만으로 주요 인물의 차이를 느낄 수 있는가
- 설정상 강자·적대자의 위험이 설명이 아니라 화면 안 사건으로 증명되는가
- 승자가 강해 보여도 패자가 볼품없어지지 않는가
- 조연 하이라이트가 주연의 중앙 결정권과 결말을 빼앗지 않는가
- 이 품질을 다른 장에도 반복 생산할 수 있는가
- 참고자료의 모사가 아니라 작품 고유 선택이 있는가
- 수정 비용과 파이프라인이 감당 가능한가

## Output

유지·변경·제외, 작품 코어 상태, 인과 플롯, 인물 아크, 캐릭터 식별 매트릭스, 상대 위상 장부, 원본 기능 `KEEP/RESTORE/REWORK/NEW/REMOVE`, 장면 목록·카드, 반례, 미확정, 사용자 결정 필요 항목을 분리한다.

## Quality gate

기능·설정 목록 전체를 코어로 고정하거나, 우연과 설명으로 인과를 대신하거나, 플롯을 위해 인물 동기를 훼손하거나, 공식에 맞추기 위해 작품의 고유 리듬을 없애거나, 설정상 강한 인물을 장면 밖 소문으로만 처리하거나, 주인공 승리를 위해 상대를 갑자기 약체화하면 실패다.

Learning Log: `skills/FICTION_SKILL_LEARNING_LOG.md`
