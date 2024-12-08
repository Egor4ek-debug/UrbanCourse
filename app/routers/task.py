from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete
from app.backend.db_depends import get_db
from app.routers.schemas import CreateTask, UpdateTask
from app.models.user import User
from app.models.task import Task

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

# Получение всех задач
@router.get("/")
async def all_tasks(db: Session = Depends(get_db)):
    tasks = db.scalars(select(Task)).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return tasks

# Получение задачи по ID
@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

# Создание задачи
@router.post("/create")
async def create_task(task: CreateTask, user_id: int, db: Session = Depends(get_db)):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")

    new_task = Task(**task.dict(), user_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Обновление задачи
@router.put("/update/{task_id}")
async def update_task(task_id: int, updated_task: UpdateTask, db: Session = Depends(get_db)):
    query = update(Task).where(Task.id == task_id).values(**updated_task.dict())
    result = db.execute(query)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update successful"}

# Удаление задачи
@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    query = delete(Task).where(Task.id == task_id)
    result = db.execute(query)
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task deleted"}
