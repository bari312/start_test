variable "region" {
  description = "AWS region for LocalStack"
  default     = "us-east-1"
}

variable "lambdas" {
  default = {
    log_lambda  = "log_lambda.lambda_handler"
    task_lambda = "task_lambda.lambda_handler"
  }
}