from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user(user_id: int = Path(ge=1, le=100, example='Enter User ID')) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/{username}/{age}')
async def user_paginator(username: str = Path(min_length=5, max_length=20, example='Enter username'),
                         age: int = Path(ge=18, le=120, example='Enter age')) -> dict:
    return {'message': f'Информация о пользователе. Имя {username}, Возраст {age}'}
