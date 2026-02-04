# Команда для запуска: fastapi dev main.py

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
import re

app = FastAPI()

class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator('message')
    def validate_message(value: str) -> str:
        message_lower = value.lower()
        forbidden_words = ["редиск", "бяк", "козяв"]
        for word in forbidden_words:
            pattern = r'\b' + word + r'[а-я]*\b'
            if re.search(pattern, message_lower):
                raise ValueError("Использование недопустимых слов")
        return value

feedbacks_db: list[Feedback] = []

@app.post("/feedbacks")
async def post_feedback(feedback: Feedback):
    feedbacks_db.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

@app.get("/feedbacks")
async def get_all_feedbacks() -> list[Feedback]:
    return feedbacks_db
