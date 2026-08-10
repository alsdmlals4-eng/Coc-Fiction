# 《폭풍의 눈》 활성 인수인계

갱신: 2026-08-10

## 먼저 읽을 파일

1. `FICTION_MASTER.md`
2. `ACTIVE_CONTEXT.md`
3. `CANON_REGISTRY.json`
4. `SOURCE_MANIFEST.md`
5. `sources/PRIMARY_SOURCE_INVENTORY.md`
6. `analysis/SCENE_PASS_REGISTRY.json`
7. 현재 묶음의 `analysis/SCENE_CARDS_*.md`
8. 최신 `reports/REVISION_*.md`
9. `analysis/REPRESENTATIVE_CHAPTER_GATES.md`
10. `analysis/REVERSE_OUTLINE_REPORT.md`
11. `MANUSCRIPT_INDEX.json`
12. 해당 부 Story Bible과 현재 작업 원고
13. 외부 최신 재퇴고본을 정본화하는 작업이면 `ACTIVE_CONTEXT.md`의 `외부 작업 산출물`과 `다음 정확한 저장소 작업` 절

## 현재 GitHub main 상태

기준: `c9c4fa647c833470759ada2514e45d1b2abb1e8b`

- 225화·45개 묶음 정상
- `006-010` 내부 연속성 패스 완료
- `091-095` 원본 직접 대조 패스 완료
- 원본 PDF 인벤토리 확보, 전체 직접 감사는 진행 중
- 기존 다음 대기 작업 `176-180` 원본 대조는 보존되어 있음
- PR #13 운영 통합 완료: Base 공용 serial-fiction 책임 재사용, 프로젝트 `serial-arc-pass` 흡수, `001-105 canon reconciliation`을 현재 우선순위로 통일.
- PR #14 Canon 동기화 완료: 주안 자기통제 프로토콜, 2부 버실라/Woff 제외, 아킴 허용, 기존 DRAFT migration debt의 fail-closed 봉인.

## 현재 대화의 최신 외부 산출물

2026-08-10 프로젝트 대화에서 제1~105화에 대해 POV·후크·캐릭터 일관성 재퇴고와 통합 QA를 수행한 별도 산출물이 있다.

- `폭풍의눈_2차퇴고_제001-105화_POV후크_캐릭터_통합최종본.zip`
- `폭풍의눈_제001-105화_통합최종_QA보고서.md`

이 산출물은 **현재 대화 기준 최신 작업 증거**지만 아직 GitHub `fiction/manuscript/`의 225화 Markdown 정본으로 전파됐다고 확인되지 않았다.

```yaml
external_revision_001_105: COMPLETE_AS_ARTIFACT
github_canon_propagation: NOT_RUN
```

따라서 다음 작업자는 둘 중 하나를 무조건 정본으로 선언하지 말고 source/canon/current manuscript와 실제 delta를 대조해야 한다.

## 외부 재퇴고본에서 보존할 작품별 원칙

- 한 화의 실제 POV 인물은 필요에 따라 1~3명을 사용할 수 있다. 이 수치는 《폭풍의 눈》 프로젝트 값이며 Base 전역 규칙이 아니다.
- 같은 사건도 POV가 달라지면 정보·감정·판단·말투·연출의 체감이 달라져야 한다.
- 주연 외 조연·엑스트라 POV도 새 정보·오해·공포·평판·직업적 관찰을 추가할 때 허용한다.
- 무표식 head-hopping은 피하고 전환 경계를 독자가 알 수 있게 한다.
- 화마다 상태 변화를 주고 Local Payoff와 다음 행동 압력을 함께 본다.
- 캐릭터의 판단 습관·윤리선·말투·관계 상태를 회귀 검사한다.
- 2부 `버실라 / 바실라 / Versilla / Woff` 직접 등장·개인 서사·독립 기능 복원 금지.
- 아킴 등장 허용.

## Base / 프로젝트 운영 경계

- 프로젝트 운영 호환성 감사 adopted Base 기준점: `53e63f7ebefbb5b2fc0dc528e335252692801421`
- 현재 확인한 Base main: `49f6190b9b5a535ceb7986755c1b68b221754cf5`
- Base `developing-and-revising-serial-fiction`의 공용 작법 원칙을 재사용한다.
- Coc-Fiction 프로젝트 Skill은 기존 5개를 유지한다.
- 장편 묶음 작업의 프로젝트 고유 파생자료 전파는 `fiction-revision-and-validation: serial-arc-pass`가 담당한다.
- stale PR #9 전체를 병합하지 않는다. closed/unmerged #12에서 검증된 고유 delta만 현재 main 위에 흡수했다.

### Base proposal handoff

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

BCP-012는 새 Canon Decision과 기존 DRAFT migration 완료 상태를 분리하고, 기존 legacy debt를 정확한 consumer set으로 봉인해 새 위치로 확산되면 실패시키는 공용 lifecycle 제안이다. **Proposal PR 병합은 Base 활성 구현 승인과 무관하다.**

## 외전1 종결 고정 — GitHub current canon

- 제90화에서 주안·아킴·조세이칸이 한국에 도착한다.
- 제91화는 한국 도착 첫날 밤의 명시적 회상으로 비행 전날 티베트 야영지·이가레스 문답을 복원한다.
- 제92화는 세 사람의 한국 공동생활과 경주 관광을 닫는다.
- 제93화는 윌리엄의 과잉 보호와 엘리스의 주안 위치 질문, 세실리아·엘레인 이동을 다룬다.
- 제94화는 엘리스가 일반 전화로 이안에게 주안의 티베트·위구르 생존을 확인한다.
- 제95화는 다빈·예나의 호텔 앞 소문과 고기 약속으로 다음 이야기를 예고한다.
- 제96화는 ‘시간은 다시 여덟 해 전’으로 외전2 과거편을 연다.

이 절은 현재 GitHub main의 직접 대조 결과다. 외부 제1~105화 재퇴고본과 충돌할 경우 임의로 한쪽을 폐기하지 말고 원본·최신 사용자 지시를 기준으로 `KEEP / APPLY / REWORK / REJECT` 판정한다.

## 원본·각색 상태

- 외전1 원본 113~147쪽 핵심 사건: `SOURCE_MATCHED`
- 오션 후일담·아프리카 임무·독립 마피아/동물 장기축: 최신 사용자 지시에 따라 제외
- 호출기: 비상 신호와 수신 확인만 가능. 제94화 연락은 일반 전화.
- 원본의 모든 농담·애드리브를 복제하지 않으며 인물 핵심·사건 결과·인계 기능을 우선한다.

## 다음 작업자의 첫 행동

1. 제1~105 최신 통합 산출물의 실제 파일을 확보한다.
2. GitHub `fiction/manuscript/`의 제1~105와 회차별 diff를 만든다.
3. 원본 사건 기록·최신 사용자 Decision·Canon 우선순위를 대조한다.
4. 한 번에 5화씩 `serial-arc-pass`를 사용해 `KEEP / APPLY / REWORK / REJECT`를 판정한다.
5. 원고 수정이 승인되면 색인·역개요 override·Scene Pass Registry·Revision Report를 같은 기준 commit으로 갱신한다.
6. 001-105 정본화가 끝난 뒤 106+ 연속 작업 및 보류된 `176-180` 원본 대조의 순서를 다시 정한다.

## 작업 절차

원본 파일·해시 확인 → 현재 묶음과 앞뒤 경계 → Canon·폐기 설정 → 수동 장면 카드 → source finding → 적대적 재판정 → 승인 범위 수정 → index/outline override → Registry·Report·기획 문서 → 구형 참조 회귀 → PR·CI·병합 순으로 진행한다.

## 주의

- baseline·archive·구형 Google Docs를 직접 작업 입력으로 사용하지 않는다.
- 원본 본체가 있어도 파일명만으로 정본을 판단하지 않는다.
- 원본 사건과 최신 사용자 지시가 충돌하면 사용자 지시를 우선하고 제외 근거를 기록한다.
- 외부 DOCX의 ‘최종’ 표기만으로 GitHub Canon 승격을 선언하지 않는다.
- 과거 CI·과거 PR head의 검증을 현재 head 검증처럼 재사용하지 않는다.
- Base BCP-012의 proposal-only 병합을 Base 활성 구현 승인으로 해석하지 않는다.
