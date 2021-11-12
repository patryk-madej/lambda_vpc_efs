import json
import os
import boto3

queue_url = os.environ.get('QUEUE_URL')
local_mount_path = os.environ.get('LOCAL_MOUNT_PATH')

def lambda_handler(event, context):
    print(event)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    #  test efs
    try:
        f = open(f'{local_mount_path}/file.txt', 'a+')
        f.write(str(body))
        f.close()
        for root, dirs, files in os.walk(local_mount_path):
            for filename in files:
                print('file:', filename)
    except Exception as err:
        print(err)



    response = {
        "statusCode": 200,
        "file": filename,
        "body": json.dumps(body)
    }

    return response