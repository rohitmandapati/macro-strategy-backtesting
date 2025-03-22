import pandas as pd

# File contains utility functions

def calculate_daily_returns(df):
    df["Returns"] = df["Close"].pct_change()
    return df