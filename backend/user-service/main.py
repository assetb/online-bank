from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="User Service")

class User(BaseModel):
    id: int
    name: str
    phone: str

# In-memory store for demo purposes
USERS = {}

@app.post("/users")
def create_user(user: User):
    USERS[user.id] = user
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return USERS.get(user_id)
