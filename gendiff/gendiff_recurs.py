import json

def generate_diff_recurs(path_file1, path_file2):
    with open(path_file1) as f1, open(path_file2) as f2:
        file1 = json.load(f1)
        file2 = json.load(f2)
    
    diff = build_diff(file1, file2)
    formatted_diff = render_stylish(diff)
    return '{\n' + formatted_diff + '\n}'

def build_diff(dict1, dict2):
    diff = {}
    all_keys = sorted(dict1.keys() | dict2.keys())
    for key in all_keys:
        if key in dict1 and key not in dict2:
            diff[key] = {"status": "removed", "value": dict1[key]}
        elif key not in dict1 and key in dict2:
            diff[key] = {"status": "added", "value": dict2[key]}
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff[key] = {"status": "nested", "children": build_diff(dict1[key], dict2[key])}
        elif dict1[key] != dict2[key]:
            diff[key] = {"status": "changed", "old_value": dict1[key], "new_value": dict2[key]}
        else:
            diff[key] = {"status": "unchanged", "value": dict1[key]}
    return diff

def render_stylish(diff, depth=1):
    indent = " " * (depth * 2 + 3)  # Ширина отступов
    lines = []
    for key, value in diff.items():
        status = value["status"]
        if status == "removed":
            lines.append(f"{' ' * (depth * 2)}- {key}: {format_value(value['value'], depth)}")
        elif status == "added":
            lines.append(f"{' ' * (depth * 2)}+ {key}: {format_value(value['value'], depth)}")
        elif status == "unchanged":
            lines.append(f"{' ' * (depth * 2)}  {key}: {format_value(value['value'], depth)}")
        elif status == "changed":
            lines.append(f"{' ' * (depth * 2)}- {key}: {format_value(value['old_value'], depth)}")
            lines.append(f"{' ' * (depth * 2)}+ {key}: {format_value(value['new_value'], depth)}")
        elif status == "nested":
            lines.append(f"{' ' * (depth * 2)}{key}: {{")
            lines.append(render_stylish(value["children"], depth + 1))
            lines.append(f"{' ' * (depth * 2)}}}")
    return "\n".join(lines)

def format_value(value, depth):
    indent = " " * (depth * 2 + 4)  # Ширина отступов
    if isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        lines.append(f"{' ' * (depth * 2)}  }}")  # Закрывающая скобка
        return "\n".join(lines)
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)

# Пример использования
print(generate_diff_recurs('gendiff/files/file1_rec.json', 'gendiff/files/file2_rec.json'))
