# Команда для запуска: fastapi dev main.py

from fastapi import FastAPI
from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    name: str
    age: int
    is_adult: bool

app = FastAPI()

@app.post("/user")
async def is_user_adult(user: UserRequest) -> UserResponse:
    name = user.name
    age = user.age
    is_adult = age >= 18
    return UserResponse(
        name=name,
        age=age,
        is_adult=is_adult
    )
