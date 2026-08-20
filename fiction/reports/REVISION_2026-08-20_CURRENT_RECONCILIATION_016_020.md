# 2026-08-20 Current Candidate Reconciliation · Ch016–020

상태: **IMPLEMENTED_ON_BRANCH / AWAITING_EXACT_HEAD_GREEN**

## 목표

QA_GREEN integrated working candidate의 제16–20화를 GitHub production manuscript의 다음 5화 단위로 승격하고 verified frontier를 `15→16`에서 `20→21`로 이동한다.

## 권위 입력

- artifact: `폭풍의눈_001-161_통합현행후보_20260820_QA_GREEN_NOT_PROMOTED.docx`
- artifact SHA256: `248d1e0076114c10724a480333421353c03ea4f76d5e629cf865c730796643d9`
- exact Ch016–020 file SHA256: `bd4b699aa9a43548371867d85fc083c76e0b378165ec817d6d16934e02201842`
- exact Git blob: `85264072bb9f4d3928d3f922fc1230a4ff872297`
- prior verified frontier: Ch15 / legacy tail Ch16+

## TDD RED

- draft PR #37은 production propagation 전에 future contract만 추가했다.
- 기존 Fiction operating-system의 6개 검증은 모두 Green.
- 추가 RED contract만 의도대로 실패했다.
- 실패 이유: frontier 15, legacy start 16, current Ch16–20 제목/완료 pass 부재, next bundle 016–020.
- PR #37은 병합하지 않고 닫았고 임시 RED script/workflow 수정은 제거했다.

## exact source transfer 검증

대용량 단일 connector 전송은 바이트 무결성을 보장하지 못해 merge 대상이 아닌 실험 브랜치에서 압축 staging을 사용했다.

- gzip/base64 조각을 GitHub-hosted job에서 조립.
- 원문 bytes: `70401`.
- 원문 SHA256: `bd4b699aa9a43548371867d85fc083c76e0b378165ec817d6d16934e02201842`.
- 생성 Git blob: `85264072bb9f4d3928d3f922fc1230a4ff872297`.
- clean GREEN branch는 main에서 다시 만들고 이 exact blob만 재사용했다.
- 실험 branch staging/workflow는 최종 promotion diff에 포함하지 않는다.

## 적용 본문

| 화 | 제목 | POV | body chars | SHA256 |
|---|---|---|---:|---|
| 16 | 마시면 돌아갈 수 있다면 | 엘리스 → 주안 → 엘리스 → 주안 → 엘리스 | 6051 | `752de081c6189ab8646a43108a1e63bf7a27f8de399b4488c4c980eec71fabca` |
| 17 | 주안 씨, 정신 차려요 | 엘리스 → 주안 → 엘리스 → 주안 | 5999 | `7146cc26b37a56ed87e29162dc2f5b1b6cd33bf0e3bd7bf9c4cdcaa791da929c` |
| 18 | 지금은 주안이 중요하니까 | 엘리스 → 주안 → 엘리스 → 주안 → 엘리스 | 4570 | `8d2c1ca43ae980884f24a39d45bb548f872287b49790d12e2db59be2d474adf0` |
| 19 | 스승이 남긴 질문 | 이안 → 주안 → 이안 → 엘리스 → 이안 → 주안 → 이안 | 7274 | `39adeba785e49f7127529d46a1c80800e630b35564e2523b32b01854b7057b06` |
| 20 | 지도 한 장을 훔치는 시간 | 이안 | 6208 | `dc78dd2f3ab00d853225ca4c98a85832d5fbb088df0b304258172e2ffd754523` |

Source-line provenance:
- Ch16 `8508–8711`
- Ch17 `8714–8992`
- Ch18 `8995–9188`
- Ch19 `9191–9408`
- Ch20 `9411–9619`

## 보호 상태

- 주안의 신체 반응성을 복종·소유의 증거로 확대하지 않는다.
- 엘리스는 타인의 반응을 이용해 결정을 대신하지 않는다.
- Ch18 정보·힘 사용은 당사자 선택을 우선한다.
- Ch19 하템과 밀리는 별도 인물이며 같은 얼굴만으로 동일인 결론을 내리지 않는다.
- 이안은 관찰·가설·검증·기록 순서를 유지한다.
- Ch20은 지도 확보 성공과 잠입 실패를 동시에 기록한다.

## reverse-outline 진단

- no-merge PR #38 / run `32346753989`.
- exact source/index에서 operating-system과 active content validation PASS.
- reverse-outline만 stale 상태로 실패하며 repository generator가 Ch15–21 exact window를 출력했다.
- generator output을 이용해 Ch15 current 연결, Ch16–20 override, Ch21 legacy boundary를 자동 생성했다.
- 일회성 materialize workflow는 생성 후 자기 자신을 삭제해 최종 diff에 남지 않는다.

## 새 경계

```yaml
reconciled_prefix_end: 20
legacy_tail_starts_at: 21
boundary_after_chapter: 20
whole_manuscript_continuity: NOT_YET_CLAIMED
next_bounded_bundle: fiction/manuscript/part-1/021-025.md
```

- Ch15→16: `PASS / CURRENT`.
- Ch20→21: `MIGRATION_BOUNDARY / NOT_YET_CLAIMED`.
- Ch21+ body는 이번 작업에서 수정하지 않는다.

## 최종 merge gate

1. exact-head `Fiction operating system` 전체 SUCCESS.
2. content/index exact body SHA PASS.
3. reverse-outline reproducibility / analysis PASS.
4. scene-pass contract가 `001-020 current production prefix; migration boundary 20→21; 021-025 next`로 PASS.
5. unresolved review thread 0.
6. branch behind 0 / current main freshness PASS.
7. squash merge 후 main structured readback 및 Notion sync.
