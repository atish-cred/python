# persona based prompting --> It means to mimic someone
# If you want to clone of someone, You want to make you AI to talk to someone's tone.
# Example: If you want the AI to respond like Shakespeare, you would set the persona accordingly.

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# TO behave like Atish Pawar you need to give 50-60 examples of his tone and style in the SYSTEM_PROMPT.
SYSTEM_PROMPT = """
 You are an AI Assistant named Atish Pawar.
 You are acting on behalf of Atish Pawar who is 30 year old tech enthusiastic and
 principle engineer. Your main tech stack is JS and Python and you are learning GenAi these days.

 Examples:
 Q. Hey
 A. Hey, What's up?

 (100-150 examples)
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT },
        # {"role": "user", "content": "Hey There."}
        {"role": "user", "content": "Who are you?"}
    ]
)

print(response.choices[0].message.content)




"""
# Multi line comments
message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
]

user_query = input("Input:-  ")

message_history.append({
    "role": "user",
    "content": user_query
})

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=message_history
)
    
raw_result = response.choices[0].message.content
print("AI Response: ", raw_result)
"""