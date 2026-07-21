import pandas as pd

DATASET_PATH = "../data/raw/Superstore.csv"

def load_dataset():
    try:
        df = pd.read_csv(DATASET_PATH, encoding="latin-1")
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None