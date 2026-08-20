# 《폭풍의 눈》 현행 정본·작업 기준

상태: **ACTIVE / SINGLE SOURCE OF TRUTH / MIXED MIGRATION**  
최종 갱신: 2026-08-20

## 1. 책임 원본

| 질문 | 현행 책임 원본 |
|---|---|
| 작품 정체성·주제·변경 금지 | `bible/01_PROJECT_CORE.md` |
| Canon 상태·별칭·폐기 | `CANON_REGISTRY.json` |
| 세계·인물·연속성 | `bible/02_CANON_AND_CONTINUITY.md`, `bible/03_PART1_STORY_BIBLE.md`, `bible/04_PART2_STORY_BIBLE.md` |
| POV·문체·표기 | `STYLE_GUIDE.md` |
| GitHub production manuscript | `manuscript/` |
| current revision input | Library `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx` |
| candidate provenance / QA | `docs/fiction-ops/2026-08-20_CURRENT_001_161_CANDIDATE_MANIFEST.json`, `docs/fiction-ops/2026-08-20_WORKING_001_161_CANDIDATE_QA.md` |
| 제목·POV·본문 SHA | `MANUSCRIPT_INDEX.json` |
| 구조 역개요 | `analysis/REVERSE_OUTLINE_001_225.json`, `analysis/REVERSE_OUTLINE_REPORT.md` |
| 완료 bundle / frontier | `analysis/SCENE_PASS_REGISTRY.json` |
| 현재 작업 | `ACTIVE_CONTEXT.md` |
| 재개 | `HANDOFF.md` |

## 2. 정본 우선순위

1. 최신 사용자 직접 지시
2. 작품 코어·Canon Registry
3. 접근 가능한 원본 TRPG 기록
4. 부별 Bible·연속성
5. 현재 승인·검증 원고 delta
6. 장면 카드·Revision Report
7. 구조 역개요·진단
8. 외부 참고

파생 분석이 원고·Canon과 충돌하면 파생 자료를 갱신한다. 분석 결과로 원고를 자동 덮어쓰지 않는다.

## 3. current candidate와 production authority

```yaml
artifact: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
candidate_qa: QA_GREEN
candidate_coverage: 001-161
repository_promotion_state: PARTIAL
reconciled_prefix: 001-020
legacy_tail_starts_at: 021
boundary_after_chapter: 020
whole_manuscript_continuity: NOT_YET_CLAIMED
next_reconciliation: 021-025
```

QA_GREEN은 revision input의 상태다. GitHub production authority는 5화 단위 bounded reconciliation이 Green일 때만 이동한다.

## 4. 저장 토폴로지

저장소의 225화/45 bundle 구조는 migration container다.

- stored `part-1`: 1–70
- stored `side-story-lake`: 71–95
- stored `side-story-alice`: 96–130
- stored `side-story-ian`: 131–165
- stored `part-2`: 166–225

이 구간은 current 001–161 narrative 최종 편성 선언이 아니다. `reconciled_prefix_end` 이후 stored chapter는 자신의 pass 전까지 legacy tail이다.

## 5. 현행 Canon 보호

- Jooan: `반응 → 멈춤 → 이유 → 선택`; 반응성을 복종으로 환원하지 않는다.
- Elise: 정신 능력은 외부 간섭 차단·선택 보존, 지배 아님.
- Ian: 관찰·가설·검증·기록; 모르는 것을 정답으로 올리지 않는다.
- Dabin: 자신의 몸과 미래를 선택할 권리.
- Jumin: 치료 가능성보다 당사자 동의·현재 환자 우선.
- Elliott: 반복 실패와 애정 때문에 타인의 미래를 대신 고정하려는 비극적 반례.
- D01: `의뢰인 → 브로커/오래된 연락 노드 → 전문 회수팀`; 최상위 client/hierarchy는 bounded ambiguity.
- D02: 교차회차 사진은 확정 미래가 아닌 실제 non-current evidence.
- D03: 다른 회차 세 시신은 명시적 사건 전까지 물리적 경찰 증거.
- 백은검: 귀속 미정·공동봉인; 반응/형상변화는 후계 인증 아님.
- Alice Carter 한국어 정본 표기: `엘리스`.
- POV: Scene-Locked Hybrid; scene-internal head hopping 금지.

## 6. current prefix 001–020 readback

- 001–015: 이전 bounded pass Green 상태 유지.
- 016 `마시면 돌아갈 수 있다면`: 위험한 해결책도 당사자 선택 없이 강행하지 않는다.
- 017 `주안 씨, 정신 차려요`: 자기 몸을 다시 자기 것으로 만드는 일을 먼저 둔다.
- 018 `지금은 주안이 중요하니까`: 정보·힘 제공과 결정 대행을 분리한다.
- 019 `스승이 남긴 질문`: 하템/밀리 별도 인물, same-face는 unknown; Ian의 검증 규율 강화.
- 020 `지도 한 장을 훔치는 시간`: 지도 획득 성공과 잠입 실패를 동시에 기록한다.

## 7. current migration boundary

```yaml
left_current: 20
right_legacy: 21
left_next_chapter: null
right_previous_chapter: null
left_flag: RECONCILIATION_MIGRATION_BOUNDARY
right_flag: LEGACY_TAIL_BOUNDARY
```

Ch20→21은 fail-closed다. 인접 numbering으로 연속성을 자동 주장하지 않는다.

## 8. 실행 순서

현재 다음 작업은 `fiction/manuscript/part-1/021-025.md`다.

`candidate exact extraction → Ch20 boundary 검증 → Canon/source 대조 → manuscript/index/outline/cards/registry/routers 원자 갱신 → exact-head CI → review thread 0/main freshness → squash merge/readback`

`176-180` deferred source-pass는 bounded migration 순서를 건너뛰지 않는다.
