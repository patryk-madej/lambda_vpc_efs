import json
import boto3
import os

queue_url = os.environ.get('QUEUE_URL')

def lambda_handler(event, context):
    body = {
        "message": "Your function executed successfully!",
        "input": event
    }
    
    # test sqs
    try:
        client = boto3.client('sqs')
        response = client.send_message(QueueUrl=queue_url, MessageBody=str(body))
        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))
    except Exception as err:
        print(err)
    
    #  test efs
    try:
        f = open('/mnt/test/file.txt', 'a+')
        f.write(str(body))
        f.close()
        for root, dirs, files in os.walk('/mnt/test'):
            for filename in files:
                print('file:', filename)
    except Exception as err:
        print(err)


    return response
