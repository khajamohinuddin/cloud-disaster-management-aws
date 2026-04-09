import json
import boto3
from datetime import datetime

sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:123456789012:DisasterAlerts"

def lambda_handler(event, context):
    try:
        disaster_type = event.get('disaster_type', 'Unknown')
        region = event.get('region', 'Unknown')
        severity = event.get('severity', 'Low')

        timestamp = datetime.utcnow().isoformat()

        message = {
            "disaster_type": disaster_type,
            "region": region,
            "severity": severity,
            "timestamp": timestamp,
            "status": "ACTIVE"
        }

        # Publish alert to SNS
        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=json.dumps(message),
            Subject=f"🚨 {disaster_type} Alert in {region}"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Alert sent successfully",
                "sns_message_id": response['MessageId']
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }

















