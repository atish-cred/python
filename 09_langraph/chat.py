# TypedDict for the state of the conversation
# Annotated is used to add metadata to the messages list, which can be used for validation or other purposes
# Import the add_messages function from the langgraph.graph.message module, which is used to add messages to the state
# START and END are the edges.

from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

# This function can call LLM model directly. No need to install openai or add extra code to call chatgpt
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
load_dotenv()


llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

# Keep adding the messages to the state so that we can keep track of the conversation history
# add_messages will contain user message first.
class State(TypedDict):
    messages: Annotated[list, add_messages] # click ctrl + mouse over add_messages to see the function signature and docstring


# Creating a node
def chatbot(state: State) :
    # Returning static message. Here you can call LLM
    print("Inside chatbot node", state)
    # return {"messages": ["Hi, This is a message from chatbot Node"]}

    response = llm.invoke(state.get("messages"))
    return {"messages":[response]}


def samplenode(state: State):
    print("Inside samplenode node", state)
    return{"messages": ["Sample message appended"]}


# Need to build state graph and pass state which is schema of the state graph
graph_builder = StateGraph(State)

# 1st param will be name of node and 2nd will be the function
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

# Create edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

# START -> chatbot -> samplenode -> END
# e.g START -> chatbot
# chatbot -> samplenode
# samplenode -> end


# After adding nodes and edges, Need to compile the graph
graph = graph_builder.compile()

# How to run? Need to invoke the graph, in invoke need to pass initial state
updated_state = graph.invoke(State({ "messages": ["Hi, My name is Atish Pawar"] }))
print("updated_state", updated_state)



# First calling  state then messages. firstime sate will you user_query,
# How it will add messages? because of Annotated list has add_messages
# state = { messages: ["Hey there"] }
# node runs: chatbot(State: ["Hey There"]) -> ["Hi, This is a message from chatbot node"]
# state = { messages: ["Hey There", "Hi, This is a message from chatbot node"] }

