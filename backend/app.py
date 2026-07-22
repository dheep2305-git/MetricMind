from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(
    title="MetricMind",
    description="AI-powered Business Intelligence Platform",
    version="1.0.0"
)

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to MetricMind!",
        "status": "Backend is running successfully."
    }