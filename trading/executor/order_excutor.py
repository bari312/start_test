# trading/executor/order_executor.py
from config.aws_client import get_s3_client
import json
from config.settings import AWS_CONFIG

class OrderExecutor:
    def __init__(self):
        self.sqs = get_s3_client
        # 注文キューのURLを設定 (事前にSQSキューを作成しておく必要があります)
        self.queue_url = AWS_CONFIG["sqs_endpoint"] + "/000000000000/order_queue"

    def send_order(self, symbol, order_type, qty, price):
        message = {
            "symbol": symbol,
            "type": order_type,
            "qty": qty,
            "price": price
        }
        self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=json.dumps(message)
        )
