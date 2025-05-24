


# 📄 Resume Repository

This project manages multiple versions of my professional resume using Markdown and Git.

## 💡 Purpose

The goal is to maintain a single source of truth (`main` branch) and create tailored resume branches for specific roles, industries, or audiences — all tracked in Git and easily exportable to PDF.

## 🚀 Workflow

1. **Write resume in Markdown**  
   - Example: `resume.md`, `resume-teaching.md`, `resume-tech-sales.md`

2. **Select resume via TUI**  
   - A Python script (`export_resume_to_pdf.py`) uses a terminal menu to pick which resume to export.

3. **Export to PDF using Pandoc**  
   - Uses `pandoc` with `xelatex` for high-quality formatting.
   - Output is saved as `resume.pdf`.

4. **Track versions with Git**  
   - Each custom resume can live in its own branch (e.g. `resume/teaching`, `resume/sales-exec`).
   - Changes are committed and optionally pushed to a private GitHub repo.

## 🛠 Requirements

- Python 3.8+
- [Pandoc](https://pandoc.org/)
- [MacTeX](https://tug.org/mactex/) (for LaTeX/PDF export)
- `questionary` (Python TUI library)

## ✅ Commands

```bash
python export_resume_to_pdf.py
```

This script will prompt you to select which Markdown file to convert to PDF.