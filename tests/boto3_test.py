import boto3
import os

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

s3.create_bucket(Bucket="my-test-bucket")
print(s3.list_buckets()) 
# {'Buckets': [{'Name': 'my-test-bucket', 'CreationDate': datetime.datetime(2024, 6, 1, 12, 0, tzinfo=tzutc())}], 'Owner': {'DisplayName': 'test', 'ID': 'test'}}

