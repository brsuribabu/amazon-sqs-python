import boto3

client = boto3.client('sqs')

response = client.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/918149105792/TEST-QUEUE-BOTO3'
)

print(response)