#!/usr/bin/env python3
from __future__ import annotations

import argparse
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
HEADER_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header"
RANGE_RE = re.compile(r"제?\s*0*(\d{1,4})\s*[–—~-]\s*0*(\d{1,4})\s*화")


def _text_from_xml(data: bytes) -> str:
    root = ET.fromstring(data)
    return "".join(node.text or "" for node in root.iter(f"{{{W_NS}}}t"))


def _header_targets(zf: zipfile.ZipFile) -> tuple[list[str], dict[str, str]]:
    document = ET.fromstring(zf.read("word/document.xml"))
    rels = ET.fromstring(zf.read("word/_rels/document.xml.rels"))

    rel_by_id: dict[str, str] = {}
    for rel in rels.findall(f"{{{PKG_REL_NS}}}Relationship"):
        if rel.attrib.get("Type") != HEADER_REL_TYPE:
            continue
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rel_id and target:
            rel_by_id[rel_id] = posixpath.normpath(posixpath.join("word", target))

    referenced_ids: list[str] = []
    for ref in document.iter(f"{{{W_NS}}}headerReference"):
        rel_id = ref.attrib.get(f"{{{R_NS}}}id")
        if rel_id and rel_id not in referenced_ids:
            referenced_ids.append(rel_id)

    targets = [rel_by_id[rel_id] for rel_id in referenced_ids if rel_id in rel_by_id]
    return targets, rel_by_id


def inspect_docx_headers(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as zf:
        targets, _ = _header_targets(zf)
        headers: list[str] = []
        for target in targets:
            if target not in zf.namelist():
                raise ValueError(f"referenced header is missing: {target}")
            headers.append(_text_from_xml(zf.read(target)).strip())
        return headers


def validate_docx_packaging(path: Path, declared_start: int, declared_end: int) -> list[str]:
    errors: list[str] = []
    try:
        headers = inspect_docx_headers(path)
    except (OSError, KeyError, ET.ParseError, zipfile.BadZipFile, ValueError) as exc:
        return [f"DOCX_PACKAGE_INVALID: {exc}"]

    explicit_ranges: list[tuple[str, int, int]] = []
    for header in headers:
        for match in RANGE_RE.finditer(header):
            explicit_ranges.append((header, int(match.group(1)), int(match.group(2))))

    # A single running header is global for this packaging contract. If it
    # claims a chapter range, that range must describe the declared artifact.
    if len(headers) <= 1:
        for header, start, end in explicit_ranges:
            if (start, end) != (declared_start, declared_end):
                errors.append(
                    "HEADER_RANGE_MISMATCH: "
                    f"header={header!r} claims {start}-{end}, "
                    f"artifact declares {declared_start}-{declared_end}"
                )
    else:
        # Multi-section documents may intentionally use per-section ranges.
        # They still may not claim chapters outside the declared artifact.
        for header, start, end in explicit_ranges:
            if start < declared_start or end > declared_end or start > end:
                errors.append(
                    "HEADER_RANGE_MISMATCH: "
                    f"header={header!r} is outside declared {declared_start}-{declared_end}"
                )

    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate semantic DOCX running-header ranges.")
    parser.add_argument("docx", type=Path)
    parser.add_argument("--declared-start", type=int, required=True)
    parser.add_argument("--declared-end", type=int, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_docx_packaging(args.docx, args.declared_start, args.declared_end)
    if errors:
        print("DOCX packaging FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    headers = inspect_docx_headers(args.docx)
    print(f"DOCX packaging PASSED ({len(headers)} referenced running headers)")
    for header in headers:
        print(f"- {header}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
