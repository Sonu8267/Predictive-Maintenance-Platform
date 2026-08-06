def clean_data(df):
    """Remove empty columns."""
    df = df.dropna(axis=1, how="all")
    return df
