import json


def generate_diff(path_file1, path_file2):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    file1 = stringify(file1)
    file2 = stringify(file2)
    print(file1)


def stringify(value, replacer = " ", space_count = 1):
    def build(curent_value, depth):
        if not isinstance(curent_value, dict):
            return str(curent_value)

        curent_indent = replacer * depth
        child_ident_size = depth + space_count
        child_indent = child_ident_size * replacer
        children = ['{']
        for key, value in curent_value.items():
            curent_string = f'{child_indent}{key}: {build(value, child_ident_size)}'
            children.append(curent_string)

        children.append(curent_indent + '}')
        return "\n".join(children)
        
        
    return build(value, 0)

generate_diff('gendiff/files/file1_rec.json', 'gendiff/files/file2_rec.json')