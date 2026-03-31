import pandas as pd

def mean_reversion_strategy(data, window=20):
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']

    rolling_mean = data['Close'].rolling(window=window).mean()

    signals['signal'] = 0
    signals.loc[window:, 'signal'] = (data['Close'][window:] < rolling_mean[window:]).astype(int)

    signals['positions'] = signals['signal'].diff()

    return signals
