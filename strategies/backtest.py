import pandas as pd

def backtest(signals, initial_cash=10000):
    positions = pd.DataFrame(index=signals.index).fillna(0)
    positions['stock'] = signals['signal']

    portfolio = positions.multiply(signals['price'], axis=0)
    pos_diff = positions.diff()

    portfolio['cash'] = initial_cash - (pos_diff['stock'] * signals['price']).cumsum()
    portfolio['total'] = portfolio['cash'] + positions['stock'] * signals['price']

    returns = portfolio['total'].pct_change()

    return portfolio, returns
