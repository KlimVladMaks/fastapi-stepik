# Команда для запуска: uvicorn app:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
