from fastapi.testclient import TestClient
import os
import importlib.util

svc_path = os.path.join(os.path.dirname(__file__), "..", "main.py")
spec = importlib.util.spec_from_file_location("notif_main", svc_path)
notif_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(notif_main)
app = notif_main.app

client = TestClient(app)

def test_notify():
    resp = client.post("/notify", params={"message": "hello"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "sent"
