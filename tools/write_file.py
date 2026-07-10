from pathlib import Path
from langchain_core.tools import tool
from utils.path_utils import resolve_workspace_path

@tool
def write_file(file_path: str, content: str):
    """
    Write or overwrite the contents of the file
    """

    path = resolve_workspace_path(file_path)

    try:
        path.write_text(
            content,
            encoding="utf8"
        )

        return "File updated successfully"
    
    except Exception as e:
        return str(e)