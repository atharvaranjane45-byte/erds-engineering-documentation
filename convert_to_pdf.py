#!/usr/bin/env python3
"""Convert a DOCX file to PDF with LibreOffice in headless mode."""
import argparse
import shutil
import subprocess
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Input DOCX path")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    source = Path(args.input).resolve()
    out_dir = Path(args.output_dir).resolve()
    if not source.is_file():
        raise SystemExit(f"Input file not found: {source}")
    if source.suffix.lower() != ".docx":
        raise SystemExit("Input must be a .docx file.")
    executable = shutil.which("libreoffice") or shutil.which("soffice")
    if not executable:
        raise SystemExit("LibreOffice was not found. Install LibreOffice and ensure 'libreoffice' or 'soffice' is on PATH.")
    out_dir.mkdir(parents=True, exist_ok=True)
    command = [executable, "--headless", "--convert-to", "pdf", "--outdir", str(out_dir), str(source)]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=args.timeout)
    except subprocess.TimeoutExpired:
        raise SystemExit(f"PDF conversion timed out after {args.timeout} seconds.")
    pdf = out_dir / (source.stem + ".pdf")
    if result.returncode != 0 or not pdf.is_file() or pdf.stat().st_size == 0:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit("PDF conversion failed or produced an empty file.")
    print(f"Created PDF: {pdf}")
    if result.stdout.strip():
        print(result.stdout.strip())

if __name__ == "__main__":
    main()
