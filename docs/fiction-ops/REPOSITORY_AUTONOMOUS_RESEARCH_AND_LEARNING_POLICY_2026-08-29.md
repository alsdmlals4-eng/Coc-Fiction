# Coc-Fiction repository-only autonomous research and learning policy

```yaml
status: CURRENT_ACTIVE
approved_by_user: 2026-08-29
scope: planning / manuscript / review / visual candidate / production operations
runtime_game_rules: NOT_APPLICABLE
```

이 문서는 Coc-Fiction의 repository workspace, 조사·현실성 검토, 사용자 관여 경계, 시각 후보와 지속 가능한 학습 규칙을 소유한다.

## 1. Authority and workspace

```text
LATEST_USER_INSTRUCTION
→ AGENTS.md
→ THIS_POLICY
→ fiction/ACTIVE_CONTEXT.md의 현재 production frontier
→ CANON_REGISTRY / SCENE_PASS_REGISTRY / CURRENT_STATE_RECEIPT
→ actual manuscript / structured analysis / tests
→ adopted Base owners
→ external evidence / historical material
```

- GitHub repository가 사람용 작품 정본, 구조화 Canon, 원고 production frontier, 검사·evidence와 current handoff의 단일 활성 owner다.
- 과거 Notion summary/Event/Relation/page/database/attachment는 `HISTORICAL_MIGRATION_REFERENCE_ONLY`다.
- routine current work에서 Notion을 읽거나 쓰거나 동기화하거나 destination readback 완료 조건으로 사용하지 않는다.
- `fiction/ACTIVE_CONTEXT.md`, 과거 handoff, historical receipt에 남은 `Notion sync`, `Notion readback`, `Notion approved summary / Event / Relation` 문구는 이 정책과 충돌하는 범위에서 `SUPERSEDED_HISTORICAL_COMPATIBILITY`다.
- 사용자 지정 DOCX는 구간별 reconstruction source authority일 수 있으나 GitHub production authority는 bounded reconciliation과 검증 뒤에만 이동한다.

## 2. Research and production feasibility

중요한 작품·운영 결정을 기억이나 단일 참고작에만 의존하지 않는다.

```text
current canon + actual manuscript + production frontier
→ existing project solution / adopted Base owner
→ targeted current official or primary research when material
→ directly relevant success / failure / mixed cases
→ materially distinct alternatives
→ ADOPT / ADAPT / REJECT
→ production feasibility judgement
→ bounded manuscript or system change
→ exact tests / readback / correction
```

조사 적용 범위 예:

- 역사·과학·법·문화·기관·지역 등 사실 정확성이 독자 신뢰와 플롯에 영향을 주는 내용
- 출판·배포·포맷·접근성·권리·인용·AI 산출물 provenance
- 장편 연속성, Scene-Locked Hybrid POV, 정보 공개, 장면 카드, bounded promotion 같은 production workflow
- 표지·삽화·마케팅 asset의 실제 consumer와 권리

외부 자료는 Canon을 자동 변경하지 않는다. 참고 작품의 문장·고유 문체·표면 장치를 복제하지 않고 `기능 → 장치 → 효과 → 전이 가능한 원리`로 분석한다.

Production feasibility packet:

```yaml
reader_or_production_value:
current_owner_and_gap:
actual_consumer_or_manuscript_range:
canon_and_continuity_impact:
pov_character_timeline_evidence_boundaries:
source_and_rights_constraints:
tooling_and_validation_path:
rollback_or_bounded_revert:
evidence_ceiling:
feasibility: FEASIBLE | PARTIAL | BLOCKED_UNVERIFIED
```

`SPEC_ONLY_IS_NOT_PRODUCTION_PROOF`: 계획·역개요·자동 진단·QA 후보가 존재해도 실제 manuscript promotion, whole-manuscript continuity, 독자 반응 또는 출판 준비를 자동 증명하지 않는다.

## 3. Long-term quality and minimum complexity

빠른 문장 수정 하나보다 장기 원고 일관성·검증 가능성·재개 가능성·중복 감소·독자 경험을 우선한다.

- current owner 하나를 유지한다.
- bounded 5화 promotion과 fail-closed boundary를 보존한다.
- 구조·인과·연속성 문제를 line edit로 가리지 않는다.
- 반복 수동 점검은 deterministic validator, registry, receipt와 readback으로 바꾼다.
- 미래 가능성만을 위한 중복 schema, dashboard, index와 process 문서를 만들지 않는다.
- 현재 작품에 필요한 최소 복잡도로 장기 품질과 rollback을 확보한다.

## 4. Minimized user intervention

승인된 범위에서 AI가 연속 처리한다.

- latest main / open PR / current owner fresh-read
- source receipt와 Canon conflict scan
- 공식·1차 자료와 벤치마크 조사
- 대안 비교와 production feasibility 판정
- bounded 원고·registry·reverse outline·scene card propagation
- 자동 검사, exact-head readback, 가역적 교정
- remaining-work recalculation과 다음 안전 묶음 준비
- 문제·교훈·회귀 방지 규칙 반영

사용자 결정으로 올리는 항목:

- 작품의 중심 질문·결말 방향·주요 인물성·세계관 Canon 변경
- 중요한 장면 의미나 관계 결론의 취향 선택
- 최종 표지·삽화 Visual Direction 또는 제품 asset lock
- 외부 공개·출판·비용·권리·보안
- 되돌리기 어려운 삭제·대규모 renumbering·migration

사용자 결정을 발명하지 않는다. 그러나 저장소에서 확인 가능한 사실과 안전한 기술적·기계적 선택 때문에 routine checkpoint를 만들지 않는다.

## 5. Visual candidate policy

실제 consumer가 있는 표지·삽화·마케팅 visual 또는 승인된 사람용 Blueprint/GDD에 필요한 구체적 시각 후보는 다음 순서를 따른다.

```text
current canon / characters / world / tone
→ existing approved visual / previous draft / rights readback
→ actual consumer and target spec
→ keep / avoid / do not drift
→ image-model-generated bounded candidate
→ objective QA
→ user LOCK / REVISE / REJECT / REFERENCE_ONLY
```

- 필요한 candidate는 이미지별 사전 승인 없이 먼저 제작할 수 있다.
- 새 이미지는 이미지 생성·편집 모델로 만들며 SVG, Canvas, Python drawing, code-drawn vector로 대신하지 않는다.
- `GENERATED_CANDIDATE != USER_APPROVED != CANON_REGISTERED != DISTRIBUTION_READY`다.
- 사용자 lock 전에는 표지·삽화·마케팅 정본이나 외부 배포 asset으로 승격하지 않는다.
- 실제 consumer 없는 AI 설명용 장식 이미지는 만들지 않고 텍스트·표·관계도·Flow를 editable 형식으로 유지한다.

## 6. Durable learning

이 정책의 학습은 모델의 임의 영구 기억이 아니라 repository에 남는 재사용 가능한 운영 evidence다.

```text
problem / repeated manual step
→ root cause
→ bounded fix
→ exact verification
→ regression guard
→ project owner / handoff update
→ Base promotion candidate when broadly reusable
```

작품 고유 교훈과 공용 운영 교훈을 분리한다. 재사용 가치가 없으면 새 process 문서나 registry 항목을 만들지 않는다.

## 7. Completion

현재 묶음 완료 후보:

```text
exact user-source receipt
→ Canon / continuity / POV / causality review
→ manuscript + affected consumers propagation
→ automated validators at exact head
→ adversarial review and corrections
→ PR review/thread/main freshness
→ permitted merge
→ new main + repository destination readback
→ CURRENT_STATE_RECEIPT / ACTIVE_CONTEXT successor
→ remaining work recalculation
```

Notion readback은 completion gate가 아니다. 자동 검사 PASS는 whole-manuscript continuity, reader experience, publication readiness를 증명하지 않는다.
