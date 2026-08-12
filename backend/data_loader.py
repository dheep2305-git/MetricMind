import os
import pandas as pd


# ==========================================
# DATASET PATH
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "Superstore.csv"
)


# ==========================================
# LOAD DATASET
# ==========================================

def load_dataset():

    try:

        # --------------------------------------
        # CHECK DATASET EXISTS
        # --------------------------------------

        if not os.path.exists(DATASET_PATH):

            print("Dataset not found:")
            print(DATASET_PATH)

            return None


        # --------------------------------------
        # READ CSV
        # --------------------------------------

        try:

            df = pd.read_csv(
                DATASET_PATH,
                encoding="utf-8"
            )

        except UnicodeDecodeError:

            # Try Latin-1 if UTF-8 fails

            df = pd.read_csv(
                DATASET_PATH,
                encoding="latin-1"
            )


        # --------------------------------------
        # CLEAN COLUMN NAMES
        # --------------------------------------

        df.columns = (
            df.columns
            .astype(str)
            .str.strip()
        )


        # --------------------------------------
        # REMOVE COMPLETELY EMPTY ROWS
        # --------------------------------------

        df = df.dropna(
            how="all"
        )


        # --------------------------------------
        # CONVERT NUMERIC COLUMNS
        # --------------------------------------

        numeric_columns = [
            "Sales",
            "Profit",
            "Quantity",
            "Discount"
        ]

        for column in numeric_columns:

            if column in df.columns:

                df[column] = pd.to_numeric(
                    df[column],
                    errors="coerce"
                )


        # --------------------------------------
        # CHECK REQUIRED COLUMNS
        # --------------------------------------

        required_columns = [
            "Sales",
            "Profit"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:

            print("WARNING: Required columns are missing:")
            print(missing_columns)


        # --------------------------------------
        # DATASET INFORMATION
        # --------------------------------------

        print("===================================")
        print("DATASET LOADED")
        print("===================================")

        print("File:", DATASET_PATH)
        print("Rows:", len(df))
        print("Columns:", len(df.columns))

        print("Columns:")
        print(list(df.columns))

        print("===================================")


        # --------------------------------------
        # PROFIT CHECK
        # --------------------------------------

        if "Profit" in df.columns:

            print("Profit column type:")
            print(df["Profit"].dtype)

            print("Missing Profit values:")
            print(df["Profit"].isna().sum())

            print("Total Profit:")
            print(df["Profit"].sum())

            print("===================================")


        # --------------------------------------
        # SALES CHECK
        # --------------------------------------

        if "Sales" in df.columns:

            print("Sales column type:")
            print(df["Sales"].dtype)

            print("Missing Sales values:")
            print(df["Sales"].isna().sum())

            print("Total Sales:")
            print(df["Sales"].sum())

            print("===================================")


        # --------------------------------------
        # RETURN DATAFRAME
        # --------------------------------------

        return df


    except Exception as e:

        print(
            "Dataset loading error:",
            e
        )

        return None