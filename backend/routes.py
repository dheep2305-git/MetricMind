# ============================================================
# METRICMIND - ROUTES
# Superstore Dataset Version
# ============================================================

import os
import shutil

import pandas as pd

from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from data_loader import load_dataset
from chatbot import ask_ai


router = APIRouter()


# ============================================================
# AI REQUEST MODEL
# ============================================================

class AIQuestion(BaseModel):

    question: str


# ============================================================
# HELPER FUNCTION
# ============================================================

def get_column(df, column_name):

    """
    Finds a Superstore column safely.
    Handles spaces and upper/lowercase differences.
    """

    for column in df.columns:

        if str(column).strip().lower() == column_name.lower():

            return column

    return None


# ============================================================
# HOME
# ============================================================

@router.get("/")
def home():

    return {
        "message": "Welcome to MetricMind API",
        "status": "Backend is running successfully."
    }


# ============================================================
# DATASET INFO
# ============================================================

@router.get("/dataset-info")
def dataset_info():

    df = load_dataset()

    if df is None:

        return {
            "error": "No Superstore dataset found."
        }

    return {

        "rows": int(len(df)),

        "columns": int(len(df.columns)),

        "column_names": list(df.columns)

    }


# ============================================================
# DATASET PREVIEW
# ============================================================

@router.get("/dataset-preview")
def dataset_preview():

    df = load_dataset()

    if df is None:

        return {
            "error": "No Superstore dataset found."
        }

    return (
        df.head(10)
        .fillna("")
        .to_dict(orient="records")
    )


# ============================================================
# TOTAL SALES
# ============================================================

@router.get("/total-sales")
def total_sales():

    df = load_dataset()

    if df is None:

        return {
            "total_sales": 0
        }

    sales_column = get_column(
        df,
        "Sales"
    )

    if sales_column is None:

        return {
            "total_sales": 0,
            "error": "Sales column not found."
        }

    sales = pd.to_numeric(
        df[sales_column],
        errors="coerce"
    ).fillna(0)

    return {

        "total_sales": round(
            float(sales.sum()),
            2
        )

    }


# ============================================================
# TOTAL PROFIT
# ============================================================

@router.get("/total-profit")
def total_profit():

    df = load_dataset()

    if df is None:

        return {
            "total_profit": 0
        }

    profit_column = get_column(
        df,
        "Profit"
    )

    if profit_column is None:

        return {
            "total_profit": 0,
            "error": "Profit column not found."
        }

    profit = pd.to_numeric(
        df[profit_column],
        errors="coerce"
    ).fillna(0)

    return {

        "total_profit": round(
            float(profit.sum()),
            2
        )

    }


# ============================================================
# TOTAL ORDERS
# ============================================================

@router.get("/total-orders")
def total_orders():

    df = load_dataset()

    if df is None:

        return {
            "total_orders": 0
        }

    order_column = get_column(
        df,
        "Order ID"
    )

    if order_column is None:

        return {
            "total_orders": 0,
            "error": "Order ID column not found."
        }

    orders = (
        df[order_column]
        .dropna()
        .astype(str)
        .str.strip()
    )

    return {

        "total_orders": int(
            orders.nunique()
        )

    }


# ============================================================
# TOP PRODUCTS
# ============================================================

@router.get("/top-products")
def top_products():

    df = load_dataset()

    if df is None:

        return {}

    product_column = get_column(
        df,
        "Product Name"
    )

    sales_column = get_column(
        df,
        "Sales"
    )

    if product_column is None:

        return {
            "error": "Product Name column not found."
        }

    if sales_column is None:

        return {
            "error": "Sales column not found."
        }

    temp = df.copy()

    temp["_sales"] = pd.to_numeric(
        temp[sales_column],
        errors="coerce"
    ).fillna(0)

    result = (
        temp
        .groupby(product_column)["_sales"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    return {

        str(product): round(
            float(sales),
            2
        )

        for product, sales in result.items()

    }


# ============================================================
# SALES BY REGION
# ============================================================

@router.get("/sales-by-region")
def sales_by_region(
    region: str = "All"
):

    df = load_dataset()

    if df is None:

        return {}

    region_column = get_column(
        df,
        "Region"
    )

    sales_column = get_column(
        df,
        "Sales"
    )

    if region_column is None:

        return {
            "error": "Region column not found."
        }

    if sales_column is None:

        return {
            "error": "Sales column not found."
        }

    temp = df.copy()

    temp["_sales"] = pd.to_numeric(
        temp[sales_column],
        errors="coerce"
    ).fillna(0)

    # --------------------------------------------------------
    # ALL REGIONS
    # --------------------------------------------------------

    if region.lower() == "all":

        result = (
            temp
            .groupby(region_column)["_sales"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

    # --------------------------------------------------------
    # SELECTED REGION
    # --------------------------------------------------------

    else:

        filtered = temp[
            temp[region_column]
            .astype(str)
            .str.strip()
            .str.lower()
            ==
            region.strip().lower()
        ]

        if filtered.empty:

            return {}

        result = (
            filtered
            .groupby(region_column)["_sales"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

    return {

        str(name): round(
            float(value),
            2
        )

        for name, value in result.items()

    }


# ============================================================
# PROFIT BY CATEGORY
# ============================================================

@router.get("/profit-by-category")
def profit_by_category():

    df = load_dataset()

    if df is None:

        return {}

    category_column = get_column(
        df,
        "Category"
    )

    profit_column = get_column(
        df,
        "Profit"
    )

    if category_column is None:

        return {
            "error": "Category column not found."
        }

    if profit_column is None:

        return {
            "error": "Profit column not found."
        }

    temp = df.copy()

    temp["_profit"] = pd.to_numeric(
        temp[profit_column],
        errors="coerce"
    ).fillna(0)

    result = (
        temp
        .groupby(category_column)["_profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    return {

        str(category): round(
            float(profit),
            2
        )

        for category, profit in result.items()

    }


# ============================================================
# MONTHLY SALES
# ============================================================

@router.get("/monthly-sales")
def monthly_sales():

    df = load_dataset()

    if df is None:

        return {}

    date_column = get_column(
        df,
        "Order Date"
    )

    sales_column = get_column(
        df,
        "Sales"
    )

    if date_column is None:

        return {
            "error": "Order Date column not found."
        }

    if sales_column is None:

        return {
            "error": "Sales column not found."
        }

    temp = df.copy()

    # Convert Order Date to datetime
    temp["_date"] = pd.to_datetime(
        temp[date_column],
        errors="coerce"
    )

    temp["_sales"] = pd.to_numeric(
        temp[sales_column],
        errors="coerce"
    ).fillna(0)

    # Remove invalid dates
    temp = temp.dropna(
        subset=["_date"]
    )

    if temp.empty:

        return {}

    # Create month
    temp["_month"] = (
        temp["_date"]
        .dt.to_period("M")
        .astype(str)
    )

    result = (
        temp
        .groupby("_month")["_sales"]
        .sum()
        .sort_index()
    )

    return {

        str(month): round(
            float(sales),
            2
        )

        for month, sales in result.items()

    }


# ============================================================
# PROFIT BY REGION
# ============================================================

@router.get("/profit-by-region")
def profit_by_region():

    df = load_dataset()

    if df is None:

        return {}

    region_column = get_column(
        df,
        "Region"
    )

    profit_column = get_column(
        df,
        "Profit"
    )

    if region_column is None:

        return {
            "error": "Region column not found."
        }

    if profit_column is None:

        return {
            "error": "Profit column not found."
        }

    temp = df.copy()

    temp["_profit"] = pd.to_numeric(
        temp[profit_column],
        errors="coerce"
    ).fillna(0)

    result = (
        temp
        .groupby(region_column)["_profit"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    return {

        str(region): round(
            float(profit),
            2
        )

        for region, profit in result.items()

    }


# ============================================================
# SALES BY CATEGORY
# ============================================================

@router.get("/sales-by-category")
def sales_by_category():

    df = load_dataset()

    if df is None:

        return {}

    category_column = get_column(
        df,
        "Category"
    )

    sales_column = get_column(
        df,
        "Sales"
    )

    if category_column is None:

        return {
            "error": "Category column not found."
        }

    if sales_column is None:

        return {
            "error": "Sales column not found."
        }

    temp = df.copy()

    temp["_sales"] = pd.to_numeric(
        temp[sales_column],
        errors="coerce"
    ).fillna(0)

    result = (
        temp
        .groupby(category_column)["_sales"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    return {

        str(category): round(
            float(sales),
            2
        )

        for category, sales in result.items()

    }


# ============================================================
# DATASET ROW COUNT
# ============================================================

@router.get("/total-rows")
def total_rows():

    df = load_dataset()

    if df is None:

        return {
            "total_rows": 0
        }

    return {

        "total_rows": int(
            len(df)
        )

    }


# ============================================================
# NUMERIC COLUMNS
# ============================================================

@router.get("/numeric-columns")
def numeric_columns():

    df = load_dataset()

    if df is None:

        return {
            "columns": []
        }

    columns = list(
        df.select_dtypes(
            include="number"
        ).columns
    )

    return {

        "columns": columns

    }


# ============================================================
# NUMERIC DATA
# ============================================================

@router.get(
    "/numeric-data/{column_name}"
)
def numeric_data(
    column_name: str
):

    df = load_dataset()

    if df is None:

        return {
            "error":
                "No dataset found."
        }

    if column_name not in df.columns:

        return {
            "error":
                "Column not found."
        }

    values = pd.to_numeric(
        df[column_name],
        errors="coerce"
    ).dropna()

    return {

        "column":
            column_name,

        "values":
            values.tolist()

    }


# ============================================================
# CATEGORICAL COLUMNS
# ============================================================

@router.get("/categorical-columns")
def categorical_columns():

    df = load_dataset()

    if df is None:

        return {
            "columns": []
        }

    columns = list(
        df.select_dtypes(
            exclude="number"
        ).columns
    )

    return {

        "columns": columns

    }


# ============================================================
# CATEGORICAL DATA
# ============================================================

@router.get(
    "/categorical-data/{column_name}"
)
def categorical_data(
    column_name: str
):

    df = load_dataset()

    if df is None:

        return {
            "error":
                "No dataset found."
        }

    if column_name not in df.columns:

        return {
            "error":
                "Column not found."
        }

    result = (
        df[column_name]
        .fillna("Unknown")
        .astype(str)
        .value_counts()
        .head(10)
    )

    return result.to_dict()


# ============================================================
# TOP VALUES
# ============================================================

@router.get("/top-values")
def top_values():

    df = load_dataset()

    if df is None:

        return {
            "error":
                "No dataset found."
        }

    result = {}

    for column in df.columns:

        if not pd.api.types.is_numeric_dtype(
            df[column]
        ):

            values = (
                df[column]
                .fillna("Unknown")
                .astype(str)
                .value_counts()
                .head(5)
                .to_dict()
            )

            result[column] = values

    return result


# ============================================================
# AI CHATBOT
# ============================================================

@router.post("/ask-ai")
def ai_chat(
    data: AIQuestion
):

    try:

        answer = ask_ai(
            data.question
        )

        return {

            "question":
                data.question,

            "answer":
                answer

        }

    except Exception as e:

        return {

            "question":
                data.question,

            "answer":
                "AI error: " + str(e)

        }


# ============================================================
# UPLOAD SUPERSTORE CSV
# ============================================================

@router.post("/upload-dataset")
async def upload_dataset(
    file: UploadFile = File(...)
):

    try:

        # ----------------------------------------------------
        # CHECK FILE
        # ----------------------------------------------------

        if not file.filename:

            return {

                "error":
                    "No file selected."

            }


        if not file.filename.lower().endswith(".csv"):

            return {

                "error":
                    "Please upload a CSV file only."

            }


        # ----------------------------------------------------
        # PROJECT ROOT
        # ----------------------------------------------------

        BASE_DIR = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )


        # ----------------------------------------------------
        # DATA FOLDER
        # ----------------------------------------------------

        raw_folder = os.path.join(
            BASE_DIR,
            "data",
            "raw"
        )


        os.makedirs(
            raw_folder,
            exist_ok=True
        )


        # ----------------------------------------------------
        # CURRENT DATASET
        # ----------------------------------------------------

        file_path = os.path.join(
            raw_folder,
            "uploaded_dataset.csv"
        )


        # ----------------------------------------------------
        # SAVE FILE
        # ----------------------------------------------------

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        # ----------------------------------------------------
        # READ DATASET
        # ----------------------------------------------------

        df = load_dataset()


        if df is None:

            return {

                "error":
                    "Dataset was uploaded but could not be read."

            }


        # ----------------------------------------------------
        # CHECK SUPERSTORE COLUMNS
        # ----------------------------------------------------

        required_columns = [

            "Sales",

            "Profit",

            "Order ID",

            "Product Name",

            "Region",

            "Category",

            "Order Date"

        ]


        missing_columns = []


        for required in required_columns:

            if get_column(
                df,
                required
            ) is None:

                missing_columns.append(
                    required
                )


        if missing_columns:

            return {

                "error":
                    "This is not a valid Superstore dataset.",

                "missing_columns":
                    missing_columns,

                "available_columns":
                    list(df.columns)

            }


        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        return {

            "message":
                "Superstore dataset uploaded successfully.",

            "filename":
                file.filename,

            "rows":
                int(len(df)),

            "columns":
                int(len(df.columns)),

            "column_names":
                list(df.columns)

        }


    except Exception as e:

        return {

            "error":
                str(e)

        }