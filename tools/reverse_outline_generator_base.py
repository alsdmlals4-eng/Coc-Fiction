#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

CHAPTER_RE = re.compile(
    r"^## 제(\d+)화 · (.*?)\n\n\*\*POV:\*\* ([^\n]+)\n\n(.*?)(?=\n\n<!-- source-lines:)",
    re.M | re.S,
)
SENTENCE_RE = re.compile(r"(?<=[.!?。！？…])\s+|\n+")
DIALOGUE_RE = re.compile(r'[“\"](.*?)[”\"]', re.S)

GOAL_TERMS = (
    "가야", "찾", "확인", "구하", "막", "지키", "살리", "탈출", "도착", "조사",
    "알아", "숨", "기다", "만나", "전달", "회수", "열", "들어가", "나가", "돌아가",
    "증명", "설득", "협상", "치료", "수술", "기록", "보고", "추적", "버티",
)
OPPOSITION_TERMS = (
    "하지만", "그러나", "문제", "위험", "죽", "피", "상처", "실패", "거부", "불가능",
    "않았", "없었", "막혔", "공격", "총", "칼", "괴물", "적", "대가", "두려", "명령",
    "납치", "무너", "닫", "갇", "잃", "사라", "오염", "독", "불", "폭풍",
)
TURN_TERMS = (
    "그때", "그러나", "하지만", "드러났다", "발견했다", "깨달았다", "사실은", "정체가",
    "바뀌었다", "나타났다", "열렸다", "무너졌다", "돌아왔다", "마침내", "갑자기", "오히려", "대신",
)
DECISION_TERMS = (
    "결정", "선택", "하기로", "거부", "받아들", "놓았", "놓지", "쐈", "들었다", "남았다",
    "떠났다", "말했다", "대답했다", "약속", "계약", "포기", "살리", "죽이", "돌아가", "멈추",
    "건넸", "내밀", "열었다", "닫았다", "지켰", "버렸",
)
THEME_TERMS = ("선택", "책임", "보호", "명령", "권리", "자유", "안전", "미래", "사람", "괴물")
FUNCTION_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("OPENING", ("출항", "첫", "아침", "휴일", "승선")),
    ("INCITING_INCIDENT", ("비명", "학살", "납치", "갈라진", "사라진", "죽었던", "공격")),
    ("INVESTIGATION", ("조사", "기록", "지도", "규칙", "보고서", "보관", "심의", "행방", "정체")),
    ("REVELATION", ("점토판", "폭로", "진실", "거짓말", "두 얼굴", "기억", "미래", "잔편", "서")),
    ("RELATIONSHIP", ("아버지", "어머니", "동료", "친구", "선배", "후배", "두 사람", "세 사람", "호출기")),
    ("NEGOTIATION", ("협상", "조건", "계약", "거래", "관할권", "회의", "조항", "허가")),
    ("ACTION", ("전투", "도주", "탈출", "작전", "순찰", "결투", "수술", "전쟁", "무너지는")),
    ("CHOICE_AND_COST", ("선택", "거부", "대가", "남는", "남긴", "보호", "지키는", "기다리지")),
    ("AFTERMATH", ("뒤의", "끝난 뒤", "장례식", "식사", "진단서", "회복", "아침")),
    ("FINALE", ("끝", "마지막", "응답하지", "레드퀸", "미래를 기록하는 사람", "네가 없는 마을")),
)
SECTION_RANGES = (
    (1, 70, "part-1", "1부 《폭풍의 눈》"),
    (71, 95, "side-story-lake", "외전1 《호수가 보이는 마을》"),
    (96, 130, "side-story-alice", "외전2 《붉은 여왕의 첫 임무》"),
    (131, 165, "side-story-ian", "외전3 《미래를 기록하는 사람》"),
    (166, 225, "part-2", "2부 《네가 없는 마을》"),
)
REPRESENTATIVE_GATES = {1, 3, 10, 20, 70, 95, 130, 165, 166, 180, 200, 225}


def clean(text: str, limit: int = 260) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def sentences(body: str) -> list[str]:
    result: list[str] = []
    for chunk in SENTENCE_RE.split(body):
        chunk = clean(chunk, 500)
        if len(chunk) >= 8:
            result.append(chunk)
    return result


def paragraphs(body: str) -> list[str]:
    return [clean(p, 1000) for p in re.split(r"\n\s*\n", body) if p.strip()]


def select_sentence(items: list[str], terms: tuple[str, ...], *, start: int = 0, default_index: int = 0) -> str:
    if not items:
        return "본문 문장 추출 실패"
    for sentence in items[start:]:
        if any(term in sentence for term in terms):
            return clean(sentence)
    return clean(items[min(max(default_index, 0), len(items) - 1)])


def section_for(number: int) -> tuple[str, str]:
    for lo, hi, key, label in SECTION_RANGES:
        if lo <= number <= hi:
            return key, label
    raise ValueError(number)


def function_tags(title: str, body: str, number: int) -> list[str]:
    sample = title + " " + body[:1200]
    tags = [tag for tag, terms in FUNCTION_RULES if any(term in sample for term in terms)]
    if number in {1, 71, 96, 131, 166}:
        tags.append("SECTION_ENTRY")
    if number in {70, 95, 130, 165, 225}:
        tags.append("SECTION_EXIT")
    if not tags:
        tags.append("PROGRESSION")
    return list(dict.fromkeys(tags))


def state_axes(body: str) -> list[str]:
    axes: list[str] = []
    groups = (
        ("EVENT", ("공격", "도착", "떠", "열렸", "무너", "사라", "죽", "살", "전투", "수술", "도주")),
        ("INFORMATION", ("알", "발견", "기록", "정체", "사실", "거짓", "규칙", "보고", "증거")),
        ("RELATIONSHIP", ("아버지", "어머니", "친구", "동료", "선배", "후배", "믿", "약속", "호출")),
        ("AGENCY", ("선택", "결정", "거부", "명령", "권리", "자유", "동의", "계약")),
        ("EMOTION", ("두려", "웃", "울", "분노", "미안", "후회", "안도", "외로", "사랑")),
        ("BODY_OR_RESOURCE", ("상처", "피", "몸", "능력", "총", "창", "장비", "독", "치료", "핵")),
        ("WORLD_RULE", ("괴이", "신", "점토판", "시간", "기억", "미래", "도원향", "쇼거스", "비야키")),
    )
    for name, terms in groups:
        if any(term in body for term in terms):
            axes.append(name)
    return axes or ["EVENT"]


def structural_flags(number: int, body: str, paras: list[str], sents: list[str]) -> list[str]:
    flags: list[str] = []
    avg_para = len(body) / max(len(paras), 1)
    dialogue_chars = sum(len(x) for x in DIALOGUE_RE.findall(body))
    dialogue_ratio = dialogue_chars / max(len(body), 1)
    theme_hits = sum(body.count(term) for term in THEME_TERMS)
    theme_per_1000 = theme_hits * 1000 / max(len(body), 1)
    turn_hits = sum(sum(sentence.count(term) for term in TURN_TERMS) for sentence in sents)
    if avg_para >= 130 or len(paras) <= 12:
        flags.append("DENSE_PARAGRAPHING")
    if dialogue_ratio < 0.055:
        flags.append("LOW_DIALOGUE_SHARE")
    if dialogue_ratio > 0.36:
        flags.append("HIGH_DIALOGUE_SHARE")
    if theme_per_1000 >= 8.0:
        flags.append("HIGH_THEME_EXPLICITNESS")
    if turn_hits >= 6:
        flags.append("MULTI_TURN_DENSITY")
    if len(body) >= 3000:
        flags.append("LONG_CHAPTER")
    if len(body) <= 2100:
        flags.append("NEAR_MINIMUM_LENGTH")
    if re.search(r"\b\d+\s*년 전|여덟 해 전|몇 년 전|과거로|시간은 다시|오래전", body):
        flags.append("TIMELINE_SHIFT")
    if number in {1, 71, 96, 131, 166}:
        flags.append("SECTION_ENTRY")
    if number in {70, 95, 130, 165, 225}:
        flags.append("SECTION_EXIT")
    return flags


def build(repo_root: Path) -> dict[str, Any]:
    fiction = repo_root / "fiction"
    index = json.loads((fiction / "MANUSCRIPT_INDEX.json").read_text(encoding="utf-8"))
    index_entries = {int(item["chapter"]): item for item in index["chapters"]}
    parsed: dict[int, dict[str, Any]] = {}
    for path in sorted((fiction / "manuscript").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in CHAPTER_RE.finditer(text):
            number = int(match.group(1))
            parsed[number] = {
                "title": match.group(2).strip(),
                "pov": match.group(3).strip(),
                "body": match.group(4).strip(),
                "bundle": path.relative_to(repo_root).as_posix(),
            }
    if sorted(parsed) != list(range(1, 226)):
        raise SystemExit(f"chapter set mismatch: {len(parsed)}")
    pov_count = Counter(item["pov"] for item in parsed.values())
    output: list[dict[str, Any]] = []
    previous: dict[str, Any] | None = None
    for number in range(1, 226):
        chapter = parsed[number]
        body = chapter["body"]
        paras = paragraphs(body)
        sents = sentences(body)
        entry = index_entries[number]
        digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
        if (
            entry["title"] != chapter["title"]
            or entry["pov"] != chapter["pov"]
            or entry["body_chars"] != len(body)
            or entry["body_sha256"] != digest
            or entry["bundle"] != chapter["bundle"]
        ):
            raise SystemExit(f"chapter {number} differs from MANUSCRIPT_INDEX.json")
        key, label = section_for(number)
        first = clean(" ".join(sents[:2]) if sents else body[:260])
        last = clean(" ".join(sents[-2:]) if sents else body[-260:])
        goal = select_sentence(sents, GOAL_TERMS, default_index=min(1, len(sents)-1))
        opposition = select_sentence(sents, OPPOSITION_TERMS, start=max(0, len(sents)//6), default_index=max(0, len(sents)//3))
        turn = select_sentence(sents, TURN_TERMS, start=max(0, len(sents)//4), default_index=max(0, len(sents)//2))
        decision = select_sentence(sents, DECISION_TERMS, start=max(0, len(sents)//3), default_index=max(0, (len(sents)*2)//3))
        dialogue_chars = sum(len(x) for x in DIALOGUE_RE.findall(body))
        flags = structural_flags(number, body, paras, sents)
        if pov_count[chapter["pov"]] == 1:
            flags.append("ONE_OFF_POV")
        if previous and previous["pov"] != chapter["pov"]:
            flags.append("POV_HANDOFF")
        next_meta = None
        if number < 225:
            nxt = parsed[number + 1]
            next_meta = {"chapter": number + 1, "title": nxt["title"], "pov": nxt["pov"]}
        theme_hits = {term: body.count(term) for term in THEME_TERMS if body.count(term)}
        item = {
            "chapter": number,
            "section": {"key": key, "label": label},
            "title": chapter["title"],
            "pov": chapter["pov"],
            "source": {
                "bundle": chapter["bundle"],
                "body_sha256": digest,
                "body_chars": len(body),
            },
            "chapter_function": function_tags(chapter["title"], body, number),
            "state_change_axes": state_axes(body),
            "evidence": {
                "starting_state": first,
                "immediate_goal_or_focus": goal,
                "opposition_and_cost": opposition,
                "turn_or_discovery": turn,
                "decision_or_choice": decision,
                "ending_state": last,
                "next_pressure": (
                    f"다음 제{number + 1}화 「{next_meta['title']}」({next_meta['pov']} POV)로 압력이 이월된다. "
                    f"현재 화 마지막 증거: {clean(sents[-1] if sents else last, 180)}"
                    if next_meta
                    else f"작품 종결. 마지막 상태 증거: {clean(sents[-1] if sents else last, 180)}"
                ),
            },
            "metrics": {
                "paragraphs": len(paras),
                "average_paragraph_chars": round(len(body) / max(len(paras), 1), 1),
                "dialogue_ratio": round(dialogue_chars / max(len(body), 1), 4),
                "theme_term_hits": theme_hits,
            },
            "structural_flags": list(dict.fromkeys(flags)),
            "review_status": "AUTO_BASELINE_REVIEW_REQUIRED",
            "representative_gate": number in REPRESENTATIVE_GATES,
            "previous_chapter": (
                {"chapter": number - 1, "title": previous["title"], "pov": previous["pov"]}
                if previous else None
            ),
            "next_chapter": next_meta,
        }
        output.append(item)
        previous = chapter
    return {
        "schema_version": 1,
        "generated_at": "2026-07-23",
        "status": "ACTIVE_ANALYSIS / EXTRACTIVE_BASELINE / MANUAL_REVIEW_REQUIRED",
        "source_of_truth": "fiction/manuscript/ plus fiction/MANUSCRIPT_INDEX.json on the same commit",
        "method": (
            "Deterministic extractive reverse-outline baseline. Evidence fields quote or compress current manuscript sentences; "
            "they are navigation aids, not final interpretive scene cards. Manual representative-gate review and source-log audit remain separate."
        ),
        "protected_content": "No manuscript body or existing body SHA is changed by this artifact.",
        "representative_gate_chapters": sorted(REPRESENTATIVE_GATES),
        "chapters": output,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument("--output", default="fiction/analysis/REVERSE_OUTLINE_001_225.json")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    data = build(root)
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    out = root / args.output
    if args.check:
        if not out.is_file() or out.read_text(encoding="utf-8") != rendered:
            raise SystemExit("reverse outline is stale; run build_fiction_reverse_outline.py")
        print("Reverse outline reproducibility PASSED (225 chapters)")
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(rendered, encoding="utf-8")
    print(f"wrote {out} ({len(data['chapters'])} chapters)")


if __name__ == "__main__":
    main()
