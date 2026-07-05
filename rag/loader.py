from langchain_core.documents import Document

from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".md",
    ".json",
    ".yaml",
    ".yml",
}

def load_codebase(directory = "workspace"):
    documents = []

    for path in Path(directory).rglob("*"):
        if path.is_file:
            if (
                path.suffix in SUPPORTED_EXTENSIONS
                or path.name in ["Dockerfile", "requirements.txt"]
            ):
                try:
                    content = path.read_text(encoding="utf-8")
                    documents.append(
                        Document(
                            page_content=content,
                            metadata = {
                                "source" : str(path)
                            }
                        )
                    )
                except Exception as e:
                    print(f"Cannot read {path}: e")
    return documents
