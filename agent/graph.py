from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.prebuilt import ToolNode, tools_condition

from tools import TOOLS

from agent.state import AgentState
from agent.nodes import chatbot
from agent.nodes import planner


builder = StateGraph(AgentState)

builder.add_node("planner", planner)
builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(TOOLS))


builder.add_edge(START, "planner")
builder.add_edge("planner", "chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

builder.add_edge("tools", "chatbot")


graph = builder.compile()