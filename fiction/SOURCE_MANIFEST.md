# SOURCE MANIFEST

상태: **ACTIVE**  
최종 갱신: 2026-07-22

## 활성 Google Docs

| 역할 | 문서 | 상태 |
|---|---|---|
| 현행 기획서·작품 코어 | [《폭풍의 눈》 현행 기획서·작품 코어](https://docs.google.com/document/d/1b7LL-q6p4UTV6DCYDj3CcLgemw3gyLcU_3WSaaSV6zE) | `ACTIVE / INTEGRATED VIEW` |
| 현재 상태·인수인계 | [《폭풍의 눈》 활성 인수인계](https://docs.google.com/document/d/1gP0yTgT0eLgMcb-21FW1qwgWQVSKxfjiAvIVLyqlJ2E) | `ACTIVE` |
| 225화 실제 편집 원고 | `fiction/manuscript/`의 45개 5화 묶음 | `ACTIVE / DRAFT` |

Google Docs 기획서는 사람이 빠르게 읽는 통합 뷰다. 충돌 시 GitHub의 `FICTION_MASTER.md`, `CANON_REGISTRY.json`, `MANUSCRIPT_INDEX.json`과 개별 책임 원본을 우선한다.

## 이전 자료 판정

- 구 통합 Google Doc: 최신 225화 확장 원고를 포함하고 있었으므로 **마이그레이션 원문 증거**로 한 번 사용했다. 현행 편집은 GitHub 분할 원고에서 수행한다.
- 별도 225화 압축 초안: 최신 통합 원고보다 짧고 오래된 파생본으로 판정해 작업 입력에서 제외했다.
- 구 인수인계: 과거 상태 확인용이며 현재 진행 상태를 책임지지 않는다.

## 로컬 내보내기 해시

- 최신 통합 문서 내보내기: SHA256 `5de05d6b332a4af4af9f44b041d743eeaf2387e277ea90143d5530efcb713e60`
- 구 225화 압축 원고 내보내기: SHA256 `05975c5b941b1935456d91ce9f914d606b644cb3fe3bc7fd17f4f3fb0288cb7f`
- 구 인수인계 내보내기: SHA256 `4700b5091c8aec7c6a4aa89db24180f48584b765c32322fef26c250ad6530c97`

해시는 누락 대조와 파생본 판별용이다. 해시만으로 해당 파일을 현행 Canon으로 승격하지 않는다.

## 구형 자료 접근

구형 Google Docs의 ID·대체 관계는 `archive/SUPERSEDED_GOOGLE_DOCS.md`에만 기록한다. 활성 작업자는 직접 참조하지 않으며, 누락 감사나 변경 근거 확인 시에만 Source Manifest를 경유한다.

## 확인 불가 자료

기존 검수 보고서 Google Doc은 연결 계정에서 직접 열리지 않았다. 활성 근거로 사용하지 않으며, 현행 검수 결과는 `reports/REVISION_2026-07-22_CANON_REFRESH.md`와 자동 검사에 기록한다.
