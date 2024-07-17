import json
from extract import get_messages
from chatgpt import client as gptClient
from claude import client as claudeClient

with open('gpt_responses.txt', 'r', encoding='utf-8') as file:
        gpt_data = file.read()
with open('claude_responses.txt', 'r', encoding='utf-8') as file:
        claude_data = file.read()
        

gpt_resp = gpt_data.split('``````')
claude_resp = claude_data.split('``````')

main_prompts , main_resp = get_messages()

main_resp = [i for i in main_resp if i != '']

for gr, cr, p, mr in zip(gpt_resp, claude_resp, main_prompts, main_resp):
        eval_g = gptClient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"In an evaluation criteria of the following: *Accuracy: How correct and factual is the information provided by the model? *Coherence: How logically consistent and clear is the generated output? *Creativity: How innovative and original is the content produced? *Relevance: How relevant is the output to the given prompt? *Quality: Overall impression of the generated text, considering aspects like grammar, style, and readability. Evaluate the response generated from the AI model and the expected response with the criteria given with a score out of 10, based on the prompts that were given. The format of the response must be: prompt Title followed scores for each ai model out of 10 in each category and lastly print which model has better scores in the end and thats it. No justification or summary is required for the scores"},
                  {"role":"user","content":f"Prompt: {p}\n\n Generated Response from GPT model: {gr}\n\n Generated Response from Sonnet model: {cr}\n\n Expected Response: {mr}"}
                  ]
        )

        eval_c = claudeClient.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=500,
        system = "In an evaluation criteria of the following: *Accuracy: How correct and factual is the information provided by the model? *Coherence: How logically consistent and clear is the generated output? *Creativity: How innovative and original is the content produced? *Relevance: How relevant is the output to the given prompt? *Quality: Overall impression of the generated text, considering aspects like grammar, style, and readability. Evaluate the response generated from the AI model and the expected response with the criteria given with a score out of 10, based on the prompts that were given. The format of the response must be: prompt Title followed scores for each ai model out of 10 in each category and lastly print which model has better scores in the end and thats it. No justification or summary is required for the scores",
        messages=[{"role":"user","content":f"Prompt: {p}\n\n Generated Response from GPT model: {gr}\n\n Generated Response from Sonnet model: {cr}\n\n Expected Response: {mr}"}]
        )
        with open('scores/gpt_scores.txt', 'a', encoding='utf-8') as f:
                f.write(eval_g.choices[0].message.content)
                f.write('\n--------------------\n')

        with open('scores/claude_scores.txt', 'a', encoding='utf-8') as f:
                f.write(eval_c.content[0].text)
                f.write('\n--------------------\n')
        