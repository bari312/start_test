# trading/simulation/portfolio.py
from typing import Dict, List

class Portfolio:
    def __init__(self, initial_cash: float):
        self.cash = initial_cash                # 現金残高
        self.positions: Dict[str, Dict] = {}   # 銘柄ごとの保有数量と平均取得価格
        self.history: List[Dict] = []          # 売買履歴
    def buy(self, symbol: str, qty: float, price: float):
        cost = qty * price
        if self.cash < cost:
            raise ValueError("資金不足")
        self.cash -= cost
        
        if symbol in self.positions:
            # 平均取得価格を更新
            total_qty = self.positions[symbol]['qty'] + qty
            avg_price = (self.positions[symbol]['qty'] * self.positions[symbol]['avg_price'] + cost) / total_qty
            self.positions[symbol]['qty'] = total_qty
            self.positions[symbol]['avg_price'] = avg_price
        else:
            self.positions[symbol] = {'qty': qty, 'avg_price': price}
        
        # 売買履歴に記録
        self.history.append({'action': 'buy', 'symbol': symbol, 'qty': qty, 'price': price})
    def sell(self, symbol: str, qty: float, price: float):
        if symbol not in self.positions or self.positions[symbol]['qty'] < qty:
            raise ValueError("保有数量不足")
        
        self.positions[symbol]['qty'] -= qty
        self.cash += qty * price
        
        if self.positions[symbol]['qty'] == 0:
            del self.positions[symbol]
        
        # 売買履歴に記録
        self.history.append({'action': 'sell', 'symbol': symbol, 'qty': qty, 'price': price})
    def calculate_value(self, current_prices: Dict[str, float]):
        """保有ポジションの評価額＋現金で総資産を計算"""
        total_value = self.cash
        for symbol, pos in self.positions.items():
            total_value += pos['qty'] * current_prices.get(symbol, pos['avg_price'])
        return total_value
    def summary(self):
        return {
            'cash': self.cash,
            'positions': self.positions,
            'history': self.history
        }
