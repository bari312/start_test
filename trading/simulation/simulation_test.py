from trading.simulation.portfolio import Portfolio
from trading.simulation.backtest_engine import BacktestEngine
# staratgy import 下のbacktestenginのstrategyも合わせる
from trading.strategy.mean_reversion import MomentumStrategy 
from data.loader import load_csv_from_s3

# データ読み込み
data = load_csv_from_s3("my-bucket", "historical_ohlc.csv")

# ポートフォリオ初期化
portfolio = Portfolio(initial_cash=100000)

# バックテスト実行
engine = BacktestEngine(portfolio, MomentumStrategy, data)
engine.run()
results = engine.report()

print(results)
