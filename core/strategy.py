import pandas as pd

# Stores logic for various trading algorithms

# Implements a basic moving average crossover strategy. Defines
# control signals, 1 meaning buy and 0 meaning no position.
def moving_average_crossover(df:pd.DataFrame, short_window=20, long_window=50) -> pd.DataFrame:
    df = df.copy()
    df["SMA Short"] = df["Close"].rolling(window=short_window).mean()
    df["SMA Long"] = df["Close"].rolling(window=long_window).mean()
    
    df["Signal"] = 0
    for i in range(short_window, len(df)):
        df["Signal"][i] = (
            df["SMA Short"][i] > df["SMA Long"][i]
        ).astype(int)
    df = compute_strategy_returns(df)
    return df

def compute_strategy_returns(df): 
    df = df.copy()
    df["Strategy_Returns"] = df["Returns"] * df["Signal"]
    return df