import json
import requests

def lambda_handler(event, context):
    # Your GroupMe bot ID
    bot_id = "b509b2b87ca46be9b0cddaaec6"

    # Check if the sender is not the bot itself
    # Assuming the message data includes sender_type or sender_id
    if event['sender_id'] != bot_id:
        # GroupMe API endpoint for posting messages
        groupme_post_message_url = "https://api.groupme.com/v3/bots/post"

        # Prepare the response message
        response_message = {
            "bot_id": bot_id,
            "text": "Hello Cracka"
        }

        # Send the message
        requests.post(groupme_post_message_url, json=response_message)

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }