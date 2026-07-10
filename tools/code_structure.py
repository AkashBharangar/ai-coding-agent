from pathlib import Path
from langchain_core.tools import tool

from parser.ast_parser import parse_python

@tool
def code_structure(file_path: str):

    """ Extrats functions, classes and imports from a Python File"""

    path = Path(file_path)

    if not path.exists():
        return f"File Not Found"
    
    code = path.read_text(encoding="utf-8")

    return str(parse_python(code))