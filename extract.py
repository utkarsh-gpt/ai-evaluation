import json
from prepros import preprocess_text

def extract_data(data):
    prompt = []
    response = []
    for item in data:
        prompt.append(item['prompt'])        
        response.append(str(item['response']))
    return prompt, response

def get_messages():
    with open('response.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    all_prompts, all_responses = extract_data(data)

    for i, item in enumerate(all_prompts):
        if type(item) != str:
            for content in item:
                content['content'] = preprocess_text(content['content'])
        else:
            all_prompts[i] = [{'role':'user','content':preprocess_text(item)}]

    return all_prompts, all_responses
