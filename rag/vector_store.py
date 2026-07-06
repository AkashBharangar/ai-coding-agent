from langchain_community.vectorstores import FAISS
from rag.embeddings import embedding_model

def build_vector_store(documents):

    return FAISS.from_documents(
        documents,
        embedding_model,
        
    )