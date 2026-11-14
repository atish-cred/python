from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="AQ.Ab8RN6LtVOAyg2rLdj1isFCRZksP_dCQdkcHMwaY9SdOH4fbQQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"    
)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message.content)

