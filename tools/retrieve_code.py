from langchain_core.tools import tool
from rag.retriever import retrieve

@tool
def retrieve_code(query: str) -> str:
    """
    Use this tool to semantically search the indexed codebase.

    Best for:

    - explaining how features work
    - locating business logic
    - finding relevant code

    Do NOT use for reading entire files.
    """

    docs = retrieve(query)
    context = []

    for doc in docs:
        context.append(
            f"File {doc.metadata['source']} \n {doc.page_content}"
        )

    return "\n\n ------------------------------- \n\n".join(context)