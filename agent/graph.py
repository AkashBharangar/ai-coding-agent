from langgraph.graph import StateGraph
from langgraph.graph import START, END
from langgraph.prebuilt import ToolNode, tools_condition

from tools import TOOLS

from agent.state import AgentState
from agent.nodes import chatbot

builder = StateGraph(AgentState)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(TOOLS))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()