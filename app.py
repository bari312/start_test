# app.py
from data.loader import PriceLoader
from trading.strategy.mean_reversion import MeanReversionStrategy
from trading.executor.order_executor import OrderExecutor
from trading.executor.risk_manager import RiskManager

def main():
    # ① 価格データの取得
    loader = PriceLoader()
    prices = loader.get_latest_prices(["BTC", "ETH"])

    # ② 戦略のインスタンス化
    strategy = MeanReversionStrategy()

    # ③ 戦略シグナル生成
    signals = strategy.generate(prices)

    # ④ リスク管理
    risk = RiskManager()
    filtered_signals = risk.filter(signals)

    # ⑤ 注文発行
    executor = OrderExecutor()
    executor.send(filtered_signals)

if __name__ == "__main__":
    main()
