# trading/strategy/momentum.py
import pandas as pd
from trading.strategy.base import BaseStrategy

class MomentumStrategy(BaseStrategy):
    def __init__(self, window: int = 20):
        self.window = window

    def generate_signals(self, data: pd.DataFrame, portfolio):
        signals = {}
        for symbol in data.columns:
            price = data[symbol].iloc[-1]
            ma = data[symbol].rolling(self.window).mean().iloc[-1]
            if price > ma:
                signals[symbol] = {"type": "buy", "qty": 1}
            elif price < ma:
                signals[symbol] = {"type": "sell", "qty": 1}
        return signals
