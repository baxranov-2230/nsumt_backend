from fastapi import APIRouter


category_router = APIRouter(prefix='/category', tags=['Kategory'])


from src.api.v1.category.add_category import router as add_category_router
from  src.api.v1.category.get_all_category import router as get_all_category_router

category_router.include_router(add_category_router)
category_router.include_router(get_all_category_router)