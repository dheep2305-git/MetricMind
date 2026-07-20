import pandas as pd
from config import DATASET_PATH

def load_dataset():
    try:
        data = pd.read_csv(DATASET_PATH)
        return data
    except FileNotFoundError:
        print("Dataset not found.")
        return None