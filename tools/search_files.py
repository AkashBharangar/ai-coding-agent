from pathlib import Path
from langchain_core.tools import tool
from utils.path_utils import WORKSPACE_ROOT

@tool
def search_files(keyword: str, directory: str = "workspace") -> str:
    """
    Search filenames inside the workspace.

    Use when the user knows part of a filename but not its location.
    """

    try:
        matches = []
        for path in WORKSPACE_ROOT.rglob("*"):
            if keyword.lower() in path.name.lower():
                matches.append(str(path))

        if not matches:
            return f"No file found"
        
        return "\n".join(matches)
    
    except Exception as e:
        return str(e)