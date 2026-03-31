import numpy as np

def sharpe_ratio(returns):
    return np.sqrt(252) * returns.mean() / returns.std()

def max_drawdown(portfolio):
    cumulative = portfolio['total']
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()
