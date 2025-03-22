import matplotlib.pyplot as plt

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

