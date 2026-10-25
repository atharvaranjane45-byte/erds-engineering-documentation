# ERDS — Engineering Research & Documentation Skill (Codex)

ERDS is a Codex skill plus a small local document-generation toolkit. It guides research, student intake, technical writing, diagram planning, citation hygiene, quality checks, and DOCX-to-PDF export.

## Included
- `SKILL.md`: Codex skill instructions.
- `agents/openai.yaml`: optional UI metadata.
- `references/`: intake, research, citations, diagram, quality, and toolkit guidance.
- `assets/templates/`: adaptable report outlines.
- `scripts/generate_report.py`: convert a simple Markdown report plus metadata JSON into a styled DOCX.
- `scripts/convert_to_pdf.py`: convert DOCX to PDF using LibreOffice.
- `scripts/validate_pdf.py`: basic PDF checks using PyMuPDF when installed.
- `examples/`: starter Markdown and metadata files.

## Install in Codex

### Repository-local
Copy the `erds-engineering-documentation` folder into your repository at:
`.agents/skills/erds-engineering-documentation/`

### User-level
Copy it into:
`~/.agents/skills/erds-engineering-documentation/`

On Windows, the user home directory is usually `C:\\Users\\<you>`. Use the path supported by your Codex environment. Codex's current skill discovery convention uses `.agents/skills`; restart Codex if the skill does not appear.

In Codex, invoke it explicitly with `$erds-engineering-documentation` or describe a matching assignment and let skill discovery select it.

## Requirements for the document toolkit
- Python 3.10+
- `python-docx`
- LibreOffice installed for PDF conversion
- Optional: `pymupdf` for richer PDF validation
- Optional diagram renderers: Mermaid CLI (`mmdc`) or Graphviz (`dot`) for workflows that need rendered diagrams.

Install Python dependencies:
```bash
python -m pip install -r requirements.txt
```

## Generate a DOCX
From the project root:
```bash
python scripts/generate_report.py \
  --markdown examples/sample_report.md \
  --metadata examples/metadata.json \
  --output-dir output
```

Windows PowerShell:
```powershell
python scripts/generate_report.py --markdown examples/sample_report.md --metadata examples/metadata.json --output-dir output
```

## Convert to PDF
```bash
python scripts/convert_to_pdf.py --input output/report.docx --output-dir output
```

## Validate PDF
```bash
python scripts/validate_pdf.py output/report.pdf
```

The validation script checks basic readability and metadata. It does not guarantee visual perfection; render pages to images and inspect them for layout issues before submission.

## Important
The skill does not itself grant web access. Research depends on the tools available to the running Codex session. It must not claim to have browsed if no web tool was used. Always verify citations, technical claims, and actual experimental results before submission.
