variable "region" {
  description = "AWS region for LocalStack"
  default     = "us-east-1"
}

variable "lambdas" {
  type = map(string)        # マップ型を指定
  default = {
    lambda_logger = "lambda_logger.lambda_handler"
  }
}

