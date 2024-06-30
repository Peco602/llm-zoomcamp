import openai

from openai import OpenAI

prompt = "What's the formula for energy?"

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

response = client.chat.completions.create(
    model='gemma:2b',
    messages=[{"role": "user", "content": prompt}],
    temperature=0.0
)

answer = response.choices[0].message.content

completion_tokens = response.usage.completion_tokens

print(f"QUESTION: {prompt}")
print(f"ANSWER: {answer}")
print(f"COMPLETION TOKENS: {completion_tokens}")
