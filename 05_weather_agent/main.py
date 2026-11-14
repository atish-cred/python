from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
# load_dotenv()

client = OpenAI()

# def get_weather(location):
#     url = f"https://wttr.in/{location.lower()}?format=%C+%t"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return f"The weather in {location} is {response.text}"
#     else:
#         return "Could not fetch weather information."


def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    print(f">> {response.choices[0].message.content}")
    
main()
# print(get_weather("mumbai"))