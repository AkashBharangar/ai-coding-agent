from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0,
    api_key=GROQ_API_KEY
)

@tool
def debug_error(error_output: str):
    """Explain ternimal error and suggests fixes"""

    response = llm.invoke(
        [
            HumanMessage(
                content=f"""
                You are an expert programming assistant.
                Read the terminal output and 
                explain the error.
                Also suggests the fixes to fix the error
                Error:
                {error_output}
                """
            )
        ]
    )

    return response.content