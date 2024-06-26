# AWS EC2 Restart Lambda Function

This project demonstrates how to set up an AWS Lambda function that gets triggered by a Sumo Logic alert to restart an EC2 instance and send a notification via SNS.

## Project Structure

- `lambda/`: Contains the Lambda function code and deployment package.
- `terraform/`: Contains Terraform scripts to deploy the infrastructure.
- `sumo_logic/`: Contains the Sumo Logic query.
- `tests/`: Contains test events and instructions for testing the Lambda function.

## Setup Instructions

### Prerequisites

- AWS CLI
- Terraform
- Python (for Lambda function development)

### Deploying the Infrastructure

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/aws-ec2-restart-lambda.git
    cd aws-ec2-restart-lambda
    ```

2. **Create the Lambda deployment package**:
    ```sh
    cd lambda
    zip function.zip lambda_function.py
    cd ..
    ```

3. **Initialize and deploy Terraform scripts**:
    ```sh
    cd terraform
    terraform init
    terraform apply
    ```

4. **Sumo Logic Setup**:
    - Use the query in `sumo_logic/query.txt` to create an alert in Sumo Logic.

### Testing the Lambda Function

- Follow the instructions in `tests/test_instructions.md` to test the Lambda function manually.

## Files

### lambda/lambda_function.py

This file contains the code for the Lambda function.

### terraform/main.tf

This file contains the main Terraform configuration.

### sumo_logic/query.txt

This file contains the Sumo Logic query to detect high response times.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
