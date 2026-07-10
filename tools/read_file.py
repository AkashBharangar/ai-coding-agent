from pathlib import Path
from langchain_core.tools import tool
from utils.path_utils import resolve_workspace_path

@tool
def read_file(file_path: str) -> str:
    """
    Read the complete contents of a specific file.

    Use only when the exact file path is already known.
    """

    try:
        path = resolve_workspace_path(file_path)

        if not path.exists():
            return f"File '{file_path}' doesn't exists"
        
        return path.read_text(encoding="utf-8")
    
    except Exception as e:
        return str(e)