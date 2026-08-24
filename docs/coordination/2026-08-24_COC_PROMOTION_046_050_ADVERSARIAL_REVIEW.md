# COC Bridge Promotion 046–050 · 5× Adversarial Review — 2026-08-24

1. **Part boundary / distortion — PASS.** `001–040 = Part 1 main`, `041–066 = Aftermath & 8-year Bridge`, `067+ = Part 2`를 유지한다. Ch046–050은 Bridge이며 Part 2 상태·주연축을 선반영하지 않는다.
2. **Agency / identity — PASS.** Ch46의 황색 체류는 강제 복종이 아니라 계약 가능한 `손님` 관계다. 배치·신체 정보 열람·민간인 희생 반대 기록에 주안의 동의가 필요하며, 임무 뒤 귀환도 자기 선택으로 남긴다. Ch49의 가론 재발 패턴은 8년간의 주안·이안 성장을 무효화하지 않는다.
3. **Investigation / consent — PASS.** Ch48–50은 생존자 구조와 검증을 재회·폭력보다 앞세운다. Ch50은 문/대화를 먼저 시도하고 환자 위장으로 진입한다. 자발적 선택을 충분한 설명·동의와 자동 동일시하지 않으며, 루바를 단순 악역으로 평탄화하지 않는다.
4. **Canon / reveal timing — PASS.** 엘리스 D04의 인간 포함 정신조작 가능 범위와 선택 보존 윤리를 유지한다. 라르고 `[규율]` 실제 공개는 Rift Accord까지 봉인한다. 원본 Ch47의 폐기된 러시아 마피아 연락축 1건은 최신 Canon 우선순위에 따라 `오래된 외부 연락책`으로만 최소 치환했으며 정보 획득 기능·사건 순서·불확실성은 유지한다.
5. **Provenance / boundary / maintenance — PASS.** 사용자 지정 041–050 DOCX에서 Ch046–050을 source-derived로 복원하고 Ch47 한 문장만 Canon-directed reconciliation했다. Ch45→46은 candidate current continuity, Ch50→51은 다음 pass 전까지 fail-closed이며 Ch51 본문은 변경하지 않는다. `101–105` source gap과 `NOT_YET_CLAIMED` whole continuity를 유지한다. 임시 payload/materializer/patcher 및 workflow write permission은 merge 전 제거한다.

## Implementation readback
- exact source DOCX SHA256: `9b2afdf288d657c210a2cc4396650ad6993103a075d0718b4b748f3434c1e9ad`
- pre-Canon-reconciliation source-derived `046-050.md` SHA256: `a8e9b44f86b4a8d599aa6ca05f191e82aee9daf9d9c1583fbdc6d6c869e3c7d7`
- post-reconciliation production `046-050.md` SHA256: `51a11403634bcf9e5f68868c0441f9573ace9b79bc09b0365660781c6124ac32`
- Ch47 source body: `6229` chars / `ed332a61c44bdac0ca394b5f8f6f24ab75c4d388bc289677768aeaee015c9e6a`
- Ch47 production body: `6228` chars / `03e0e7c4fcbfedd4326f335bdc5f49b79fbaf3acc2c1ceaa8e56fa91c8bc6a83`
- Canon reconciliation + consumer propagation bot commit: `570ce1b`
- payload staging issue was isolated to an extra `w==` suffix on part01; the one-time materializer normalizes only that known transport artifact, verifies the pre-reconciliation source-derived file/body hashes, then performs exactly one Canon substitution and verifies post-reconciliation production file/body hashes before writing.

`CLEAN_REVIEW_EXIT` requires fresh full hosted CI Green on the current human-authored head, unresolved review thread 0, latest-main freshness, and one-time-tool cleanup followed by another exact-head Green run.
