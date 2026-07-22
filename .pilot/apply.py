#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
PAT=re.compile(r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",re.M|re.S)

def replace_chapter(item):
    path=ROOT/item["path"]
    text=path.read_text(encoding="utf-8")
    target=next((m for m in PAT.finditer(text) if int(m.group(1))==int(item["chapter"])),None)
    if target is None: raise SystemExit(f"chapter {item['chapter']} missing in {path}")
    old_body=target.group(4).strip()
    digest=hashlib.sha256(old_body.encode("utf-8")).hexdigest()
    if digest!=item["old_sha256"]: raise SystemExit(f"chapter {item['chapter']} baseline SHA mismatch: {digest}")
    new_body=item["new_body"]
    if hashlib.sha256(new_body.encode("utf-8")).hexdigest()!=item["new_sha256"]: raise SystemExit(f"chapter {item['chapter']} payload SHA mismatch")
    path.write_text(text[:target.start(4)]+new_body+text[target.end(4):],encoding="utf-8")

def replace_chunks(item):
    path=ROOT/item["path"]
    text=path.read_text(encoding="utf-8")
    for chunk in item["chunks"]:
        count=text.count(chunk["old"])
        if count!=1: raise SystemExit(f"chapter {item['chapter']} replacement count={count} in {path}")
        text=text.replace(chunk["old"],chunk["new"],1)
    path.write_text(text,encoding="utf-8")

def main():
    for module in sorted((ROOT/".pilot/major").glob("*.json")):
        for item in json.loads(module.read_text(encoding="utf-8")): replace_chapter(item)
    for module in sorted((ROOT/".pilot/simple").glob("*.json")):
        for item in json.loads(module.read_text(encoding="utf-8")): replace_chunks(item)
    index_path=ROOT/"fiction/MANUSCRIPT_INDEX.json"
    index=json.loads(index_path.read_text(encoding="utf-8"))
    actual={}
    for path in sorted((ROOT/"fiction/manuscript").rglob("*.md")):
        for match in PAT.finditer(path.read_text(encoding="utf-8")):
            body=match.group(4).strip(); n=int(match.group(1))
            actual[n]=(len(body),hashlib.sha256(body.encode("utf-8")).hexdigest())
    if sorted(actual)!=list(range(1,226)): raise SystemExit("chapter set mismatch")
    for item in index["chapters"]:
        item["body_chars"],item["body_sha256"]=actual[int(item["chapter"])]
    index["generated_at"]="2026-07-23"
    index_path.write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
