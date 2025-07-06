from fastapi.testclient import TestClient
import os
import importlib.util

svc_path = os.path.join(os.path.dirname(__file__), "..", "main.py")
spec = importlib.util.spec_from_file_location("tx_main", svc_path)
tx_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tx_main)
app = tx_main.app
TX = tx_main.TX

client = TestClient(app)

def test_transactions():
    TX.clear()
    resp = client.post("/cards/10/fund", params={"amount": 50})
    assert resp.status_code == 200
    assert resp.json()["type"] == "fund"

    resp = client.post("/cards/10/withdraw", params={"amount": 20})
    assert resp.json()["type"] == "withdraw"

    resp = client.get("/transactions")
    assert len(resp.json()) == 2
