import pandas as pd
from config import DATASET_PATH

def load_dataset():
    try:
        return pd.read_csv(DATASET_PATH)
    except Exception as e:
        return None