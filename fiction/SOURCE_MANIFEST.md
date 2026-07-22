# SOURCE MANIFEST

상태: **ACTIVE**  
최종 갱신: 2026-07-23

## 활성 Google Docs

| 역할 | 문서 | 상태 |
|---|---|---|
| 현행 기획서·작품 코어 | [《폭풍의 눈》 현행 기획서·작품 코어](https://docs.google.com/document/d/1b7LL-q6p4UTV6DCYDj3CcLgemw3gyLcU_3WSaaSV6zE) | `ACTIVE / INTEGRATED VIEW` |
| 현재 상태·인수인계 | [《폭풍의 눈》 활성 인수인계](https://docs.google.com/document/d/1gP0yTgT0eLgMcb-21FW1qwgWQVSKxfjiAvIVLyqlJ2E) | `ACTIVE` |
| 225화 실제 편집 원고 | `fiction/manuscript/`의 45개 5화 묶음 | `ACTIVE / DRAFT` |

Google Docs 기획서는 사람이 빠르게 읽는 통합 뷰다. 충돌 시 GitHub의 `FICTION_MASTER.md`, `CANON_REGISTRY.json`, `MANUSCRIPT_INDEX.json`과 개별 책임 원본을 우선한다.

## 이전 자료 판정

- 구 통합 문서: 최신 225화 확장 원고를 GitHub로 이전할 때 마이그레이션 원문 증거로 한 번 사용했다. 현행 편집은 GitHub 분할 원고에서만 수행한다.
- 별도 225화 압축 초안: 최신 원고보다 짧고 오래된 파생본이다. 파일럿에서는 사건 뼈대가 바뀌지 않았는지 보는 보조 비교에만 사용했으며 문장·Canon 권한은 부여하지 않았다.
- 구 인수인계: 원본 파일명과 과거 재감사 범위를 확인하는 보조 증거다. 현재 진행 상태와 원고 문장을 책임지지 않는다.

## 원본 자료 가용성 감사

2026-07-23에 Google Drive와 대화·파일 라이브러리를 다시 검색했다. 과거 인수인계가 열거한 원본 1부·외전1·2부 PDF/텍스트와 원본 재감사 보고서의 **실제 본체는 확인되지 않았다**. 현재 확인 가능한 것은 파일명·존재 기록·일부 사건 교정 요약뿐이다.

따라서 다음은 계속 `UNVERIFIED`다.

- 제1화~제225화와 원본 로그의 장면 단위 완전 일치
- 제10화·제95화·제180화의 원문 대사·세부 동선 보존
- 과거 표본 검수 보고서의 전체 62개 항목

원본 본체가 제공되면 `PRIMARY`로 등록하고, 현재 원고와의 차이를 finding으로 남긴 뒤 사용자 승인 범위에서만 반영한다.

## 로컬 내보내기 해시

- 최신 통합 문서 내보내기: SHA256 `5de05d6b332a4af4af9f44b041d743eeaf2387e277ea90143d5530efcb713e60`
- 구 225화 압축 원고 내보내기: SHA256 `05975c5b941b1935456d91ce9f914d606b644cb3fe3bc7fd17f4f3fb0288cb7f`
- 구 인수인계 내보내기: SHA256 `4700b5091c8aec7c6a4aa89db24180f48584b765c32322fef26c250ad6530c97`

해시는 누락 대조와 파생본 판별용이다. 해시만으로 해당 파일을 현행 Canon으로 승격하지 않는다.

## 구형 자료 접근

구형 Google Docs의 ID·대체 관계는 `archive/SUPERSEDED_GOOGLE_DOCS.md`에만 기록한다. 활성 작업자는 직접 참조하지 않으며, 누락 감사나 변경 근거 확인 시에만 Source Manifest를 경유한다.

## 확인 불가 자료

기존 검수 보고서 Google Doc은 연결 계정에서 직접 열리지 않았다. 활성 근거로 사용하지 않으며 현행 검수 결과는 `reports/`와 자동 검사에 기록한다.
