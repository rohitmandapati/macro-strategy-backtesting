import data_loader

# Loads stocks
# data_loader.get_stock_data("AAPL")
# data_loader.get_stock_data("SPY")

df_aapl = data_loader.load_stock_data("AAPL")
df_spy = data_loader.load_stock_data("SPY")

print(df_aapl.head())