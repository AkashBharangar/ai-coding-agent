from pathlib import Path
from langchain_core.tools import tool
from utils.path_utils import resolve_workspace_path

@tool
def delete_file(file_path: str):
    """Deletes a file"""

    try:
        path = resolve_workspace_path(file_path)

        if not path.exists:
            return "File not found"
        

        path.unlink()

        return "File deleted successfully"
    
    except Exception as e:
        return str(e)