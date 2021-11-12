import json
import boto3
import os

queue_url = os.environ.get('QUEUE_URL')
local_mount_path = os.environ.get('LOCAL_MOUNT_PATH')


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
        response='no sqs'
        print(err)
        
    
    #  test efs
    try:
        f = open(f'{local_mount_path}/file.txt', 'a+')
        f.write(str(body))
        f.close()
        for root, dirs, files in os.walk(local_mount_path):
            for filename in files:
                print('file:', filename)
    except Exception as err:
        filename='no file'
        print(err)


    return 200, response, filename
