import os
import tempfile

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from parser import extract_text
from comparator import generate_html_diff
from qwen_client import analyze_policy_changes

app = FastAPI()


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/compare")
async def compare_documents(
        legacy: UploadFile = File(...),
        modern: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=legacy.filename) as f1:

        f1.write(await legacy.read())
        legacy_path = f1.name

    with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=modern.filename) as f2:

        f2.write(await modern.read())
        modern_path = f2.name

    try:

        legacy_text = extract_text(
            legacy_path
        )

        modern_text = extract_text(
            modern_path
        )

        html_diff = generate_html_diff(
            legacy_text,
            modern_text
        )

        analysis = analyze_policy_changes(
            legacy_text,
            modern_text
        )

        return {
            "analysis": analysis,
            "diff_html": html_diff
        }

    finally:

        if os.path.exists(legacy_path):
            os.remove(legacy_path)

        if os.path.exists(modern_path):
            os.remove(modern_path)
