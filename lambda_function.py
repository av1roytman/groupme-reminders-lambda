import json
import requests
import os
import boto3
import datetime

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

    # Get current date
    today = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

    # Print all reminders
    for reminder in reminders:
        # If eventDate is today (only compare year, month, and day, not hours and minutes), send message
        if reminder['eventDate'][:10] == today[:10]:
            extractedHourMinute = reminder['eventTime'][11:16]
            convertToEnglish = datetime.datetime.strptime(extractedHourMinute, "%H:%M").strftime("%I:%M %p")
            send_message('Reminder: ' + reminder['eventName'] + ' at ' + convertToEnglish)
    

    return {
        'reminders': reminders,
        'statusCode': 200,
        'body': json.dumps('OK')
    }