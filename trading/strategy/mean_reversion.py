# trading/strategy/mean_reversion.py
import pandas as pd
from trading.strategy.base import BaseStrategy

class MeanReversionStrategy(BaseStrategy):
    def __init__(self, window: int = 20, threshold: float = 0.02):
        self.window = window
        self.threshold = threshold

    def generate_signals(self, data: pd.DataFrame, portfolio):
        signals = {}
        for symbol in data.columns:
            price = data[symbol].iloc[-1]
            ma = data[symbol].rolling(self.window).mean().iloc[-1]
            diff = (price - ma) / ma
            if diff < -self.threshold:
                signals[symbol] = {"type": "buy", "qty": 1}
            elif diff > self.threshold:
                signals[symbol] = {"type": "sell", "qty": 1}
        return signals
