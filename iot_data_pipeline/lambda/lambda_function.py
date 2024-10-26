import json
import os
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE_NAME']
table = dynamodb.Table(table_name)

def handler(event, context):
    # GraphQL mutasyonundan gelen verileri al
    data = json.loads(event['arguments']['input'])
    
    device_id = data['deviceId']
    temperature = data['temperature']
    humidity = data['humidity']
    timestamp = datetime.utcnow().isoformat()
    a=5

    # DynamoDB'ye veriyi kaydet
    table.put_item(
        Item={
            'deviceId': device_id,
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'deviceId': device_id,
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity
        })
    }
