import ast
import random
import string
import astor


name_map = {}  # to store the mapping between old and new names


def random_name(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def check_existence(value):
    global name_map
    if name_map.get(value):
        return name_map[value]
    else:
        _new_name = random_name()
        name_map[value] = _new_name
        return _new_name


def extract_and_replace_names(file_path):
    global name_map
    with open(file_path, 'r') as file:
        code = file.read()

    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, (ast.Store, ast.Load)):
                old_name = node.id
                new_name = check_existence(old_name)
                node.id = new_name
        elif isinstance(node, ast.FunctionDef):
            old_name = node.name
            new_name = check_existence(old_name)
            node.name = new_name
        elif isinstance(node, ast.ClassDef):
            old_name = node.name
            new_name = check_existence(old_name)
            node.name = new_name
    # use the `astor.to_source()` function to convert the AST to source code
    _new_code = astor.to_source(tree)
    return _new_code


def convert_back_to_original(_new_code, _name_map):
    for old_name, new_name in name_map.items():
        _new_code = _new_code.replace(new_name, old_name)
    return _new_code


if __name__ == '__main__':
    path = 'C:\Development\PythonHackStuff\ReverseShell2\ServerInControl\ServerInControl.py'
    new_code = extract_and_replace_names(path)
    open("new.py", "w").write(new_code)
    input()
    original_code = convert_back_to_original(new_code, name_map)
    open("new.py", "w").write(original_code)
