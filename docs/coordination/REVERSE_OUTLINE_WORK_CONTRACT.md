# 225화 역개요 작업 계약

상태: ACTIVE / TEMPORARY CHECKPOINT
갱신: 2026-07-22

```yaml
objective: 제1화~제225화의 구조 역개요를 생성하고 대표 품질 게이트 12개 화를 선정한다.
manuscript_stage: REVISE
work_mode: REVIEW
scope:
  - 225화 구조 역개요 baseline
  - 부·외전별 구조 진단
  - 대표 품질 게이트 12화 선정 근거
  - 구형 참조 및 정본 최신성 감사
excluded_scope:
  - 원고 본문 직접 수정
  - 작품 코어·결말·인물성·POV 변경
  - line/copy/proofread
canonical_sources:
  - fiction/FICTION_MASTER.md
  - fiction/ACTIVE_CONTEXT.md
  - fiction/CANON_REGISTRY.json
  - fiction/MANUSCRIPT_INDEX.json
  - fiction/bible/
  - fiction/STYLE_GUIDE.md
  - fiction/manuscript/
protected_core_and_prose:
  - MANUSCRIPT_INDEX.json의 기존 본문 SHA
  - fiction/manuscript/ 전체 본문
  - CORE_CONFIRMED 항목
concurrent_branches_and_overlap: 열린 PR 없음. 현행 상태 문서와 검증기만 OVERLAP_REVIEW.
outputs:
  - fiction/analysis/REVERSE_OUTLINE_001_225.json
  - fiction/analysis/REVERSE_OUTLINE_REPORT.md
  - fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md
  - 갱신된 ACTIVE_CONTEXT.md, HANDOFF.md, 기획서
acceptance_criteria:
  - 225화 정확히 한 번씩 포함
  - 각 화의 시작 상태·목표·장애·전환·대가·종료 상태·다음 압력 필드 존재
  - 12개 품질 게이트가 편성·POV·기능을 대표
  - 구형 문서·archive를 활성 입력으로 참조하지 않음
validation:
  - 기존 운영체계·원고 검사
  - 역개요 스키마·화수·원문 SHA 연결 검사
  - reference-freshness 재감사
rollback: 새 analysis 파일 제거 및 상태 문서 직전 커밋 복원
```
