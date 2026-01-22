import pandas as pd

def load_csv(file_path: str, target_column: str):
    df = pd.read_csv(file_path)

    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found.")

    return df
