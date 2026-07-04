from langgraph.graph import StateGraph
from langgraph.graph import START,END

from agent.nodes import chatbot
from agent.state import AgentState

builder = StateGraph(AgentState)

builder.add_node("chatbot", chatbot)

builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()