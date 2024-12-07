from fastapi import FastAPI

from ..models.task import router as task_router
from ..models.user import router as user_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task_router)
app.include_router(user_router)
