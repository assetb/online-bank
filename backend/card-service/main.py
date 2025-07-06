from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Card Service")

class Card(BaseModel):
    id: int
    user_id: int
    number: str
    balance: float = 0.0

CARDS = {}

@app.post("/cards")
def create_card(card: Card):
    CARDS[card.id] = card
    return card

@app.get("/cards/{card_id}")
def get_card(card_id: int):
    return CARDS.get(card_id)
