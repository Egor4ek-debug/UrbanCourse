from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> users:
    return users


@app.post('/users/{username}/{age}')
async def create_new_message(username: str, age: int) -> User:
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_current_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_current_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            delete_user = users.pop(user_id - 1)
            return delete_user
    raise HTTPException(status_code=404, detail='User was not found')
