import pandas as pd
from config import DATASET_PATH

def load_dataset():
    data = pd.read_csv(DATASET_PATH)
    return data