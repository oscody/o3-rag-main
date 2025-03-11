from openai import OpenAI
# from rag_openai import search
from rag_openaiV2 import search

client = OpenAI()

user_input = 'Find notes on self-reflection'
context = search(user_input)
prompt_with_context = f"Context: {context}\n\nUser input: {user_input}"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt_with_context}],
)

print(response.choices[0].message.content)
