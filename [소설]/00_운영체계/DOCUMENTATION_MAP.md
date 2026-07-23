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
| POV·문체·표기·묶음 패스 규칙 | `fiction/STYLE_GUIDE.md` |
| 실제 확장 원고 | `fiction/manuscript/` |
| 화별 제목·POV·분량·원문 SHA | `fiction/MANUSCRIPT_INDEX.json` |
| 225화 구조 역개요·구조 진단 | `fiction/analysis/REVERSE_OUTLINE_001_225.json`, `fiction/analysis/REVERSE_OUTLINE_REPORT.md` |
| 대표 화 품질 기준 | `fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md` |
| 완료 묶음·다음 묶음·SHA | `fiction/analysis/SCENE_PASS_REGISTRY.json` |
| 제6~10화 수동 장면 카드 | `fiction/analysis/SCENE_CARDS_006_010.md` |
| 대표 3화 파일럿 근거 | `fiction/reports/REVISION_2026-07-23_PILOT_10_95_180.md` |
| 제6~10화 변경 근거 | `fiction/reports/REVISION_2026-07-23_SCENE_PASS_006_010.md` |
| 출처·원본 가용성·Google Docs 상태 | `fiction/SOURCE_MANIFEST.md` |
| 인수인계 | `fiction/HANDOFF.md` |
| 과거 자료 | `fiction/archive/` — 기본 입력 금지 |
| Skill 선택 | `[소설]/00_운영체계/SKILL_REGISTRY.json` |

## 파생 분석본 규칙

색인과 역개요는 활성 manifest가 immutable baseline과 승인된 묶음 override를 합성한다. baseline을 직접 소비하지 않고 `tools/fiction_composed_data.py`만 사용한다. 수동 장면 카드는 완료 묶음의 현재 해석과 경계 상태를 책임진다. 역개요·진단 보고서는 원고와 색인을 탐색하는 파생 분석본이다. 모든 분석본은 원고·Canon보다 우선하지 않으며 원고 변경 시 같은 PR에서 갱신한다.

Revision Report는 특정 변경의 근거·범위·회귀 결과를 책임지며 현재 다음 작업을 지시하지 않는다. 현재 작업은 항상 `ACTIVE_CONTEXT.md`를 따른다.

## 단일 책임 원본

같은 질문은 한 활성 파일만 책임진다. 과거 초안은 Git 이력 또는 archive에만 둔다. `latest`, `final`, `v2` 활성 복제본을 만들지 않는다. 구형 문서나 이름을 바꾸면 `fiction-canon-and-research: reference-freshness`와 `fiction-revision-and-validation: regression-check`를 실행한다.

## 자동 검증

- `python tools/check_fiction_operating_system.py`
- `python tools/check_fiction_content.py`
- `python tools/build_fiction_reverse_outline.py --check`
- `python tools/check_fiction_reverse_outline.py`
- `python tools/check_fiction_scene_passes.py`
