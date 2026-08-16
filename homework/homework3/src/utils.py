import pandas as pd

def parse_date_column(df, column):
    df = df.copy()

    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    return df
