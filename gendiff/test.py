import json


def processing(file):
    res = []
    for k in file:
        res.append(k)
    return res


def generate_diff(path_file1, path_file2):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    all = list(set(file1.items()) | set(file2.items()))
    all2 = []
    for key in sorted(file1 | file2):
        all2.append(key)
    all = processing(all)
    common = file1.items() & file2.items()
    common = processing(common)
    unique1 = file1.items() - file2.items()
    unique1 = processing(unique1)
    unique2 = file2.items() - file1.items()
    unique2 = processing(unique2)
    res = ' '
    for k in all2:
        for l in common:
            if k == l[0]:
                res +=  "   " + l[0] + ": " + str(l[1]) + "\n"
        for l in unique1:
            if k == l[0]:
                res += " - " + l[0] + ": " + str(l[1]) + "\n"
        for l in unique2:
            if k == l[0]:
                res += " + " +  l[0] + ": " + str(l[1]) + "\n"
    res = '{\n' + res[1:] + '}'
    print (res)
    return (res)


        
generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')