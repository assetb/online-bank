from fastapi.testclient import TestClient
import os
import importlib.util

svc_path = os.path.join(os.path.dirname(__file__), "..", "main.py")
spec = importlib.util.spec_from_file_location("card_main", svc_path)
card_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(card_main)
app = card_main.app
CARDS = card_main.CARDS

client = TestClient(app)

def test_card_workflow():
    CARDS.clear()
    resp = client.post("/cards", json={"id": 1, "user_id": 1, "number": "123", "name": "demo"})
    assert resp.status_code == 200

    resp = client.post("/cards/1/block")
    assert resp.json()["blocked"] is True

    resp = client.post("/cards/1/limits", json={"daily": 100})
    assert resp.json()["daily"] == 100

    resp = client.get("/cards/1/limits")
    assert resp.json()["daily"] == 100

    resp = client.post("/cards/1/tokenize")
    assert "token" in resp.json()

    resp = client.delete("/cards/1")
    assert resp.json()["status"] == "deleted"
