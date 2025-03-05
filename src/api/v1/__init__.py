from fastapi import APIRouter
from .category import category_router
from .faculty import faculty_router

api_v1_router = APIRouter(prefix='/v1')


api_v1_router.include_router(category_router)
api_v1_router.include_router(faculty_router)