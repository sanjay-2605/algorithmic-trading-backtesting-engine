import yfinance as yf

data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
data.to_csv("data/stock_data.csv")

print("Stock data downloaded")
