# utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

        if os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
            # Lambda環境 → CloudWatch Logsに流す
            handler = logging.StreamHandler()
        else:
            # ローカル → ファイルに出力
            os.makedirs("logs", exist_ok=True)
            handler = RotatingFileHandler(
                "logs/app.log",
                maxBytes=1_000_000,
                backupCount=3
            )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

