from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        # system prompt -- is special instruction given to the model to set the behavior of the assistant
        {   "role": "system",
            # "content": "You are an expert in Maths and only and only answers maths related questions."
            "content": "You are an expert in Maths and only and only answers maths related questions. That if the query is not related to Maths. Just say sorry and do not answer the question."
        },
        {
            "role": "user",
            # "content": "Hey, I am Atish Pawar! Nice to meet you. Who are you?"
            # "content": "Can you code a python program that can print hello world?"
            "content": "Can you help me to solve the a + b whole square?"
        }
    ]
)

print(response.choices[0].message.content)

