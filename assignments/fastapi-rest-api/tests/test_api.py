from fastapi.testclient import TestClient
from starter_code import app


client = TestClient(app)


def test_create_get_update_delete():
    # Create
    resp = client.post("/items", json={"name": "pen", "price": 1.5})
    assert resp.status_code == 201
    data = resp.json()
    item_id = data["id"]
    assert data["name"] == "pen"

    # Get
    resp = client.get(f"/items/{item_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == item_id

    # Update
    resp = client.put(f"/items/{item_id}", json={"name": "pen", "price": 2.0})
    assert resp.status_code == 200
    assert resp.json()["price"] == 2.0

    # Delete
    resp = client.delete(f"/items/{item_id}")
    assert resp.status_code == 204

    # Confirm deletion
    resp = client.get(f"/items/{item_id}")
    assert resp.status_code == 404


def test_list_items_empty():
    resp = client.get("/items")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
