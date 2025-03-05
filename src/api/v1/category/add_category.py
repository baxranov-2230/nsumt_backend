from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.base.db import get_db
from src.models import Category
from src.schemas.category import CategoryCreateRequest

router = APIRouter()


@router.post('/add_category')
async def add_category(create_category: CategoryCreateRequest,
                       db: AsyncSession = Depends(get_db)):
    new_category = Category(
        name_uz=create_category.name_uz,
        name_ru=create_category.name_ru,
        name_en=create_category.name_en,
    )
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return {"message": "Kategoriya muvaffaqiyatli yaratildi"}
