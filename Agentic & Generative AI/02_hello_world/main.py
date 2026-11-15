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

