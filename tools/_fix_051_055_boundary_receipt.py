#!/usr/bin/env python3
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'fiction'
chapter_re=re.compile(r'^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)',re.M|re.S)
text=(F/'manuscript/part-1/056-060.md').read_text(encoding='utf-8')
parsed={int(m.group(1)):m.group(4).strip() for m in chapter_re.finditer(text)}
if 56 not in parsed: raise SystemExit('legacy Ch56 not parsed')
actual=hashlib.sha256(parsed[56].encode('utf-8')).hexdigest()
path=F/'analysis/SCENE_PASS_REGISTRY.json'; data=json.loads(path.read_text(encoding='utf-8'))
match=[x for x in data['completed_bundle_passes'] if x.get('bundle')=='fiction/manuscript/part-1/051-055.md']
if len(match)!=1: raise SystemExit('Ch051-055 scene pass missing or duplicated')
match[0]['preserved_boundary_shas']['56']=actual
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'current legacy Ch56 boundary SHA={actual}')
