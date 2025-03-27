from core.data_loader import load_stock_data
from core.plotting import *
from core.strategy import *
from core.utils import *

# Loads stocks
df_aapl = load_stock_data("AAPL")
df_aapl = compute_strategy_returns(moving_average_crossover(df_aapl))

df_spy = load_stock_data("SPY")
df_spy = compute_strategy_returns(moving_average_crossover(df_spy))

plot_equity_curve(df_aapl, "AAPL")
plot_equity_curve(df_spy, "SPY")


