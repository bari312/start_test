# trading/strategy/base.py
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def generate_signals(self, data, portfolio):
        """
        売買シグナルを生成する
        data: pd.DataFrame（過去価格など）
        portfolio: Portfolio インスタンス
        return: dict {symbol: {"type": "buy"/"sell", "qty": 数量}}
        """
        pass
