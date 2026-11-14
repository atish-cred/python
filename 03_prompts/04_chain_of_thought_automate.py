# Chain of Thought Prompting
# The model is encouraged to reason step by step before providing the final answer.
# It will think if your question has multiple answer and it will give more reliable response.
# Example:
# Q. What is the sum of the first 10 natural numbers?
# A. Code 1, code 2, code 3
# if code 3 is correct, then it will be used to compute the final answer.

from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()


SYSTEM_PROMPT = """
You are an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple ste
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly follow the given JSON output format.
- Only run one step at a time.
- The sequence of steps in START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to user).

Output JSON format:
{
    "step": "START" | "PLAN" | "OUTPUT",
    "content": "string"
}

Example:
START. Hey, Can you solve 2 + 3 * 5 / 10
PLAN: {
    "step": "PLAN",
    "content": "Seems like user is interested in maths problem"
}
PLAN: {
    "step": "PLAN",
    "content": "Looking at the problem, we should solve this using BODMAS Method"
}
PLAN: {
    "step": "PLAN",
    "content": "Yes, The BODMAS is correct thing to be done here"
}
PLAN: {
    "step": "PLAN",
    "content": "First we must multiply 3 and 5 as per BODMAS rule"
}
PLAN: {
    "step": "PLAN",
    "content": "Now the new equation is 2 + 15 / 10"
}
PLAN: {
    "step": "PLAN",
    "content": "Next, we should perform the division 15 / 10"
}

PLAN: {
    "step": "PLAN",
    "content": "Now the new equation is 2 + 1.5"
}

PLAN: {
    "step": "PLAN",
    "content": "Finally, we add 2 and 1.5 to get the result"
}

OUTPUT: {
    "step": "OUTPUT",
    "content": "The final answer is 3.5"
}

"""

print("\n\n\n\n")


message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
]

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
        print("-- ", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("** ", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("== ", parsed_result.get("content"))
        break;

print("\n\n\n\n")