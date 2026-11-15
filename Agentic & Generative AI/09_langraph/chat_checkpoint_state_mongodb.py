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

from langgraph.checkpoint.mongodb import MongoDBSaver

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
    # print("Inside chatbot node", state)
    # return {"messages": ["Hi, This is a message from chatbot Node"]}

    response = llm.invoke(state.get("messages"))
    return {"messages":[response]}


# Need to build state graph and pass state which is schema of the state graph
graph_builder = StateGraph(State)

# 1st param will be name of node and 2nd will be the function
graph_builder.add_node("chatbot", chatbot)

# Create edges
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)


# After adding nodes and edges, Need to compile the graph
# graph = graph_builder.compile()

""" 
## It is not working

def compile_graph_with_checkpointer():
    # langgraph is database name is given, we can give anything it will create new
    DB_URL = 'mongodb://admin:admin@localhost:27017'
    with MongoDBSaver.from_conn_string(DB_URL) as checkpointer:
        graph = graph_builder.compile(checkpointer=checkpointer)
    return graph


graph_with_checkpointer = compile_graph_with_checkpointer()

# whatever i invoke, you store at atish level
config = {
    "configurable": {
        "thread_id": "atish"
    }
}

# How to run? Need to invoke the graph, in invoke need to pass initial state
updated_state = graph_with_checkpointer.invoke(
    State({ "messages": ["Hi, My name is Atish Pawar"] }),
    config
)
print("updated_state", updated_state)
"""


def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)


DB_URL = 'mongodb://admin:admin@localhost:27017'
with MongoDBSaver.from_conn_string(DB_URL) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer)

    # whatever i invoke, you store at atish level
    config = {
        "configurable": {
            "thread_id": "atish" # it is unique id, which store all the information into mongodb
        }
    }

    # How to run? Need to invoke the graph, in invoke need to pass initial state
    # this is for invoking the checkpointer directly
    # updated_state = graph_with_checkpointer.invoke(
    #     # State({ "messages": ["Hi, My name is Atish Pawar"] }),
    #     State({ "messages": ["Hey, What is my name?"] }),
    #     config
    # )
    # print("\n\nupdated_state", updated_state)

    for chunk in graph_with_checkpointer.stream(
        # State({ "messages": ["Hey, What is my name?"] }),
        # State({ "messages": ["You know that I am learning langgraph"] }),
        State({ "messages": ["What am i learning?"] }),
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()





# Checkpointer (atish) = Hey, My name is Atish Pawar
# Run file/function --> return message will be --> how i can assist you
# close the terminal and try again 
# Run file/function --> return message will be --> Your name is atish, how i can assist you

