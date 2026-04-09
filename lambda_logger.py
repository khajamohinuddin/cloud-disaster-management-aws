import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DisasterEvents')

def lambda_handler(event, context):
    try:
        item = {
            "event_id": event.get("event_id"),
            "disaster_type": event.get("disaster_type"),
            "region": event.get("region"),
            "severity": event.get("severity"),
            "timestamp": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps("Event stored successfully")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }
