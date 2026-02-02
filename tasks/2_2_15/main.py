# Команда для запуска: fastapi dev main.py

from fastapi import FastAPI
from models import User

app = FastAPI()

user: User = User(id=1, name="John Doe")

@app.get("/users")
async def get_user() -> User:
    return user
