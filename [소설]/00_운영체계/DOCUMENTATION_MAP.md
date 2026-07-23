# Coc-Fiction Documentation Map

## 질문별 책임 원본

| 질문 | 책임 원본 |
|---|---|
| 현재 상태와 다음 작업 | `fiction/ACTIVE_CONTEXT.md` |
| 작품 정체성·변경 금지 | `fiction/bible/01_PROJECT_CORE.md` |
| 우선순위·편성·작업 기준 | `fiction/FICTION_MASTER.md` |
| Canon·폐기·별칭 | `fiction/CANON_REGISTRY.json` |
| 인물·세계·연속성 | `fiction/bible/02_CANON_AND_CONTINUITY.md` |
| 1부·외전1·2부 구조 | `fiction/bible/03_PART1_STORY_BIBLE.md`, `fiction/bible/04_PART2_STORY_BIBLE.md` |
| 원본 파일명·SHA·가용성 | `fiction/sources/PRIMARY_SOURCE_INVENTORY.md` |
| 출처 정책·직접 대조 범위 | `fiction/SOURCE_MANIFEST.md` |
| 실제 확장 원고 | `fiction/manuscript/` |
| 화별 제목·POV·분량·SHA | `fiction/MANUSCRIPT_INDEX.json` |
| 구조 역개요 | `fiction/analysis/REVERSE_OUTLINE_001_225.json`, `fiction/analysis/REVERSE_OUTLINE_REPORT.md` |
| 대표 품질 판정 | `fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md` |
| 완료 묶음·경계·SHA | `fiction/analysis/SCENE_PASS_REGISTRY.json` |
| 제6~10화 카드 | `fiction/analysis/SCENE_CARDS_006_010.md` |
| 제91~95화 원본 카드 | `fiction/analysis/SCENE_CARDS_091_095.md` |
| 제6~10화 변경 근거 | `fiction/reports/REVISION_2026-07-23_SCENE_PASS_006_010.md` |
| 제91~95화 원본 변경 근거 | `fiction/reports/REVISION_2026-07-23_SOURCE_PASS_091_095.md` |
| 인수인계 | `fiction/HANDOFF.md` |
| Skill 선택 | `[소설]/00_운영체계/SKILL_REGISTRY.json` |

## 파생 데이터 규칙

색인과 역개요는 활성 manifest가 immutable baseline과 승인된 묶음 override를 합성한다. 소비자는 `tools/fiction_composed_data.py`를 사용한다. baseline과 과거 Revision Report는 현재 다음 작업을 지시하지 않는다.

## 단일 책임·구형 방지

같은 질문은 한 활성 파일만 책임진다. 과거 자료의 대체 관계는 Source Manifest가 관리한다. 활성 문서가 구형 Google Docs ID·압축 초안·140화 편성·과거 단계 문구를 참조하면 검증 실패다.

## 자동 검증

- `python tools/check_fiction_operating_system.py`
- `python tools/check_fiction_content.py`
- `python tools/build_fiction_reverse_outline.py --check`
- `python tools/check_fiction_reverse_outline.py`
- `python tools/check_fiction_scene_passes.py`
