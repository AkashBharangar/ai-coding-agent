from rag.loader import load_codebase
from rag.chunker import split_documents
from rag.vector_store import build_vector_store

print("Loading Files...")

documents = load_codebase()
print(f"Total {len(documents)} files were loaded")

chunks = split_documents(documents)
print(f"Total {len(chunks)} chunks were created")

vector_store = build_vector_store(chunks)

vector_store.save_local("faiss-index")
print("Index created Successfully")