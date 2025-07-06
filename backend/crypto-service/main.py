from fastapi import FastAPI

app = FastAPI(title="Crypto Service")

@app.get("/crypto/address")
def get_address(currency: str = "USDT"):
    # In a real system, generate address via wallet provider
    return {"currency": currency, "address": "demo-address"}
