# trading/simulation/backtest_engine.py
from typing import Callable, Dict
import pandas as pd
from trading.simulation.portfolio import Portfolio

class BacktestEngine:
    def __init__(self, portfolio: Portfolio, strategy: Callable, data: pd.DataFrame):
        self.portfolio = portfolio
        self.strategy = strategy
        self.data = data
        self.trade_log = []
    def run(self):
        for idx, row in self.data.iterrows():
            current_prices = {symbol: row[symbol] for symbol in row.index}  # 各シンボルの価格
            signals = self.strategy(row, self.portfolio)  # 戦略から売買シグナル取得

            for symbol, action in signals.items():
                if action['type'] == 'buy':
                    self.portfolio.buy(symbol, action['qty'], current_prices[symbol])
                elif action['type'] == 'sell':
                    self.portfolio.sell(symbol, action['qty'], current_prices[symbol])

            self.trade_log.append({
                'date': row.name,
                'portfolio_value': self.portfolio.calculate_value(current_prices)
            })
    def report(self):
        total_return = self.trade_log[-1]['portfolio_value'] - self.portfolio.history[0]['price'] if self.trade_log else 0
        return {
            'final_portfolio_value': self.trade_log[-1]['portfolio_value'] if self.trade_log else 0,
            'total_return': total_return,
            'trades': self.portfolio.history
        }
