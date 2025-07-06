from fastapi import FastAPI

app = FastAPI(title="Notification Service")

@app.post("/notify")
def send_notification(message: str):
    # Placeholder for Telegram Bot integration
    return {"status": "sent", "message": message}
