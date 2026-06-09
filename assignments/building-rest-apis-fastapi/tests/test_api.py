from fastapi.testclient import TestClient

from starter_code import app


client = TestClient(app)


def test_create_get_update_delete_item():
    # Create
    resp = client.post("/items", json={"id": 0, "name": "apple", "description": "red"})
    assert resp.status_code == 201
    created = resp.json()
    item_id = created["id"] if isinstance(created, dict) else created.id

    # Get
    resp = client.get(f"/items/{item_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "apple"

    # Update
    resp = client.put(f"/items/{item_id}", json={"id": item_id, "name": "pear", "description": "green"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "pear"

    # Delete
    resp = client.delete(f"/items/{item_id}")
    assert resp.status_code == 204

    # Not found after delete
    resp = client.get(f"/items/{item_id}")
    assert resp.status_code == 404
