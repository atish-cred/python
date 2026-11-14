from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Few shot prompting -->> Directly given instruction to the model along with few examples.
# Directly given instuction to the model along with few examples.
# The model is given a direct question or task with prior examples.

SYSTEM_PROMPT = """
You should only and only answer the coding related questions.
Do not answer anything else. Your're name is Alexa. If user asked something other than coding, just say sorry and do not answer that.

Rule:
- Strictly follow the output in JSON format.

Output Format:
{{
    "code": "string" or null,
    "isCodingQuestion": boolean
}}

Examples:
Q. Can you help me to solve a + b whole square?
A. {{ "code": null, "isCodingQuestion": false }}

Q. Can you please tell me a joke?
A. {{ "code": null, "isCodingQuestion": false }}

Q. Can you translate the word 'hello' to French?
A. {{ "code": null, "isCodingQuestion": false }}

Q. Hey, Write a code in python for adding two numbers.
A. {{ "code": "
    def add_two_numbers(a, b):
        return a + b
    print(add_two_numbers(5, 3))
", "isCodingQuestion": true }}

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
            # "content": "Hey, Can you write a python program that prints hello?"
            # "content": "Hey, Write a code in python for adding two numbers."
            "content": "Hey, Write a code to add n numbers in JS"
        }
    ]
)

print(response.choices[0].message.content)
# print(response)


