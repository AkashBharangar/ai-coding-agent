from langchain_core.tools import tool
from pathlib import Path

@tool
def create_file(file_path: str, content: str):
    """Create a new file"""

    try:
        path = Path(file_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            content,
            encoding="utf8"
        )

        return "File created successfully"
    
    except Exception as e:
        return str(e)