from langchain_core.messages import AIMessage

from groq import Groq

from agent.prompts import SYSTEM_PROMPT
from utils.config import GROQ_API_KEY, MODEL_NAME

client=Groq(api_key=GROQ_API_KEY)

def chatbot(state):
    messages=[
        {
            "role":"system",
            "content": SYSTEM_PROMPT 
        }
    ]

    role_map = {
    "human": "user",
    "ai": "assistant",
    "system": "system",
    "tool": "tool",
    }


    for msg in state["messages"]:
        messages.append(
            {
             "role": role_map[msg.type],
            "content": msg.content,
            }
        )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0
    )

    return {
        "messages": [
        AIMessage(content=response.choices[0].message.content)
        ]
    }

