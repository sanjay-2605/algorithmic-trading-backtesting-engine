import pandas as pd

from strategies.moving_average import moving_average_strategy
from strategies.momentum import momentum_strategy
from strategies.mean_reversion import mean_reversion_strategy
from backtester.backtest import backtest
from utils.metrics import sharpe_ratio, max_drawdown
from utils.plot import plot_equity_curve

data = pd.read_csv("data/stock_data.csv", index_col=0, parse_dates=True)

# Choose strategy
signals = moving_average_strategy(data)
# signals = momentum_strategy(data)
# signals = mean_reversion_strategy(data)

portfolio, returns = backtest(signals)

print("Sharpe Ratio:", sharpe_ratio(returns))
print("Max Drawdown:", max_drawdown(portfolio))

plot_equity_curve(portfolio)
