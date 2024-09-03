import yaml
from gendiff.recurs_for_json import build_diff, render_stylish


def generate_diff_recurs_yaml(path_file1, path_file2):
    with open(path_file1, 'r') as file:
        prime_file = yaml.safe_load(file)
    with open(path_file2, 'r') as file:
        second_file = yaml.safe_load(file)
    diff = build_diff(prime_file, second_file)
    formatted_diff = render_stylish(diff)
    return '{\n' + formatted_diff + '\n}'
