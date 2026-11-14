# Chain of Thought Prompting

from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

import requests
import json


load_dotenv(Path(__file__).resolve().parent.parent / ".env")
# load_dotenv()

client = OpenAI()

def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    else:
        return "Could not fetch weather information."


# Here we are creating the mapping for the tools.
available_tools = {
    "get_weather":get_weather
}


# in Output JSON format: TOOL added. it will call an external tool/function or API when needed.
# Some examples are given
# Tool is passed as a function here and given the idea/reference
SYSTEM_PROMPT = """
You are an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple ste
Once you think enough PLAN has been done, finally you can give an OUTPUT.
You can also call a tool if required from the list of available tools.
for every tool call wait for the OBSERVE step which is the output from the called tool.

Rules:
- Strictly follow the given JSON output format.
- Only run one step at a time.
- The sequence of steps in START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to user).

Output JSON format:
{
    "step": "START" | "PLAN" | "OUTPUT" | "TOOL",
    "content": "string",
    "tool": "string",
    "input": "string",
}

Available Tools:
- get_weather(city: str): Takes city name as an input string and returns the weather information for that city.


Example 1:
START. Hey, Can you solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN", "content": "Seems like user is interested in maths problem" }
PLAN: { "step": "PLAN", "content": "Looking at the problem, we should solve this using BODMAS Method" }
PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
PLAN: { "step": "PLAN", "content": "First we must multiply 3 and 5 as per BODMAS rule" }
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
PLAN: { "step": "PLAN", "content": "Next, we should perform the division 15 / 10" }
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
PLAN: { "step": "PLAN", "content": "Finally, we add 2 and 1.5 to get the result" }
OUTPUT: { "step": "OUTPUT", "content": "The final answer is 3.5" }

Example 2:
START. What is the weather of Delhi?
PLAN: { "step": "PLAN", "content": "Seems like user is interssted ing getting weather of Delhi in India." }
PLAN: { "step": "PLAN", "content": "Let's see if we have any available tool from the list of available tools." }
PLAN: { "step": "PLAN", "content": "Great, we have get_weather tool available for this query." }
PLAN: { "step": "PLAN", "content": "I need to call get_weather tool for delhi as input for city." }
PLAN: { "step": "TOOL", "tool": "get_weather", "input": "Delhi" }
PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The weather in Delhi is cloudy with 20 C." }
PLAN: { "step": "PLAN", "content": "Great, I got the weather information for Delhi." }
PLAN: { "step": "OUTPUT", "content": "The current weather in Delhi is cloudy with 20 C with some cloudy sky." }

"""

# print("\n")

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
]

# Outer loop is for continuously taking user input and processing it
# You can comment it out if you don't want continuous input loop
while True:
    user_query = input("Input:-  ")

    # First, append the user's query to the message history
    message_history.append({
        "role": "user",
        "content": user_query
    })

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=message_history
        )
        
        raw_result = response.choices[0].message.content
        message_history.append({
            "role": "assistant",
            "content": raw_result
        })

        # Loaded back into a Python dictionary from JSON string
        parsed_result = json.loads(raw_result)

        if parsed_result.get("step") == "START":
            print("-> ", parsed_result.get("content"))
            continue

        if parsed_result.get("step") == "PLAN":
            print("-->> ", parsed_result.get("content"))
            continue

        # if the tool called then you will get the "tool" as a property that is named as tool.
        if parsed_result.get("step") == "TOOL":

            # Below we used tool and input which are provided in SYSTEM_PROMPT
            tool_to_call = parsed_result.get("tool")
            tool_input = parsed_result.get("input")

            print(f"----: {tool_to_call} with input: {tool_input}")

            # Here we are calling mapping function.
            tool_response = available_tools[tool_to_call](tool_input)
            print(f"---- TOOL RESPONSE: {tool_response}")

            message_history.append({
                "role": "developer",
                "content": json.dumps({
                    "step": "OBSERVE",
                    "tool": tool_to_call,
                    "input": tool_input,
                    "output": tool_response
                })
            })

            continue

        if parsed_result.get("step") == "OBSERVE":
            print("-->>> OBSERVE: ", parsed_result.get("tool"), "output:", parsed_result.get("output"))
            continue

        if parsed_result.get("step") == "OUTPUT":
            print("-->>> ", parsed_result.get("content"))
            break;
            
    print("\n\n")