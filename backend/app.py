from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="MetricMind",
    description="AI-powered Business Intelligence Platform",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to MetricMind!",
        "status": "Backend is running successfully."
    }