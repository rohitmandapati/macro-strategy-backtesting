import pandas as pd

# File contains utility functions

def calculate_daily_returns(df) -> pd.DataFrame:
    df["Returns"] = df["Close"].pct_change()
    return df

# Computes returns for the strategy, based on signal and returns columns
def compute_strategy_returns(df) -> pd.DataFrame: 
    df = df.copy()
    for i in range(0, len(df)):
        df.loc[df.index[i], "Strategy Returns"] = float(df["Signal"][i]) * df["Returns"][i]
    return df

# Deprecated
def compute_total_strategy_returns(df) -> pd.DataFrame: 
    df = df.copy()
    sum = 0
    for i in range(0, len(df)):
        value = df["Strategy Returns"][i]
        if pd.notna(value):  # Only add if not NaN
            sum += value
        df.loc[df.index[i], "Total Strategy Returns"] = sum
    return df