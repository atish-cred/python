from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Create .env file --> add below line
# OPENAI_API_KEY=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

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Hey There"
        }
    ]
)

print(response.choices[0].message.content)

