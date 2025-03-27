import matplotlib.pyplot as plt
import pandas as pd

# Plots price data of a ticker
def plot_price(df, ticker):
    plt.figure(figsize=(12, 5))
    plt.plot(df["Date"], df["Close"])
    plt.title(f"{ticker} Adjusted Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plots percent returns data of a ticker
def plot_returns(df, ticker):
    plt.figure(figsize=(12, 4))
    plt.plot(df["Date"], df["Returns"])
    plt.title(f"{ticker} Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plots price data of a ticker
def plot_strategy_returns(df, strategy:str):
    plt.figure(figsize=(12, 5))
    plt.plot(df["Date"], df["Strategy Returns"])
    plt.title(f"{strategy} Strategy Returns")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
# Function to plot custom information
def plot(df, ticker:str, col:str):
    plt.figure(figsize=(12, 5))
    plt.plot(df["Date"], df[col])
    plt.title(f"{ticker} {col}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
# Plots equity curves of strategy and holding, good for comparing strategy returns
def plot_equity_curve(df:pd.DataFrame, ticker):
    df = df.copy()
    df["Cumulative Market"] = (1 + df["Returns"]).cumprod()
    df["Cumulative Strategy"] = (1 + df["Strategy Returns"]).cumprod()

    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Cumulative Market"], label="Buy & Hold")
    plt.plot(df["Date"], df["Cumulative Strategy"], label="Strategy")
    plt.title(f"{ticker} Strategy vs Buy & Hold")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

