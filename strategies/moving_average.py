import pandas as pd

def moving_average_strategy(data, short_window=20, long_window=50):
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']

    signals['short_ma'] = data['Close'].rolling(window=short_window).mean()
    signals['long_ma'] = data['Close'].rolling(window=long_window).mean()

    signals['signal'] = 0
    signals.loc[short_window:, 'signal'] = (
        signals['short_ma'][short_window:] > signals['long_ma'][short_window:]
    ).astype(int)

    signals['positions'] = signals['signal'].diff()

    return signals
