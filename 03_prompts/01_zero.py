# Zero short prompting -->> Giving the instructions to the model without any examples or demonstrations <<-- OR -->> Directly giving the instructions to the model without any examples or demonstrations.
# It is a technique where you provide the model with a task without any examples or demonstrations. 
# The model is expected to understand the task and generate an appropriate response based solely on the prompt.


from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Zero short prompting
SYSTEM_PROMPT = "You should only and only answer the coding related questions. Do not answer anything else. Your name is Alexa. If user asks something other than coding just say sorry."

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            # "content": "Can you help me to solve the a + b whole square?"
            # "content": "Can you tell me a joke?"
            # "content": "Can you translate the word 'hello' to Hindi?"
            "content": "Can you write a python code to print hello world?"
        }
    ]
)

print(response.choices[0].message.content)

