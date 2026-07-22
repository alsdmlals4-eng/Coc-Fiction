#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit('usage: bootstrap_generate_content.py INTEGRATED.txt HANDOFF.txt REPO_ROOT')
SRC = Path(sys.argv[1])
HANDOFF = Path(sys.argv[2])
ROOT = Path(sys.argv[3])
text = SRC.read_text(encoding='utf-8-sig').replace('\r\n','\n').replace('\r','\n')
lines = text.splitlines()

# Preserve the directly exported coauthor handoff with a small archival header.
handoff_text = HANDOFF.read_text(encoding='utf-8-sig').replace('\r\n','\n').replace('\r','\n').strip()
handoff_out = ROOT/'fiction/archive/source-imports/COAUTHOR_HANDOFF_SOURCE.md'
handoff_out.parent.mkdir(parents=True, exist_ok=True)
handoff_out.write_text(
    '# 공동 작업 인수인계 기준서 · 원문 보존본\n\n'
    '> Google Docs 내보내기 원문을 Markdown으로 보존한다. 활성 작업 기준은 `../../HANDOFF.md`이며, 이 파일은 누락 대조와 역사 확인용이다.\n\n'
    '---\n\n' + handoff_text + '\n', encoding='utf-8')

# Extract all 225 chapters and split them into human-editable five-chapter bundles.
start_re = re.compile(r'^\(제(\d+)화 시작 - (.*?)\)$')
end_re = re.compile(r'^\(제(\d+)화 끝\)$')
chapters: dict[int, tuple[str,str,str,int,int]] = {}
i = 0
while i < len(lines):
    m = start_re.match(lines[i].strip())
    if not m:
        i += 1
        continue
    n = int(m.group(1)); title = m.group(2).strip(); start_line = i + 1
    j = i + 1
    while j < len(lines) and not lines[j].strip(): j += 1
    if j >= len(lines) or lines[j].strip() != '---':
        raise SystemExit(f'chapter {n}: missing POV separator')
    j += 1
    while j < len(lines) and not lines[j].strip(): j += 1
    if j >= len(lines): raise SystemExit(f'chapter {n}: missing POV')
    pov = lines[j].strip(); j += 1
    body_start = j
    while j < len(lines) and not end_re.match(lines[j].strip()): j += 1
    if j >= len(lines): raise SystemExit(f'chapter {n}: missing end marker')
    em = end_re.match(lines[j].strip())
    if int(em.group(1)) != n: raise SystemExit(f'chapter {n}: mismatched end marker')
    body = '\n'.join(lines[body_start:j]).strip()
    chapters[n] = (title, pov, body, start_line, j + 1)
    i = j + 1
if set(chapters) != set(range(1, 226)):
    raise SystemExit(f'chapter set mismatch: got {len(chapters)} chapters')

def group(n: int) -> tuple[str,str]:
    if n <= 70: return 'part-1', '1부 《폭풍의 눈》'
    if n <= 95: return 'side-story-lake', '외전1 《호수가 보이는 마을》'
    if n <= 130: return 'side-story-alice', '외전2 — 엘리스'
    if n <= 165: return 'side-story-ian', '외전3 — 이안'
    return 'part-2', '2부'

manuscript = ROOT/'fiction/manuscript'
for d in ('part-1','side-story-lake','side-story-alice','side-story-ian','part-2'):
    (manuscript/d).mkdir(parents=True, exist_ok=True)
for lo in range(1, 226, 5):
    hi = min(lo + 4, 225)
    directory, label = group(lo)
    out = [f'# {label} · 제{lo}화~제{hi}화', '', '> 편집 단위: 5화. 각 화의 원문 문구와 순서를 보존한다.', '', '---', '']
    for n in range(lo, hi + 1):
        title, pov, body, sl, el = chapters[n]
        out.extend([f'## 제{n}화 · {title}', '', f'**POV:** {pov}', '', body, '', f'<!-- source-lines: {sl}-{el} -->', ''])
        if n < hi:
            out.extend(['---', ''])
    (manuscript/directory/f'{lo:03d}-{hi:03d}.md').write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')

# Human-editable story-bible conversion. The line ranges are stable source sections
# immediately before the corresponding manuscript blocks.
def md_normalize(block: list[str]) -> str:
    out: list[str] = []
    for raw in block:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            out.append('')
            continue
        if set(stripped) == {'='}:
            continue
        if stripped.startswith('■ '):
            out.append('## ' + stripped[2:].strip())
        elif stripped.startswith('● '):
            out.append('### ' + stripped[2:].strip())
        elif stripped.startswith('• '):
            out.append('- ' + stripped[2:].strip())
        elif stripped.startswith('└ '):
            out.append('  - ' + stripped[2:].strip())
        else:
            out.append(stripped)
    compact: list[str] = []
    for line in out:
        if line == '' and compact and compact[-1] == '':
            continue
        compact.append(line)
    return '\n'.join(compact).strip() + '\n'

p1 = ROOT/'fiction/bible/03_PART1_STORY_BIBLE.md'
p1.parent.mkdir(parents=True, exist_ok=True)
p1.write_text(
    '# 1부 스토리 바이블\n\n> 원문 출처: 통합 문서 1996행부터. 문구를 보존하고 Markdown 표기만 정리했다.\n\n'
    + md_normalize(lines[1995:5514]), encoding='utf-8')
p2 = ROOT/'fiction/bible/04_PART2_STORY_BIBLE.md'
p2.write_text(
    '# 2부 스토리 바이블\n\n> 원문 출처: 통합 문서 21363행부터. 문구를 보존하고 Markdown 표기만 정리했다.\n\n'
    + md_normalize(lines[21362:22330]), encoding='utf-8')

# Preserve the non-manuscript source evidence without duplicating active manuscript.
archive = ROOT/'fiction/archive/source-imports/INTEGRATED_NON_MANUSCRIPT_SOURCE.md'
archive.write_text(
    '# 통합 문서 비원고 원문 보존본\n\n'
    '> 상태: **ARCHIVE / SOURCE EVIDENCE**  \n'
    '> 기본 집필·퇴고 시 읽지 않는다. 활성 규칙과 설정은 `../../FICTION_MASTER.md` 및 `../../bible/`을 사용한다.  \n'
    '> 이 파일은 가지치기·재구성 과정에서 고유 정보가 사라지지 않았는지 대조하기 위한 원문 보존본이다.\n\n'
    '---\n' + '\n'.join(lines[:5514]).strip() + '\n\n'
    '---\n\n[원고 제1화~제95화는 `fiction/manuscript/`로 분리됨]\n\n'
    + '\n'.join(lines[21362:22330]).strip() + '\n\n'
    '---\n\n[원문 22331행 이후는 원고 제96화~제225화로 분리됨]\n',
    encoding='utf-8')
print('generated 225 chapters, two story bibles, and two source archives')
