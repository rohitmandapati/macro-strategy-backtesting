import pandas as pd

# File contains utility functions

def calculate_daily_returns(df) -> pd.DataFrame:
    df["Returns"] = df["Close"].pct_change()
    return df