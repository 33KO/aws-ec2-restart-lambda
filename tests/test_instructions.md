# Testing the Lambda Function

To test the Lambda function manually, follow these steps:

1. Go to the AWS Lambda console.
2. Select the `RebootEC2Instance` function.
3. Click on the "Test" button.
4. Configure a new test event using the JSON in `lambda_test_event.json`.
5. Run the test and verify that the EC2 instance is rebooted and a notification is sent to the SNS topic.

You can also publish a message to the SNS topic from the AWS SNS console to trigger the Lambda function.
