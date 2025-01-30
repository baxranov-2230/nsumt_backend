from fastapi import APIRouter
from .category import category_router

api_v1_router = APIRouter(prefix='/v1')


api_v1_router.include_router(category_router)