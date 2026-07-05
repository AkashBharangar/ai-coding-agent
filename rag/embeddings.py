from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)