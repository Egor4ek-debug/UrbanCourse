from fastapi import FastAPI
from app.models.task import router as task_router
from app.models.user import router as user_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)
