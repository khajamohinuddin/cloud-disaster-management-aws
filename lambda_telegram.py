import json
import requests

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

def lambda_handler(event, context):
    try:
        disaster = event.get("disaster_type")
        region = event.get("region")
        severity = event.get("severity")

        msg = f"🚨 ALERT!\n\nType: {disaster}\nRegion: {region}\nSeverity: {severity}"

        send_telegram_message(msg)

        return {
            "statusCode": 200,
            "body": json.dumps("Telegram alert sent")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }
