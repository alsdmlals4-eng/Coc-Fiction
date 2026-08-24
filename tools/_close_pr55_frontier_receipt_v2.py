#!/usr/bin/env python3
from pathlib import Path

import _close_pr55_frontier_receipt as closure

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "fiction/HANDOFF.md"


def main() -> None:
    text = HANDOFF.read_text(encoding="utf-8")
    old = "`frontier_observed_at_main: null`은 PR #55가 아직 pending candidate임을 뜻한다. 마지막 실제 main frontier 변경은 PR #50의 `001–035`이며, PR #55 병합 전 `001–040`을 main production으로 부르지 않는다."
    new = f"`frontier_observed_at_main`은 PR #55가 production frontier를 `001–040`으로 이동시킨 실제 merge `{closure.MERGE_SHA}`를 기록한다. 저장소 최신 SHA 포인터로 재사용하지 않고 재개 시 최신 main을 다시 조회한다."
    if old in text:
        HANDOFF.write_text(text.replace(old, new, 1), encoding="utf-8")
    closure.main()


if __name__ == "__main__":
    main()
