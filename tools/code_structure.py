from pathlib import Path

from langchain_core.tools import tool

from parser.ast_parser import parse_python


@tool
def code_structure(file_path: str):

    """
    Extract functions, classes and imports from a Python file.
    """

    path = Path(file_path)

    if not path.exists():
        return "File not found."

    code = path.read_text(encoding="utf8")

    return str(parse_python(code))