from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Card Service")

class Card(BaseModel):
    id: int
    user_id: int
    number: str
    name: str | None = None
    balance: float = 0.0
    blocked: bool = False
    limits: dict | None = None

CARDS = {}

@app.post("/cards")
def create_card(card: Card):
    CARDS[card.id] = card
    return card

@app.get("/cards/{card_id}")
def get_card(card_id: int):
    card = CARDS.get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

@app.put("/cards/{card_id}")
def update_card(card_id: int, card: Card):
    if card_id not in CARDS:
        raise HTTPException(status_code=404, detail="Card not found")
    CARDS[card_id] = card
    return card

@app.delete("/cards/{card_id}")
def delete_card(card_id: int):
    if card_id not in CARDS:
        raise HTTPException(status_code=404, detail="Card not found")
    del CARDS[card_id]
    return {"status": "deleted"}

@app.post("/cards/{card_id}/block")
def block_card(card_id: int):
    card = CARDS.get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    card.blocked = True
    return card

@app.post("/cards/{card_id}/unblock")
def unblock_card(card_id: int):
    card = CARDS.get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    card.blocked = False
    return card

@app.post("/cards/{card_id}/limits")
def set_limits(card_id: int, limits: dict):
    card = CARDS.get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    card.limits = limits
    return limits

@app.get("/cards/{card_id}/limits")
def get_limits(card_id: int):
    card = CARDS.get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card.limits or {}

@app.post("/cards/{card_id}/tokenize")
def tokenize(card_id: int):
    card = CARDS.get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return {"token": f"token-{card_id}"}
