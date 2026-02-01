# Команда для запуска тестов: pytest tests.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.parametrize("num1,num2,expected", [
    (5, 10, 15),
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
    (2.5, 2.5, 5.0),
    (0.1, 0.2, 0.3),
    (-0.1, 0.5, 0.4),
])
def test(num1, num2, expected):
    response = client.post(
        "/calculate",
        json={"num1": num1, "num2": num2}
    )
    assert response.status_code == 200

    if isinstance(expected, float):
        assert abs(response.json()["result"] - expected) < 0.000001
    else:
        assert response.json()["result"] == expected
