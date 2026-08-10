# 《폭풍의 눈》 현행 정본·작업 기준

상태: **ACTIVE / SINGLE SOURCE OF TRUTH**
최종 갱신: 2026-08-10

## 1. 책임 원본

| 질문 | 현행 책임 원본 |
|---|---|
| 작품 정체성·주제·변경 금지 | `bible/01_PROJECT_CORE.md` |
| Canon 상태·별칭·폐기 | `CANON_REGISTRY.json` |
| 세계·인물·연속성·부별 설계 | `bible/02_CANON_AND_CONTINUITY.md`, `bible/03_PART1_STORY_BIBLE.md`, `bible/04_PART2_STORY_BIBLE.md` |
| POV·문체·표기 | `STYLE_GUIDE.md` |
| 실제 저장 원고 | `manuscript/` |
| 화별 제목·POV·분량·원문 SHA | `MANUSCRIPT_INDEX.json` |
| 저장 원고 구조 역개요·구조 진단 | `analysis/REVERSE_OUTLINE_001_225.json`, `analysis/REVERSE_OUTLINE_REPORT.md` |
| 대표 게이트·완료 묶음 패스 | `analysis/REPRESENTATIVE_CHAPTER_GATES.md`, `analysis/SCENE_PASS_REGISTRY.json` |
| 원본 파일·감사 상태 | `SOURCE_MANIFEST.md`, `sources/PRIMARY_SOURCE_INVENTORY.md` |
| 현재 상태·다음 작업 | `ACTIVE_CONTEXT.md` |
| 인수인계 | `HANDOFF.md` |

## 2. 정본 우선순위

1. 사용자의 가장 최근 직접 지시
2. 본 코어 계약과 Canon Registry
3. 접근 가능한 원본 TRPG 로그/PDF의 사건 순서·인물 동행·결과
4. 부별 스토리 바이블·연속성 문서
5. 현재 승인·검증된 원고 delta
6. 수동 장면 카드·Revision Report
7. 구조 역개요·진단 보고서
8. 외부 참고

색인과 역개요는 활성 manifest가 immutable baseline과 승인된 묶음 override를 합성한다. baseline을 직접 편집 입력으로 사용하지 않는다. 원고·Canon과 충돌하면 파생 분석을 갱신하며 분석을 근거로 원고를 자동 덮어쓰지 않는다.

현재 대화의 제1~105화 통합 재퇴고본은 최신 작업 증거다. 이 외부 산출물 전체를 파일명의 `최종` 표기만으로 자동 정본 승격하지 않고 `ACTIVE_CONTEXT.md`의 reconciliation 절차에 따라 원본·최신 사용자 지시·현행 Canon과 5화씩 대조한다. **제1~5화는 2026-08-10 reconciliation을 통과해 GitHub manuscript에 반영됐고, 제6화 이후는 아직 legacy tail이다.**

## 3. 저장 토폴로지와 narrative migration

현재 저장소는 기존 225화 파일 경로·bundle 구조를 migration 컨테이너로 유지한다.

- 저장 `part-1`: 제1화~제70화
- 저장 `side-story-lake`: 제71화~제95화
- 저장 `side-story-alice`: 제96화~제130화
- 저장 `side-story-ian`: 제131화~제165화
- 저장 `part-2`: 제166화~제225화

**이 225화 구간표는 현재 narrative numbering의 최종 편성 선언이 아니다.** 외부 최신 제1~105화는 사건을 압축·재편성했고, GitHub는 이를 5화씩 source/canon reconciliation 중이다. `SCENE_PASS_REGISTRY.external_artifact_reconciliation`의 `reconciled_prefix_end` 이후 stored chapter는 자신의 reconciliation을 통과하기 전까지 legacy tail로 취급한다.

2026-08-10 현재:

```yaml
reconciled_prefix: 1-5
legacy_tail_starts_at: 6
whole_manuscript_continuity: NOT_YET_CLAIMED
next_reconciliation: 6-10
```

따라서 새 제5화 뒤에 저장 구 제6화를 자동으로 ‘다음 사건’이라고 간주하지 않는다. reverse outline도 migration boundary에서 `next_chapter / previous_chapter` 연속성 주장을 끊는다.

구 140화 편성 및 `[SUPERSEDED]` 225화 압축 초안은 역사 기록일 뿐 활성 기획·원고·검수 입력으로 사용하지 않는다.

## 4. 화당 분량 기준

- 모든 신규/재퇴고 화 본문 하한: 2,000자
- 일반 목표는 작품 상태와 장면 기능에 따라 판단한다.
- 전투·반전·부 결말은 사건·감정 종결점을 우선한다.
- 분량 충족은 전체 퇴고 완료가 아니다.
- migration 중 legacy tail의 기존 분량 충족을 최신 narrative continuity의 증거로 사용하지 않는다.

## 5. 심화 개선 원칙

이미 하한을 충족한 화를 분량만 늘리지 않는다. 인과·선택·대가·후유증 또는 원본 충실도 결함이 증거로 확인된 경우에만 수정한다. `SOURCE_MATCHED`는 사건 순서·동행·행선지·결과 판정이며 원문 문장 복제를 뜻하지 않는다. 원본에 있더라도 최신 사용자 지시가 폐기한 축은 복원하지 않고 제외 근거를 남긴다.

## 6. 퇴고 순서

Source inventory → Canon audit → Developmental → Structural reverse outline → Scene diagnostic → Continuity → Line edit → Copyedit → Proofread 순서를 지킨다. 5화 단위로 원본·인과·POV·시간·동선·상태를 검수하고, 현재 migration prefix와 legacy tail 사이 경계도 별도로 회귀한다.

완료:

- 구조 역개요 기준선
- 제10·95·180화 대표 파일럿
- 구 편성 `006-010` 내부 연속성 패스 — 역사적 검증 증거로 보존, external reconciliation은 별도 필요
- `091-095` 원본 직접 대조 패스
- 외부 최신 `001-005` source/canon reconciliation 및 migration boundary 설치

현재 운영 우선순위는 `ACTIVE_CONTEXT.md`와 `analysis/SCENE_PASS_REGISTRY.json`이 책임진다. 다음 묶음은 **외부 최신 `006-010`**이며, 기존 `176-180` 원본 직접 대조는 이후 대기 작업으로 보존한다.

## 7. 폐기 설정 정책

독립 러시아 마피아·쵸르브라트·미하일·피엘렛토·붉은 늑대·컨소시엄·협상 책임자 장기 서사축은 `SUPERSEDED`다. 오션 후일담·아프리카 임무·독립 마피아/동물 장기축은 활성 작업 입력으로 사용하지 않는다. 최신 사용자 지시에서 추가로 폐기·허용한 인물/설정은 `CANON_REGISTRY.json`에 별도 전파한 뒤 원고 검사에 반영한다.

2부 `버실라 / 바실라 / Versilla / Woff` 직접 등장·개인 서사·독립 기능 복원은 금지하고 아킴은 등장 가능하다. 주안의 현재 자기통제는 `반응 → 멈춤 → 이유 → 선택`이며 주안–엘리스 관계를 명령/복종으로 환원하지 않는다.

## 8. 구형 파일 정책

- 역사·누락 대조 자료는 활성 작업 입력이 아니다.
- 활성 문서는 구형 Google Docs·압축 초안·구 편성을 직접 링크하거나 근거로 사용하지 않는다.
- 대체 관계는 Source Manifest를 경유한다.
- `latest`, `final`, `v2` 같은 경쟁 활성본을 만들지 않는다.
