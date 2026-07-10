from pathlib import Path
from langchain_core.tools import tool

@tool
def delete_file(file_path: str):
    """Deletes a file"""

    try:
        path = Path(file_path)

        if not path.exists:
            return "File not found"
        

        path.unlink()

        return "File deleted successfully"
    
    except Exception as e:
        return str(e)