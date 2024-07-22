from fastapi.testclient import TestClient
from genrative_ai.main import app

def test_root_path():
    client = TestClient(app=app) 
    response = client.get("/hy/")
    assert response.status_code == 200
    assert response.json()== {"message" : "Hello"}

def test_root_path2():
    client= TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello" : "world"}



def test_root():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"} 