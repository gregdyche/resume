import subprocess
from pathlib import Path

def export_resume():
    md_file = Path("resume.md")
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