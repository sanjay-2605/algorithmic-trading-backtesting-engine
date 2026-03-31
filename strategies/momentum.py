import pandas as pd

def momentum_strategy(data, window=10):
    signals = pd.DataFrame(index=data.index)
    signals['price'] = data['Close']

    signals['momentum'] = data['Close'] - data['Close'].shift(window)
    signals['signal'] = 0
    signals.loc[window:, 'signal'] = (signals['momentum'][window:] > 0).astype(int)

    signals['positions'] = signals['signal'].diff()

    return signals
