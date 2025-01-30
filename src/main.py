import uvicorn
from fastapi import FastAPI

from src.api.v1 import api_v1_router
from starlette.middleware.cors import CORSMiddleware

app=FastAPI()


app.include_router(api_v1_router)

if __name__=='__main__':
    uvicorn.run('main:app', reload=True)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Разрешаем доступ с вашего фронтенда
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP методы
    allow_headers=["*"],  # Разрешаем все заголовки
)