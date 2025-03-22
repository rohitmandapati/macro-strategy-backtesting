import yfinance as yf
import pandas as pd
import os
import core.utils as utils

path = "data"

# Saves data of specified ticker into csv file
def get_stock_data(ticker: str, start:str ="2018-01-01", end:str="2024-12-31") -> str:
    data = yf.download(ticker, start, end, auto_adjust=True)
    filename = f"{path}/{ticker.lower()}.csv"
    data.to_csv(filename)
    
    #Fixes csv download issue from yfinance
    with open(filename, "+r") as file:
        lines = file.readlines()
        lines[0] = "Date,Close,High,Low,Open,Volume\n"
        lines[1] = ''
        lines[2] = ''
    with open(filename, "+w") as file:
        file.writelines(lines)
    
    
    print(f"Saved {ticker} to {filename}")
    return filename

# Loads data of specified ticker into pandas df
def load_stock_data(ticker:str):
    filename = get_stock_data(ticker=ticker)
    if not os.path.exists:
        raise FileNotFoundError(f"No data found for {ticker} at {filename}")
    else:
        df = pd.read_csv(filename, parse_dates=["Date"])
        df = df[["Date","Close"]].copy()
        
        #Calculates daily returns and adds column
        df = utils.calculate_daily_returns(df)
        
        return df
        
