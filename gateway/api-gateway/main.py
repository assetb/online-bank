from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway")

USER_SERVICE = "http://localhost:8001"
CARD_SERVICE = "http://localhost:8002"
TRANSACTION_SERVICE = "http://localhost:8003"

@app.post("/users")
async def create_user(user: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{USER_SERVICE}/users", json=user)
        return resp.json()

@app.post("/cards")
async def create_card(card: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{CARD_SERVICE}/cards", json=card)
        return resp.json()

@app.post("/transactions")
async def create_tx(tx: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{TRANSACTION_SERVICE}/transactions", json=tx)
        return resp.json()
