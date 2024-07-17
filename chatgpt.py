from openai import OpenAI
from extract import get_messages
from prepros import preprocess_text
import json

key = ""
client = OpenAI(api_key=key)

all_messages, _ = get_messages()

for message in all_messages:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=message,
    )
    with open('responses/gpt_responses.txt', 'a', encoding='utf-8') as f:
        f.write(response.choices[0].message.content)