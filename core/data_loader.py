import yfinance as yf

def get_stock_data(ticker: str, start:str ="2018-01-01", end:str="2024-12-31"):
    data = yf.download(ticker, start, end)
    filename = f"data/{ticker.lower()}.csv"
    data.to_csv(filename)
    print(f"Saved {ticker} to {filename}")

