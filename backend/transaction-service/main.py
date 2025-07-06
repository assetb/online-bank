from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Transaction Service")

class Transaction(BaseModel):
    id: int
    card_id: int
    amount: float
    type: str

TX = {}

@app.post("/transactions")
def create_tx(tx: Transaction):
    TX[tx.id] = tx
    return tx

@app.get("/transactions/{tx_id}")
def get_tx(tx_id: int):
    return TX.get(tx_id)

@app.get("/transactions")
def list_tx():
    return list(TX.values())

@app.post("/cards/{card_id}/fund")
def fund_card(card_id: int, amount: float):
    tx_id = len(TX) + 1
    tx = Transaction(id=tx_id, card_id=card_id, amount=amount, type="fund")
    TX[tx_id] = tx
    return tx

@app.post("/cards/{card_id}/withdraw")
def withdraw_card(card_id: int, amount: float):
    tx_id = len(TX) + 1
    tx = Transaction(id=tx_id, card_id=card_id, amount=amount, type="withdraw")
    TX[tx_id] = tx
    return tx
