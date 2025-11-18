output "s3_bucket_name" {
  value = aws_s3_bucket.trade_bucket.bucket
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.orders.name
}

output "sqs_queue_url" {
  value = aws_sqs_queue.trade_queue.id
}

output "lambda_name" {
  lambda_logger  = "lambda_logger.lambda_handler"
}
