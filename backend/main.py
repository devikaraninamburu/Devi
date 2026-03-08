from fastapi import FastAPI
from scheduler.appointment_engine import book_appointment, cancel_appointment

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Voice AI Agent Running"}

@app.post("/book")
def book(data: dict):
    return book_appointment(data)

@app.post("/cancel")
def cancel(data: dict):
    return cancel_appointment(data)
