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

response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey, Write a code to add n numbers in JS"
        },
        # Mannually keep adding messages history --> this is added from running the program. 
        # you need to run this program multiple times append the history in assistant messages.
        #

        {
            "role": "assistant",
            "content": json.dumps({"step": "START","content": "User is requesting a JavaScript code to add n numbers."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "To write a code for adding nnumbers, we can use a loop to iterate through the numbers. We need to decide on the method to collect the input numbers."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "We can use an array to hold the numbers and then use the reduce method or a simple forloop to calculate the sum."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "We should also consider how the user would provide these n numbers, possibly as user input or predefined in the code."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "Let's write a function that takes an array of numbers as input and returns their sum using the reduce method as it's a clean approach."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "The implementation could look something like this: function addNumbers(numbers) { return numbers.reduce((acc, num) => acc + num, 0); }."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "PLAN", "content": "We will also include a way to call this function with an example array to demonstrate how it works."})
        },
        {
            "role": "assistant",
            "content": json.dumps({"step": "OUTPUT", "content": "Here is a JavaScript code to add n numbers:\n\n```javascript\nfunction addNumbers(numbers) {\n    return numbers.reduce((acc, num) => acc + num, 0);\n}\n\n// Example usage:\nconst nums = [1, 2, 3, 4, 5];\nconsole.log(addNumbers(nums)); // Outputs: 15\n```"})
        },
        # {
        #     "role": "assistant",
        #     "content": json.dumps()
        # },

        # {
        #     "role": "assistant",
        #     "content": json.dumps(
        #         [
        #             {"step": "START", "content": "User is requesting a JavaScript code to add n numbers."},
        #             {"step": "PLAN", "content": "To write a code for adding nnumbers, we can use a loop to iterate through the numbers. We need to decide on the method to collect the input numbers."}
        #         ]
        #     )
        # }
    ]
)

print(response.choices[0].message.content)