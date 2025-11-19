from portfolio import Portfolio


ini_cash = Portfolio(10000)
print(ini_cash.history)
ini_cash.buy("AAPL", 10, 150)
ini_cash.buy("GOOGL", 5, 1000)
ini_cash.sell("AAPL", 5, 160)
print(ini_cash.summary())
