# Define any outputs for the Terraform script
output "ec2_instance_id" {
  description = "The ID of the EC2 instance"
  value       = aws_instance.my_instance.id
}

output "sns_topic_arn" {
  description = "The ARN of the SNS topic"
  value       = aws_sns_topic.my_topic.arn
}

output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.reboot_ec2.function_name
}
