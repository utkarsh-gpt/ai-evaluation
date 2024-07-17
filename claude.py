from anthropic import Anthropic
import os
from extract import get_messages

api_key = ""
client = Anthropic(api_key=api_key)

all_messages, _ = get_messages()

for message in all_messages:
    if message[0]['role'] == 'system':
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=500,
            system = message[0]['content'],
            messages=message[1]
        )
    else:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=500,
            messages=message
        )
    with open('responses/claude_responses.txt', 'a', encoding='utf-8') as f:
        f.write(response.content[0].text)
        f.write('\n`````\n')
