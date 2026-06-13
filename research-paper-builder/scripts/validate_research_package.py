from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


CJK_RE = re.compile(r"[\u4e00-\u9fff]")
CITATION_RE = re.compile(r"\[([0-9][0-9,\-; ]*)\]")


def read_docx_paragraphs(path: Path) -> tuple[list[str], str]:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paragraphs: list[str] = []
    for p in root.findall(".//w:p", ns):
        texts = [t.text or "" for t in p.findall(".//w:t", ns)]
        if texts:
            paragraphs.append("".join(texts))
        else:
            paragraphs.append("")
    return paragraphs, xml


def expand_citation_group(group: str) -> set[int]:
    values: set[int] = set()
    for part in re.split(r"[,;]", group):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            bits = [b.strip() for b in part.split("-", 1)]
            if len(bits) == 2 and bits[0].isdigit() and bits[1].isdigit():
                start, end = int(bits[0]), int(bits[1])
                if start <= end and end - start <= 500:
                    values.update(range(start, end + 1))
            continue
        if part.isdigit():
            values.add(int(part))
    return values


def citation_numbers(paragraphs: list[str]) -> list[int]:
    refs_idx = find_heading(paragraphs, "references")
    body = "\n".join(paragraphs[:refs_idx] if refs_idx is not None else paragraphs)
    numbers: set[int] = set()
    for group in CITATION_RE.findall(body):
        numbers.update(expand_citation_group(group))
    return sorted(numbers)


def find_heading(paragraphs: list[str], heading: str) -> int | None:
    target = heading.strip().lower()
    for i, para in enumerate(paragraphs):
        if para.strip().lower() == target:
            return i
    return None


def reference_numbers(paragraphs: list[str]) -> list[int]:
    refs_idx = find_heading(paragraphs, "references")
    if refs_idx is None:
        return []
    numbers: list[int] = []
    for para in paragraphs[refs_idx + 1 :]:
        match = re.match(r"^\s*\[?(\d{1,3})\]?[\.\s]", para)
        if match:
            numbers.append(int(match.group(1)))
    return numbers


def scan_text_files(root: Path, forbidden: list[str], scan_cjk: bool = False) -> list[dict[str, str | int]]:
    hits: list[dict[str, str | int]] = []
    if not root.exists():
        return hits
    suffixes = {".md", ".txt", ".csv", ".tsv", ".py", ".r", ".json", ".yaml", ".yml"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()
        for term in forbidden:
            needle = term.lower().strip()
            if needle and needle in lower:
                hits.append({"file": str(path), "term": term})
        if scan_cjk and CJK_RE.search(text):
            hits.append({"file": str(path), "term": "CJK"})
    return hits


def count_files(path: Path, pattern: str) -> int:
    if not path.exists():
        return 0
    return sum(1 for p in path.glob(pattern) if p.is_file())


def image_summary(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    try:
        from PIL import Image
    except Exception:
        Image = None
    rows: list[dict[str, object]] = []
    for p in sorted(path.glob("*")):
        if not p.is_file() or p.suffix.lower() not in {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".pdf"}:
            continue
        row: dict[str, object] = {"name": p.name, "bytes": p.stat().st_size}
        if Image is not None and p.suffix.lower() != ".pdf":
            try:
                with Image.open(p) as im:
                    row["size"] = list(im.size)
            except Exception:
                pass
        rows.append(row)
    return rows


def workbook_summary(path: Path) -> list[str]:
    if not path.exists():
        return []
    return sorted(p.name for p in path.rglob("*") if p.is_file() and p.suffix.lower() in {".xlsx", ".xls", ".xlsm"})


def zip_summary(path: Path | None) -> dict[str, object] | None:
    if path is None or not path.exists():
        return None
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
    return {
        "entries": len(names),
        "main_figures": sum("/figures/main/" in n.replace("\\", "/") and not n.endswith("/") for n in names),
    }


def validate(args: argparse.Namespace) -> dict[str, object]:
    result: dict[str, object] = {}
    package = Path(args.package) if args.package else None
    docx = Path(args.docx) if args.docx else None
    forbidden = [x.strip() for x in (args.forbidden or "").split(",") if x.strip()]

    if docx and docx.exists():
        paragraphs, xml = read_docx_paragraphs(docx)
        cited = citation_numbers(paragraphs)
        refs = reference_numbers(paragraphs)
        ref_set = set(refs)
        result["docx"] = str(docx)
        result["paragraphs"] = len(paragraphs)
        result["docx_has_cjk"] = any(CJK_RE.search(p) for p in paragraphs)
        result["docx_xml_has_cjk"] = bool(CJK_RE.search(xml))
        result["citation_numbers"] = cited
        result["reference_numbers"] = refs
        result["citation_reference_exact_match"] = bool(refs) and set(cited) == ref_set
        result["uncited_references"] = sorted(ref_set - set(cited))
        result["out_of_range_citations"] = sorted(n for n in cited if ref_set and n not in ref_set)
        if forbidden:
            text = "\n".join(paragraphs).lower()
            result["docx_forbidden_hits"] = [term for term in forbidden if term.lower() in text]

    if package and package.exists():
        result["package"] = str(package)
        result["main_figures"] = image_summary(package / "figures" / "main")
        result["source_panel_count"] = count_files(package / "figures" / "source_panels", "*")
        result["qc_figure_count"] = count_files(package / "figures" / "qc", "*")
        result["workbooks"] = workbook_summary(package / "tables")
        result["source_data"] = workbook_summary(package / "source_data")
        result["text_file_hits"] = scan_text_files(package, forbidden, args.scan_cjk_text_files)

    result["zip"] = zip_summary(Path(args.zip)) if args.zip else None
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a research manuscript package.")
    parser.add_argument("--package", help="Submission package directory")
    parser.add_argument("--docx", help="Main manuscript DOCX")
    parser.add_argument("--zip", help="Submission package ZIP")
    parser.add_argument("--forbidden", help="Comma-separated terms that should not appear")
    parser.add_argument("--scan-cjk-text-files", action="store_true", help="Also scan package text files for CJK characters")
    args = parser.parse_args()
    print(json.dumps(validate(args), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
