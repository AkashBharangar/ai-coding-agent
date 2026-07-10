from tree_sitter_language_pack import get_parser

parser = get_parser("python")


def traverse(node, result):
    if node.type == "function_definition":
        name = node.childe_by_field_name("name")
        if name:
            result["functions"].append(name.text.decode())

    elif node.type == "class_definition":
        name = node.childe_by_field_name("name")
        if name:
            result["classes"].append(name.text.decode())
    
    elif node.type == "import_statement":
        name = node.childe_by_field_name("name")
        if name:
            result["imports"].append(name.text.decode())

    for child in node.children:
        traverse(child, result)



def parse_tree_sitter(code):
    tree = parser.parse(bytes(code, "utf8"))

    result = {
        "functions": [],
        "classes": [],
        "imports": []
    }

    traverse(tree.root_node, result)