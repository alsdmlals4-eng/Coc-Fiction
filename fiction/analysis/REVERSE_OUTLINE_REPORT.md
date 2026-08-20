# 저장 원고 구조 역개요 보고서

상태: **ACTIVE / COMPOSED BASELINE + APPROVED OVERRIDES / MIXED MIGRATION**  
갱신: 2026-08-20

## 1. 데이터 구조

- immutable baseline: `analysis/baselines/`
- current bundle overrides: `MANUSCRIPT_INDEX_OVERRIDE_*.json`, `REVERSE_OUTLINE_OVERRIDE_*.json`
- active manifests: `MANUSCRIPT_INDEX.json`, `REVERSE_OUTLINE_001_225.json`
- composed consumer: `tools/fiction_composed_data.py`
- migration truth: `analysis/SCENE_PASS_REGISTRY.json#/external_artifact_reconciliation`

baseline은 과거 저장 구조 기준선이며 current 편집 입력이 아니다.

## 2. current override 상태

- `001–005`: current reconciliation
- `006–010`: current reconciliation
- `011–015`: current reconciliation; Ch15→16 current 연결
- `016–020`: current reconciliation; **Ch20 migration boundary**
- `021`: legacy-tail boundary override
- `091–095`: 역사적 원본 직접 대조 source pass

## 3. current 구조 지도

```yaml
current_revision_input: 폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx
current_revision_sha256: 248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9
reconciled_prefix_end: 20
legacy_tail_starts_at: 21
boundary_after_chapter: 20
whole_manuscript_continuity: NOT_YET_CLAIMED
```

- Ch5→6, Ch10→11, Ch15→16은 current continuity.
- Ch20은 `RECONCILIATION_MIGRATION_BOUNDARY`, `next_chapter=null`.
- stored Ch21은 `LEGACY_TAIL_BOUNDARY`, `previous_chapter=null`.
- Ch21+는 자신의 bounded reconciliation 전까지 current narrative 연속성을 주장하지 않는다.

## 4. Ch016–020 generator readback

repository generator가 frontier 20 상태에서 Ch15–21을 직접 재생성했다.

- Ch15: current Ch16 `마시면 돌아갈 수 있다면`로 연결.
- Ch16–19: current body/index와 일치하는 previous/next 관계.
- Ch20: `지도 한 장을 훔치는 시간`; 새 migration boundary.
- Ch21: stored legacy `섬의 왕을 보다`; current Ch20을 previous로 주장하지 않음.

생성기 출력을 임의로 재작성하지 않고 bundle override에 저장했다.

## 5. Finding-first 판정

### RESOLVED
- 기존 15→16 boundary는 Ch16–20 promotion으로 제거.
- Ch15의 migration flag 제거 및 Ch16 current 연결.

### ACTIVE BOUNDARY
- 새 fail-closed 경계: **20→21**.
- QA_GREEN 001–161 artifact 존재만으로 Ch21+ production authority를 자동 승격하지 않는다.

### KEEP
- 225 stored topology는 migration container.
- 자동 structural flag는 탐색 단서이며 원고 수정 명령이 아니다.
- 원본 사건·최신 사용자 Decision·Canon이 파생 역개요보다 우선한다.

## 6. 검증 계약

exact HEAD에서 다음을 함께 검증한다.

- composed manuscript index ↔ 실제 body chars/SHA
- reverse-outline reproducibility 225 chapters
- reverse-outline analysis
- completed Scene Pass registry
- current boundary `20→21`
- next bounded bundle `021–025`

과거 Green을 현재 Green으로 재사용하지 않는다.

## 7. 다음 정확한 작업

`fiction/manuscript/part-1/021-025.md`

Ch20 current 종료 상태와 legacy Ch21을 먼저 비교한 뒤 같은 bounded lifecycle을 반복한다.
