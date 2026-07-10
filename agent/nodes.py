from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY, MODEL_NAME
from agent.prompts import SYSTEM_PROMPT
from agent.planner import create_plan
from tools import TOOLS

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

llm = llm.bind_tools(TOOLS)

def chatbot(state):
    plan = state.get("plan", {})

    messages = [
        SystemMessage(content=SYSTEM_PROMPT +
            f"\n\nExecution Plan:\n{plan}"),
        *state["messages"],
    ]

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }

def planner(state):
    user_message = state["messages"][-1].content

    plan = create_plan(user_message)
    print("=============================\n")
    print(plan)
    print("\n=============================\n")


    return {
        "plan": plan
    }