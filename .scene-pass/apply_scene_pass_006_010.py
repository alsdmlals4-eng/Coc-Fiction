#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
BUNDLE = FICTION / "manuscript" / "part-1" / "006-010.md"
INDEX_PATH = FICTION / "MANUSCRIPT_INDEX.json"
DATE = "2026-07-23"

CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)

EXPECTED_BEFORE = {
    6: "21439bdc3195607dd40d08965ec0e9fe98e1b0cd2b3de637e3564a4d26a3380a",
    7: "21ab36521212e93c78cb9f7f029b273b741607dbcb75fc430747521c760a80a5",
    8: "9c5c5e4b5fef29eb98de705a5af331881fa49078b5e9db66ee912a452591cbe2",
    9: "26acae6a529afc11bb47e68bdbbbd91846fbb683ab15939fb3c6f7190582855f",
    10: "62492d465a2cb3e0a83761ad050c04858e145596c44285accc63b3468ea72bdb",
}

REPLACEMENTS = [
    (
        "CH6_TIMELINE_ANCHOR",
        "저녁 식당은 바다 위에 떠 있다는 사실을 잊게 만들 만큼 밝았다.",
        "복도에서 첫 총성이 울리기 전, 저녁 식당은 바다 위에 떠 있다는 사실을 잊게 만들 만큼 밝았다.",
    ),
    (
        "CH7_SAME_SELF_PROTECTIVE_RESPONSE",
        "그러나 머릿속 어딘가에서 다른 자신이 문을 세게 두드렸다.",
        "그러나 자기 안의 차가운 보호 반응이 머릿속 문을 세게 두드렸다.",
    ),
    (
        "CH9_NO_DUPLICATE_BOARDING",
        """아킴이 선내로 들어왔을 때 식당은 이미 피와 증기로 가득했다.


지원선에서 갈고리를 타고 넘어오는 동안에도 비명이 들렸지만, 금속 문을 여는 순간 냄새가 먼저 덮쳤다. 피, 술, 타버린 전선, 뜨거운 음식이 뒤섞인 냄새였다. 사람들은 살기 위해 달렸고 비야키는 그 움직임을 사냥감의 신호로 받아들였다.""",
        """같은 시각, 아킴이 식당 쪽 복도에 들어섰을 때 문틈에서는 이미 피와 증기가 밀려나오고 있었다.


조금 전 서비스 통로에서 데커와 총을 주고받는 동안에도 비명은 끊이지 않았다. 금속 방화문을 여는 순간 냄새가 먼저 덮쳤다. 피, 술, 타버린 전선, 뜨거운 음식이 뒤섞인 냄새였다. 사람들은 살기 위해 달렸고 비야키는 그 움직임을 사냥감의 신호로 받아들였다.""",
    ),
]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_manuscript() -> dict[int, dict[str, object]]:
    parsed: dict[int, dict[str, object]] = {}
    for path in sorted((FICTION / "manuscript").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in CHAPTER_RE.finditer(text):
            number = int(match.group(1))
            if number in parsed:
                raise SystemExit(f"duplicate chapter {number}")
            body = match.group(4).strip()
            parsed[number] = {
                "chapter": number,
                "title": match.group(2).strip(),
                "pov": match.group(3).strip(),
                "body": body,
                "body_chars": len(body),
                "body_sha256": sha(body),
                "bundle": path.relative_to(ROOT).as_posix(),
            }
    if sorted(parsed) != list(range(1, 226)):
        raise SystemExit(f"chapter set mismatch: {len(parsed)}")
    return parsed


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one old block, found {count}")
    if new in text:
        raise SystemExit(f"{label}: new block already present before replacement")
    return text.replace(old, new, 1)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def update_existing(path: Path, replacements: list[tuple[str, str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    for label, old, new in replacements:
        text = replace_once(text, old, new, f"{path.relative_to(ROOT)}::{label}")
    write_text(path, text)


before = parse_manuscript()
for number, expected in EXPECTED_BEFORE.items():
    actual = str(before[number]["body_sha256"])
    if actual != expected:
        raise SystemExit(f"chapter {number} precondition SHA mismatch: {actual}")

bundle_text = BUNDLE.read_text(encoding="utf-8")
for label, old, new in REPLACEMENTS:
    bundle_text = replace_once(bundle_text, old, new, label)
write_text(BUNDLE, bundle_text)

after = parse_manuscript()
changed = [n for n in range(1, 226) if before[n]["body_sha256"] != after[n]["body_sha256"]]
if changed != [6, 7, 9]:
    raise SystemExit(f"unexpected changed chapters: {changed}")

index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
index_entries = {int(item["chapter"]): item for item in index["chapters"]}
for number in range(1, 226):
    chapter = after[number]
    entry = index_entries[number]
    entry["title"] = chapter["title"]
    entry["pov"] = chapter["pov"]
    entry["body_chars"] = chapter["body_chars"]
    entry["body_sha256"] = chapter["body_sha256"]
    entry["bundle"] = chapter["bundle"]
INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

subprocess.run(
    [sys.executable, "tools/build_fiction_reverse_outline.py"],
    cwd=ROOT,
    check=True,
)

chapter_rows = "\n".join(
    f"| 제{n}화 | {before[n]['body_chars']}자 | {after[n]['body_chars']}자 | `{after[n]['body_sha256']}` |"
    for n in range(6, 11)
)

scene_cards = f"""# 제6화~제10화 수동 장면 카드·연속성 패스

상태: **ACTIVE / BUNDLE PASS COMPLETE / PRIMARY SOURCE DIRECT MATCH UNVERIFIED**  
갱신: {DATE}

## 범위와 근거

- 대상 원고: `fiction/manuscript/part-1/006-010.md`
- 경계 확인: 제5화와 제11화
- 사용 근거: 현행 작품 코어, Canon Registry, 1부 바이블, Style Guide, 같은 커밋의 원고·색인·역개요
- 원본 근거: 사용자가 제공한 Drive 폴더는 현재 연결 계정에서 메타데이터 404·자식 0개로 반환되어 직접 대조하지 못했다.
- 판정 한계: 원본 TRPG 로그·PDF와 대사·세부 동선의 완전 일치는 `UNVERIFIED`

## 제6화 · 평생의 과제

```yaml
scene_id: P1-006
pov_time_place: 이안 / 제5화 후 제시되지만 실제 시간은 복도 첫 총성 직전 / 저녁 식당
starting_state: 브루스와 이안은 고서·펜던트 반응을 경계하고, 승객들은 평범한 항해 중이라고 믿는다.
immediate_goal_or_focus: 이안이 펜던트 진동·브루스의 반응·선내 퇴로를 기록한다.
opposition_and_cost: 브루스는 진실을 숨기고, 윌리엄의 선제 보호 논리가 위험한 주제 압력을 설치한다.
turn_or_discovery: 물잔은 움직이지 않는데 펜던트만 반응하고 노란 코트의 사내가 문밖에서 홀을 센다.
ending_state: 이안과 브루스만 이상을 인지하며 밀리는 아직 보호받지 못한 정보 상태에 남는다.
revealed_and_withheld_information: 노란 코트와 펜던트의 연결은 공개되지만 고서·선박의 정확한 규칙은 숨겨진다.
character_world_state_changes: 이안은 지식보다 퇴로를 먼저 외우며 능동적 생존 태도로 이동한다.
protected_image_line_or_emotion: 밝은 식당 전체와 맞지 않는 문밖의 노란 소매.
next_pressure: 제7화에서 노란 코트가 실제로 홀에 들어온다.
continuity_dependencies: 제5화의 침투·총격보다 시간상 앞선 병행 장면임을 첫 문장에 표시한다.
```

## 제7화 · 노란 코트가 들어온 밤

```yaml
scene_id: P1-007
pov_time_place: 엘리스 / 제6화 직후 / 저녁 식당
starting_state: 엘리스는 아버지의 부재에 서운하고 주안의 비강제적 경호 방식에 신뢰를 보이기 시작한다.
immediate_goal_or_focus: 가족과 식사하며 평범한 시간을 유지하고 불길한 감각에서 벗어난다.
opposition_and_cost: 차가운 보호 반응이 위험을 먼저 감지하고 노란 코트가 홀 전체를 의식의 대상으로 삼는다.
turn_or_discovery: 엘리스가 이유를 설명하지 못한 채 즉시 퇴장을 요구하고 주안이 질문보다 이동을 우선한다.
ending_state: 평범한 저녁은 비야키 출현 직전까지 붕괴하며 엘리스는 위험을 직접 보겠다고 선택한다.
revealed_and_withheld_information: 보호 반응은 같은 자아의 내부 기능으로 제시되지만 기원과 규칙은 숨긴다.
character_world_state_changes: 엘리스는 보호 대상에 머물지 않고 정보와 선택에 참여한다.
protected_image_line_or_emotion: 식탁보 아래의 숨소리, 노란 구두, 잔을 두드리는 맑은 소리.
next_pressure: 제8화의 첫 비명과 식당 학살.
continuity_dependencies: 노란 코트는 합석하지 않고 홀 전체에 축배를 든다는 Canon을 유지한다.
```

## 제8화 · 식당의 비명

```yaml
scene_id: P1-008
pov_time_place: 주안 / 제7화 즉시 연속 / 식당과 주방 입구
starting_state: 주안과 엘리스는 원탁 아래에 있고 세실리아는 케인과 서쪽 복도로 이동한다.
immediate_goal_or_focus: 엘리스와 민간인을 주방 후방 통로로 탈출시킨다.
opposition_and_cost: 비야키·군중 압사·황색 침투조·노란 코트의 인식 공격이 동시에 작동한다.
turn_or_discovery: 엘리스가 아이를 두고 갈지 묻고 주안은 명령이 아니라 이미 자신의 몸이 움직일 준비를 했음을 인지한다.
ending_state: 민간인 일부와 엘리스는 주방 통로로 이동하고 주안은 흰 방 기억의 첫 잔향을 숨긴다.
revealed_and_withheld_information: 주안의 비정상적 힘과 노란 코트가 그를 찾았다는 사실은 드러나나 과거의 정체는 숨긴다.
character_world_state_changes: 주안은 보호 대상만 구하라는 교육보다 눈앞의 민간인을 구하는 선택을 우선한다.
protected_image_line_or_emotion: 상식에서 벗어난 것은 괴물만이 아니었다.
next_pressure: 제9화의 병행 세실리아 납치와 제10화의 브루고 추적.
continuity_dependencies: 뺨의 얕은 상처, 흰 방 잔향, 세실리아가 서쪽 복도에 있다는 지식이 다음 화로 이월된다.
```

## 제9화 · 납치된 세실리아

```yaml
scene_id: P1-009
pov_time_place: 아킴 / 제8화와 병행 / 식당 반대편·남서 창고 방향 복도
starting_state: 아킴은 제5화에서 이미 승선해 데커와 교전했고 황색 침투 작전은 식당 학살과 동시에 진행된다.
immediate_goal_or_focus: 세실리아를 생존 상태로 확보하고 황색 작전의 이탈 변수를 관리한다.
opposition_and_cost: 카터 경호원, 데커·델타그린 방어선, 선박을 섬으로 끄는 제3의 힘이 작전을 흔든다.
turn_or_discovery: 세실리아 확보에는 성공하지만 엔진·방향타와 무관한 외력이 배를 섬으로 끌고 간다.
ending_state: 세실리아는 황색 포로가 되고, 아킴은 황색 내부 명령 주체가 하나가 아님을 기억한다.
revealed_and_withheld_information: 히템은 육체가 있는 상태로 등장하고 이안에 대한 별도 상부 명령은 이유를 숨긴다.
character_world_state_changes: 아킴의 친절과 효율이 납치의 정당화와 모순되지 않는 인물 윤리가 강화된다.
protected_image_line_or_emotion: 죽일 필요가 없는 사람을 죽이지 않는 것과 납치가 잘못됐다고 보는 것은 다른 문제다.
next_pressure: 브루고가 엘리스를 추적하고 선박 자체가 붕괴한다.
continuity_dependencies: 제5화의 승선·데커 교전을 반복하지 않고 그 뒤 시간으로 연결한다. 엘리스·주안은 세실리아의 실제 납치를 아직 모른다.
```

## 제10화 · 거짓 무전과 브루고

```yaml
scene_id: P1-010
pov_time_place: 주안 / 제8화 직후 / 객실 복도
starting_state: 주안과 엘리스는 식당을 탈출했고 세실리아가 서쪽 복도로 갔다는 정보만 안다.
immediate_goal_or_focus: 가짜 무전을 판별하고 엘리스를 안전한 경로로 이동시킨다.
opposition_and_cost: 케인의 목소리를 흉내 낸 무전, 브루고의 육체, 노란 코트의 정신 공격이 판단·몸·자아를 순차 압박한다.
turn_or_discovery: 엘리스가 명령을 철회하고 주안 자신의 혐오와 선택을 붙잡게 하면서 정신 공격에 빈틈이 생긴다.
ending_state: 주안은 일어서지만 떨림과 뼈의 감촉이 남고, 선체 붕괴가 전투보다 큰 압력으로 전환된다.
revealed_and_withheld_information: 복종 각인의 문장은 보이지만 엘리스를 지키려는 감정의 기원은 계속 증명 불가다.
character_world_state_changes: 엘리스는 강제 명령 대신 주안의 감정과 선택을 되돌려 준다.
protected_image_line_or_emotion: “내가 명령해서가 아니라, 당신이 저 사람을 싫어하잖아.”
next_pressure: 제11화에서 선체가 갈라지고 탈론이 등장한다.
continuity_dependencies: 브루고의 뼈 감촉·무릎 떨림·보호 반응 상태가 제11화 초반에 잔류한다.
```

## 경계 연속성

| 경계 | 시간·POV | 상태 이월 | 판정 |
|---|---|---|---|
| 제5→6화 | 아킴에서 이안 / 제6화는 시간상 짧은 되감기 | 황색은 이미 침투 중이지만 식당 승객은 아직 총성을 듣기 전 | `MUST_FIX RESOLVED` — 시간 표지 추가 |
| 제6→7화 | 같은 식당 / 이안에서 엘리스 | 노란 코트가 문밖에서 홀 안으로 진입 | `PASS` |
| 제7→8화 | 즉시 연속 / 엘리스에서 주안 | 원탁 아래 위치, 세실리아 서쪽 이동, 비야키 출현 | `PASS` |
| 제8→9화 | 병행 전환 / 주안에서 아킴 | 식당 반대편에서 세실리아 확보 작전 진행 | `MUST_FIX RESOLVED` — 중복 승선 제거 |
| 제9→10화 | 병행선 합류 / 아킴에서 주안 | 브루고의 엘리스 추적, 선박의 비정상적 기울기 | `PASS` |
| 제10→11화 | 즉시 연속 / 주안 유지 | 정신·육체 후유증, 브루고 쓰러짐, 선체 균열 | `PASS` |

## 인물·상태 체크포인트

| 인물 | 위치 | 부상·상태 | 지식 | 소지품·비밀 |
|---|---|---|---|---|
| 이안 | 제6화 식당 | 펜던트 진동 감지 | 노란 코트와 펜던트 반응을 인지 | 펜던트·수첩, 밀리에게 이상을 숨김 |
| 엘리스 | 제10화 객실 복도 | 공포 뒤 보호 반응 전면화 | 노란 코트가 위험하고 세실리아가 서쪽으로 이동했다고 앎 | 캐릭터 인형, 주안의 선택을 강제하지 않으려 함 |
| 주안 | 제10화 객실 복도 | 뺨 상처, 비정상적 힘, 무릎 떨림, 흰 방 잔향 | 가짜 무전·노란 코트의 인식·복종 문장을 일부 경험 | 무전기, 자신의 감정 기원은 비밀·불확실 |
| 아킴 | 세실리아 호송선 | 데커와의 교전 흔적, 전투 가능 | 황색 내부 명령 주체가 하나가 아니며 섬이 배를 끈다고 판단 | 소총, 이안 생존 예외 명령 기억 |
| 세실리아 | 황색 포로 호송 | 생존·강제 이동 | 엘리스 위치를 모름 | 황색이 돈·정치보다 다른 목적을 가짐을 추정 |
| 히템 | 선내 황색 병력과 합류 | 육체 보유 상태 | 카터·고서 회수 상황을 공유 | 아직 신체 상실 전 |

## Finding-first 판정

### MUST_FIX-01 — 제5→6화 시간 되감기 무표지 — RESOLVED

제5화는 총성과 비상등까지 진행하지만 제6화는 더 이른 평온한 식당으로 돌아간다. 첫 문장에 총성 이전이라는 시간 표지를 추가해 병행 구조를 명시했다.

### MUST_FIX-02 — 제9화 아킴 중복 승선 — RESOLVED

아킴은 제5화에서 이미 갈고리로 승선하고 데커와 교전했다. 제9화에서 다시 지원선·갈고리 승선을 서술하던 문단을 식당 쪽 복도로 이동하는 현재 장면으로 교체했다.

### SHOULD_FIX-01 — 제7화 보호 반응의 별개 자아 오독 위험 — RESOLVED

`다른 자신`을 같은 자아 안의 차가운 보호 반응으로 교정했다. 내부 명령형 목소리와 공포 감지 기능은 보존했다.

### REJECT-01 — 제8화와 제10화 흰 방 기억의 중복 삭제

제8화는 노란 코트가 주안을 알아보며 처음 잔향을 건드리는 설치이고, 제10화는 직접 정신 공격으로 복종 문장을 체험하는 확대다. 정보·비용이 전진하므로 구조 중복이 아니다.

### UNVERIFIED-01 — 원본 장면 직접 충실도

현행 원고·Canon·경계 인과는 일치한다. 그러나 제공된 원본 폴더가 현재 연결 계정에서 열리지 않아 원본 대사·세부 동선·사건 순서의 직접 대조는 완료하지 않았다.

## 현재 SHA

{chapter_rows}
"""

registry = {
    "schema_version": 1,
    "updated_at": DATE,
    "status": "ACTIVE / MANUAL_SCENE_PASS_TRACKER",
    "source_policy": {
        "primary_source_direct_match": "UNVERIFIED",
        "reason": "User-provided Google Drive source folder is not accessible to the connected account; metadata 404 and direct children empty.",
        "folder_url": "https://drive.google.com/drive/folders/1EPA-bg8ExjvK-XPadKqdab2cCSNMWVt0",
    },
    "representative_pilots": [10, 95, 180],
    "completed_bundle_passes": [
        {
            "bundle": "fiction/manuscript/part-1/006-010.md",
            "chapters": [6, 7, 8, 9, 10],
            "boundary_chapters": [5, 11],
            "scene_cards": "fiction/analysis/SCENE_CARDS_006_010.md",
            "revision_report": "fiction/reports/REVISION_2026-07-23_SCENE_PASS_006_010.md",
            "chapter_shas": {str(n): after[n]["body_sha256"] for n in range(6, 11)},
            "status": "COMPLETE_INTERNAL_CONTINUITY / PRIMARY_SOURCE_UNVERIFIED",
        }
    ],
    "next_bundle_passes": [
        "fiction/manuscript/side-story-lake/091-095.md",
        "fiction/manuscript/part-2/176-180.md",
    ],
}
write_text(FICTION / "analysis" / "SCENE_CARDS_006_010.md", scene_cards)
write_text(
    FICTION / "analysis" / "SCENE_PASS_REGISTRY.json",
    json.dumps(registry, ensure_ascii=False, indent=2),
)

report = f"""# 제6화~제10화 5화 묶음 장면 카드·연속성 패스 Revision Report

상태: **COMPLETED BUNDLE PASS / WHOLE-MANUSCRIPT REVISION NOT COMPLETE**  
날짜: {DATE}

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

{chapter_rows}

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
"""
write_text(FICTION / "reports" / "REVISION_2026-07-23_SCENE_PASS_006_010.md", report)

contract = """# 제6화~제10화 묶음 장면 카드·연속성 작업 계약

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
"""
write_text(ROOT / "docs" / "coordination" / "SCENE_PASS_006_010_WORK_CONTRACT.md", contract)

active_context = """# ACTIVE CONTEXT

갱신: 2026-07-23

## 현재 단계

- Work Mode: `REVIEW`
- Manuscript Stage: `REVISE`
- 주 Skill: `fiction-revision-and-validation: scene-diagnostic / continuity-check / adversarial-loop / regression-check / pr-review`
- 보조 Skill: `fiction-story-development: scene-card / plot-and-causality / stress-test`, `fiction-canon-and-research: canon-audit / continuity-map / timeline-and-state / reference-freshness`, `fiction-drafting: approved-rewrite / pov-and-distance / action-and-reaction`, `fiction-project-operations: checkpoint / handoff / execution-report`

## 완료

- 제1화~제225화 최신 확장 원고와 45개 5화 묶음 유지
- 화별 제목·POV·분량·본문 SHA 색인과 구조 역개요 기준선 유지
- 대표 품질 게이트 12화와 제10·95·180화 파일럿 완료
- 제177화~제225화 비정본 장기 세력 기능 전파 교정 완료
- `006-010` 묶음의 제6화~제10화 수동 장면 카드와 제5·11화 경계 연속성 패스 완료
- 제5→6화 시간 되감기 표지, 제9화 중복 승선, 제7화 동일 자아 보호 반응 표현 교정
- 변경 제6·7·9화의 분량·SHA와 225화 역개요 재생성
- Scene Pass Registry와 전용 회귀 검사 추가

## 현재 원고 상태

- 화수: 225
- 편집 묶음: 45
- 상태: `확장 원고 DRAFT / 구조 역개요 기준선 완료 / 대표 3화 파일럿 완료 / 006-010 묶음 패스 완료 / 원본 전체 감사 전`

사용자가 제공한 원본 Drive 폴더는 현재 연결 계정에서 폴더 자식 0개·메타데이터 404로 확인됐다. 따라서 `006-010` 묶음의 내부 Canon·연속성은 검증했지만 원본 대사·세부 동선 직접 충실도는 `UNVERIFIED`다.

## 이번 묶음에서 확정한 규칙

1. 병행 POV가 더 이른 시점으로 돌아가면 첫 문단에 시간 앵커를 둔다.
2. 다른 POV에서 이미 완료된 승선·이동·교전을 새 현재 장면처럼 반복하지 않는다.
3. 같은 사건의 병행 전환은 `동일 시각`과 서로 다른 위치·목표를 명료하게 한다.
4. 보호 반응은 같은 자아의 상태·기능으로 유지한다.
5. 장면 카드에 시간·위치·부상·지식·소지품·비밀 상태를 함께 기록한다.

## 남은 구조 우선순위

1. `091-095` 묶음의 장문단·호수 결말 경계와 제90→91·제95→96화 인계
2. `176-180` 묶음의 의료·기관 절차·권한 연속성
3. 외전2 제96화~제100화의 시간 전환·설명 밀도
4. 외전3·2부의 주제어 직접 설명 집중
5. 2부 중반의 절차·책임 논점 반복 위험

## 다음 정확한 작업

`fiction/manuscript/side-story-lake/091-095.md`를 대상으로 제90화와 제96화까지 포함해 수동 장면 카드·연속성 패스를 수행한다. 그다음 `fiction/manuscript/part-2/176-180.md`로 이동한다.

## 변경 금지

`FICTION_MASTER.md`와 `CANON_REGISTRY.json`을 따른다. 자동 역개요와 통계 플래그를 수정 명령으로 쓰지 않는다. 원고 수정 시 색인·역개요·Scene Pass Registry·Revision Report를 같은 PR에서 갱신한다.
"""
write_text(FICTION / "ACTIVE_CONTEXT.md", active_context)

handoff = """# 《폭풍의 눈》 활성 인수인계

갱신: 2026-07-23

## 먼저 읽을 파일

1. `FICTION_MASTER.md`
2. `ACTIVE_CONTEXT.md`
3. `CANON_REGISTRY.json`
4. `analysis/SCENE_PASS_REGISTRY.json`
5. 현재 묶음의 `analysis/SCENE_CARDS_*.md`
6. 최신 `reports/REVISION_*.md`
7. `analysis/REPRESENTATIVE_CHAPTER_GATES.md`
8. `analysis/REVERSE_OUTLINE_REPORT.md`
9. `MANUSCRIPT_INDEX.json`
10. `bible/01_PROJECT_CORE.md`
11. 해당 부의 Story Bible과 현재 작업할 5화 원고

`analysis/REVERSE_OUTLINE_001_225.json`은 화별 탐색·자동 검사에 사용하며 일반 작업 시작 시 전체를 정독하지 않는다.

## 현재 상태

- 제1화~제225화 확장 원고와 45개 묶음 정상
- 225화 구조 역개요 기준선과 대표 품질 게이트 12화 정상
- 제10화·제95화·제180화 대표 파일럿 완료
- `006-010` 묶음 수동 장면 카드·연속성 패스 완료
- 제6·7·9화 최소 수정과 색인·역개요 동기화 완료
- 다음 단계: `091-095` → `176-180` 묶음 패스

## 제6화~제10화 경계 고정

- 제5화의 아킴 승선·데커 교전과 제6화 식당은 병행 구조다. 제6화는 복도 첫 총성 이전으로 명시한다.
- 제6→7→8화는 식당의 불길함·축배·비야키 학살이 직접 이어진다.
- 제9화는 제8화와 같은 시각 식당 반대편에서 세실리아 확보가 진행되는 병행 POV다.
- 제10→11화는 선체 붕괴와 주안의 후유증이 직접 이어진다.
- 제10화 종료 시 엘리스·주안은 세실리아가 서쪽으로 이동했다는 정보만 알고 실제 납치는 모른다.
- 히템은 선박에서 육체가 있는 상태다.

## 원본 자료 상태

사용자가 원본 폴더 `https://drive.google.com/drive/folders/1EPA-bg8ExjvK-XPadKqdab2cCSNMWVt0`를 제공했다. 현재 연결된 Google 계정에서는 자식 파일이 0개로 반환되고 폴더 메타데이터가 404다. 원본 본체에 접근하기 전까지 직접 원문 대조 완료로 표시하지 않는다.

권한이 열리면 `006-010` 묶음을 가장 먼저 재감사한 뒤 `091-095`, `176-180` 순서로 원본 비교를 확장한다.

## 작업 절차

현재 5화 원고 → 앞뒤 경계 화 → Scene Pass Registry → 해당 역개요 → 색인 SHA → 수동 장면 카드 → 시간·동선·부상·지식·소지품 → 적대적 비판 재판정 → 최소 수정 → 색인·역개요·Registry·Revision Report → 회귀 검사 순으로 진행한다.

## 주의

- 자동 역개요는 탐색 기준선이며 원고보다 우선하지 않는다.
- 파일럿·완료 묶음의 규칙을 모든 화에 기계적으로 복제하지 않는다.
- archive와 구형 Google Docs를 활성 입력으로 사용하지 않는다.
- 원본 폴더가 열려도 파일명만으로 최신·정본을 판단하지 않고 내용·수정 시각·Canon을 대조한다.
"""
write_text(FICTION / "HANDOFF.md", handoff)

start_here = """# Coc-Fiction 소설 작업 시작 지점

## 최초 읽기

```text
docs/coordination/CONCURRENT_WORK.md
→ [소설]/00_운영체계/OPERATING_MODEL.md
→ [소설]/00_운영체계/DOCUMENTATION_MAP.md
→ fiction/FICTION_MASTER.md
→ fiction/ACTIVE_CONTEXT.md
→ fiction/CANON_REGISTRY.json
→ fiction/analysis/SCENE_PASS_REGISTRY.json
→ 현재 묶음의 scene card·Revision Report
→ fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md
→ fiction/analysis/REVERSE_OUTLINE_REPORT.md
→ fiction/MANUSCRIPT_INDEX.json
→ fiction/STYLE_GUIDE.md
→ 현재 5화 원고 묶음
```

`REVERSE_OUTLINE_001_225.json`은 화별 탐색과 자동 검증에 사용하며 일반 작업 시작 시 전체를 매번 읽지 않는다.

## Work Mode와 Manuscript Stage

- Work Mode: `PLAN / BUILD / REVIEW`
- Manuscript Stage: `DISCOVER → OUTLINE → DRAFT → REVISE → POLISH`

현재 작품은 `REVISE`다. 225화 분량 확장, 구조 역개요 기준선, 대표 3화 파일럿, `006-010` 묶음 수동 장면 카드·연속성 패스가 완료됐다. 원본 전체 장면 감사와 나머지 묶음의 구조·연속성·문체·최종 교정은 완료되지 않았다.

## 프로젝트 Skill

- `fiction-project-operations`: 범위·동시 작업·체크포인트·인수인계
- `fiction-story-development`: 코어·주제·인물·인과·장면 카드·대표 장 품질
- `fiction-drafting`: 승인된 POV·대화·묘사·행동·리듬 수정
- `fiction-canon-and-research`: Canon·연표·지식·출처·구형 참조 감사
- `fiction-revision-and-validation`: 구조·연속성·문장·적대적 검토·회귀·PR 검수

사용자가 Skill을 직접 고를 필요는 없다. 요청에 맞는 최소 Skill과 mode를 자동 선택한다.

## 절대 우선순위

최신 사용자 지시 → `fiction/bible/01_PROJECT_CORE.md` → `fiction/CANON_REGISTRY.json` → 접근 가능한 원본 사건 기록 → 부별 바이블·연속성 → 현재 원고 → 수동 장면 카드 → 역개요·진단 → 외부 참고 순이다.

## 보호 규칙

- archive와 구형 Google Docs를 활성 정본처럼 사용하지 않는다.
- 사용자 승인 없이 작품 코어·결말·인물성·POV·문체를 바꾸지 않는다.
- 자동 역개요와 정량 플래그를 오류나 수정 명령으로 취급하지 않는다.
- 원본 본체가 없거나 접근되지 않으면 직접 대조 완료로 표시하지 않는다.
- 병행 POV의 시간·위치 전환을 무표지로 두거나 완료된 이동을 반복하지 않는다.
- 5화 단위 수정 뒤 원본·인과·POV·동선·상태·금지 설정·색인·역개요·Scene Pass Registry 회귀를 남긴다.

## 다음 시작 묶음

`fiction/manuscript/side-story-lake/091-095.md` → `fiction/manuscript/part-2/176-180.md` 순으로 수동 장면 카드와 연속성 패스를 진행한다.
"""
write_text(ROOT / "[소설]" / "00_운영체계" / "START_HERE.md", start_here)

documentation_map = """# Coc-Fiction Documentation Map

## 질문별 책임 원본

| 질문 | 책임 원본 |
|---|---|
| 현재 상태와 다음 작업 | `fiction/ACTIVE_CONTEXT.md` |
| 작품 정체성·주제·변경 금지 | `fiction/bible/01_PROJECT_CORE.md` |
| 정본 우선순위·편성·분량·작업 기준 | `fiction/FICTION_MASTER.md` |
| Canon·폐기·별칭 | `fiction/CANON_REGISTRY.json` |
| 인물·세계·연속성 | `fiction/bible/02_CANON_AND_CONTINUITY.md` |
| 1부·2부 구조 | `fiction/bible/03_PART1_STORY_BIBLE.md`, `fiction/bible/04_PART2_STORY_BIBLE.md` |
| POV·문체·표기·묶음 패스 규칙 | `fiction/STYLE_GUIDE.md` |
| 실제 확장 원고 | `fiction/manuscript/` |
| 화별 제목·POV·분량·원문 SHA | `fiction/MANUSCRIPT_INDEX.json` |
| 225화 구조 역개요·구조 진단 | `fiction/analysis/REVERSE_OUTLINE_001_225.json`, `fiction/analysis/REVERSE_OUTLINE_REPORT.md` |
| 대표 화 품질 기준 | `fiction/analysis/REPRESENTATIVE_CHAPTER_GATES.md` |
| 완료 묶음·다음 묶음·SHA | `fiction/analysis/SCENE_PASS_REGISTRY.json` |
| 제6~10화 수동 장면 카드 | `fiction/analysis/SCENE_CARDS_006_010.md` |
| 대표 3화 파일럿 근거 | `fiction/reports/REVISION_2026-07-23_PILOT_10_95_180.md` |
| 제6~10화 변경 근거 | `fiction/reports/REVISION_2026-07-23_SCENE_PASS_006_010.md` |
| 출처·원본 가용성·Google Docs 상태 | `fiction/SOURCE_MANIFEST.md` |
| 인수인계 | `fiction/HANDOFF.md` |
| 과거 자료 | `fiction/archive/` — 기본 입력 금지 |
| Skill 선택 | `[소설]/00_운영체계/SKILL_REGISTRY.json` |

## 파생 분석본 규칙

수동 장면 카드는 완료 묶음의 현재 해석과 경계 상태를 책임진다. 역개요·진단 보고서는 원고와 색인을 탐색하는 파생 분석본이다. 모든 분석본은 원고·Canon보다 우선하지 않으며 원고 변경 시 같은 PR에서 갱신한다.

Revision Report는 특정 변경의 근거·범위·회귀 결과를 책임지며 현재 다음 작업을 지시하지 않는다. 현재 작업은 항상 `ACTIVE_CONTEXT.md`를 따른다.

## 단일 책임 원본

같은 질문은 한 활성 파일만 책임진다. 과거 초안은 Git 이력 또는 archive에만 둔다. `latest`, `final`, `v2` 활성 복제본을 만들지 않는다. 구형 문서나 이름을 바꾸면 `fiction-canon-and-research: reference-freshness`와 `fiction-revision-and-validation: regression-check`를 실행한다.

## 자동 검증

- `python tools/check_fiction_operating_system.py`
- `python tools/check_fiction_content.py`
- `python tools/build_fiction_reverse_outline.py --check`
- `python tools/check_fiction_reverse_outline.py`
- `python tools/check_fiction_scene_passes.py`
"""
write_text(ROOT / "[소설]" / "00_운영체계" / "DOCUMENTATION_MAP.md", documentation_map)

update_existing(
    FICTION / "FICTION_MASTER.md",
    [
        (
            "RESPONSIBILITY_ROW",
            "| 대표 품질 게이트·파일럿 판정 | `analysis/REPRESENTATIVE_CHAPTER_GATES.md`, `reports/REVISION_2026-07-23_PILOT_10_95_180.md` |",
            "| 대표 품질 게이트·파일럿·완료 묶음 패스 | `analysis/REPRESENTATIVE_CHAPTER_GATES.md`, `analysis/SCENE_PASS_REGISTRY.json`, `reports/REVISION_2026-07-23_PILOT_10_95_180.md`, `reports/REVISION_2026-07-23_SCENE_PASS_006_010.md` |",
        ),
        (
            "NEXT_STAGE",
            "Structural reverse outline 기준선과 제10·95·180화 파일럿 Scene diagnostic은 완료됐다. 다음 단계는 파일럿이 포함된 5화 묶음 `006-010 → 091-095 → 176-180`의 수동 장면 카드·연속성 패스다.",
            "Structural reverse outline 기준선, 제10·95·180화 파일럿, `006-010` 묶음 수동 장면 카드·연속성 패스가 완료됐다. 다음 단계는 `091-095 → 176-180` 묶음 패스다.",
        ),
    ],
)

update_existing(
    FICTION / "STYLE_GUIDE.md",
    [
        (
            "BUNDLE_CONTINUITY_RULES",
            "- 새 조직명으로 폐기 세력의 협상·장비 공급·회수 기능을 묶어 복원하지 않는다. 같은 장비라도 출처, 보관, 기술 운용, 증거보전, 의료 결정권을 분리해 표기한다.",
            """- 새 조직명으로 폐기 세력의 협상·장비 공급·회수 기능을 묶어 복원하지 않는다. 같은 장비라도 출처, 보관, 기술 운용, 증거보전, 의료 결정권을 분리해 표기한다.

## 5화 묶음 연속성 규칙

- 앞 화보다 이른 병행 시점으로 돌아가면 첫 문단에 시간 앵커를 둔다.
- POV가 바뀌어도 이미 완료된 승선·이동·교전을 현재 사건처럼 다시 시작하지 않는다.
- 병행 사건은 `같은 시각`만 쓰고 끝내지 말고 서로 다른 위치·목표·확보 정보를 명시한다.
- 묶음 검수는 앞 화와 다음 화를 경계로 포함해 시간·동선·부상·지식·소지품·비밀을 확인한다.
- 문단이나 설명을 늘리기 전에 경계 오류와 중복 이동을 먼저 제거한다.""",
        )
    ],
)

update_existing(
    FICTION / "bible" / "02_CANON_AND_CONTINUITY.md",
    [
        (
            "EARLY_BOUNDARY",
            "- EP2 종료: 주안과 탈론이 함께 파도에 휩쓸리고 이안·엘리스는 해안에서 합류한다.",
            """- EP2 종료: 주안과 탈론이 함께 파도에 휩쓸리고 이안·엘리스는 해안에서 합류한다.
- 제5~11화 시간선: 제5화의 황색 승선·데커 교전과 제6화 식당은 병행한다. 제6화는 복도 첫 총성 이전, 제7~8화는 직접 연속, 제9화는 같은 시각 세실리아 납치, 제10~11화는 직접 연속이다.
- 제10화 종료 상태: 엘리스·주안은 세실리아가 서쪽 복도로 이동했다는 정보만 알며 실제 납치는 모른다. 주안의 뺨 상처·흰 방 잔향·비정상적 힘과 엘리스의 보호 반응이 남는다.""",
        )
    ],
)

update_existing(
    FICTION / "bible" / "03_PART1_STORY_BIBLE.md",
    [
        (
            "EARLY_ARC",
            "이안의 금기 해독, 엘리스의 선택권 결핍, 주안의 명령 저항이 출항부터 설치된다. 세 사람은 분리와 재회를 반복하며 섬·황색·델타그린의 보호 논리를 경험한다. 후반 능력은 초반 징후와 오사용 비용을 회수해야 한다.",
            """이안의 금기 해독, 엘리스의 선택권 결핍, 주안의 명령 저항이 출항부터 설치된다. 세 사람은 분리와 재회를 반복하며 섬·황색·델타그린의 보호 논리를 경험한다. 후반 능력은 초반 징후와 오사용 비용을 회수해야 한다.

## 초반 제5화~제11화 고정

- 제5화 황색 승선과 제6화 저녁 식당은 병행 시간선이다. 제6화 첫 문단에서 총성 이전임을 표시한다.
- 제7화 노란 코트의 축배와 제8화 식당 학살은 직접 이어진다.
- 제9화는 같은 시각 식당 반대편에서 세실리아가 생존 상태로 납치되는 병행 POV다. 아킴의 승선은 제5화에서 이미 완료됐다.
- 제10화는 브루고 추적·노란 코트 정신 공격·같은 자아의 보호 반응·선체 붕괴 순서를 유지한다.
- 제11화 초반에는 주안의 떨림·뼈 감촉·흰 방 잔향과 엘리스 보호 반응이 남아 있다.
- 히템은 선박에서 육체가 있는 상태로 등장한다.""",
        )
    ],
)

update_existing(
    FICTION / "SOURCE_MANIFEST.md",
    [
        (
            "SOURCE_AUDIT",
            """2026-07-23에 Google Drive와 대화·파일 라이브러리를 다시 검색했다. 과거 인수인계가 열거한 원본 1부·외전1·2부 PDF/텍스트와 원본 재감사 보고서의 **실제 본체는 확인되지 않았다**. 현재 확인 가능한 것은 파일명·존재 기록·일부 사건 교정 요약뿐이다.""",
            """2026-07-23에 Google Drive와 대화·파일 라이브러리를 다시 검색했다. 과거 인수인계가 열거한 원본 1부·외전1·2부 PDF/텍스트와 원본 재감사 보고서의 **실제 본체는 확인되지 않았다**. 사용자가 원본 폴더 `https://drive.google.com/drive/folders/1EPA-bg8ExjvK-XPadKqdab2cCSNMWVt0`를 제공했으나 현재 연결 계정에서는 자식 파일 0개, 메타데이터 404로 반환됐다. 현재 확인 가능한 것은 파일명·존재 기록·일부 사건 교정 요약뿐이다.""",
        ),
        (
            "UNVERIFIED_SCOPE",
            "- 제10화·제95화·제180화의 원문 대사·세부 동선 보존",
            "- 제6화~제10화, 제95화, 제180화의 원문 대사·세부 동선 보존",
        ),
    ],
)

update_existing(
    FICTION / "analysis" / "REPRESENTATIVE_CHAPTER_GATES.md",
    [
        (
            "STATUS",
            "상태: **ACTIVE REVIEW / PILOT 3 COMPLETE**",
            "상태: **ACTIVE REVIEW / PILOT 3 COMPLETE / BUNDLE 006-010 COMPLETE**",
        ),
        (
            "ROW10",
            "| 10 | 거짓 무전과 브루고 · 주안 | 전투 동선·도덕 선택·정신 공격·능력 비용 | PILOT PASS | 같은 자아의 보호 반응·후유증 연결·사건 순서 보존 |",
            "| 10 | 거짓 무전과 브루고 · 주안 | 전투 동선·도덕 선택·정신 공격·능력 비용 | BUNDLE PASS | 같은 자아의 보호 반응·후유증·제5~11화 경계 연속성 보존 |",
        ),
        (
            "HEADING10",
            "### 제10화 · 거짓 무전과 브루고 — PILOT PASS",
            "### 제10화 · 거짓 무전과 브루고 — BUNDLE PASS",
        ),
        (
            "TRANSITION10",
            "- **전이 규칙:** 다중 전환 화에서는 새 설명 장면을 추가하기보다 전환 직전 감각·부상 한 줄로 이전 비용을 남긴다.",
            """- **전이 규칙:** 다중 전환 화에서는 새 설명 장면을 추가하기보다 전환 직전 감각·부상 한 줄로 이전 비용을 남긴다.
- **묶음 회귀:** 제5화 총격 이전을 표시한 제6화 → 제7·8화 직접 연속 → 제9화 병행 납치 → 제10·11화 직접 연속이 확인됐다.""",
        ),
    ],
)

update_existing(
    FICTION / "analysis" / "REVERSE_OUTLINE_REPORT.md",
    [
        (
            "SCOPE",
            "이 보고서는 현행 `fiction/manuscript/`와 같은 커밋의 `fiction/MANUSCRIPT_INDEX.json`을 사용해 제1화~제225화의 구조를 감사한 결과다. 제10·95·180화 파일럿과 2부 정본 전파 교정 뒤 변경된 26개 화의 분량·SHA를 갱신하고 기준선을 재생성했다.",
            "이 보고서는 현행 `fiction/manuscript/`와 같은 커밋의 `fiction/MANUSCRIPT_INDEX.json`을 사용해 제1화~제225화의 구조를 감사한 결과다. 제10·95·180화 파일럿, 2부 정본 전파 교정, `006-010` 묶음 장면 카드·연속성 패스 뒤 변경 화의 분량·SHA를 갱신하고 기준선을 재생성했다.",
        ),
        (
            "VALIDATION_RESULT",
            "- 파일럿·정본 전파로 원고 **26화 / 14개 묶음** 갱신",
            "- 파일럿·정본 전파 뒤 `006-010` 묶음에서 제6·7·9화 추가 갱신 및 수동 장면 카드 5화 확정",
        ),
        (
            "NEW_FINDINGS",
            "### SHOULD_FIX-01 — 외전1의 장문단 밀집",
            """### MUST_FIX-02 — 제5→6화 시간 되감기 무표지 — RESOLVED

- **위치:** 제5화 종료와 제6화 첫 문단
- **증거:** 제5화는 총성과 폭발·비상등까지 진행하지만 제6화는 더 이른 평온한 저녁으로 돌아가면서 시간 표지가 없었다.
- **영향:** 독자가 침투·식당·소환 순서를 역전해서 이해할 수 있었다.
- **수정:** 제6화 첫 문장에 복도 첫 총성 이전이라는 시간 앵커를 추가했다.

### MUST_FIX-03 — 제9화 아킴 중복 승선 — RESOLVED

- **위치:** 제9화 첫 두 문단
- **증거:** 아킴은 제5화에서 이미 갈고리로 승선하고 데커와 교전했지만 제9화에서 다시 지원선에서 넘어오는 것으로 서술됐다.
- **영향:** 인물 위치·시간·교전 순서가 초기화됐다.
- **수정:** 제9화를 같은 시각 식당 쪽 복도로 진입하는 장면으로 연결하고 제5화 데커 교전을 이월했다.

### SHOULD_FIX-06 — 제7화 보호 반응의 별개 자아 오독 — RESOLVED

- **위치:** 제7화 위험 감지 문단
- **증거:** `다른 자신` 표현이 현행 Canon의 같은 자아 보호 반응과 충돌할 여지가 있었다.
- **수정:** 자기 안의 차가운 보호 반응으로 명료화하고 내부 명령형 목소리는 유지했다.

### SHOULD_FIX-01 — 외전1의 장문단 밀집""",
        ),
        (
            "SECTION8",
            "## 8. 파일럿 수행 결과",
            "## 8. 파일럿·`006-010` 묶음 수행 결과",
        ),
        (
            "RESULTS",
            "- **전파 교정:** 파일럿 중 발견한 2부 비정본 세력 기능을 제177화~제225화의 모든 소비자에서 갱신했다.",
            """- **전파 교정:** 파일럿 중 발견한 2부 비정본 세력 기능을 제177화~제225화의 모든 소비자에서 갱신했다.
- **`006-010` 묶음:** 제5→6화 시간 앵커, 제9화 중복 승선, 제7화 동일 자아 표현을 교정하고 5화 수동 장면 카드와 제5·11화 경계 상태를 확정했다.""",
        ),
        (
            "NEXT",
            """1. 파일럿이 포함된 `006-010`, `091-095`, `176-180` 묶음의 나머지 화까지 수동 장면 카드를 확정한다.
2. 각 묶음에서 사건·인과·POV·동선·부상·지식 상태를 검수한다.
3. 파일럿 규칙은 동일 결함이 확인된 화에만 적용하고 문단 수·대사 비중을 기계적으로 맞추지 않는다.
4. 원고 수정 시 `MANUSCRIPT_INDEX.json`, 역개요, Revision Report를 같은 커밋에서 갱신한다.""",
            """1. `091-095`, `176-180` 묶음의 나머지 화까지 수동 장면 카드를 확정한다.
2. 각 묶음에서 앞뒤 경계를 포함해 사건·인과·POV·동선·부상·지식·소지품 상태를 검수한다.
3. 파일럿·완료 묶음 규칙은 동일 결함이 확인된 화에만 적용하고 문단 수·대사 비중을 기계적으로 맞추지 않는다.
4. 원고 수정 시 `MANUSCRIPT_INDEX.json`, 역개요, Scene Pass Registry, Revision Report를 같은 커밋에서 갱신한다.""",
        ),
    ],
)

learning_log = (ROOT / "skills" / "FICTION_SKILL_LEARNING_LOG.md").read_text(encoding="utf-8").rstrip()
learning_append = """

## 2026-07-23 — 첫 5화 묶음 장면 카드와 병행 시간선

- 사용: `REVIEW → BUILD → REVIEW` / `fiction-revision-and-validation: scene-diagnostic, continuity-check, adversarial-loop, regression-check, pr-review` / `fiction-story-development: scene-card, plot-and-causality, stress-test` / `fiction-canon-and-research: timeline-and-state, continuity-map, source-log, reference-freshness`.
- 상황: 제10화 파일럿을 포함한 `006-010` 묶음과 제5·11화 경계를 수동 검수했다.
- 발견한 실패: POV 전환 자체는 명확했지만 제5→6화가 과거로 돌아가는 시간 표지가 없었고, 제9화는 제5화에서 완료된 아킴의 승선을 다시 시작했다. 제7화에는 같은 자아 보호 반응을 별개 자아처럼 읽을 표현이 남아 있었다.
- 실제 변경: 제6화 시간 앵커, 제9화 식당 복도 병행 진입, 제7화 동일 자아 표현을 최소 교정하고 5화 장면 카드·경계 상태·Scene Pass Registry를 추가했다.
- 검증·증거: 원고 변경은 제6·7·9화로 제한, 제8·10화와 나머지 220화 SHA 보존, 색인·225화 역개요 재생성.
- 재사용 가능한 교훈 1: 5화 묶음 검수는 묶음 내부만 읽지 않고 직전·직후 화를 포함해야 시간 되감기와 부상·지식 이월 오류를 잡을 수 있다.
- 재사용 가능한 교훈 2: 다중 POV 장편에서는 동일 사건을 다시 보여주는 것과 이미 완료된 이동을 새 사건처럼 반복하는 것을 구분한다.
- 재사용 가능한 교훈 3: 사용자가 원본 폴더를 제공해도 연결 계정에서 본체를 읽지 못하면 `PRIMARY`로 승격하지 않고 접근 상태와 재감사 순서만 기록한다.
- 다음 재검토 조건: 원본 Drive 폴더 접근 가능 시 `006-010` 우선 재감사, 이후 `091-095 → 176-180` 진행.
"""
write_text(ROOT / "skills" / "FICTION_SKILL_LEARNING_LOG.md", learning_log + learning_append)

checker = r"""#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FICTION = ROOT / "fiction"
CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)
errors: list[str] = []

index = json.loads((FICTION / "MANUSCRIPT_INDEX.json").read_text(encoding="utf-8"))
index_entries = {int(item["chapter"]): item for item in index["chapters"]}
registry = json.loads((FICTION / "analysis" / "SCENE_PASS_REGISTRY.json").read_text(encoding="utf-8"))

parsed: dict[int, str] = {}
for path in sorted((FICTION / "manuscript").rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    for match in CHAPTER_RE.finditer(text):
        parsed[int(match.group(1))] = match.group(4).strip()

passes = registry.get("completed_bundle_passes", [])
if len(passes) != 1:
    errors.append(f"expected one completed bundle pass, got {len(passes)}")
else:
    item = passes[0]
    if item.get("bundle") != "fiction/manuscript/part-1/006-010.md":
        errors.append("unexpected completed bundle")
    if item.get("chapters") != [6, 7, 8, 9, 10]:
        errors.append("006-010 chapter list mismatch")
    if item.get("boundary_chapters") != [5, 11]:
        errors.append("006-010 boundary list mismatch")
    for key in ("scene_cards", "revision_report"):
        rel = item.get(key)
        if not rel or not (ROOT / rel).is_file():
            errors.append(f"missing scene pass artifact: {rel}")
    for raw_number, expected_sha in item.get("chapter_shas", {}).items():
        number = int(raw_number)
        body = parsed.get(number, "")
        actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if actual != expected_sha:
            errors.append(f"scene pass chapter {number} registry SHA mismatch")
        if index_entries.get(number, {}).get("body_sha256") != actual:
            errors.append(f"scene pass chapter {number} index SHA mismatch")

required = {
    6: "복도에서 첫 총성이 울리기 전",
    7: "자기 안의 차가운 보호 반응",
    9: "조금 전 서비스 통로에서 데커와 총을 주고받는 동안",
}
for number, phrase in required.items():
    if phrase not in parsed.get(number, ""):
        errors.append(f"chapter {number} missing scene-pass invariant: {phrase}")

forbidden = {
    7: "다른 자신이 문을 세게 두드렸다",
    9: "지원선에서 갈고리를 타고 넘어오는 동안",
}
for number, phrase in forbidden.items():
    if phrase in parsed.get(number, ""):
        errors.append(f"chapter {number} stale continuity text remains: {phrase}")

expected_next = [
    "fiction/manuscript/side-story-lake/091-095.md",
    "fiction/manuscript/part-2/176-180.md",
]
if registry.get("next_bundle_passes") != expected_next:
    errors.append("next bundle pass order mismatch")

cards = (FICTION / "analysis" / "SCENE_CARDS_006_010.md").read_text(encoding="utf-8")
for number in range(6, 11):
    if f"## 제{number}화" not in cards:
        errors.append(f"scene card missing chapter {number}")
for boundary in ("제5→6화", "제6→7화", "제7→8화", "제8→9화", "제9→10화", "제10→11화"):
    if boundary not in cards:
        errors.append(f"scene card missing boundary {boundary}")

if errors:
    print("Fiction scene-pass validation FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("Fiction scene-pass validation PASSED (bundle 006-010)")
"""
write_text(ROOT / "tools" / "check_fiction_scene_passes.py", checker)

update_existing(
    ROOT / ".github" / "workflows" / "fiction-ops-validation.yml",
    [
        (
            "WATCH_CHECKER",
            '      - "tools/check_fiction_reverse_outline.py"\n      - ".github/workflows/fiction-ops-validation.yml"',
            '      - "tools/check_fiction_reverse_outline.py"\n      - "tools/check_fiction_scene_passes.py"\n      - ".github/workflows/fiction-ops-validation.yml"',
        ),
        (
            "PUSH_WATCH_CHECKER",
            '      - "tools/check_fiction_reverse_outline.py"\n\npermissions:',
            '      - "tools/check_fiction_reverse_outline.py"\n      - "tools/check_fiction_scene_passes.py"\n\npermissions:',
        ),
        (
            "RUN_CHECKER",
            """      - name: Validate reverse-outline analysis
        run: python tools/check_fiction_reverse_outline.py""",
            """      - name: Validate reverse-outline analysis
        run: python tools/check_fiction_reverse_outline.py
      - name: Validate completed scene passes
        run: python tools/check_fiction_scene_passes.py""",
        ),
    ],
)

subprocess.run([sys.executable, "tools/check_fiction_operating_system.py"], cwd=ROOT, check=True)
subprocess.run([sys.executable, "tools/check_fiction_content.py"], cwd=ROOT, check=True)
subprocess.run([sys.executable, "tools/build_fiction_reverse_outline.py", "--check"], cwd=ROOT, check=True)
subprocess.run([sys.executable, "tools/check_fiction_reverse_outline.py"], cwd=ROOT, check=True)
subprocess.run([sys.executable, "tools/check_fiction_scene_passes.py"], cwd=ROOT, check=True)

print("scene pass 006-010 applied and validated")
