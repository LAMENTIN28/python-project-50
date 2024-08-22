import yaml


def generate_diff_yaml(path_file1, path_file2):
    with open(path_file1, 'r') as file:
        prime_file = yaml.safe_load(file)
    with open(path_file2, 'r') as file:
        second_file = yaml.safe_load(file)
    prime_file = dict(sorted(prime_file.items()))
    prel = build_prime_file(prime_file, second_file)
    for k2, v2 in second_file.items():
        if k2 not in prime_file.keys():
            prel.append(f' + {k2}: {v2}')
    res = stylish(prel)
    return res


def stylish(prel):
    res = "{\n"
    for k in prel:
        res += f'{k}\n'
    res = res.lower() + '}'
    return res


def build_prime_file(prime_file, second_file):
    prel = []
    for k1, v1 in prime_file.items():
        if k1 in second_file.keys() and (v1 in second_file.values()):
            prel.append(f'   {k1}: {v1}')
        elif k1 in second_file.keys() and v1 not in second_file.values():
            prel.append(f' - {k1}: {v1}')
            for k2, v2 in second_file.items():
                if k1 == k2:
                    prel.append(f' + {k2}: {v2}')
        else:
            prel.append(f' - {k1}: {v1}')
    return prel
