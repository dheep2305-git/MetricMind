import pandas as pd
from fastapi import APIRouter
from data_loader import load_dataset

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to MetricMind API"
    }


@router.get("/dataset-info")
def dataset_info():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns)
    }


@router.get("/dataset-preview")
def dataset_preview():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    return df.head().to_dict(orient="records")


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


@router.get("/sales-by-region")
def sales_by_region():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    result = df.groupby("Region")["Sales"].sum()

    return result.to_dict()


@router.get("/sales-by-category")
def sales_by_category():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    result = df.groupby("Category")["Sales"].sum()

    return result.to_dict()


@router.get("/monthly-sales")
def monthly_sales():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    result = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .astype(float)
    )

    return {str(k): v for k, v in result.items()}


@router.get("/top-products")
def top_products():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    result = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return result.to_dict()


@router.get("/profit-by-category")
def profit_by_category():
    df = load_dataset()

    if df is None:
        return {"error": "Dataset not found"}

    result = df.groupby("Category")["Profit"].sum()

    return result.to_dict()