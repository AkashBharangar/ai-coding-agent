from typing import TypedDict
from typing_extensions import Annotated

from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]