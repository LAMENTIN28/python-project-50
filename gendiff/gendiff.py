import json


def iter_list(key, list, par):
    res = ""
    for item in list:
        if key == item[0]:
            res += par + str(item[0]) + ": " + (str(item[1])).lower() + "\n"
    return res


def gen_diff(path_file1, path_file2):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    all2 = []
    for key in sorted(file1 | file2):
        all2.append(key)
    common = list(file1.items() & file2.items())
    unique1 = list(file1.items() - file2.items())
    unique2 = list(file2.items() - file1.items())
    res1 = ""
    for key in all2:
        res1 += iter_list(key, common, "   ")
        res1 += iter_list(key, unique1, " - ")
        res1 += iter_list(key, unique2, " + ")
    res1 = '{\n' + res1 + '}'
    return res1
