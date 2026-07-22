# Coc-Fiction Documentation Map

## 질문별 책임 원본

| 질문 | 책임 원본 |
|---|---|
| 현재 상태와 다음 작업 | `fiction/ACTIVE_CONTEXT.md` |
| 작품 정체성·주제·변경 금지 | `fiction/bible/01_PROJECT_CORE.md` |
| 정본 우선순위·편성·분량·작업 기준 | `fiction/FICTION_MASTER.md` |
| Canon·폐기·별칭 | `fiction/CANON_REGISTRY.json` |
| 인물·세계·연속성 | `fiction/bible/02_CANON_AND_CONTINUITY.md` |
| 1부·2부 구조 | `fiction/bible/03_PART1_STORY_BIBLE.md`, `fiction/bible/04_PART2_STORY_BIBLE.md` |
| POV·문체·표기 | `fiction/STYLE_GUIDE.md` |
| 실제 확장 원고 | `fiction/manuscript/` |
| 화별 제목·POV·분량·원문 SHA | `fiction/MANUSCRIPT_INDEX.json` |
| 출처·Google Docs 상태 | `fiction/SOURCE_MANIFEST.md` |
| 인수인계 | `fiction/HANDOFF.md` |
| 과거 자료 | `fiction/archive/` — 기본 입력 금지 |
| Skill 선택 | `[소설]/00_운영체계/SKILL_REGISTRY.json` |

## 단일 책임 원본

같은 질문은 한 활성 파일만 책임진다. 과거 초안은 Git 이력 또는 archive에만 둔다. `latest`, `final`, `v2` 활성 복제본을 만들지 않는다. 구형 문서나 이름을 바꾸면 `fiction-canon-and-research: reference-freshness`와 `fiction-revision-and-validation: regression-check`를 실행한다.

## 자동 검증

- `python tools/check_fiction_operating_system.py`
- `python tools/check_fiction_content.py`
