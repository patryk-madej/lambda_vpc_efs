import json
import boto3
import os

queue_url = os.environ.get('QUEUE_URL')

def lambda_handler(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    

    client = boto3.client('sqs')
    response = client.send_message(QueueUrl=queue_url, MessageBody=str(body))
    
    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))


    return response
