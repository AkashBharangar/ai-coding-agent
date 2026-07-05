from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY, MODEL_NAME
from agent.prompts import SYSTEM_PROMPT
from tools import TOOLS

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

llm = llm.bind_tools(TOOLS)

def chatbot(state):
    print("Entering chatbot")

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"],
    ]

    print("Calling LLM...")
    response = llm.invoke(messages)

    print("Content:", response.content)
    print("Tool calls:", response.tool_calls)

    return {
        "messages": [response]
    }