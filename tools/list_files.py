from langchain_core.tools import tool
from pathlib import Path

@tool
def list_files(directory: str = "workspace") -> str:
    """
    List all files recursively in the directory.
    """
    print("list_files tool running")
    try:
        files = []

        for path in Path(directory).rglob("*"):
            if path.is_file:
                files.append(str(path))

        if not files:
            return "No files found"
        print(files)
        print("\n".join(files))
        return "\n".join(files)
    
    except Exception as e:
        return str(e)