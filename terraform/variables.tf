# Define any variables needed for the Terraform script
variable "aws_region" {
  description = "The AWS region to deploy the resources in"
  type        = string
  default     = "us-west-2"
}
