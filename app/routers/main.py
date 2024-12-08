from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.task import router as task_router
from app.backend.db import Base, engine

app = FastAPI()

# Создание таблиц при старте приложения
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager"}

app.include_router(user_router)
app.include_router(task_router)
