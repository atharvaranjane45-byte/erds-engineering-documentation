#!/usr/bin/env python3
"""Perform basic PDF existence, page-count, and text checks."""
import argparse
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", help="PDF path to validate")
    ap.add_argument("--min-pages", type=int, default=1)
    args = ap.parse_args()
    path = Path(args.pdf)
    if not path.is_file():
        raise SystemExit(f"FAIL: PDF not found: {path}")
    if path.stat().st_size < 1000:
        raise SystemExit(f"FAIL: PDF looks too small ({path.stat().st_size} bytes)")
    try:
        import fitz
    except ImportError:
        print("WARNING: PyMuPDF is not installed; only file existence/size was checked.")
        print(f"PASS (basic): {path.resolve()} ({path.stat().st_size} bytes)")
        return
    try:
        doc = fitz.open(path)
    except Exception as exc:
        raise SystemExit(f"FAIL: PDF cannot be opened: {exc}")
    pages = len(doc)
    if pages < args.min_pages:
        raise SystemExit(f"FAIL: expected at least {args.min_pages} page(s), found {pages}")
    text_chars = sum(len(page.get_text("text").strip()) for page in doc)
    if text_chars == 0:
        print("WARNING: No extractable text found. This may be a scanned/image-only PDF.")
    print(f"PASS: {path.resolve()}")
    print(f"Pages: {pages}")
    print(f"Bytes: {path.stat().st_size}")
    print(f"Extractable text characters: {text_chars}")
    print("Note: this is not a visual layout inspection. Render pages and inspect them before submission.")
    doc.close()

if __name__ == "__main__":
    main()
