from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Zero shot prompting -->> The model will only answer coding related questions and will not answer anything else.
# Directly given instuction to the model. Just throw the instruction to model
# The model is given a direct question or task without prior examples.

SYSTEM_PROMPT = """
You should only and only answer the coding related questions.
Do not answer anything else. Your're name is Alexa. If user asked something other than coding, just say sorry and do not answer that.

"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user", 
            # "content": "Hey, Can you help me to solve a + b whole square?"
            # "content": "Hey, Can you please tell me a joke?"
            # "content": "Hey, Can you translate the word 'hello' to French?"
            "content": "Hey, Can you write a python program that prints hello?"
        }
    ]
)

print(response.choices[0].message.content)
# print(response)


