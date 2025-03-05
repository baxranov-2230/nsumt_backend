import os
import shutil
import uuid
from fastapi import UploadFile, File
import aiofiles
from pathlib import Path

# Fayl saqlanadigan katalog


UPLOAD_DIR = "../../../../src/upload"  # Upload papkasining yo'li

async def save_uploaded_img(file: UploadFile = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    # Faylning yangi nomini yaratish (unique qilish uchun)
    file_extension = file.filename.split(".")[-1]  # Fayl kengaytmasi (.jpg, .png, .jpeg)
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Faylni asinxron tarzda saqlash
    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()  # Fayl mazmunini o'qish
        await out_file.write(content)  # Faylga yozish

    return file_path