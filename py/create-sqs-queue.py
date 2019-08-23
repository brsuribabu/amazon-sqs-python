import boto3

client = boto3.client('sqs')

response = client.send_message(
    QueueUrl='string',
    MessageBody='string'
)