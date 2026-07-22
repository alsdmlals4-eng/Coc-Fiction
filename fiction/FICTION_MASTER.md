# 《폭풍의 눈》 현행 정본·작업 기준

상태: **ACTIVE / SINGLE SOURCE OF TRUTH**  
최종 갱신: 2026-07-22

## 1. 책임 원본

| 질문 | 현행 책임 원본 |
|---|---|
| 작품 정체성·주제·변경 금지 | `bible/01_PROJECT_CORE.md` |
| Canon 상태·별칭·폐기 | `CANON_REGISTRY.json` |
| 세계·인물·연속성·부별 설계 | `bible/02_CANON_AND_CONTINUITY.md`, `bible/03_PART1_STORY_BIBLE.md`, `bible/04_PART2_STORY_BIBLE.md` |
| POV·문체·표기 | `STYLE_GUIDE.md` |
| 실제 225화 확장 원고 | `manuscript/` |
| 화별 제목·POV·분량·원문 SHA | `MANUSCRIPT_INDEX.json` |
| 현재 상태·다음 작업 | `ACTIVE_CONTEXT.md` |
| 인수인계 | `HANDOFF.md` |
| 출처와 구형 자료 상태 | `SOURCE_MANIFEST.md`, `archive/` |

## 2. 정본 우선순위

1. 사용자의 가장 최근 직접 지시
2. 본 코어 계약과 Canon Registry
3. 원본 TRPG 로그/PDF의 사건 순서·인물 동행·결과
4. 부별 스토리 바이블·연속성 문서
5. 현재 사건 배치 원고
6. 각색 제안·외부 벤치마킹

## 3. 현행 편성

- 1부 《폭풍의 눈》: 제1화~제70화
- 외전1 《호수가 보이는 마을》: 제71화~제95화
- 외전2 《붉은 여왕의 첫 임무》: 제96화~제130화
- 외전3 《미래를 기록하는 사람》: 제131화~제165화
- 2부 《네가 없는 마을》: 제166화~제225화

구 140화 편성은 `archive/SUPERSEDED_140_EPISODE_PLAN.md`에만 존재하며 활성 기획과 원고에서 참조하지 않는다.

## 4. 화당 분량 기준

- 모든 화 본문 하한: 2,000자
- 일반 목표: 2,300~2,700자
- 전투·반전·부 결말: 2,800~3,500자 허용
- 분량보다 장면의 사건·감정 종결점을 우선한다.
- 현재 225화는 모두 하한을 충족한 확장 원고 DRAFT다. 분량 충족을 전체 퇴고 완료로 해석하지 않는다.

## 5. 심화 개선 원칙

이미 하한을 충족한 화를 분량만 늘리지 않는다. 역개요에서 누락된 인과·선택·대가·후유증이 확인된 경우에만 원본 대화와 만담, POV 관찰·판단, 공간과 동선, 선택하지 않은 대안을 보강한다. 모든 변경은 `MANUSCRIPT_INDEX.json`과 Revision Report에 전파한다.

## 6. 퇴고 순서

Developmental → Structural reverse outline → Scene diagnostic → Continuity → Line edit → Copyedit → Proofread 순서를 지킨다. 5화 단위로 원본·인과·POV·동선·상태를 검수하고, 부 단위와 225화 전체 회귀 검토를 별도로 수행한다.

## 7. 폐기 설정 정책

독립 러시아 마피아·쵸르브라트·미하일·피엘렛토·붉은 늑대 장기 서사축은 `SUPERSEDED`다. 전투·압박 기능은 황색 과격파·외부 용병의 단발 적대, 추적·후송은 경찰·의료진·라르고 팀, 장비는 델타그린 압수 장비와 공동 관리 구조로 분산한다. 활성 원고에 폐기 명칭이 남으면 검증 실패다.

## 8. 구형 파일 정책

- `archive/`는 역사·누락 대조 전용이다.
- 활성 문서는 archive를 작업 입력으로 링크하지 않는다.
- Google Docs 구형 문서는 `SUPERSEDED`로 이름을 바꾸고 `SOURCE_MANIFEST.md`에서만 기록한다.
- `latest`, `final`, `v2` 같은 경쟁 활성본을 만들지 않는다.
