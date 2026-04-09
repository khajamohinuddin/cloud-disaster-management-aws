import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    try:
        severity = event.get("severity")

        if severity == "High":
            # Simulate failover action
            response = ec2.describe_instances()

            return {
                "statusCode": 200,
                "body": json.dumps("Recovery process triggered: Failover initiated")
            }

        return {
            "statusCode": 200,
            "body": json.dumps("No recovery needed")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }
