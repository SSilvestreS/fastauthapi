from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Saulo", "email": "saulo@test.com", "password": "123"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Saulo"
    assert data["email"] == "saulo@test.com"
    assert "hashed_password" not in data