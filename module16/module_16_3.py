from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_new_message(username: str, age: str) -> str:
    last_index = str(int(max(users, key=int)) + 1)
    users[last_index] = f'Имя: {username}, возраст: {age}'
    return f'User {last_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_current_user(user_id: str, username: str, age: str) -> str:
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} is updated'
    return 'User not found'


@app.delete('/user/{user_id}')
async def delete_current_user(user_id: str) -> str:
    if user_id in users:
        users.pop(user_id)
        return f'User {user_id} has been deleted'
    return 'User not found'
