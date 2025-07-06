from fastapi import FastAPI, HTTPException
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

@app.get("/users")
def list_users():
    return list(USERS.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    USERS[user_id] = user
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    del USERS[user_id]
    return {"status": "deleted"}
