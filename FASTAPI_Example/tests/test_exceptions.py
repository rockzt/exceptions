import pytest
from fastapi.testclient import TestClient

from main import app

def test_user_not_found():
    client = TestClient(app)
    response = client.get("/users/999")  # Assuming user ID 999 does not exist
    assert response.status_code == 404
    assert "not found" in response.json()["error"]

def test_invalid_user_data():
    client = TestClient(app)
    response = client.post("/users", json={"invalid": "data"})  # Invalid user data
    assert response.status_code == 404
    assert "Invalid user data" in response.json()["error"]

