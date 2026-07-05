from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter.from_language(
    language="python",
    chunk_size=800,
    chunk_overlap=100
)

def split_documents(documents):
    return splitter.split_documents(documents)