from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Voice AI Agent Running"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=10000)
