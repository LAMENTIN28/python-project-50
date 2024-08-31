import json
from gendiff.gendiff_recurs import build_diff


def generate_diff_plain(path_file1, path_file2, format=''):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    diff = build_diff(file1, file2)
    if format == 'plain':
        return render_plain(diff)


def render_plain(diff, parent=''):
    lines = []
    for key, value in diff.items():
        property_name = f"{parent}{key}"
        status = value['status']
        if status == 'removed':
            lines.append(f"Property '{property_name}' was removed")
        elif status == 'added':
            formatted_value = format_plain_value(value['value'])
            lines.append(f"Property '{property_name}' was added with value: {formatted_value}")
        elif status == 'changed':
            old_value = format_plain_value(value['old_value'])
            new_value = format_plain_value(value['new_value'])
            lines.append(f"Property '{property_name}' was updated. From {old_value} to {new_value}")
        elif status == 'nested':
            lines.append(render_plain(value['children'], f"{property_name}."))
    return "\n".join(lines)


def format_plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    return str(value)
