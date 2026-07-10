import ast

def parse_python(code: str):

    tree = ast.parse(code)

    result = {
        "functions": [],
        "classes": [],
        "imports": []
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            result["functions"].append(node.name)
        
        elif isinstance(node, ast.ClassDef):
            result["classes"].append(node.name)
        
        elif isinstance(node, ast.Import):
            for alias in node.names:
                result["imports"].append(alias.name)
        
        elif isinstance(node, ast.ImportFrom):
            result["imports"].append(node.module)

    return result