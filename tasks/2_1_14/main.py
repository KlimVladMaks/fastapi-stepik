# Команда для запуска: uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumbersRequest(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate_sum(numbers: NumbersRequest):
    """
    Принимает два числа и возвращает их сумму.
    """
    result = numbers.num1 + numbers.num2
    return {"result": result}
