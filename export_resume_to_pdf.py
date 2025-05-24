import subprocess
from pathlib import Path
import questionary

def export_resume():
    resume_files = list(Path('.').glob("*.md"))
    if not resume_files:
        print("❌ No markdown resumes found.")
        return

    choices = [f.name for f in resume_files]
    selected_file = questionary.select(
        "Which resume would you like to export?",
        choices=choices
    ).ask()

    if not selected_file:
        print("❌ No selection made.")
        return

    md_file = Path(selected_file)
    pdf_file = Path("resume.pdf")

    if not md_file.exists():
        print("❌ resume.md not found.")
        return

    try:
        print("📄 Converting resume.md to resume.pdf...")
        subprocess.run([
            "pandoc",
            str(md_file),
            "-o", str(pdf_file),
            "--from", "markdown",
            "--pdf-engine=pdflatex"
        ], check=True)
        print("✅ Done. File saved as:", pdf_file)
    except subprocess.CalledProcessError as e:
        print("❌ Pandoc failed:", e)

if __name__ == "__main__":
    export_resume()