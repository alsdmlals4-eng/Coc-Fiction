# AGENTS.md

이 저장소는 **Coc-Fiction / 장편 서사 프로젝트**다. 게임 런타임 프로젝트가 아니며 Godot 관련 실행·Scene·Resource 규칙은 `NOT_APPLICABLE`이다.

## 권한 순서

1. 사용자의 최신 직접 지시
2. 이 `AGENTS.md`
3. `fiction/ACTIVE_CONTEXT.md`와 승인된 작업 계약
4. 작품 정본과 실제 원고·구조화 데이터·검사
5. 프로젝트 내부 운영 문서와 채택된 Base 계약
6. Base 원격과 외부 자료

## 최초 읽기

```text
[소설]/00_운영체계/START_HERE.md
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ docs/fiction-ops/CURRENT_STATE_RECEIPT.json
→ 현재 묶음 Scene Card / Revision Report / 실제 manuscript
```

`CURRENT_STATE_RECEIPT.json`의 SHA/PR은 현재 production frontier가 마지막으로 바뀐 readback 증거다. 저장소의 영구적인 최신 SHA/PR이 아니므로 재개할 때는 반드시 최신 `main`과 open PR 상태를 다시 조회한다.

## 정본 경계

- 외부/Library의 `QA_GREEN` candidate는 **revision input**이며 자동으로 GitHub production authority가 되지 않는다.
- GitHub production authority는 `SCENE_PASS_REGISTRY.json`의 bounded reconciliation frontier가 책임진다.
- `current prefix / legacy tail / migration boundary`를 인접 화수만으로 자동 연결하지 않는다.
- `whole_manuscript_continuity=NOT_YET_CLAIMED`를 전체 연속성 완료로 확대 해석하지 않는다.
- Canon과 사용자 Decision이 파생 역개요·자동 진단보다 우선한다.

## 보호 규칙

- 진행 중 `open/draft/ready` PR은 사용자가 현재 작업에서 PR 번호와 허용 동작을 명시하지 않는 한 **read-only**다.
- 닫힌 RED/diagnostic PR과 과거 migration 자료는 역사 증거이며 임의 삭제·재병합하지 않는다.
- `엘리스`가 Alice Carter의 현행 한글 Canon 표기다.
- 주안의 `반응 → 멈춤 → 이유 → 선택`, Scene-Locked Hybrid, D01/D02/D03/N04 및 귀속 미정 공동봉인 규칙을 회귀시키지 않는다.
- 기존 5화 bounded promotion을 대규모 일괄 승격으로 바꾸지 않는다.

## 검증

소설/운영 변경은 exact head에서 최소 다음을 실행한다.

```bash
python tools/check_fiction_operating_system.py
python tools/check_fiction_content.py
python tools/build_fiction_reverse_outline.py --check
python tools/check_fiction_reverse_outline.py
python tools/check_fiction_scene_passes.py
python -m unittest tests.test_current_state_closure -v
python -m unittest tests.test_fiction_docx_packaging -v
```

추가 테스트가 도입된 변경은 해당 테스트도 함께 실행한다. 과거 Green을 현재 head의 Green으로 재사용하지 않는다.

## 완료

GitHub 병합 뒤 새 `main`을 다시 읽고, Notion CURRENT 정본이 적용되는 변경이면 GitHub 증거 이후에만 사람용 CURRENT 페이지를 갱신한다. GitHub와 Notion을 모두 readback한 뒤에만 `SYNCED` 또는 완료로 보고한다.
