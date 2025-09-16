from fastapi.testclient import TestClient
from src.api.run.main import app
import pytest

<<<<<<< HEAD
=======

>>>>>>> develop
@pytest.fixture
def personal_info():
    return {
        "id": 1045678580,
        "name": "Никита",
        "email": "jeson.jesonov@gmail.com",
        "phone": "+79821511903",
        "age": 19

    }
<<<<<<< HEAD
=======


>>>>>>> develop
def test_add_user(personal_info: dict):
    url = "/v1/user/addUser"
    client = TestClient(app)
    response = client.post(url, json=personal_info)
    assert response.status_code == 200
    data = response.json()
<<<<<<< HEAD
    assert data.get("success") == True
=======
    assert data.get("success")
>>>>>>> develop


