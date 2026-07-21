# Coc-Fiction Documentation Map

이 지도는 작품 이전이 끝난 뒤 실제 경로를 연결하는 기준이다. 현재 존재하지 않는 원고·설정 파일을 임의로 생성하거나 정본으로 선언하지 않는다.

## 질문별 책임 원본

| 질문 | 책임 원본 |
|---|---|
| 현재 무엇을 작업 중이며 다음 작업은 무엇인가? | 프로젝트의 `ACTIVE_CONTEXT.md` 또는 동등한 현행 상태 문서 |
| 작품의 정체성과 변경 금지 범위는? | 작품 코어 계약·통합 기획서 |
| 어떤 사실이 Canon인가? | Canon Registry와 등록된 설정·인물·연표 원본 |
| 전체 사건 순서와 인과는? | 현행 플롯·시놉시스·장면 목록 |
| 인물의 욕망·비밀·관계·변화는? | 현행 인물 원본 |
| 세계 규칙·장소·조직·용어는? | 현행 세계관 원본과 용어집 |
| 누가 언제 무엇을 알고 있는가? | 연표·지식 상태·장면 카드 |
| POV·시제·문체·표기 규칙은? | 현행 Style Guide |
| 실제 문장은 무엇인가? | Manuscript 원고 |
| 자료의 사실성과 출처는? | Research Source Log·Reference Card |
| 어떤 Skill을 사용해야 하는가? | `SKILL_REGISTRY.json` |
| 작법·퇴고 방법의 근거는? | `docs/fiction-ops/CRAFT_RESEARCH.md` |
| Base에서 무엇을 가져오고 제외했는가? | `docs/fiction-ops/BASE_ADOPTION_AUDIT.md` |
| 다른 채팅과 어떻게 충돌을 피하는가? | `docs/coordination/CONCURRENT_WORK.md` |
| 새 상태·Canon·장면·문체·퇴고 파일을 어떻게 시작하는가? | `templates/fiction-ops/` |

## 단일 책임 원본 정책

- Canon 사실은 Registry에 등록된 한 원본만 책임진다.
- 원고 속 서술과 설정 문서가 충돌하면 원고를 몰래 고치지 않고 finding을 기록한다.
- 시놉시스·장면 카드·원고는 서로 다른 상세도이므로 모두 존재할 수 있지만, 같은 질문의 답을 중복 소유하지 않는다.
- 과거 초안은 Git 이력 또는 명시적 Archive로 보존하고 현행 정본처럼 읽히지 않게 한다.
- `final`, `latest`, `v2` 같은 활성 복제본을 늘리지 않는다.

## 권장 Canon 상태

- `CANON`: 사용자 승인된 현행 사실
- `PROPOSED`: 검토 대기 후보
- `DRAFT`: 원고에만 나타난 미확정 사실
- `RETCON_PENDING`: 기존 Canon과 충돌해 결정 대기
- `SUPERSEDED`: 대체됐으며 역사 확인용
- `UNVERIFIED`: 근거 부족

## 설치 템플릿

| 템플릿 | 용도 |
|---|---|
| `ACTIVE_CONTEXT.template.md` | 현재 상태·다음 작업·재개 지점 |
| `CANON_REGISTRY.template.json` | Canon 상태·원본·충돌·별칭 색인 |
| `SCENE_CARD.template.md` | 장면 전후 변화·정보·연속성 계약 |
| `STYLE_GUIDE.template.md` | POV·시제·거리·문장·대화·표기 기준 |
| `REVISION_REPORT.template.md` | finding·승인 수정·회귀 증거 |

템플릿은 빈 구조일 뿐 작품 정본이 아니다. 실제 이전 결과와 사용자 승인에 맞춰 설치한 파일만 Registry에 등록한다.

## 작품 이전 뒤 연결할 최소 항목

```text
작품 코어
인물
세계 규칙·장소·조직
연표
전체 플롯·장면 목록
용어·고유명사
POV·시제·문체
원고
연구·참고자료
현재 상태
```

경로가 확정되면 Canon Registry에 등록하고 `fiction-canon-and-research: canon-audit`와 `fiction-revision-and-validation: continuity-check`를 실행한다.
