from config.aws_client import get_s3_client
import json

def load_json_from_s3(bucket: str, key: str) -> dict:
    """S3 から JSON の価格データを取得"""
    s3 = get_s3_client()
    obj = s3.get_object(Bucket=bucket, Key=key)
    data = obj["Body"].read().decode("utf-8")
    return json.loads(data)


def load_csv_from_s3(bucket: str, key: str) -> list:
    """S3 から CSV（OHLCなど）を読み込む"""
    s3 = get_s3_client()
    obj = s3.get_object(Bucket=bucket, Key=key)
    csv_str = obj["Body"].read().decode("utf-8")
    rows = csv_str.splitlines()
    return [r.split(",") for r in rows]