from langchain_community.vectorstores import FAISS
from rag.embeddings import embedding_model

vector_store = FAISS.load_local(
    "faiss-index",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever(
    search_kwargs={
        "k":5
    }
)

def retrieve(query):
    docs = retriever.invoke(query)
    return docs