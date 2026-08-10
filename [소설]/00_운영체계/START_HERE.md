# Coc-Fiction 소설 작업 시작 지점

## 최초 읽기

```text
docs/coordination/CONCURRENT_WORK.md
→ [소설]/00_운영체계/OPERATING_MODEL.md
→ [소설]/00_운영체계/DOCUMENTATION_MAP.md
→ fiction/FICTION_MASTER.md
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/SOURCE_MANIFEST.md
→ fiction/sources/PRIMARY_SOURCE_INVENTORY.md
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ 현재 묶음의 Scene Card·Revision Report
→ fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md
→ fiction/analysis/REVERSE_OUTLINE_REPORT.md
→ fiction/MANUSCRIPT_INDEX.json
→ fiction/STYLE_GUIDE.md
→ 현재 원고 묶음
```

색인과 역개요의 대형 데이터는 manifest+override로 합성한다. baseline은 직접 작업 입력으로 읽거나 수정하지 않는다.

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- GitHub 저장 토폴로지: 225화/45묶음 구조를 유지하지만, 외부 최신 제1~105화의 압축 편성을 5화씩 선택적으로 정본화하는 **mixed migration** 상태다.
- 외부 최신 작업: 제1~105화 POV·후크·캐릭터 통합 재퇴고본 존재.
- 외부 reconciliation 완료 prefix: **제1~5화**.
- 제1~5 최신 제목/본문은 GitHub manuscript에 적용했고 원본 COC 사건·최신 Canon·신호기 제한을 대조했다.
- 저장소 구 제6화 이후는 아직 legacy tail이며 제5→6의 서사 연속성은 `NOT_YET_CLAIMED`다.
- 진행 중 우선순위: 외부 최신 제6~10화와 legacy 저장 묶음 `fiction/manuscript/part-1/006-010.md`의 선택적 정본 reconciliation.
- 기존 `176-180` 원본 직접 대조는 삭제하지 않고 reconciliation 이후 대기 작업으로 유지.

## 프로젝트 Skill

- `fiction-project-operations`: 범위·계약·체크포인트·인수인계·병합
- `fiction-story-development`: 코어·인과·인물·장면 카드·stress-test
- `fiction-drafting`: 승인된 POV·대화·묘사·리듬 수정
- `fiction-canon-and-research`: 원본 로그·Canon·연표·출처·구형 참조 감사
- `fiction-revision-and-validation`: 구조·묶음 퇴고·연속성·적대적 검토·회귀·PR 검수

Base의 `developing-and-revising-serial-fiction`은 공용 작법·연재 pacing·POV/voice 원칙을 제공한다. 작품 Canon, 원본 로그, 합성 색인, reverse-outline override, Scene Pass Registry 같은 프로젝트 고유 책임은 위 5개 프로젝트 Skill에 남긴다.

## 절대 우선순위

최신 사용자 지시 → 작품 코어·Canon Registry → 접근 가능한 원본 사건 기록 → 부별 바이블·연속성 → 현재 원고 → 수동 장면 카드·Revision Report → 역개요·진단 → 외부 참고.

외부 최신 재퇴고본과 GitHub current manuscript가 충돌하면 파일명의 `최종` 표기만으로 어느 한쪽을 자동 승격하지 않는다. 위 우선순위로 회차별 delta를 재판정한다.

## 보호 규칙

- 구형 Google Docs·압축 초안·구 편성을 활성 입력으로 사용하지 않는다.
- 원본에 존재해도 최신 사용자 지시가 폐기한 축은 복원하지 않는다.
- 자동 역개요와 정량 플래그를 수정 명령으로 쓰지 않는다.
- `SOURCE_MATCHED`를 문장 전체 복사로 해석하지 않는다.
- 묶음 수정 뒤 원본·인과·POV·시간·동선·상태·금지 설정·색인·역개요·Registry·기획 문서 회귀를 남긴다.
- stale PR은 전체 rebase/merge보다 current main 위 고유 delta 선택적 재적용을 우선한다.
- 외부 최신 prefix와 unreconciled legacy tail 사이에는 `SCENE_PASS_REGISTRY.external_artifact_reconciliation`의 migration boundary를 따른다. 그 경계를 자동 역개요의 정상 `next_chapter`로 해석하지 않는다.

## 다음 시작 묶음

`fiction/manuscript/part-1/006-010.md`.

목적은 구 `006-010` 내부 연속성 패스를 반복하는 것이 아니라, 현재 대화의 최신 외부 제6~10화와 GitHub legacy `006-010`의 delta를 원본·최신 사용자 Decision·Canon으로 다시 판정하는 `EXTERNAL_ARTIFACT_CANON_RECONCILIATION`이다.

```text
006-010 외부/legacy 원고 대조
→ 제5화 새 종료 상태에서 앞 경계 확인
→ KEEP / APPLY / REWORK / REJECT
→ 원본 사건·POV·인물 상태 검증
→ 승인된 delta만 적용
→ index / outline override / Scene Pass Registry / Revision Report 전파
→ reconciled prefix를 10까지 확장
→ 다음 5화
```

`176-180` 원본 직접 대조는 `SCENE_PASS_REGISTRY.json#/deferred_bundle_passes`에 보존한다.

## 작업 단계 지도

- Work Mode: `PLAN → BUILD → REVIEW`
- Manuscript Stage: `DISCOVER → OUTLINE → DRAFT → REVISE → POLISH`
- 현재 단계는 `REVIEW / REVISE`이며, 다음 묶음도 계획·원본 대조·승인된 수정·회귀 검증 순서를 생략하지 않는다.
