from pathlib import Path
import fitz
import docx


def extract_text(file_path: str):

    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        text = ""

        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        return text

    elif suffix == ".docx":

        doc = docx.Document(file_path)

        return "\n".join(
            para.text
            for para in doc.paragraphs
        )

    elif suffix == ".txt":

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    raise Exception("Unsupported file")
