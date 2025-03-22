from core.data_loader import load_stock_data
from core.plotting import *
from core.strategy import *

# Loads stocks
df_aapl = load_stock_data("AAPL")

print(df_aapl.head())

# plot_price(df_aapl, "AAPL")
# plot_returns(df_aapl, "AAPL")

moving_average_crossover(df_aapl)

plot_strategy_returns(df_aapl, "AAPL, SMA")

print(df_aapl)
