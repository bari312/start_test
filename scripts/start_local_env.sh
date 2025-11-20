#!/bin/bash
set -e  # エラーが発生したら停止
echo "Starting LocalStack environment..."
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_REGION=us-east-1
docker-compose up -d
echo "Waiting for LocalStack services to be ready..."
sleep 5  # サービスが立ち上がるまで少し待つ
echo "LocalStack environment started!"
