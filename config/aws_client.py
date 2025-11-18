# config/aws_client.py
import os
import boto3
from config.settings import AWS_CONFIG

def get_dynamodb_client():
    """
    LocalStack と 本番 AWS を自動で切り替える DynamoDB クライアントを返す
    """
    return boto3.client(
        "dynamodb",
        region_name=AWS_CONFIG["region"],
        endpoint_url=AWS_CONFIG["dynamodb_endpoint"]  # LocalStack の場合はここが http://localhost:4566
    )

def get_s3_client():
    """
    LocalStack と 本番 AWS を自動で切り替える S3 クライアントを返す
    """
    return boto3.client(
        "s3",
        region_name=AWS_CONFIG["region"],
        endpoint_url=AWS_CONFIG["s3_endpoint"]
    )
def get_lambda_client():
    """
    LocalStack と 本番 AWS を自動で切り替える Lambda クライアントを返す
    """
    return boto3.client(
        "lambda",
        region_name=AWS_CONFIG["region"],
        endpoint_url=AWS_CONFIG["lambda_endpoint"]
    )
def get_sqs_client():
    """
    LocalStack と 本番 AWS を自動で切り替える SQS クライアントを返す
    """
    return boto3.client(
        "sqs",
        region_name=AWS_CONFIG["region"],
        endpoint_url=AWS_CONFIG["sqs_endpoint"]
    )
