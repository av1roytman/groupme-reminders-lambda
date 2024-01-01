import json
import requests
import random
import traceback
import os
import re

bot_id = os.environ['BOT_ID']
groupme_post_message_url = "https://api.groupme.com/v3/bots/post"

def send_message(message):
    response_message = {
        "bot_id": bot_id,
        "text": message
    }

    # Send the message
    requests.post(groupme_post_message_url, json=response_message)

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }