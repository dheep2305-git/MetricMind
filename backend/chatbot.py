import pandas as pd

from data_loader import load_dataset
from semantic_layer import METRICS
from mm_langchain.agent import ask_agent


# ============================================================
# METRICMIND CHATBOT
# ============================================================


def ask_ai(question):

    try:

        # ====================================================
        # LOAD DATASET
        # ====================================================

        df = load_dataset()

        if df is None:

            return "Unable to load the Superstore dataset."


        # ====================================================
        # CLEAN NUMERIC COLUMNS
        # ====================================================

        df["Sales"] = pd.to_numeric(
            df["Sales"],
            errors="coerce"
        ).fillna(0)

        df["Profit"] = pd.to_numeric(
            df["Profit"],
            errors="coerce"
        ).fillna(0)


        # ====================================================
        # BASIC BUSINESS METRICS
        # ====================================================

        total_sales = round(
            df["Sales"].sum(),
            2
        )

        total_profit = round(
            df["Profit"].sum(),
            2
        )

        total_orders = int(
            df["Order ID"]
            .dropna()
            .nunique()
        )


        # ====================================================
        # PROFIT MARGIN
        # ====================================================

        if total_sales != 0:

            profit_margin = round(
                (total_profit / total_sales) * 100,
                2
            )

        else:

            profit_margin = 0


        # ====================================================
        # SALES BY REGION
        # ====================================================

        sales_by_region = (
            df.groupby("Region")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
            .round(2)
            .to_dict()
        )


        # ====================================================
        # PROFIT BY REGION
        # ====================================================

        profit_by_region = (
            df.groupby("Region")["Profit"]
            .sum()
            .sort_values(
                ascending=False
            )
            .round(2)
            .to_dict()
        )


        # ====================================================
        # SALES BY CATEGORY
        # ====================================================

        sales_by_category = (
            df.groupby("Category")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
            .round(2)
            .to_dict()
        )


        # ====================================================
        # PROFIT BY CATEGORY
        # ====================================================

        profit_by_category = (
            df.groupby("Category")["Profit"]
            .sum()
            .sort_values(
                ascending=False
            )
            .round(2)
            .to_dict()
        )


        # ====================================================
        # TOP PRODUCTS BY SALES
        # ====================================================

        top_products_sales = (
            df.groupby("Product Name")["Sales"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(10)
            .round(2)
            .to_dict()
        )


        # ====================================================
        # TOP PRODUCTS BY PROFIT
        # ====================================================

        top_products_profit = (
            df.groupby("Product Name")["Profit"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(10)
            .round(2)
            .to_dict()
        )


        # ====================================================
        # MONTHLY SALES
        # ====================================================

        df["Order Date"] = pd.to_datetime(
            df["Order Date"],
            errors="coerce"
        )

        valid_dates = df.dropna(
            subset=["Order Date"]
        ).copy()

        valid_dates["Month"] = (
            valid_dates["Order Date"]
            .dt.to_period("M")
            .astype(str)
        )

        monthly_sales = (
            valid_dates
            .groupby("Month")["Sales"]
            .sum()
            .round(2)
            .to_dict()
        )


        # ====================================================
        # MONTHLY PROFIT
        # ====================================================

        monthly_profit = (
            valid_dates
            .groupby("Month")["Profit"]
            .sum()
            .round(2)
            .to_dict()
        )


        # ====================================================
        # BEST REGION
        # ====================================================

        best_sales_region = (
            max(
                sales_by_region,
                key=sales_by_region.get
            )
            if sales_by_region
            else "Unknown"
        )


        best_profit_region = (
            max(
                profit_by_region,
                key=profit_by_region.get
            )
            if profit_by_region
            else "Unknown"
        )


        # ====================================================
        # BEST CATEGORY
        # ====================================================

        best_sales_category = (
            max(
                sales_by_category,
                key=sales_by_category.get
            )
            if sales_by_category
            else "Unknown"
        )


        best_profit_category = (
            max(
                profit_by_category,
                key=profit_by_category.get
            )
            if profit_by_category
            else "Unknown"
        )


        # ====================================================
        # BUSINESS CONTEXT
        # ====================================================

        business_context = f"""
You are MetricMind, an enterprise Business Intelligence assistant.

IMPORTANT RULES:

1. Answer numerical questions ONLY using the supplied business data.
2. NEVER invent or guess a number.
3. If a value is not available in the supplied data, clearly say that it is not available.
4. Use the approved semantic metrics whenever applicable.
5. Explain calculations briefly when useful.
6. Keep answers clear and business-friendly.
7. When comparing values, identify the highest and lowest where appropriate.

============================================================
APPROVED SEMANTIC METRICS
============================================================

{METRICS}

============================================================
OVERALL BUSINESS METRICS
============================================================

Total Sales : {total_sales}

Total Profit : {total_profit}

Total Orders : {total_orders}

Profit Margin : {profit_margin}%

============================================================
SALES BY REGION
============================================================

{sales_by_region}

============================================================
PROFIT BY REGION
============================================================

{profit_by_region}

============================================================
SALES BY CATEGORY
============================================================

{sales_by_category}

============================================================
PROFIT BY CATEGORY
============================================================

{profit_by_category}

============================================================
TOP 10 PRODUCTS BY SALES
============================================================

{top_products_sales}

============================================================
TOP 10 PRODUCTS BY PROFIT
============================================================

{top_products_profit}

============================================================
MONTHLY SALES
============================================================

{monthly_sales}

============================================================
MONTHLY PROFIT
============================================================

{monthly_profit}

============================================================
BUSINESS INSIGHTS
============================================================

Highest Sales Region : {best_sales_region}

Highest Profit Region : {best_profit_region}

Highest Sales Category : {best_sales_category}

Highest Profit Category : {best_profit_category}

============================================================
END BUSINESS CONTEXT
============================================================
"""


        # ====================================================
        # SEND TO LANGCHAIN AGENT
        # ====================================================

        answer = ask_agent(
            business_context,
            question
        )


        return answer


    except Exception as e:

        return f"Error: {e}"