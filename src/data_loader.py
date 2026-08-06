import pandas as pd

def load_data(file_path):
    """Load the CMAPSS dataset."""
    return pd.read_csv(file_path, sep=r"\s+", header=None)
