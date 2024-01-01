import json
import requests
import random
import traceback
import os
import re
import boto3

bot_id = os.environ['BOT_ID']
table_name = os.environ['TABLE_NAME']
groupme_post_message_url = "https://api.groupme.com/v3/bots/post"

def send_message(message):
    response_message = {
        "bot_id": bot_id,
        "text": message
    }

    # Send the message
    requests.post(groupme_post_message_url, json=response_message)

def lambda_handler(event, context):
    # Get all reminders from dynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.scan()
    reminders = response['Items']

    # Print all reminders
    for reminder in reminders:
        print(reminder)
    

    return {
        'reminders': reminders,
        'statusCode': 200,
        'body': json.dumps('OK')
    }