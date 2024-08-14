from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/foo", headers={"X-Token":"super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {
        "id":"foo",
        "title":"Foo",
        "description":"There goes my hero",
    }

def test_read_item_bad_token():
    response = client.get("/items/foo",headers={"X-Token":"not-real-token"})
    assert response.status_code == 400
    assert response.json() == {"detail":"Invalid X-Token header"}

def test_read_nonexistent_item():
    response = client.get("/items/baz",headers={"X-Token":"super-secret-token"})
    assert response.status_code == 404 
    assert response.json() == {"detail":"item not found"}

def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token":"super-secret-token"},
        json={"id":"foobar","title":"Foo Bar", "description":"The Foo Barters"},
    )
    assert response.status_code== 200
    assert response.json() == {
        "id": "foobar",
        "title":"Foo Bar",
        "description":"The Foo Barters",
    }

def test_create_item_bad_item():
    response = client.post(
        "/items/",
        headers={"X-Token":"hailhydra"},
        json={"id":"bazz", "title":"Bazz", "description":"Drop the bazz"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail":"Invalid X-token header"}

def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"X-token":"super-secret-token"},
        json={
            "id":"foo",
            "title":"the foo id stealers",
            "description":"there goes my stealer",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail":"Item already exists"} 