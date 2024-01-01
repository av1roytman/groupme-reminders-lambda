import json
import requests
import os
import boto3
import datetime
import pytz

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
    est = pytz.timezone('US/Eastern')
    today = datetime.datetime.now(est).strftime("%Y-%m-%dT%H:%M")

    # Print all reminders
    for reminder in reminders:
        # If eventDate is today (only compare year, month, and day, not hours and minutes), send message
        print(reminder)
        print(reminder['eventDate'][:10])
        print(today[:10])
        if reminder['eventDate'][:10] == today[:10]:
            extractedHourMinute = reminder['eventDate'][11:16]
            print(extractedHourMinute)
            convertToEnglish = datetime.datetime.strptime(extractedHourMinute, "%H:%M").strftime("%I:%M %p")
            print(convertToEnglish)
            send_message('Reminder: ' + reminder['eventName'] + ' at ' + convertToEnglish)
    

    return {
        'reminders': reminders,
        'statusCode': 200,
        'body': json.dumps('OK')
    }