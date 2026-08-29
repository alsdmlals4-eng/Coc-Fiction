# AGENTS.md

이 저장소는 **Coc-Fiction / 장편 서사 프로젝트**다. 게임 런타임 프로젝트가 아니며 Godot 관련 실행·Scene·Resource 규칙은 `NOT_APPLICABLE`이다.

## 권한 순서

1. 사용자의 최신 직접 지시
2. 이 `AGENTS.md`
3. `docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md`
4. `fiction/ACTIVE_CONTEXT.md`와 승인된 작업 계약
5. 작품 정본과 실제 원고·구조화 데이터·검사
6. 프로젝트 내부 운영 문서와 채택된 Base 계약
7. Base 원격과 외부 자료

## 최초 읽기

```text
[소설]/00_운영체계/START_HERE.md
→ docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ docs/fiction-ops/CURRENT_STATE_RECEIPT.json
→ 현재 묶음 Scene Card / Revision Report / 실제 manuscript
```

`CURRENT_STATE_RECEIPT.json`의 SHA/PR은 현재 production frontier가 마지막으로 바뀐 readback 증거다. 저장소의 영구적인 최신 SHA/PR이 아니므로 재개할 때는 반드시 최신 `main`과 open PR 상태를 다시 조회한다.

## Repository-only 정본 경계

- GitHub repository가 사람용 작품 정본, 구조화 Canon, 원고 production frontier, 검사·evidence와 current handoff의 단일 활성 owner다.
- 과거 Notion summary/Event/Relation/page/database/attachment는 `HISTORICAL_MIGRATION_REFERENCE_ONLY`다. routine current work의 read/write/sync/destination readback 또는 완료 조건으로 사용하지 않는다.
- `fiction/ACTIVE_CONTEXT.md`, 과거 handoff와 receipt에 남은 Notion sync/readback 문구는 `docs/fiction-ops/REPOSITORY_AUTONOMOUS_RESEARCH_AND_LEARNING_POLICY_2026-08-29.md`와 충돌하는 범위에서 `SUPERSEDED_HISTORICAL_COMPATIBILITY`다.
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

## 조사·현실성·장기 품질

중요한 작품·운영·시각 결정을 확정하기 전 다음을 수행한다.

```text
current canon + actual manuscript + production frontier
→ existing project solution / adopted Base owner
→ targeted current official or primary research when material
→ directly relevant success / failure / mixed cases
→ materially distinct alternatives
→ ADOPT / ADAPT / REJECT
→ FEASIBLE / PARTIAL / BLOCKED_UNVERIFIED
→ bounded change / exact verification / readback
```

- 외부 자료는 Canon을 자동 변경하지 않는다.
- 참고 작품의 문장·고유 문체·표면 장치를 복제하지 않는다.
- 빠른 문장 수정 하나보다 장기 원고 일관성, 재개 가능성, 검증 가능성, rollback과 독자 경험을 우선한다.
- 미래 가능성만을 위한 중복 schema, dashboard, index와 process 문서를 만들지 않는다.
- 계획·역개요·자동 진단·QA 후보가 존재해도 manuscript promotion, 전체 연속성, 독자 반응 또는 출판 준비를 자동 증명하지 않는다.

## 자동화·사용자 관여·학습

승인 범위 안의 fresh-read, 조사, source receipt, Canon conflict scan, bounded propagation, 자동 검사, readback, 가역적 교정, 남은 작업 재계산과 다음 안전 묶음 준비는 routine 재승인 없이 계속한다.

사용자에게는 작품 중심 질문·결말·주요 인물성·세계관 Canon, 중요한 장면 의미의 취향 선택, 최종 Visual Direction, 외부 공개·출판·비용·권리, 되돌리기 어려운 삭제·대규모 renumbering·migration만 올린다.

학습은 모델의 임의 영구 기억이 아니라 다음 repository loop다.

```text
problem
→ root cause
→ bounded fix
→ exact verification
→ regression guard
→ project owner / handoff
→ broadly reusable할 때 Base promotion candidate
```

## 시각 후보

실제 consumer가 있는 표지·삽화·마케팅 visual 또는 승인된 사람용 Blueprint/GDD에 필요한 구체적 시각 후보는 현재 Canon·인물·세계·톤, 기존 승인 Visual·시안과 권리를 먼저 읽는다.

```text
actual consumer + target spec
→ keep / avoid / do not drift
→ image-model-generated bounded candidate
→ objective QA
→ user LOCK / REVISE / REJECT / REFERENCE_ONLY
```

필요한 candidate는 이미지별 사전 승인 없이 먼저 제작할 수 있다. 사용자 lock 전에는 정본·외부 배포 asset으로 승격하지 않는다. `GENERATED_CANDIDATE != USER_APPROVED != CANON_REGISTERED != DISTRIBUTION_READY`다. SVG·Canvas·Python drawing·code-drawn vector를 이미지 모델 대용으로 사용하지 않는다.

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

GitHub 변경 뒤 exact head를 검증하고, 허용된 경우 병합한 다음 새 `main`, 변경 owner, `CURRENT_STATE_RECEIPT`와 successor context를 repository에서 readback한다. Notion CURRENT 갱신·sync·readback은 완료 조건이 아니다.

완료 보고는 source/static validation, manuscript/registry propagation, automated test, reader/human evidence, publication readiness를 구분한다. 실행하지 않은 증거는 `NOT_RUN` 또는 `UNVERIFIED`로 남긴다.
