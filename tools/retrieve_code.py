from langchain_core.tools import tool
from rag.retriever import retrieve

@tool
def retrieve_code(query: str) -> str:
    """
    Retrieve relevant code from the indexed codebase
    """

    docs = retrieve(query)
    context = []

    for doc in docs:
        context.append(
            f"File {doc.metadata['source']} \n {doc.page_content}"
        )

    return "\n\n ------------------------------- \n\n".join(context)