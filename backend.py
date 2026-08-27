import os
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv


load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

graph = StateGraph(ChatState)

def chat_node_fxn(state: ChatState):
    quary = state["messages"]
    response = llm.invoke(quary)
    return {"messages": [response]}


graph.add_node("chat_node", chat_node_fxn)
graph.add_edge(START, "chat_node")
graph.add_edge('chat_node', END)


chatBot = graph.compile(checkpointer=InMemorySaver())

