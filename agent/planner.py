import json
import re

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from agent.planner_prompt import PLANNER_PROMPT
from utils.config import GROQ_API_KEY, MODEL_NAME


planner_llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0,
)


def extract_json(text: str):
    """
    Extract the first JSON object from an LLM response.
    """

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        return None

    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return None


def create_plan(user_input: str):
    """
    Generate a structured execution plan for the user's request.
    """

    response = planner_llm.invoke(
        [
            SystemMessage(content=PLANNER_PROMPT),
            HumanMessage(content=user_input),
        ]
    )

    plan = extract_json(response.content)

    if plan:
        return plan

    return {
        "goal": user_input,
        "steps": [
            "Understand the request",
            "Use appropriate tools if required",
            "Provide the final answer",
        ],
    }