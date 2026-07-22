#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit("usage: bootstrap_generate_content.py INTEGRATED.txt HANDOFF.txt REPO_ROOT")
SRC, HANDOFF, ROOT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
text = SRC.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
lines = text.splitlines()
start_re = re.compile(r"^\(제(\d+)화 시작 - (.*?)\)$")
end_re = re.compile(r"^\(제(\d+)화 끝\)$")
chapters = {}
i = 0
while i < len(lines):
    match = start_re.match(lines[i].strip())
    if not match:
        i += 1
        continue
    number, title, source_start = int(match.group(1)), match.group(2).strip(), i + 1
    j = i + 1
    while j < len(lines) and not lines[j].strip(): j += 1
    if j >= len(lines) or lines[j].strip() != "---": raise SystemExit(f"chapter {number}: missing POV separator")
    j += 1
    while j < len(lines) and not lines[j].strip(): j += 1
    if j >= len(lines): raise SystemExit(f"chapter {number}: missing POV")
    pov = lines[j].strip(); j += 1; body_start = j
    while j < len(lines) and not end_re.match(lines[j].strip()): j += 1
    if j >= len(lines) or int(end_re.match(lines[j].strip()).group(1)) != number: raise SystemExit(f"chapter {number}: bad end marker")
    body = "\n".join(lines[body_start:j]).strip()
    chapters[number] = (title, pov, body, source_start, j + 1)
    i = j + 1
if set(chapters) != set(range(1, 226)): raise SystemExit(f"chapter set mismatch: {len(chapters)}")
forbidden = ("쵸르브라트", "미하일 카쉬프", "피엘렛토", "붉은 늑대")
for number, (_, _, body, _, _) in chapters.items():
    if len(body) < 2000: raise SystemExit(f"chapter {number}: below 2,000 chars ({len(body)})")
    stale = [term for term in forbidden if term in body]
    if stale: raise SystemExit(f"chapter {number}: stale active terms {stale}")

def group(number):
    if number <= 70: return "part-1", "1부 《폭풍의 눈》"
    if number <= 95: return "side-story-lake", "외전1 《호수가 보이는 마을》"
    if number <= 130: return "side-story-alice", "외전2 《붉은 여왕의 첫 임무》"
    if number <= 165: return "side-story-ian", "외전3 《미래를 기록하는 사람》"
    return "part-2", "2부 《네가 없는 마을》"

manuscript = ROOT / "fiction/manuscript"
if manuscript.exists():
    import shutil; shutil.rmtree(manuscript)
index = {"schema_version":1,"source":"[SUPERSEDED] integrated Google Doc export used only for migration evidence","generated_at":"2026-07-22","counting_rule":"본문만 집계하며 시작·끝 마커와 POV 표식은 제외한다. 공백과 줄바꿈은 포함한다.","chapters":[]}
for lower in range(1, 226, 5):
    upper = min(lower + 4, 225); directory, label = group(lower)
    bundle = f"fiction/manuscript/{directory}/{lower:03d}-{upper:03d}.md"
    output = [f"# {label} · 제{lower}화~제{upper}화", "", "> 상태: 2,000자 이상 확장 원고 DRAFT. 전체 구조·연속성·문장 심화 퇴고 전.", ""]
    for number in range(lower, upper + 1):
        title, pov, body, start, end = chapters[number]
        output += [f"## 제{number}화 · {title}", "", f"**POV:** {pov}", "", body, "", f"<!-- source-lines: {start}-{end} -->", ""]
        if number < upper: output += ["---", ""]
        index["chapters"].append({"chapter":number,"title":title,"pov":pov,"body_chars":len(body),"body_sha256":hashlib.sha256(body.encode()).hexdigest(),"bundle":bundle})
    path = ROOT / bundle; path.parent.mkdir(parents=True, exist_ok=True); path.write_text("\n".join(output).rstrip()+"\n", encoding="utf-8")
(ROOT/"fiction/MANUSCRIPT_INDEX.json").write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def md_normalize(block):
    out=[]
    for raw in block:
        stripped=raw.strip()
        if not stripped: out.append(""); continue
        if set(stripped)=={"="}: continue
        if stripped.startswith("■ "): out.append("## "+stripped[2:].strip())
        elif stripped.startswith("● "): out.append("### "+stripped[2:].strip())
        elif stripped.startswith("• "): out.append("- "+stripped[2:].strip())
        elif stripped.startswith("└ "): out.append("  - "+stripped[2:].strip())
        else: out.append(stripped)
    compact=[]
    for line in out:
        if line=="" and compact and compact[-1]=="": continue
        compact.append(line)
    return "\n".join(compact).strip()+"\n"

p1=ROOT/"fiction/bible/03_PART1_STORY_BIBLE_SOURCE.md"; p1.parent.mkdir(parents=True,exist_ok=True)
p1.write_text("# 1부 상세 기획 원문 변환본\n\n> 상태: SOURCE DETAIL. 현행 코어·상태 판정은 `01_PROJECT_CORE.md`와 `ACTIVE_CONTEXT.md`를 우선한다.\n\n"+md_normalize(lines[1995:5514]),encoding="utf-8")
p2=ROOT/"fiction/bible/04_PART2_STORY_BIBLE_SOURCE.md"
p2.write_text("# 2부 상세 기획 원문 변환본\n\n> 상태: SOURCE DETAIL. 현행 코어·상태 판정은 `01_PROJECT_CORE.md`와 `ACTIVE_CONTEXT.md`를 우선한다.\n\n"+md_normalize(lines[21362:22330]),encoding="utf-8")
archive=ROOT/"fiction/archive/source-imports/INTEGRATED_NON_MANUSCRIPT_SOURCE.md"; archive.parent.mkdir(parents=True,exist_ok=True)
archive.write_text("# 통합 문서 비원고 원문 보존본\n\n> 상태: ARCHIVE / SOURCE EVIDENCE. 기본 작업 입력 금지.\n\n---\n"+"\n".join(lines[:5514]).strip()+"\n\n---\n\n[원고 제1화~제95화는 fiction/manuscript/로 분리됨]\n\n"+"\n".join(lines[21362:22330]).strip()+"\n\n---\n\n[원문 22331행 이후는 원고 제96화~제225화로 분리됨]\n",encoding="utf-8")
if HANDOFF.is_file():
    handoff=ROOT/"fiction/archive/source-imports/COAUTHOR_HANDOFF_SOURCE.md"
    handoff.write_text("# 공동 작업 인수인계 기준서 · 원문 보존본\n\n> 상태: ARCHIVE / SOURCE EVIDENCE. 활성 기준은 fiction/HANDOFF.md다.\n\n---\n\n"+HANDOFF.read_text(encoding="utf-8-sig").strip()+"\n",encoding="utf-8")
print("generated 225 expanded chapters, hash index, and source-detail archives")
