from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "Healthy",
        "message": "Backend service is active."
    }

@router.get("/about")
def about():
    return {
        "project": "MetricMind",
        "description": "AI-powered Business Intelligence Platform",
        "version": "1.0.0"
    }