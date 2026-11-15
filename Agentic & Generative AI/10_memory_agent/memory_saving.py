from dotenv import load_dotenv
from mem0 import Memory
from openai import OpenAI

import os

load_dotenv()

client = OpenAI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v1.1",
    # This config for embedder - from openai, text to vector db embedding
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        }
    },
    # This config for which llm need to use
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4.1"
        }
    },
    # Where do you want to store this memory data?
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

# add all the config to setup the memory
# 1. version of memory config
# 2. Embedding config
# 3. openai or any other ai config
# 4. database config e.g. qdrant
mem_client = Memory.from_config(config)

while True :
    user_query = input("> ")

    response = client.chat.completions.create(
        model= "gpt-4.1-mini",
        messages= [
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content
    print("Ai", ai_response)


    # Need to store all the chat to the memory
    # This add method automatically add extracts, factual & semantic from messages and stored it.
    mem_client.add(
        user_id="atishpawar",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response},
        ]
    )

    print("Memory has been saved.")
