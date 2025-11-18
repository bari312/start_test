# config/settings.py

# 1. 環境フラグ
IS_LOCALSTACK = True  # TrueならLocalStackに接続、Falseなら本番AWSに接続
AWS_CONFIG = {
    "region": "ap-northeast-1",
    "dynamodb_endpoint": "http://localhost:4566" if USE_LOCALSTACK else None,
    "s3_endpoint": "http://localhost:4566" if USE_LOCALSTACK else None,
    "lambda_endpoint": "http://localhost:4566" if USE_LOCALSTACK else None,
    "sqs_endpoint": "http://localhost:4566" if USE_LOCALSTACK else None,
}
# 2. AWS共通設定
AWS_REGION = "ap-northeast-1"  # 東京リージョン
AWS_PROFILE = "default"         # AWS CLIのプロファイル名

# 3. リソース名の定義
LAMBDA_NAMES = {
    "logger": "lambda_logger",
    "trade": "tradeLambda"
}

S3_BUCKETS = {
    "data_bucket": "trade-data-bucket",
    "logs_bucket": "my-logs-bucket"
}

DYNAMODB_TABLES = {
    "orders": "orders"
    "trades": "trades_table"
}
