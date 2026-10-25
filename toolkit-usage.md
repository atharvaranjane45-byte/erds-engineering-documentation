# Toolkit usage

The scripts automate the formatting/export stage; they do not perform web research by themselves.

## Input format
Provide a Markdown report and a JSON metadata file. Metadata keys can include:
`student_names`, `college`, `department`, `roll_numbers`, `academic_year`, `subject`, `title`, `guide`, `document_type`, `date`, and `citation_style`.

Example:
```json
{
  "title": "IoT-Based Smart Irrigation System",
  "student_names": ["Student Name"],
  "college": "College Name",
  "department": "Department of Computer Engineering",
  "guide": "Guide Name",
  "academic_year": "2026-2027",
  "document_type": "Mini-Project Report",
  "citation_style": "IEEE"
}
```

## Commands
```bash
python scripts/generate_report.py --markdown examples/sample_report.md --metadata examples/metadata.json --output-dir output
python scripts/convert_to_pdf.py --input output/report.docx --output-dir output
python scripts/validate_pdf.py output/report.pdf
```

The DOCX generator supports headings, paragraphs, unordered/ordered lists, simple Markdown tables, inline bold/italic/code, and fenced code blocks. It does not execute embedded code or fetch external images. Add diagrams as image files through a future extension or insert them into the DOCX manually; the skill instructions explain how to plan/render diagrams.
