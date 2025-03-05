from fastapi import APIRouter


faculty_router = APIRouter(prefix='/faculty', tags=['Faculty'])


from src.api.v1.faculty.add_faculty import router as add_faculty_router
from src.api.v1.faculty.get_all_faculty import router as get_all_faculty_router


faculty_router.include_router(add_faculty_router)
faculty_router.include_router(get_all_faculty_router)

