import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to StarHopper" in response.json()["message"]

# More tests go here for user registration, login, rides, etc.
