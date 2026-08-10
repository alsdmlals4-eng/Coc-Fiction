# ACTIVE CONTEXT

갱신: 2026-08-10

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- 프로젝트 주 책임: `fiction-canon-and-research: source-log / canon-audit / continuity-map / timeline-and-state`
- 프로젝트 보조 책임: `fiction-revision-and-validation: serial-arc-pass / scene-diagnostic / adversarial-loop / regression-check / pr-review`, `fiction-story-development: scene-card / plot-and-causality / stress-test`, `fiction-drafting: approved-rewrite / pov-and-distance / dialogue-and-subtext`, `fiction-project-operations: checkpoint / handoff / execution-report`
- Base 공용 작법: `developing-and-revising-serial-fiction`의 Canon/각색 경계, POV·voice, 회차 가치, Local Payoff/Open Loop를 선택적으로 재사용한다.

## GitHub main에서 검증된 완료 상태

기준 main: `c9c4fa647c833470759ada2514e45d1b2abb1e8b`

- 제1화~제225화와 45개 5화 묶음 유지
- 구조 역개요 기준선·대표 게이트·제10·95·180화 파일럿 완료
- `006-010` 내부 연속성 패스와 제6·7·9화 최소 수정 완료
- 원본 1부·외전1·2부 PDF 파일 인벤토리와 SHA256 등록
- `091-095` 원본 직접 대조 패스 완료
- 외전1 종결의 이가레스 문답 → 한국 정착 → 엘리스·이안 통화 → 다빈·예나 예고 순서 복원
- 제90·96화 SHA 보존, 제91~95화만 색인·역개요 override 갱신
- PR #13에서 Base 공용 `developing-and-revising-serial-fiction` 재사용, 프로젝트 `serial-arc-pass` 흡수, `001-105 canon reconciliation`을 다음 우선순위로 정리했다.
- PR #14에서 최신 사용자 Decision을 Canon에 동기화했다: 주안 `반응 → 멈춤 → 이유 → 선택`, 2부 `버실라 / 바실라 / Versilla / Woff` 제외, 아킴 등장 허용.
- PR #14는 기존 DRAFT의 폐기 설정 debt를 blind rewrite하지 않고 정확한 consumer set으로 봉인해 신규 확산만 fail-closed하는 migration debt 계약을 프로젝트에 적용했다.

## 현재 대화에서 완료된 외부 작업 산출물

2026-08-10 현재 프로젝트 대화에서 **제1~105화 POV·후크·캐릭터 통합 재퇴고본**이 별도 DOCX 묶음으로 제작·검수됐다.

확인된 산출물 이름:

- `폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip`
- `폭풍의눈_제001-105화_통합최종_QA보고서.md`

해당 산출물에서 사용한 주요 편집 원칙:

- 한 화의 실제 POV 인물은 필요에 따라 1~3명까지 사용한다. **이 숫자는 작품별 production rule이며 Base 공용 규칙이 아니다.**
- 같은 사건도 POV에 따라 정보·감정·판단·대화 반응·연출이 달라져야 한다.
- 주연뿐 아니라 조연·엑스트라 POV도, 주연이 모르는 정보·오해·공포·외부평가·직업적 관찰을 실제로 추가할 때 사용할 수 있다.
- 화 안에서 상태 변화와 Local Payoff를 주고, 다음 행동을 요구하는 질문·발견·선택·위험·감정 변화 중 하나를 Open Loop로 남긴다.
- 캐릭터의 판단 습관·말투·윤리선·관계 상태를 회귀 검사한다.
- 2부 `버실라 / 바실라 / Versilla / Woff` 직접 등장·개인 서사·독립 기능 복원은 금지한다. 아킴은 등장 가능하다.

### 증거 경계

위 제1~105화 산출물은 **현재 대화의 최신 작업 결과**다. 그러나 아직 GitHub `fiction/manuscript/`의 225화 Markdown과 동일한 정본으로 병합됐다는 증거는 없다.

따라서 현재 상태는 다음처럼 분리한다.

```yaml
github_manuscript_main: 225화 DRAFT / 006-010 및 091-095 검증 반영
external_current_chat_revision_001_105: COMPLETE_AS_ARTIFACT
external_revision_github_canon_propagation: NOT_RUN
```

외부 DOCX를 GitHub 정본보다 우선한다고 자동 선언하거나, 반대로 GitHub의 오래된 해당 회차를 최신 대화 작업보다 최신이라고 추정하지 않는다. 양쪽을 원본 사건 기록·최신 사용자 결정과 대조해 선택적으로 통합해야 한다.

## Base 적용 상태

- 프로젝트 운영 호환성 감사의 adopted Base 기준점: `53e63f7ebefbb5b2fc0dc528e335252692801421`
- 현재 확인한 Base main: `49f6190b9b5a535ceb7986755c1b68b221754cf5`
- Base BCP-009의 `developing-and-revising-serial-fiction`은 공용 작법·검수 책임으로 재사용한다.
- Coc-Fiction의 프로젝트 Skill은 5개를 유지한다.
- stale PR #9의 유효 고유 delta는 새 Skill이 아니라 `fiction-revision-and-validation: serial-arc-pass`로 선택적 흡수했다.
- stale #9 전체 branch를 merge/rebase하지 않는다.

### Base proposal locator

```yaml
base_proposal:
  id: BCP-2026-012-serial-fiction-canon-migration-debt
  proposal_pr: https://github.com/alsdmlals4-eng/Base/pull/234
  merged_to_base_main: true
  base_main_after_merge: 49f6190b9b5a535ceb7986755c1b68b221754cf5
  proposal_status: SUBMITTED
  existing_solution_verdict: ABSORB
  proposal_storage_merge_authority: GRANTED_BY_SINGLE_FILE_EXECUTION_CONTRACT
  base_implementation_authority: NOT_GRANTED_IN_THIS_STAGE
  implementation_status: NOT_STARTED_IN_THIS_STAGE
  implementation_boundary: SEPARATE_FOLLOWUP_STAGE
  active_base_files_changed_by_proposal_pr: 0
  next_action: 별도 후속 단계에서 구현 승인·추가 증거를 확인하기 전까지 Base 활성 구현 금지
```

BCP-012는 프로젝트에서 검증된 `Canon Decision의 즉시 유효성`과 `기존 DRAFT migration 완료 상태`를 분리하고, 기존 debt를 정확한 consumer set으로 봉인해 새 위치로 증가하면 실패시키는 lifecycle을 공용 후보로 제안한다. 이 제안 병합은 Base 활성 구현 승인이 아니다.

## 작품별 고정 연속성

1. 원본 사건 순서가 현행 각색 장면으로 대체됐다면 주제적 장점만으로 유지하지 않는다.
2. 이미 다음 시간대에 도착한 경계 뒤에서 원본 선행 사건을 복원할 때는 명시적 회상 앵커를 둔다.
3. 호출기와 일반 전화·녹음 장치를 기능별로 분리한다.
4. 원본에 있어도 최신 사용자 지시가 폐기한 사건·인물축은 복원하지 않는다.
5. `SOURCE_MATCHED`는 사건 순서·동행·결과 판정이며 문장 전체 복사를 뜻하지 않는다.
6. 외부 재퇴고본의 fixed POV count 같은 작품 값은 Base 공용 표준으로 승격하지 않는다.

## 다음 정확한 저장소 작업

**제1~105화 외부 통합 재퇴고본을 GitHub 정본에 바로 덮어쓰지 말고, 먼저 source/canon/current manuscript와 대조해 delta를 회수하는 `001-105 canon reconciliation`을 수행한다.**

순서:

```text
제1~105 최신 외부 산출물 확보
→ GitHub current manuscript의 같은 화 대조
→ 원본 사건 기록·최신 사용자 Decision 우선순위 확인
→ 회차별 KEEP / APPLY / REWORK / REJECT 판정
→ 5화 단위 serial-arc-pass
→ 승인된 원고 delta만 적용
→ MANUSCRIPT_INDEX·역개요 override·Scene Pass Registry·Revision Report 전파
→ 적대적 회귀·PR
```

이 reconciliation이 끝나기 전에 GitHub 225화 원고를 기준으로 제106화 이후를 ‘이미 연속된 최신본’이라고 간주하지 않는다. 기존 `176-180` 원본 대조 작업은 삭제하지 않고 **001-105 최신본 정본화 뒤의 대기 작업**으로 유지한다.

## 변경 금지

`FICTION_MASTER.md`와 `CANON_REGISTRY.json`을 따른다. 자동 역개요는 수정 명령이 아니다. 원고 수정 시 색인·역개요·Scene Pass Registry·Revision Report·활성 기획 문서를 같은 PR에서 갱신한다. 외부 산출물 존재만으로 GitHub Canon 완료를 주장하지 않는다. Base BCP-012의 병합을 Base 활성 구현 승인으로 해석하지 않는다.
