variable "region" {
  description = "AWS region for LocalStack"
  default     = "us-east-1"
}

variable "lambdas" {
  default = {
    lambda_logger  = "lambda_logger.lambda_handler"
  }
}