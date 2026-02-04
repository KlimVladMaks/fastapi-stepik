# Команда для запуска: fastapi dev main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

feedbacks_db: list[Feedback] = []

@app.post("/feedback")
async def post_feedback(feedback: Feedback):
    feedbacks_db.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

@app.get("/feedbacks")
async def get_all_feedbacks() -> list[Feedback]:
    return feedbacks_db
