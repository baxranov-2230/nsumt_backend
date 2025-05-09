import os
import shutil
from uuid import uuid4
from fastapi import UploadFile, File
from pathlib import Path

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_file(file: UploadFile) -> str:
    if file:
        filename = f"{uuid4()}_{file.filename}"
        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return filepath
    return None