from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete
from app.models.user import User
from app.models.task import Task
from app.routers.schemas import CreateUser, UpdateUser
from app.backend.db_depends import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/")
async def all_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.get("/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this user")
    return tasks


@router.post("/create")
async def create_user(new_user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.scalars(select(User).where(User.username == new_user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    db.execute(insert(User).values(**new_user.dict()))
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User and tasks deleted"}
