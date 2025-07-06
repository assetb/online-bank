from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway")

USER_SERVICE = "http://localhost:8001"
CARD_SERVICE = "http://localhost:8002"
TRANSACTION_SERVICE = "http://localhost:8003"
CRYPTO_SERVICE = "http://localhost:8005"

@app.post("/users")
async def create_user(user: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{USER_SERVICE}/users", json=user)
        return resp.json()

@app.get("/users")
async def list_users():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{USER_SERVICE}/users")
        return resp.json()

@app.post("/cards")
async def create_card(card: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CARD_SERVICE}/cards", json=card)
        return resp.json()

@app.post("/cards/{card_id}/block")
async def block_card(card_id: int):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CARD_SERVICE}/cards/{card_id}/block")
        return resp.json()

@app.post("/cards/{card_id}/unblock")
async def unblock_card(card_id: int):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CARD_SERVICE}/cards/{card_id}/unblock")
        return resp.json()

@app.post("/cards/{card_id}/limits")
async def set_limits(card_id: int, limits: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CARD_SERVICE}/cards/{card_id}/limits", json=limits)
        return resp.json()

@app.get("/cards/{card_id}/limits")
async def get_limits(card_id: int):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CARD_SERVICE}/cards/{card_id}/limits")
        return resp.json()

@app.post("/cards/{card_id}/tokenize")
async def tokenize(card_id: int):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CARD_SERVICE}/cards/{card_id}/tokenize")
        return resp.json()

@app.post("/transactions")
async def create_tx(tx: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{TRANSACTION_SERVICE}/transactions", json=tx)
        return resp.json()

@app.get("/transactions")
async def list_tx():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TRANSACTION_SERVICE}/transactions")
        return resp.json()

@app.post("/cards/{card_id}/fund")
async def fund_card(card_id: int, amount: float):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{TRANSACTION_SERVICE}/cards/{card_id}/fund", params={"amount": amount})
        return resp.json()

@app.post("/cards/{card_id}/withdraw")
async def withdraw_card(card_id: int, amount: float):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{TRANSACTION_SERVICE}/cards/{card_id}/withdraw", params={"amount": amount})
        return resp.json()

@app.get("/crypto/address")
async def crypto_address(currency: str = "USDT"):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{CRYPTO_SERVICE}/crypto/address", params={"currency": currency})
        return resp.json()

@app.post("/crypto/deposit")
async def crypto_deposit(currency: str, amount: float):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CRYPTO_SERVICE}/crypto/deposit", params={"currency": currency, "amount": amount})
        return resp.json()

@app.post("/crypto/withdraw")
async def crypto_withdraw(currency: str, amount: float):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CRYPTO_SERVICE}/crypto/withdraw", params={"currency": currency, "amount": amount})
        return resp.json()
