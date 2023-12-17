import json
import requests
import random
from openai import OpenAI
import traceback

bot_id = "b509b2b87ca46be9b0cddaaec6"
groupme_post_message_url = "https://api.groupme.com/v3/bots/post"
openai_api_key = "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"

def generate_response_and_send_message(input_message):

    client = OpenAI(
        api_key = openai_api_key
    )

    try:
        message = "Hey Cracka!"

        # Generate a response using OpenAI
        chat_completion = client.chat.completions.create(
            messages= [
                {
                    "role": "system",
                    "content": "You are a creative and imaginative comedian."
                },
                {
                    "role": "user",
                    "content": input_message,
                }
            ],
            model="gpt-3.5-turbo-1106",
            max_tokens=150,
        )

        # Extract the text from the response
        message = chat_completion.choices[0].message.content

        # Prepare the response message
        response_message = {
            "bot_id": bot_id,
            "text": message
        }

        # Send the message
        requests.post(groupme_post_message_url, json=response_message)

    except Exception as e:
        print(f"Error generating response: {str(e)}")
        traceback.print_exc()
        message = "Sorry, I couldn't process that."


def lambda_handler(event, context):
    # Your GroupMe bot ID

    random_numer = random.randint(0, 10)

    # Check if the sender is not the bot itself
    # Assuming the message data includes sender_type or sender_id
    if event['sender_id'] != bot_id and event['sender_type'] != "bot" and random_numer > 9:
        # GroupMe API endpoint for posting messages

        # Send the message
        generate_response_and_send_message(event['text'])

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }