from fastapi.testclient import TestClient
import os
import importlib.util

svc_path = os.path.join(os.path.dirname(__file__), "..", "main.py")
spec = importlib.util.spec_from_file_location("crypto_main", svc_path)
crypto_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crypto_main)
app = crypto_main.app
DEPOSITS = crypto_main.DEPOSITS

client = TestClient(app)

def test_crypto():
    DEPOSITS.clear()
    resp = client.get("/crypto/address", params={"currency": "BTC"})
    assert resp.status_code == 200
    assert resp.json()["currency"] == "BTC"

    resp = client.post("/crypto/deposit", params={"currency": "USDT", "amount": 10})
    assert resp.json()["amount"] == 10

    resp = client.post("/crypto/withdraw", params={"currency": "USDT", "amount": 5})
    assert resp.json()["status"] == "processing"
