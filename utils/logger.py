# utils/logger.py
import logging
import os

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(os.environ.get('LOG_LEVEL', 'INFO').upper())

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        handler = logging.StreamHandler()  # Lambdaなら標準出力に
        handler.setFormatter(formatter)
        
    # Lambda なら AWS_LAMBDA_FUNCTION_NAME が環境変数に入っている
    if os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
        from logging import StreamHandler
        handler = StreamHandler()  # CloudWatch Logs に流す
    else:
        handler = RotatingFileHandler(
            "logs/app.log",
            maxBytes=1_000_000,
            backupCount=3
    
    return logger
