import json
import requests
import random
from openai import OpenAI
import traceback
import re

bot_id = "b509b2b87ca46be9b0cddaaec6"
groupme_post_message_url = "https://api.groupme.com/v3/bots/post"
openai_api_key = "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"
omar_user_id = "60388229"

def generate_response_and_send_message(style_message, input_message):

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
                    "content": style_message,
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


    # Check if message contains "Luke Butt" using regex
    if event['sender_id'] != bot_id and event['sender_type'] != "bot":
        random_numer = random.randint(0, 10)

        if event['sender_id'] == omar_user_id:
            generate_response_and_send_message("You are a creative, imaginative, and rude old man named Uncle Sherwin.", \
                                               event['nickname'] + "is a realistic humanoid toy that is malfunctioning. Tell it to get rid of itself or to shut it off. Do this in a creative manner")

        elif re.search(r"luke butt", event['text'].lower()):
            generate_response_and_send_message("You are a creative and imaginative comedian that is slightly evil.", event['text'])

        # Check if the sender is not the bot itself
        # Assuming the message data includes sender_type or sender_id
        elif random_numer > 9:
            # GroupMe API endpoint for posting messages

            # Send the message
            generate_response_and_send_message("You are a creative and imaginative comedian that is slightly evil.", event['text'])

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }