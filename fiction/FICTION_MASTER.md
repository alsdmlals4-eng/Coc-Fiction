# 《폭풍의 눈》 현행 정본·작업 기준

상태: **ACTIVE / SINGLE SOURCE OF TRUTH / MIXED MIGRATION**  
최종 갱신: 2026-08-20

## 1. 책임 원본

| 질문 | 현행 책임 원본 |
|---|---|
| 작품 정체성·주제·변경 금지 | `bible/01_PROJECT_CORE.md` |
| Canon 상태·별칭·폐기 | `CANON_REGISTRY.json` |
| 세계·인물·연속성·부별 설계 | `bible/02_CANON_AND_CONTINUITY.md`, `bible/03_PART1_STORY_BIBLE.md`, `bible/04_PART2_STORY_BIBLE.md` |
| POV·문체·표기 | `STYLE_GUIDE.md` |
| 실제 GitHub 저장 원고 | `manuscript/` |
| current revision input | Library `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx` |
| current candidate provenance | `docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json` |
| current candidate QA | `docs/fiction-ops/2026-08-20_WORKING_001_161_CANDIDATE_QA.md` |
| 화별 제목·POV·분량·원문 SHA | `MANUSCRIPT_INDEX.json` |
| 저장 원고 구조 역개요·구조 진단 | `analysis/REVERSE_OUTLINE_001_225.json`, `analysis/REVERSE_OUTLINE_REPORT.md` |
| 대표 게이트·완료 묶음 패스 | `analysis/REPRESENTATIVE_CHAPTER_GATES.md`, `analysis/SCENE_PASS_REGISTRY.json` |
| 원본 파일·감사 상태 | `SOURCE_MANIFEST.md`, `sources/PRIMARY_SOURCE_INVENTORY.md` |
| 현재 상태·다음 작업 | `ACTIVE_CONTEXT.md` |
| 인수인계 | `HANDOFF.md` |

## 2. 정본 우선순위

1. 사용자의 가장 최근 직접 지시
2. 작품 코어·Canon Registry
3. 접근 가능한 원본 TRPG 로그/PDF의 사건 순서·인물 동행·결과
4. 부별 스토리 바이블·연속성 문서
5. 현재 승인·검증된 원고 delta
6. 수동 장면 카드·Revision Report
7. 구조 역개요·진단 보고서
8. 외부 참고

색인과 역개요는 immutable baseline과 승인된 묶음 override를 합성한다. baseline을 직접 편집 입력으로 사용하지 않는다. 원고·Canon과 충돌하면 파생 분석을 갱신하며 분석을 근거로 원고를 자동 덮어쓰지 않는다.

## 3. current candidate와 GitHub production authority

현재 통합 revision input:

```yaml
artifact: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
candidate_qa: QA_GREEN
candidate_coverage: 001-161
repository_promotion_state: PARTIAL
```

`QA_GREEN`은 외부/통합 후보의 품질 상태이며 GitHub manuscript 전체 승격을 뜻하지 않는다. GitHub production authority는 5화 단위 bounded reconciliation이 Green일 때만 frontier를 이동한다.

현재 bounded production state:

```yaml
reconciled_prefix: 001-010
legacy_tail_starts_at: 011
boundary_after_chapter: 010
whole_manuscript_continuity: NOT_YET_CLAIMED
next_reconciliation: 011-015
```

제5→6은 current continuity로 재연결됐다. 제10→11은 현재 fail-closed migration boundary이며 제11화 이후 stored chapter를 current 제10화의 정상 다음 사건으로 자동 해석하지 않는다.

## 4. 저장 토폴로지와 narrative migration

저장소는 기존 225화 파일 경로·bundle 구조를 migration container로 유지한다.

- stored `part-1`: 1–70
- stored `side-story-lake`: 71–95
- stored `side-story-alice`: 96–130
- stored `side-story-ian`: 131–165
- stored `part-2`: 166–225

**이 225화 구간표는 current 001–161 narrative의 최종 편성 선언이 아니다.** `SCENE_PASS_REGISTRY.external_artifact_reconciliation`의 `reconciled_prefix_end` 이후 stored chapter는 자신의 reconciliation을 통과하기 전까지 legacy tail이다.

## 5. 분량·퇴고 기준

- 신규/재퇴고 GitHub production 화 본문 하한: 2,000자.
- 분량만 채우기 위한 padding은 하지 않는다.
- 인과·선택·대가·후유증·원본 충실도 결함이 증거로 확인될 때만 증보한다.
- `SOURCE_MATCHED`는 사건 순서·동행·행선지·결과 판정이며 원문 문장 복제를 뜻하지 않는다.
- current candidate의 platform용 회차 재패키징은 story canon과 별도 distribution layer다.

## 6. 현행 Canon 보호

- 주안: `반응 → 멈춤 → 이유 → 선택`; 관계를 자동 복종으로 환원하지 않는다.
- 엘리스: 정신 능력은 지배가 아니라 외부 간섭 차단·선택 보존.
- 이안: 관찰·가설·검증·기록; 모르는 것을 정답으로 올리지 않는다.
- 다빈: 자신의 몸과 미래를 선택할 권리.
- 주민: 치료 가능성보다 당사자 동의·현재 환자 우선.
- 엘리엇: 반복된 실패와 애정 때문에 타인의 미래를 대신 고정하려는 비극적 반례.
- 외부 회수압력: `의뢰인 → 브로커/오래된 연락 노드 → 전문 회수팀`의 경계형 회수망. 최상위 client/hierarchy는 bounded ambiguity.
- 교차회차 사진: 확정 미래가 아닌 실제 non-current cross-loop evidence.
- 다른 회차 세 시신: 명시적 사건이 상태를 바꾸기 전까지 물리적 경찰 증거.
- 백은검: 귀속 미정·공동봉인. 주민 근처 반응/메스 변형은 소유·후계 인증이 아니다.
- Alice Carter 한국어 정본 표기: `엘리스`.
- POV: Scene-Locked Hybrid; 실제 장면분리 없는 head-hopping 금지.

폐기·금지 별칭과 축의 정확한 목록은 `CANON_REGISTRY.json`만 책임진다. 이 Master에서 목록을 중복 복제하지 않는다.

## 7. current prefix 001–010 readback

- 001–005: 기존 current reconciliation 유지.
- 006 `따뜻한 피난처`: 해안 엘리스/이안과 감옥 주안 두 전선이 제5화에서 직접 이어짐. 신호기는 단방향.
- 007 `죽은 척해야 사는 곳`: 즉흥 돌격 대신 구조 가능성을 만들고 동굴로 이동.
- 008 `같은 편은 아닙니다`: 밀리 생존, 하템 별도 계약자, 같은 목적지의 임시 동행.
- 009 `카터라는 이름`: 증거와 추론 분리.
- 010 `친구를 쏜 날`: 밀리 소실 후 시체·피가 없어 객관적 사망은 미확정. 이안의 정서적 상실과 사실 판정을 분리.

## 8. 실행 순서

현재 다음 작업은 `fiction/manuscript/part-1/011-015.md`의 current candidate reconciliation이다.

```text
current candidate 011-015 추출
→ current Ch10 종료와 앞 경계 검증
→ 원본·Canon·사용자 Decision 대조
→ KEEP / APPLY / REWORK / REJECT
→ manuscript + index + reverse outline + Scene Pass + routers 원자 갱신
→ exact-head CI
→ merge/readback
→ frontier 15로 이동
```

기존 deferred source-pass는 `SCENE_PASS_REGISTRY.json`이 보존하며 bounded migration 순서를 건너뛰는 근거로 사용하지 않는다.
