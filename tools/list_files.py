from langchain_core.tools import tool
from pathlib import Path
from utils.path_utils import WORKSPACE_ROOT


@tool
def list_files(directory: str = "workspace") -> str:
    """
    List all files recursively in the directory.
    """
    print("list_files tool running")

    try:
        files = []

        target_path = WORKSPACE_ROOT / directory

        for path in target_path.rglob("*"):
            if path.is_file():
                files.append(str(path))

        if not files:
            return "No files found"

        print(files)
        print("\n".join(files))

        return "\n".join(files)

    except Exception as e:
        return str(e)