terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = var.region
  access_key                  = "mock"
  secret_key                  = "mock"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3       = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
    sqs      = "http://localhost:4566"
    lambda   = "http://localhost:4566"
    iam      = "http://localhost:4566"
  }
}

# -----------------------------
# IAM Role
# -----------------------------
resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda-exec-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  name = "lambda-basic-policy"
  role = aws_iam_role.lambda_exec_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:*",
          "s3:*",
          "sqs:*",
          "dynamodb:*"
        ]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}

# -----------------------------
# S3
# -----------------------------
resource "aws_s3_bucket" "trade_bucket" {
  bucket = "trade-data-bucket"
}

# -----------------------------
# DynamoDB
# -----------------------------
resource "aws_dynamodb_table" "orders" {
  name         = "orders"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "order_id"

  attribute {
    name = "order_id"
    type = "S"
  }
}

# -----------------------------
# SQS
# -----------------------------
resource "aws_sqs_queue" "trade_queue" {
  name = "trade-queue"
}

# -----------------------------
# Lambda
# -----------------------------

resource "aws_lambda_function" "all" {
  for_each      = var.lambdas
  function_name = each.key
  filename      = "../../dist/${each.key}.zip"
  handler       = each.value
  runtime       = "python3.11"
  role          = aws_iam_role.lambda_exec.arn
  source_code_hash = filebase64sha256("${path.module}/lambda/lambda_payload.zip")
}
