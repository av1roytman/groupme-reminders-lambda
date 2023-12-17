import json
import requests
import random
from openai import OpenAI
import traceback

def lambda_handler(event, context):
    # Your GroupMe bot ID
    bot_id = "b509b2b87ca46be9b0cddaaec6"

    # Check if the sender is not the bot itself
    # Assuming the message data includes sender_type or sender_id
    if event['sender_id'] != bot_id and event['sender_type'] != "bot":
        # GroupMe API endpoint for posting messages
        groupme_post_message_url = "https://api.groupme.com/v3/bots/post"

        message = "Hey Cracka!"

        client = OpenAI(
            api_key = "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"
        )

        try:
            # Generate a response using OpenAI
            print("I got here")
            chat_completion = client.chat.completions.create(
                messages= [
                    {
                        "role": "system",
                        "content": "You are a creative and imaginative comedian."
                    },
                    {
                        "role": "user",
                        "content": event['text'],
                    }
                ],
                model="gpt-3.5-turbo-1106",
                max_tokens=150,
            )
            print("I got here too")

            print("response: ", chat_completion)

            # Extract the text from the response
            message = chat_completion.choices[0].message['content']

        except Exception as e:
            print(f"Error generating response: {str(e)}")
            traceback.print_exc()
            message = "Sorry, I couldn't process that."

        # Generate random number between 1 and 5
        # number = random.randint(1, 5)

        # if event['sender_id'] == "60388229" and number == 3:
        #     message = "Holy shit Omar. God Damn it. I cannot believe this shit. Shame, Shame, Shame on you. For thinking that anybody in this chat will read any damn message you ever send. How can you be this fucking retarded???? Hit the gym, get bigger, never speak again."

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