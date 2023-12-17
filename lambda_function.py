import json
import requests

def lambda_handler(event, context):
    # Your GroupMe bot ID
    bot_id = "b509b2b87ca46be9b0cddaaec6"

    # Check if the sender is not the bot itself
    # Assuming the message data includes sender_type or sender_id
    if event['sender_id'] != bot_id and event['sender_type'] != "bot":
        # GroupMe API endpoint for posting messages
        groupme_post_message_url = "https://api.groupme.com/v3/bots/post"

        message = "Hey Cracka!"

        if event['sender_id'] == "60388229":
            message = "Holy shit Omar. God Damn it. I cannot believe this shit. Shame, Shame, Shame on you. For thinking that anybody in this chat will \
                read any damn message you ever send. How can you be this fucking retarded???? Hit the gym, get bigger, never speak again."

        # Prepare the response message
        response_message = {
            "bot_id": bot_id,
            "text": message
        }

        # Send the message
        requests.post(groupme_post_message_url, json=response_message)

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }