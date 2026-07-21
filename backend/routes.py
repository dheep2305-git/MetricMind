from fastapi import APIRouter
from data_loader import load_dataset

router = APIRouter()

@router.get("/")
def home():
    return {"message": "MetricMind API Running"}

@router.get("/total-sales")
def total_sales():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    return {
        "total_sales": float(df["Sales"].sum())
    }


@router.get("/total-profit")
def total_profit():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    return {
        "total_profit": float(df["Profit"].sum())
    }


@router.get("/total-orders")
def total_orders():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    return {
        "total_orders": int(df["Order ID"].nunique())
    }