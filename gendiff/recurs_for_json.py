import json


STATUSES = {'removed': '- ',
            'added': '+ ',
            'unchanged': '  '}


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
    lines = []
    absatz = depth * 2 + 1
    for key, value in diff.items():
        status = value["status"]
        for type, sign in STATUSES.items():
            if status == type:
                lines.append(f"{' ' * (absatz)}{sign}{key}: {format_value(value['value'], depth)}")
        if status == "changed":
            lines.append(f"{' ' * (absatz)}- {key}: {format_value(value['old_value'], depth)}")
            lines.append(f"{' ' * (absatz)}+ {key}: {format_value(value['new_value'], depth)}")
        elif status == "nested":
            lines.append(f"{' ' * (absatz)}{key}: {{")
            lines.append(render_stylish(value["children"], depth + 1))
            lines.append(f"{' ' * (absatz)}}}")
    return "\n".join(lines)


def format_value(value, depth):
    indent = " " * (depth * 2 + 4)
    if isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        lines.append(f"{' ' * (depth * 2 - 1)}  }}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    return str(value)
