import pandas as pd

def get_dataset_preview(data, rows=5):
    return data.head(rows).to_dict(orient="records")