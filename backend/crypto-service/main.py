from fastapi import FastAPI

app = FastAPI(title="Crypto Service")

@app.get("/crypto/address")
def get_address(currency: str = "USDT"):
    # In a real system, generate address via wallet provider
    return {"currency": currency, "address": "demo-address"}


DEPOSITS = []


@app.post("/crypto/deposit")
def create_deposit(currency: str, amount: float):
    dep = {"currency": currency, "amount": amount}
    DEPOSITS.append(dep)
    return dep


@app.post("/crypto/withdraw")
def withdraw(currency: str, amount: float):
    # Placeholder for withdraw logic
    return {"status": "processing", "currency": currency, "amount": amount}
