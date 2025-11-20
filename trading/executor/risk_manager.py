# trading/executor/risk_manager.py
class RiskManager:
    def __init__(self, max_position_per_symbol: float):
        self.max_position_per_symbol = max_position_per_symbol

    def check_order(self, portfolio, symbol, qty, price):
        # 現在ポジション + 注文数量が上限を超えていないか
        current_qty = portfolio.positions.get(symbol, {}).get('qty', 0)
        if current_qty + qty > self.max_position_per_symbol:
            return False
        # 現金不足チェック
        if portfolio.cash < qty * price:
            return False
        return True
