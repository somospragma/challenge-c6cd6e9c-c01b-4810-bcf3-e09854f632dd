from fastapi.testclient import TestClient
from..main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Product 1", "price": 10.0, "stock": 100, "category": "Category 1"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Product 1", "price": 10.0, "stock": 100, "category": "Category 1"}

def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Product 1", "price": 10.0, "stock": 100, "category": "Category 1"}

def test_update_product():
    response = client.put("/products/1", json={"name": "Product 2", "price": 20.0, "stock": 200, "category": "Category 2"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Product 2", "price": 20.0, "stock": 200, "category": "Category 2"}

def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Product deleted"}