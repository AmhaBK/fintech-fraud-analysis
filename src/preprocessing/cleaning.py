import pandas as pd

def handle_missing_values(df, strategy="drop", fill_value=None):
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill":
        return df.fillna(fill_value)
    elif strategy == "median":
        return df.fillna(df.median(numeric_only=True))
    else:
        raise ValueError("Invalid strategy. Choose 'drop', 'fill', or 'median'.")

def remove_duplicates(df):
    return df.drop_duplicates()

def convert_to_datetime(df, cols):
    for col in cols:
        df[col] = pd.to_datetime(df[col])
    return df
