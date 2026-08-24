#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOCKS = {
    ROOT / "fiction/ACTIVE_CONTEXT.md": "\n".join([
        "- Ch41 `잘 돌아왔다`: Part 1 결전 이후 가족 재회와 살아 돌아온 관계의 비정상성을 Bridge의 출발점으로 정리한다.",
        "- Ch42 `살아 돌아온 몸`: 주안의 변화한 몸을 보상이 아니라 선택을 침식할 수 있는 후유 상태로 검증한다.",
        "- Ch43 `확인하고 설명하겠습니다`: 주안은 자기 감정의 기원을 확인하지만 엘리스의 현재 선택을 대신 판정하지 않는다.",
        "- Ch44 `응답하지 않은 호출기`: 미응답을 영구 이별로 확정하지 않고 관계의 불확실성과 수신기 보존을 함께 남긴다.",
        "- Ch45 `노란 옷은 안 입습니다`: 황색과 거리를 둔 주안의 현재 선택을 고정하고 다음 8년 Bridge 생활·훈련 축으로 넘긴다.",
    ]),
    ROOT / "fiction/FICTION_MASTER.md": "\n".join([
        "- 041 `잘 돌아왔다`: 가족 재회와 살아 돌아온 관계를 Aftermath & 8-year Bridge의 출발점으로 재정렬한다.",
        "- 042 `살아 돌아온 몸`: 주안의 변화한 몸을 보상으로 단순화하지 않고 선택 침식 가능성이 있는 후유 상태로 검증한다.",
        "- 043 `확인하고 설명하겠습니다`: 주안은 자기 감정의 기원을 검증하되 엘리스의 현재 선택을 대신 판정하지 않는다.",
        "- 044 `응답하지 않은 호출기`: 미응답을 영구 이별로 확정하지 않고 수신기를 보존한다.",
        "- 045 `노란 옷은 안 입습니다`: 황색과 거리를 둔 주안의 현재 선택을 고정하고 다음 Bridge 생활·훈련 축으로 넘긴다.",
    ]),
}

for path, block in BLOCKS.items():
    text = path.read_text(encoding="utf-8")
    doubled = block + "\n" + block
    while doubled in text:
        text = text.replace(doubled, block, 1)
    path.write_text(text, encoding="utf-8")

print("normalized PR57 receipt bridge readback blocks")
