from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)

templates = Jinja2Templates(directory='module16/templates')
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/', response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse(
        "users.html",
        {"request": request, "users": users}
    )


@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse(
        "users.html",
        {"request": request, "user": user}
    )


@app.post('/users/{username}/{age}')
async def post_user(username: str, age: int) -> User:
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
