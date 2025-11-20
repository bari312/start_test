# scripts/invoke_lambda_local.py
from lambda_handlers.my_lambda import lambda_handler

# モックイベント（Lambda に渡す入力データ）
event = {
    "action": "buy",
    "symbol": "BTC",
    "qty": 1,
    "price": 50000
}

# モックコンテキスト（必要なら）
class Context:
    function_name = "my_lambda"
    memory_limit_in_mb = 128
    def get_remaining_time_in_millis(self):
        return 300000

context = Context()
# Lambda ハンドラを直接呼ぶ
result = lambda_handler(event, context)

print("Lambda result:", result)
