from fastapi import APIRouter
from data_loader import load_dataset

router = APIRouter()

@router.get("/")
def home():
    return {"message": "MetricMind Backend Running"}

@router.get("/dataset-info")
def dataset_info():
    data = load_dataset()

    return {
        "rows": len(data),
        "columns": list(data.columns)
    }