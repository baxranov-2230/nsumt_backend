import os
import shutil
import uuid
from fastapi import UploadFile

# Fayl saqlanadigan katalog
STORAGE_DIR = "storage"
os.makedirs(STORAGE_DIR, exist_ok=True)

def save_uploaded_image(file: UploadFile) -> str:
    """Faylni saqlaydi va URL manzilini qaytaradi"""
    file_extension = file.filename.split(".")[-1]  # Fayl kengaytmasi (.jpg, .png, ...)
    unique_filename = f"{uuid.uuid4()}.{file_extension}"  # Unikal nom yaratish
    file_path = os.path.join(STORAGE_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return f"/storage/{unique_filename}"
