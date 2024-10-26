import json
import os
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE_NAME']
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        # Gelen veriyi loglayın
        print("Received event: " + json.dumps(event))

        # Doğru anahtarı belirleyin. 'body' kullanıyorsanız:
        data = json.loads(event.get('body', '{}'))
        
        # Veri işlemleri
        device_id = data['deviceId']
        temperature = data['temperature']
        humidity = data['humidity']
        timestamp = datetime.utcnow().isoformat()

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

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal Server Error', 'error': str(e)})
        }