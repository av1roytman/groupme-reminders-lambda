import json
import requests

def lambda_handler(event, context):
    # Your GroupMe bot ID
    bot_id = "b509b2b87ca46be9b0cddaaec6"

    # Parse the incoming event
    message_data = json.loads(event['body'])
    print(message_data)
    print(message_data.get('sender_type'))
    print(message_data.get('sender_id'))

    # Check if the sender is not the bot itself
    # Assuming the message data includes sender_type or sender_id
    if message_data.get('sender_type') != 'bot' and message_data.get('sender_id') != bot_id:
        # GroupMe API endpoint for posting messages
        groupme_post_message_url = "https://api.groupme.com/v3/bots/post"

        # Prepare the response message
        response_message = {
            "bot_id": bot_id,
            "text": "Hello"
        }

        # Send the message
        requests.post(groupme_post_message_url, json=response_message)

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }