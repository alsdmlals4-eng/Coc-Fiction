# SOURCE PASS 091-095 작업 계약

상태: **COMPLETE**
갱신: 2026-07-23

## 목표

원본 《호수가 보이는 마을》 113~147쪽과 제91~95화 및 제90·96화 경계를 직접 대조해 외전1 종결 사건 순서와 다음 이야기 인계를 복원한다.

## 사용 Skill

- `fiction-project-operations`: route, contract, checkpoint, handoff, execution-report
- `fiction-canon-and-research`: source-log, canon-audit, continuity-map, timeline-and-state, reference-freshness
- `fiction-story-development`: scene-card, plot-and-causality, character-arc, stress-test
- `fiction-drafting`: approved-rewrite, pov-and-distance, dialogue-and-subtext, action-and-reaction
- `fiction-revision-and-validation`: scene-diagnostic, continuity-check, adversarial-loop, regression-check, evidence-report, pr-review

## 수정 허용 범위

- 원고 본문: 제91~95화
- 경계 검증: 제90화와 제96화
- 파생 데이터: 색인 override, 역개요 override, 장면 카드, Registry, 대표 게이트, Revision Report
- 활성 문서: Master, Active Context, Handoff, Story Bible, Source Manifest, 운영 시작 문서
- 자동 검사: 완료 묶음·출처 상태·구형 참조 회귀

## 보호 범위

- 제90화와 제96화 본문 SHA 보존
- 제1~90화·제96~225화 본문 SHA 보존
- 오션 후일담·아프리카 임무·독립 마피아/동물 장기축 복원 금지
- 호출기는 일방향 비상 송신과 수신 확인만 유지
- 원본에 없는 GPS·문자·음성 기능 추가 금지
- 원본 대사 복사는 최소화하고 사건 순서·인물 동행·결과를 보존한다.

## 완료 조건

1. 원본 핵심 종결 순서가 제91~95화에 존재한다.
2. 제90→91화의 시간 회상과 제95→96화의 8년 전 전환이 명시된다.
3. 변경 화만 index/reverse-outline override에 포함된다.
4. 활성 문서에 원본 미접근이라는 구형 상태 문구가 남지 않는다.
5. CI와 PR 검토가 통과한 뒤 squash 병합한다.
