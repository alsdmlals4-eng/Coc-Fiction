# 제6화~제10화 묶음 장면 카드·연속성 작업 계약

```yaml
objective: 제6화~제10화의 장면 기능과 앞뒤 경계 연속성을 수동 확정하고 검증된 최소 수정만 반영한다.
manuscript_stage: REVISE
work_mode: REVIEW → BUILD → REVIEW
scope:
  - fiction/manuscript/part-1/006-010.md
  - 제5화와 제11화 경계
  - 색인·역개요·장면 카드·Revision Report·활성 진입 문서
excluded_scope:
  - 제12화 이후 본문
  - 작품 코어·결말·화 제목·POV 변경
  - 원본이 없는 상태에서 직접 충실도 완료 선언
canonical_sources:
  - fiction/FICTION_MASTER.md
  - fiction/CANON_REGISTRY.json
  - fiction/bible/01_PROJECT_CORE.md
  - fiction/bible/02_CANON_AND_CONTINUITY.md
  - fiction/bible/03_PART1_STORY_BIBLE.md
  - fiction/STYLE_GUIDE.md
  - 같은 커밋의 원고·색인·역개요
protected_core_and_prose:
  - 밝은 식당이 학살로 꺾이는 명암 대비
  - 엘리스가 민간인을 두고 가지 않는 선택
  - 주안의 비정상적 힘·복종 각인·자발성의 불확실성
  - 아킴의 친절과 폭력이 공존하는 윤리
  - 히템의 선박 내 육체 보유
concurrent_branches_and_overlap: 열린 PR 0개 / 최신 main에서 독립 브랜치 / OVERLAP_REVIEW
outputs:
  - 수동 장면 카드 5화
  - 경계 연속성 표
  - 최소 원고 수정
  - 색인·역개요·Revision Report·상태 문서 갱신
acceptance_criteria:
  - 변경 화가 제6·7·9화로 제한
  - 화수·제목·POV·사건 결과 보존
  - 모든 화 2,000자 이상
  - 원고·색인·역개요 SHA 일치
  - 구형 자료 활성 참조 0건
validation:
  - 운영체계·콘텐츠·역개요·scene-pass 검사
  - 적대적 PR 검토
rollback: squash PR을 병합하지 않거나 병합 커밋을 일반 revert한다.
```
