# 제6화~제10화 5화 묶음 장면 카드·연속성 패스 Revision Report

상태: **COMPLETED BUNDLE PASS / WHOLE-MANUSCRIPT REVISION NOT COMPLETE**  
날짜: 2026-07-23

## 범위

- 제6화~제10화 전 화 수동 장면 카드
- 제5→6화와 제10→11화 경계
- 시간·POV·동선·부상·지식·소지품·비밀 상태
- 동일 자아 보호 반응과 파일럿 규칙 소비자 점검

제1화~제225화 전체 line/copy/proofread는 범위에 포함하지 않았다.

## 출처 상태

1. 현행 작품 코어·Canon Registry·1부 바이블·Style Guide
2. 현행 원고와 같은 커밋의 색인·역개요
3. 사용자 제공 원본 폴더: `https://drive.google.com/drive/folders/1EPA-bg8ExjvK-XPadKqdab2cCSNMWVt0`
4. 현재 연결 계정 결과: 폴더 자식 0개, 메타데이터 404

따라서 내부 연속성은 검증했으나 원본 로그·PDF 직접 충실도는 `UNVERIFIED`다.

## Finding-first 결과

- `MUST_FIX-01 RESOLVED`: 제5화의 총격·폭발 뒤 제6화가 이전 시점으로 돌아가는 무표지 경계를 시간 앵커로 교정
- `MUST_FIX-02 RESOLVED`: 제5화에서 이미 승선한 아킴이 제9화에서 다시 갈고리로 승선하는 중복 이동 제거
- `SHOULD_FIX-01 RESOLVED`: 제7화 `다른 자신`을 같은 자아의 보호 반응으로 명료화
- `REJECT-01`: 제8화의 기억 잔향과 제10화의 직접 정신 공격은 단계가 전진하므로 통합·삭제하지 않음
- `UNVERIFIED-01`: 원본 폴더 접근 전까지 대사·세부 동선 직접 대조 보류

## 변경 범위

- 원고 변경: 제6·7·9화 / 1개 묶음
- 원고 미변경: 제8·10화 및 나머지 220화
- 화수·제목·POV·사건 결과·결말 방향: 변경 없음
- 제10화 파일럿 수정: 보존
- 모든 화 2,000자 이상: 유지

## 변경 전후

| 제6화 | 2326자 | 2344자 | `1b2681bdb7f660583b2a1a9f59b059f95d89ca2dd692cdcb6a1db162ce96e92a` |
| 제7화 | 2640자 | 2644자 | `11fcb4fe99c8840fb3845def385df801b5cdec35e7bfbc285a8747d9caa850d0` |
| 제8화 | 2686자 | 2686자 | `9c5c5e4b5fef29eb98de705a5af331881fa49078b5e9db66ee912a452591cbe2` |
| 제9화 | 2567자 | 2598자 | `9bc13a600ddc48f3284c01cf9522b41a8575c72e081fe65f26d82aa5aacdeab3` |
| 제10화 | 3063자 | 3063자 | `62492d465a2cb3e0a83761ad050c04858e145596c44285accc63b3468ea72bdb` |

## 정본 전파

- `MANUSCRIPT_INDEX.json` 재생성
- `REVERSE_OUTLINE_001_225.json` 재생성
- `SCENE_CARDS_006_010.md`와 `SCENE_PASS_REGISTRY.json` 추가
- 1부 바이블·Canon 연속성·Style Guide·진입 문서 갱신
- Google Drive 원본 폴더의 접근 차단 상태를 Source Manifest에 기록
- 다음 묶음을 `091-095 → 176-180`으로 이동

## 사용 Skill·mode

- `fiction-project-operations`: `route`, `contract`, `coordinate-concurrent-work`, `checkpoint`, `handoff`, `execution-report`
- `fiction-revision-and-validation`: `scene-diagnostic`, `continuity-check`, `adversarial-loop`, `regression-check`, `evidence-report`, `pr-review`
- `fiction-story-development`: `scene-card`, `plot-and-causality`, `stress-test`
- `fiction-canon-and-research`: `canon-audit`, `continuity-map`, `timeline-and-state`, `source-log`, `reference-freshness`
- `fiction-drafting`: `approved-rewrite`, `pov-and-distance`, `action-and-reaction`

## 회귀 검증

- 변경 대상이 제6·7·9화로 제한되는지 확인
- 제5화 승선·교전 → 제6화 이전 시점 병행 → 제7·8화 직접 연속 → 제9화 병행 → 제10·11화 직접 연속 확인
- 제7화와 제10·11화의 보호 반응이 같은 자아로 유지되는지 확인
- 제9화의 히템 육체 보유와 세실리아 생존 납치 유지
- 원고·색인·역개요 SHA 일치
- 구형 문서 ID·구 140화 편성·폐기 설정 재등장 없음

## 다음 작업

`fiction/manuscript/side-story-lake/091-095.md`의 제90→91화·제95→96화 경계를 포함한 수동 장면 카드·연속성 패스를 수행한다. 원본 폴더 권한이 열리면 제6~10화를 우선 재감사한다.
