from pathlib import Path
from langchain_core.tools import tool

@tool
def write_file(file_apth: str, content: str):
    """
    Write or overwrite the contents of the file
    """

    path = Path(file_apth)

    try:
        path.write_text(
            content,
            encoding="utf8"
        )

        return "File updated successfully"
    
    except Exception as e:
        return str(e)