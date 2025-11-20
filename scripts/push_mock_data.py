# scripts/push_mock_data.py
from config.aws_client import get_s3_client
from config.settings import AWS_CONFIG
import pandas as pd

s3 = get_s3_client()  # ← aws_client.py で共通化済み
bucket_name = AWS_CONFIG["S3_BUCKET"]

# データ作成
data = {
    "date": pd.date_range("2025-01-01", periods=10),
    "BTC": [50000 + i*100 for i in range(10)]
}
df = pd.DataFrame(data)
csv_file = "/tmp/mock_prices.csv"
df.to_csv(csv_file, index=False)

# S3 にアップロード
s3.put_object(Bucket=bucket_name, Key="historical_prices/mock_prices.csv", Body=open(csv_file, "rb"))
