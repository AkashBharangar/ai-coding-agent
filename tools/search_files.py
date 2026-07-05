from pathlib import Path
from langchain_core.tools import tool

@tool
def search_files(keyword: str, directory: str = "workspace") -> str:
    """
    Search for filename containing a keyword
    """

    try:
        matches = []
        for path in Path(directory).rglob("*"):
            if keyword.lower() in path.name.lower():
                matches.append(str(path))

        if not matches:
            return f"No file found"
        
        return "\n".join(matches)
    
    except Exception as e:
        return str(e)