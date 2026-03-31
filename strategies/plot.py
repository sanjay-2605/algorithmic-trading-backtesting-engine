import matplotlib.pyplot as plt

def plot_equity_curve(portfolio):
    plt.figure(figsize=(10,5))
    plt.plot(portfolio['total'])
    plt.title("Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.show()
