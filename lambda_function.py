import json
import requests

def lambda_handler(event, context):
    # GroupMe bot ID - replace with your bot's ID
    bot_id = "b509b2b87ca46be9b0cddaaec6"

    # GroupMe API endpoint for posting messages
    groupme_post_message_url = "https://api.groupme.com/v3/bots/post"

    # Prepare the message
    message = {
        "bot_id": bot_id,
        "text": "Hello"
    }

    # Send the message to the GroupMe chat
    response = requests.post(groupme_post_message_url, json=message)

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to GroupMe chat')
    }
