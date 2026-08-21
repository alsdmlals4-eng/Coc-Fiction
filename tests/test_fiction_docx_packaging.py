import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/check_fiction_docx_packaging.py"


def make_docx_like(path: Path, header_text: str) -> None:
    document_xml = """<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<w:document xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
 xmlns:r='http://schemas.openxmlformats.org/officeDocument/2006/relationships'>
  <w:body><w:p><w:r><w:t>제1화. 테스트</w:t></w:r></w:p>
    <w:sectPr><w:headerReference w:type='default' r:id='rIdHeader1'/></w:sectPr>
  </w:body>
</w:document>"""
    rels_xml = """<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<Relationships xmlns='http://schemas.openxmlformats.org/package/2006/relationships'>
  <Relationship Id='rIdHeader1'
    Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/header'
    Target='header1.xml'/>
</Relationships>"""
    header_xml = f"""<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<w:hdr xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'>
  <w:p><w:r><w:t>{header_text}</w:t></w:r></w:p>
</w:hdr>"""
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("word/document.xml", document_xml)
        zf.writestr("word/_rels/document.xml.rels", rels_xml)
        zf.writestr("word/header1.xml", header_xml)


class FictionDocxPackagingTests(unittest.TestCase):
    def run_checker(self, docx: Path) -> subprocess.CompletedProcess[str]:
        self.assertTrue(SCRIPT.exists(), "semantic DOCX packaging checker must exist")
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(docx),
                "--declared-start",
                "1",
                "--declared-end",
                "161",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_rejects_narrow_running_header_for_full_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.docx"
            make_docx_like(path, "폭풍의 눈 · 제001–010화")
            result = self.run_checker(path)
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("HEADER_RANGE_MISMATCH", result.stdout + result.stderr)

    def test_accepts_neutral_full_range_header(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "good.docx"
            make_docx_like(path, "폭풍의 눈 · 001–161 통합 검수본")
            result = self.run_checker(path)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("DOCX packaging PASSED", result.stdout)


if __name__ == "__main__":
    unittest.main()
