# 《폭풍의 눈》 현행 정본·작업 기준

상태: **ACTIVE / SINGLE SOURCE OF TRUTH**
최종 갱신: 2026-07-23

## 1. 책임 원본

| 질문 | 현행 책임 원본 |
|---|---|
| 작품 정체성·주제·변경 금지 | `bible/01_PROJECT_CORE.md` |
| Canon 상태·별칭·폐기 | `CANON_REGISTRY.json` |
| 세계·인물·연속성·부별 설계 | `bible/02_CANON_AND_CONTINUITY.md`, `bible/03_PART1_STORY_BIBLE.md`, `bible/04_PART2_STORY_BIBLE.md` |
| POV·문체·표기 | `STYLE_GUIDE.md` |
| 실제 225화 확장 원고 | `manuscript/` |
| 화별 제목·POV·분량·원문 SHA | `MANUSCRIPT_INDEX.json` |
| 225화 구조 역개요·구조 진단 | `analysis/REVERSE_OUTLINE_001_225.json`, `analysis/REVERSE_OUTLINE_REPORT.md` |
| 대표 게이트·완료 묶음 패스 | `analysis/REPRESENTATIVE_CHAPTER_GATES.md`, `analysis/SCENE_PASS_REGISTRY.json` |
| 원본 파일·감사 상태 | `SOURCE_MANIFEST.md`, `sources/PRIMARY_SOURCE_INVENTORY.md` |
| 현재 상태·다음 작업 | `ACTIVE_CONTEXT.md` |
| 인수인계 | `HANDOFF.md` |

## 2. 정본 우선순위

1. 사용자의 가장 최근 직접 지시
2. 본 코어 계약과 Canon Registry
3. 접근 가능한 원본 TRPG 로그/PDF의 사건 순서·인물 동행·결과
4. 부별 스토리 바이블·연속성 문서
5. 현재 확장 원고
6. 수동 장면 카드·Revision Report
7. 구조 역개요·진단 보고서
8. 외부 참고

색인과 역개요는 활성 manifest가 immutable baseline과 승인된 묶음 override를 합성한다. baseline을 직접 편집 입력으로 사용하지 않는다. 원고·Canon과 충돌하면 파생 분석을 갱신하며 분석을 근거로 원고를 자동 덮어쓰지 않는다.

## 3. 현행 편성

- 1부 《폭풍의 눈》: 제1화~제70화
- 외전1 《호수가 보이는 마을》: 제71화~제95화
- 외전2 《붉은 여왕의 첫 임무》: 제96화~제130화
- 외전3 《미래를 기록하는 사람》: 제131화~제165화
- 2부 《네가 없는 마을》: 제166화~제225화

구 140화 편성은 역사 기록일 뿐 활성 기획·원고·검수 입력으로 사용하지 않는다.

## 4. 화당 분량 기준

- 모든 화 본문 하한: 2,000자
- 일반 목표: 2,300~2,700자
- 전투·반전·부 결말: 2,800~3,500자 허용
- 분량보다 사건·감정 종결점을 우선한다.
- 현재 225화는 모두 하한을 충족한 확장 원고 DRAFT다. 하한 충족은 전체 퇴고 완료가 아니다.

## 5. 심화 개선 원칙

이미 하한을 충족한 화를 분량만 늘리지 않는다. 인과·선택·대가·후유증 또는 원본 충실도 결함이 증거로 확인된 경우에만 수정한다. `SOURCE_MATCHED`는 사건 순서·동행·행선지·결과 판정이며 원문 문장 복제를 뜻하지 않는다. 원본에 있더라도 최신 사용자 지시가 폐기한 축은 복원하지 않고 제외 근거를 남긴다.

## 6. 퇴고 순서

Source inventory → Canon audit → Developmental → Structural reverse outline → Scene diagnostic → Continuity → Line edit → Copyedit → Proofread 순서를 지킨다. 5화 단위로 원본·인과·POV·시간·동선·상태를 검수하고 부 단위와 225화 전체 회귀를 별도로 수행한다.

완료:

- 구조 역개요 기준선
- 제10·95·180화 대표 파일럿
- `006-010` 내부 연속성 패스
- `091-095` 원본 직접 대조 패스

다음: `176-180` 원본 직접 대조 패스.

## 7. 폐기 설정 정책

독립 러시아 마피아·쵸르브라트·미하일·피엘렛토·붉은 늑대·컨소시엄·협상 책임자 장기 서사축은 `SUPERSEDED`다. 오션 후일담·관계·동기 복원, 아프리카 임무, 버실라/Woff 독립 동물 서사도 사용하지 않는다. 원본에 존재해도 최신 사용자 지시를 우선한다.

## 8. 구형 파일 정책

- 역사·누락 대조 자료는 활성 작업 입력이 아니다.
- 활성 문서는 구형 Google Docs·압축 초안·구 편성을 직접 링크하거나 근거로 사용하지 않는다.
- 대체 관계는 Source Manifest를 경유한다.
- `latest`, `final`, `v2` 같은 경쟁 활성본을 만들지 않는다.
