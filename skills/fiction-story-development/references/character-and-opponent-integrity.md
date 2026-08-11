# Character & Opponent Integrity — Coc-Fiction 적용 렌즈

Base `developing-and-revising-serial-fiction/references/character-distinctiveness-and-opponent-threat.md`의 공용 원칙을 이 프로젝트의 정본·원본 대조 절차에 연결한다.

## 적용 순서

```text
최신 사용자 Decision
→ Google Drive 원본/원본사건감사
→ 현재 활성 원고
→ 225화 압축 초안
→ 구형 기획·archive
```

원본과 225화 초안은 동일 권위가 아니다. 225화는 사건 기능·인물 동선·하이라이트 후보를 비교하는 자료이며 최신 Canon과 충돌하면 그대로 복원하지 않는다.

## 캐릭터 감사

주요 인물마다 다음을 기록한다.

```yaml
attention_filter:
voice_and_thought:
problem_solving_method:
strength_or_competence_proof:
human_charm:
flaw_with_cost:
signature_highlight:
source_function:
current_gap:
revision_action: KEEP | RESTORE | REWORK | NEW | REMOVE
```

- 설정상 강자라면 중요도에 비례한 **화면 안 증명 장면**이 필요하다.
- 여러 강자가 같은 방식으로 강하면 역할을 분리한다.
- 조연 하이라이트는 1부/2부 각 주연의 중앙 결정권을 빼앗지 않는다.

## 상대 위상 감사

```yaml
opponent:
threat_rule:
on_screen_threat_proof:
own_turn:
protagonist_crisis:
win_or_survival_reason:
frontal_outcome_if_conditions_changed:
post_defeat_dignity:
continuity_payoff:
```

주인공을 강하게 만들기 위해 적이 갑자기 약해지거나 멍청해지면 실패다. 적의 첫 성공·비용 부과·목표 일부 달성·후속 흔적 중 하나 이상을 확보한다.

## 원본 기능 복원

원본에 인물의 매력·강함·관계를 증명하는 장면이 있었는데 압축 과정에서 소실됐다면 `RESTORE`를 우선 검토한다. 원문 문장을 복사하지 말고 **기능과 결과**를 현재 정본에 맞게 재구성한다.

## 검수 결과

- `KEEP`: 현행 장면이 충분함
- `RESTORE`: 원본 기능이 사라져 복원 필요
- `REWORK`: 기능은 있으나 최신 정본·개연성과 충돌
- `NEW`: 원본에 빈칸이 있고 최신 정본을 증명할 신규 장면 필요
- `REMOVE`: 구각색·중복·위상 훼손 장면

불확실한 원본 사실은 `UNVERIFIED_SOURCE_DETAIL`로 남기고 임의 확정하지 않는다.
