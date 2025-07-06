from fastapi import FastAPI
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
