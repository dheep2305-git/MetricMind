from fastapi import APIRouter
from data_loader import load_dataset
from utils import get_dataset_preview

router = APIRouter()

@router.get("/")
def home():
    return {"message": "MetricMind Backend Running"}

@router.get("/dataset-info")
def dataset_info():
    data = load_dataset()

    if data is None:
        return {"error": "Dataset not found"}

    return {
        "rows": len(data),
        "columns": list(data.columns)
    }

@router.get("/dataset-preview")
def dataset_preview():
    data = load_dataset()

    if data is None:
        return {"error": "Dataset not found"}

    return get_dataset_preview(data)