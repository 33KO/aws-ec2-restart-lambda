import boto3
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize clients
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

# Define the EC2 instance ID and SNS topic ARN
EC2_INSTANCE_ID = 'i-0123456789abcdef0'
SNS_TOPIC_ARN = 'arn:aws:sns:us-west-2:123456789012:MySNSTopic'

def lambda_handler(event, context):
    # Restart the EC2 instance
    try:
        ec2_client.reboot_instances(InstanceIds=[EC2_INSTANCE_ID])
        logger.info(f'Successfully rebooted EC2 instance {EC2_INSTANCE_ID}')
    except Exception as e:
        logger.error(f'Error rebooting EC2 instance: {str(e)}')
        raise e
    
    # Log the action
    log_message = f'Rebooted EC2 instance {EC2_INSTANCE_ID} at {context.aws_request_id}'
    logger.info(log_message)
    
    # Send a notification to the SNS topic
    try:
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=log_message,
            Subject='EC2 Instance Reboot Notification'
        )
        logger.info(f'Successfully sent notification to SNS topic {SNS_TOPIC_ARN}')
    except Exception as e:
        logger.error(f'Error sending notification to SNS topic: {str(e)}')
        raise e

    return {
        'statusCode': 200,
        'body': log_message
    }
