import json

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

from utils.config import GROQ_API_KEY, MODEL_NAME
from agent.planner_prompt import PLANNER_PROMPT

planner_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

def create_plan(user_input: str):
    response = planner_llm.invoke([
        SystemMessage(content=PLANNER_PROMPT),
        HumanMessage(content=user_input)
    ])

    try:
        return json.loads(response.content)
    
    except Exception:
        return {
            "goal": user_input,
            "steps": []
        }