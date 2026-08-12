from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router


# ==========================================
# CREATE FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="MetricMind",
    description="AI-powered Business Intelligence Dashboard",
    version="1.0.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ==========================================
# INCLUDE ROUTES
# ==========================================

app.include_router(router)


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to MetricMind!",
        "status": "Backend is running successfully."
    }