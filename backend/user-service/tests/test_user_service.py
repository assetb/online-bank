from fastapi.testclient import TestClient
import os
import importlib.util

svc_path = os.path.join(os.path.dirname(__file__), "..", "main.py")
spec = importlib.util.spec_from_file_location("user_main", svc_path)
user_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user_main)
app = user_main.app
USERS = user_main.USERS

client = TestClient(app)


def test_crud_user():
    USERS.clear()
    resp = client.post("/users", json={"id": 1, "name": "Alice", "phone": "123"})
    assert resp.status_code == 200
    assert resp.json()["name"] == "Alice"

    resp = client.get("/users/1")
    assert resp.status_code == 200
    assert resp.json()["phone"] == "123"

    resp = client.put("/users/1", json={"id": 1, "name": "Bob", "phone": "555"})
    assert resp.status_code == 200
    assert resp.json()["name"] == "Bob"

    resp = client.get("/users")
    assert len(resp.json()) == 1

    resp = client.delete("/users/1")
    assert resp.status_code == 200
    assert resp.json()["status"] == "deleted"
